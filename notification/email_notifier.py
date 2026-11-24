# ============================================================
# ENTROPY - Automated Incident Email Notifier
# notification/email_notifier.py
#
# Sends the victim an email when an incident is detected (recovery in
# progress) and a second email when recovery is complete.
#
#   * Sending uses Python's standard SMTP client against Gmail
#     (smtp.gmail.com:587 + STARTTLS) with a dedicated project account.
#   * Sender display name: "EntroVault Security System".
#   * Body content is generated from live incident data (affected /
#     unaffected counts, recovery status) — never hardcoded.
#   * Each (incident, stage) is recorded in the shared SQLite
#     `notifications` table, which is the dedup guarantee: a detection
#     alert and a recovery alert are each sent at most once per incident,
#     even across pipeline restarts.
#   * Every failure is contained: a missing account, an SMTP error or a
#     database problem never raises into the detection pipeline.
# ============================================================

from __future__ import annotations

import json
import logging
import os
import smtplib
from datetime import datetime
from email.message import EmailMessage
from email.utils import formataddr

import config
from storage.database import connect, notification_sent, record_notification

log = logging.getLogger("EmailNotifier")

DETECTION_STAGE = "detected"
RECOVERY_STAGE = "completed"

DETECTION_SUBJECT = "EntroVault Security Alert – File Recovery in Progress"
RECOVERY_SUBJECT = "EntroVault Security Alert – File Recovery Complete"


class EmailNotifier:
    """Builds and dispatches incident notifications to the victim."""

    def __init__(self, db_path: str | None = None):
        self.db_path = db_path or config.DB_PATH

    @property
    def enabled(self) -> bool:
        # Read the master switch dynamically so a change at runtime (or
        # in tests) takes effect without rebuilding the notifier.
        return bool(config.EMAIL_ENABLED)

    # ── configuration / recipient ─────────────────────────

    @property
    def _dry_send(self) -> bool:
        return bool(config.EMAIL_SEND_DRY_RUN)

    @property
    def _configured(self) -> bool:
        return bool(config.EMAIL_SENDER_ADDRESS and
                    config.EMAIL_SENDER_PASSWORD)

    def resolve_recipient(self) -> str:
        """The victim's registered email.

        Reads the profile the victim-side application maintains so a
        change made in the victim UI is honoured; falls back to the
        configured default.
        """
        profile = self._load_victim_profile()
        email = (profile or {}).get("email")
        if email:
            return str(email).strip()
        return config.VICTIM_EMAIL

    def _load_victim_profile(self) -> dict:
        path = config.VICTIM_PROFILE_PATH
        try:
            with open(path, encoding="utf-8") as handle:
                data = json.load(handle)
        except (OSError, ValueError):
            return {}
        return data if isinstance(data, dict) else {}

    # ── message construction ──────────────────────────────

    def _sender(self) -> str:
        return formataddr((config.EMAIL_SENDER_NAME,
                           config.EMAIL_SENDER_ADDRESS))

    def _base_message(self, subject: str, recipient: str) -> EmailMessage:
        message = EmailMessage()
        message["From"] = self._sender()
        message["To"] = recipient
        message["Subject"] = subject
        message["Date"] = datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")
        return message

    def build_detection_email(self, incident) -> EmailMessage:
        recipient = self.resolve_recipient()
        message = self._base_message(DETECTION_SUBJECT, recipient)

        affected = incident.affected_count
        unaffected = incident.unaffected_count
        lines = [
            "Dear User,",
            "",
            "EntroVault has detected suspicious file modification activity "
            "on your system.",
            "",
            f"Our security system has identified {affected} affected file(s). "
            "These files have been isolated and are currently undergoing "
            "recovery. They will be available shortly.",
            "",
            f"All remaining {unaffected} file(s) are safe and accessible.",
            "",
            "EntroVault is continuously monitoring your system to prevent "
            "further suspicious activity.",
        ]
        if incident.dry_run:
            lines += [
                "",
                "Note: this notice was produced in simulation (dry-run) "
                "mode. No files were modified on your system.",
            ]
        lines += [
            "",
            "Regards,",
            "EntroVault Security System",
            "Automated Incident Response & Recovery",
        ]
        message.set_content("\n".join(lines))
        return message

    def build_recovery_email(self, incident) -> EmailMessage:
        recipient = self.resolve_recipient()
        message = self._base_message(RECOVERY_SUBJECT, recipient)

        affected = incident.affected_count
        unaffected = incident.unaffected_count
        recovered = incident.recovered_count
        failed = incident.failed_count

        if incident.dry_run:
            status_line = (
                "The recovery procedure completed in simulation "
                "(dry-run) mode. No files were modified on your system."
            )
        elif failed == 0:
            status_line = (
                f"Recovery is now complete. All {affected} affected file(s) "
                "were restored from secure backups and are available again."
            )
        else:
            status_line = (
                f"Recovery is partially complete. {recovered} of "
                f"{affected} affected file(s) were restored. {failed} "
                "file(s) could not be automatically restored and require "
                "manual recovery."
            )

        lines = [
            "Dear User,",
            "",
            "This is a follow-up regarding the security incident detected "
            "on your system.",
            "",
            status_line,
            "",
            f"All remaining {unaffected} file(s) remain safe and accessible.",
            "",
            "EntroVault is continuously monitoring your system to prevent "
            "further suspicious activity.",
            "",
            "Regards,",
            "EntroVault Security System",
            "Automated Incident Response & Recovery",
        ]
        message.set_content("\n".join(lines))
        return message

    def _message_for(self, incident, stage: str) -> EmailMessage:
        if stage == DETECTION_STAGE:
            return self.build_detection_email(incident)
        return self.build_recovery_email(incident)

    # ── persistence (dedup) ────────────────────────────────

    def _already_notified(self, incident_id: str, stage: str) -> bool:
        conn = None
        try:
            conn = connect(self.db_path)
            return notification_sent(conn, incident_id, stage)
        except Exception as exc:
            log.warning("[EMAIL] Dedup lookup failed: %s", exc)
            return False
        finally:
            if conn is not None:
                try:
                    conn.close()
                except Exception:
                    pass

    def _record(self, incident_id: str, stage: str, recipient: str,
                subject: str, status: str, detail: str = "") -> None:
        conn = None
        try:
            conn = connect(self.db_path)
            record_notification(
                conn, incident_id=incident_id, stage=stage,
                recipient=recipient, subject=subject, status=status,
                detail=detail,
            )
        except Exception as exc:
            log.warning("[EMAIL] Dedup record failed: %s", exc)
        finally:
            if conn is not None:
                try:
                    conn.close()
                except Exception:
                    pass

    # ── SMTP transport ────────────────────────────────────

    def _send_smtp(self, message: EmailMessage) -> None:
        """Deliver *message* through Gmail's SMTP server."""
        with smtplib.SMTP(config.EMAIL_SMTP_HOST,
                          config.EMAIL_SMTP_PORT,
                          timeout=config.EMAIL_SEND_TIMEOUT) as server:
            server.ehlo()
            if config.EMAIL_USE_TLS:
                server.starttls()
                server.ehlo()
            server.login(config.EMAIL_SENDER_ADDRESS,
                         config.EMAIL_SENDER_PASSWORD)
            server.send_message(message)

    # ── public API ────────────────────────────────────────

    def notify(self, incident, stage: str) -> dict:
        """Send (or simulate) one notification for *incident*/*stage*.

        Returns a result dict and never raises: a misconfigured sender,
        an SMTP failure or a storage problem is logged and reported.
        """
        if not self.enabled:
            return {"sent": False, "status": "disabled",
                    "detail": "email notifications disabled"}
        if stage not in (DETECTION_STAGE, RECOVERY_STAGE):
            return {"sent": False, "status": "invalid_stage",
                    "detail": f"unknown stage {stage!r}"}

        incident_id = incident.incident_id
        if self._already_notified(incident_id, stage):
            log.info("[EMAIL] Duplicate %s alert for incident %s — skipped",
                     stage, incident_id[:8])
            return {"sent": False, "status": "duplicate",
                    "detail": "already notified for this incident"}

        recipient = self.resolve_recipient()
        message = self._message_for(incident, stage)
        subject = message["Subject"]

        if self._dry_send:
            status = "dry_run"
            detail = "SMTP send simulated (ENTROPY_EMAIL_SEND_DRY_RUN)"
            log.warning(
                "[EMAIL][DRY-RUN] %s → %s | subject=%r",
                stage, recipient, subject,
            )
        elif not self._configured:
            status = "skipped"
            detail = ("sender account not configured "
                      "(ENTROPY_EMAIL_ADDRESS / ENTROPY_EMAIL_PASSWORD)")
            log.error(
                "[EMAIL] %s alert for incident %s skipped: %s",
                stage, incident_id[:8], detail,
            )
        else:
            try:
                self._send_smtp(message)
                status = "sent"
                detail = f"delivered to {recipient}"
                log.warning("[EMAIL] %s alert sent to %s", stage, recipient)
            except (smtplib.SMTPException, OSError) as exc:
                status = "failed"
                detail = f"SMTP error: {exc}"
                log.error("[EMAIL] %s alert delivery failed: %s",
                          stage, exc)

        self._record(incident_id, stage, recipient, subject, status, detail)
        return {
            "sent": status in ("sent", "dry_run"),
            "status": status,
            "recipient": recipient,
            "subject": subject,
            "detail": detail,
            "incident_id": incident_id,
            "stage": stage,
        }

    def notify_detected(self, incident) -> dict:
        return self.notify(incident, DETECTION_STAGE)

    def notify_recovered(self, incident) -> dict:
        return self.notify(incident, RECOVERY_STAGE)

    def configured(self) -> bool:
        return self._configured
