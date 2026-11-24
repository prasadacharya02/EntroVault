# ============================================================
# ENTROPY - Incident Tracker
# notification/incidents.py
#
# Tracks one logical incident from detection through recovery so the
# notification layer can report honest, deduplicated figures:
#
#   * affected file count   — files the incident touched
#   * recovery status       — in progress / completed / partial
#   * unaffected file count — estate files the incident never touched
#
# An incident is keyed so that every file of the same campaign maps to
# the SAME incident (one alert set, not one per file), while distinct
# campaigns and distinct single-file incidents stay separate.
# ============================================================

from __future__ import annotations

import logging
import os
import uuid
from datetime import datetime

import config

log = logging.getLogger("IncidentTracker")


def _incident_key(event: dict, decision: dict) -> str:
    """Stable identity for one incident.

    A confirmed campaign shares one key across all of its files; a
    single-file incident keys on its event id; a fallback keys on the
    absolute path so the same path never yields two alerts for one event.
    """
    campaign_id = (decision or {}).get("campaign_id")
    if campaign_id:
        return f"campaign:{campaign_id}"
    event_id = (event or {}).get("event_id")
    if event_id:
        return f"event:{event_id}"
    path = (event or {}).get("file_path") or ""
    return f"file:{os.path.abspath(path)}"


def count_estate_files(root: str | None = None) -> int:
    """Count files in the victim's protected estate.

    Used for the "unaffected files" figure. Returns 0 when the estate
    directory does not exist yet.
    """
    root = root or config.VICTIM_USER_FILES
    if not root or not os.path.isdir(root):
        return 0
    total = 0
    for _dirpath, _dirnames, filenames in os.walk(root):
        total += sum(1 for name in filenames
                     if os.path.isfile(os.path.join(_dirpath, name)))
    return total


class Incident:
    """A single detected incident and its recovery outcome."""

    def __init__(self, key: str, trigger_path: str = "",
                 dry_run: bool = False, estate_total: int = 0):
        self.incident_id = uuid.uuid4().hex
        self.key = key
        self.trigger_path = trigger_path
        self.started_at = datetime.now().isoformat()
        self.dry_run = dry_run
        self.estate_total = estate_total
        self.recovery_status = "pending"

        # path -> {"recovered", "failed", "simulated", "outcome"}
        self._affected: dict[str, dict] = {}

    # ── lifecycle ───────────────────────────────────────────

    def mark_recovery_started(self) -> None:
        self.recovery_status = "in_progress"

    def mark_recovery_complete(self) -> None:
        self.recovery_status = (
            "completed" if self.failed_count == 0 else "partial"
        )

    def add_affected(self, path: str, *, recovered: bool = False,
                     failed: bool = False, simulated: bool = False,
                     outcome: str = "") -> None:
        """Record (or update) one affected file's outcome."""
        if not path:
            return
        path = os.path.abspath(path)
        self._affected[path] = {
            "recovered": bool(recovered),
            "failed": bool(failed),
            "simulated": bool(simulated),
            "outcome": outcome,
        }

    def record_outcome(self, path: str, status: str) -> None:
        """Derive the recovery outcome from an execute_response status."""
        status = str(status or "")
        if "RESTORED" in status:
            self.add_affected(path, recovered=True, outcome=status)
        elif "DRY_RUN_RESTORE" in status:
            self.add_affected(path, simulated=True, outcome=status)
        elif ("RESTORE_FAILED" in status or "RESTORE_SKIPPED" in status):
            self.add_affected(path, failed=True, outcome=status)
        else:
            # Quarantined / already contained with no restore result.
            self.add_affected(path, outcome=status)

    # ── introspection ──────────────────────────────────────

    @property
    def affected_count(self) -> int:
        return len(self._affected)

    @property
    def recovered_count(self) -> int:
        return sum(1 for v in self._affected.values() if v["recovered"])

    @property
    def failed_count(self) -> int:
        return sum(1 for v in self._affected.values() if v["failed"])

    @property
    def simulated_count(self) -> int:
        return sum(1 for v in self._affected.values() if v["simulated"])

    @property
    def unaffected_count(self) -> int:
        return max(0, self.estate_total - self.affected_count)

    def affected_names(self, limit: int = 20) -> list[str]:
        return [os.path.basename(p) for p in sorted(self._affected)][:limit]

    def summary(self) -> dict:
        return {
            "incident_id": self.incident_id,
            "key": self.key,
            "trigger_path": self.trigger_path,
            "started_at": self.started_at,
            "dry_run": self.dry_run,
            "recovery_status": self.recovery_status,
            "affected_count": self.affected_count,
            "recovered_count": self.recovered_count,
            "failed_count": self.failed_count,
            "simulated_count": self.simulated_count,
            "unaffected_count": self.unaffected_count,
        }

    def __repr__(self) -> str:
        return (f"<Incident {self.incident_id[:8]} {self.key} "
                f"status={self.recovery_status} "
                f"affected={self.affected_count}>")


class IncidentTracker:
    """Registry of incidents keyed for deduplication."""

    def __init__(self):
        self._incidents: dict[str, Incident] = {}

    def begin(self, event: dict, decision: dict) -> Incident:
        """Return the incident for *event*/*decision*, creating it once."""
        key = _incident_key(event, decision)
        existing = self._incidents.get(key)
        if existing is not None:
            return existing
        incident = Incident(
            key,
            trigger_path=(event or {}).get("file_path", ""),
            dry_run=bool(config.DRY_RUN),
            estate_total=count_estate_files(),
        )
        self._incidents[key] = incident
        log.warning(
            "[INCIDENT] Opened %s (%s) — estate=%d file(s)",
            incident.incident_id[:8], key, incident.estate_total,
        )
        return incident

    def get(self, key: str) -> Incident | None:
        return self._incidents.get(key)

    def all(self) -> list[Incident]:
        return list(self._incidents.values())

    def reset(self) -> None:
        self._incidents.clear()
