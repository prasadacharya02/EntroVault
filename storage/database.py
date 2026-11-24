"""Shared SQLite storage and schema management for ENTROPY."""

from __future__ import annotations

import sqlite3
from pathlib import Path

import config

SCHEMA_VERSION = 5

_EVENTS_SCHEMA = """
CREATE TABLE IF NOT EXISTS events (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp     TEXT,
    file_path     TEXT,
    event_type    TEXT,
    entropy       REAL,
    entropy_delta REAL,
    pid           INTEGER,
    process_name  TEXT,
    action        INTEGER,
    status        TEXT,
    requested_action INTEGER,
    outcome       TEXT,
    restore_result TEXT,
    dry_run       INTEGER,
    engine        TEXT,
    confidence    REAL,
    explanation   TEXT,
    q_values      TEXT
)
"""

# One row per email notification attempt. The UNIQUE constraint on
# (incident_id, stage) is the dedup guarantee: a detection alert and a
# recovery alert can each be sent at most once per incident, even if the
# pipeline re-processes the same campaign or restarts mid-incident.
_NOTIFICATIONS_SCHEMA = """
CREATE TABLE IF NOT EXISTS notifications (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    incident_id  TEXT NOT NULL,
    stage        TEXT NOT NULL,
    recipient    TEXT NOT NULL,
    subject      TEXT NOT NULL,
    status       TEXT NOT NULL,
    detail       TEXT,
    sent_at      TEXT
)
"""

_NOTIFICATIONS_UNIQUE = (
    "CREATE UNIQUE INDEX IF NOT EXISTS idx_notifications_incident_stage "
    "ON notifications(incident_id, stage)"
)


def connect(path: str | None = None) -> sqlite3.Connection:
    """Open the application database with consistent connection settings, WAL mode, and timeouts."""
    database_path = path or config.DB_PATH
    # ADDED: timeout=30.0 to prevent "database is locked" errors on Windows
    connection = sqlite3.connect(database_path, check_same_thread=False, timeout=30.0)
    connection.row_factory = sqlite3.Row
    
    # ADDED: Enable Write-Ahead Logging and 30-second busy timeout for high concurrency
    try:
        connection.execute("PRAGMA journal_mode=WAL;")
        connection.execute("PRAGMA busy_timeout=30000;")
    except sqlite3.OperationalError:
        pass
        
    return connection


def _ensure_events_columns(connection: sqlite3.Connection) -> None:
    """Upgrade the original Day 1 table without destroying existing data."""
    existing = {
        row[1] for row in connection.execute("PRAGMA table_info(events)")
    }
    columns = {
        "timestamp": "TEXT",
        "file_path": "TEXT",
        "event_type": "TEXT",
        "entropy": "REAL",
        "entropy_delta": "REAL",
        "pid": "INTEGER",
        "process_name": "TEXT",
        "action": "INTEGER",
        "status": "TEXT",
        "requested_action": "INTEGER",
        "outcome": "TEXT",
        "restore_result": "TEXT",
        "dry_run": "INTEGER",
        "engine": "TEXT",
        "confidence": "REAL",
        "explanation": "TEXT",
        "q_values": "TEXT",
    }
    for name, definition in columns.items():
        if name not in existing:
            connection.execute(
                f"ALTER TABLE events ADD COLUMN {name} {definition}"
            )


def init_db(path: str | None = None) -> sqlite3.Connection:
    """Create or migrate the shared events schema and return a connection."""
    database_path = Path(path or config.DB_PATH)
    database_path.parent.mkdir(parents=True, exist_ok=True)
    connection = connect(str(database_path))
    
    # Lock the database briefly to ensure serial table creation
    with connection:
        connection.execute(_EVENTS_SCHEMA)
        _ensure_events_columns(connection)
        connection.execute(_NOTIFICATIONS_SCHEMA)
        connection.execute(_NOTIFICATIONS_UNIQUE)
        connection.execute("CREATE INDEX IF NOT EXISTS idx_events_action ON events(action)")
        connection.execute("CREATE INDEX IF NOT EXISTS idx_events_timestamp ON events(timestamp)")
        connection.execute("CREATE INDEX IF NOT EXISTS idx_events_file_path ON events(file_path)")
        connection.execute(
            "CREATE TABLE IF NOT EXISTS schema_meta "
            "(key TEXT PRIMARY KEY, value TEXT NOT NULL)"
        )
        connection.execute(
            "INSERT INTO schema_meta(key, value) VALUES('schema_version', ?) "
            "ON CONFLICT(key) DO UPDATE SET value=excluded.value",
            (str(SCHEMA_VERSION),),
        )
    return connection


# ── Pipeline heartbeat ──────────────────────────────────────
# The detection pipeline and the SOC dashboard are separate processes
# that only share this database. The pipeline writes a heartbeat row
# (what it watches, dry-run state, counters) every couple of seconds so
# the dashboard can show whether detection is actually running and
# which folder it is looking at — instead of silently showing nothing.

_PIPELINE_STATUS_SCHEMA = """
CREATE TABLE IF NOT EXISTS pipeline_status (
    id             INTEGER PRIMARY KEY CHECK (id = 1),
    heartbeat      REAL NOT NULL,
    started_at     REAL,
    pid            INTEGER,
    watch_folders  TEXT,
    dry_run        INTEGER,
    engine         TEXT,
    stats          TEXT
)
"""


def write_pipeline_heartbeat(connection: sqlite3.Connection, *,
                             started_at: float, pid: int,
                             watch_folders: list, dry_run: bool,
                             engine: str, stats: dict) -> None:
    """Upsert the single pipeline heartbeat row."""
    import json
    import time

    with connection:
        connection.execute(_PIPELINE_STATUS_SCHEMA)
        connection.execute(
            """
            INSERT INTO pipeline_status
                (id, heartbeat, started_at, pid, watch_folders, dry_run,
                 engine, stats)
            VALUES (1, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                heartbeat=excluded.heartbeat, started_at=excluded.started_at,
                pid=excluded.pid, watch_folders=excluded.watch_folders,
                dry_run=excluded.dry_run, engine=excluded.engine,
                stats=excluded.stats
            """,
            (time.time(), started_at, pid, json.dumps(list(watch_folders)),
             1 if dry_run else 0, engine, json.dumps(stats or {})),
        )


def read_pipeline_heartbeat(connection: sqlite3.Connection) -> dict | None:
    """Return the last pipeline heartbeat, or None if it never ran."""
    import json

    connection.execute(_PIPELINE_STATUS_SCHEMA)
    row = connection.execute(
        "SELECT * FROM pipeline_status WHERE id = 1"
    ).fetchone()
    if row is None:
        return None
    data = dict(row)
    data["watch_folders"] = json.loads(data.get("watch_folders") or "[]")
    data["stats"] = json.loads(data.get("stats") or "{}")
    data["dry_run"] = bool(data.get("dry_run"))
    return data


# ── Incident email notifications ────────────────────────────
# The notifications table (created in init_db) records one row per
# alert attempt. The (incident_id, stage) unique index is the dedup
# guarantee used by the notification layer.


def notification_sent(connection: sqlite3.Connection,
                      incident_id: str, stage: str) -> bool:
    """True if an alert for *incident_id* at *stage* was already attempted."""
    row = connection.execute(
        "SELECT 1 FROM notifications WHERE incident_id = ? AND stage = ? "
        "LIMIT 1",
        (incident_id, stage),
    ).fetchone()
    return row is not None


def record_notification(connection: sqlite3.Connection, *,
                        incident_id: str, stage: str, recipient: str,
                        subject: str, status: str,
                        detail: str | None = None) -> bool:
    """Record one notification attempt.

    Returns True when the row was inserted, False when an attempt for the
    same (incident_id, stage) already exists (the duplicate was ignored).
    """
    try:
        cursor = connection.execute(
            "INSERT OR IGNORE INTO notifications "
            "(incident_id, stage, recipient, subject, status, detail, sent_at) "
            "VALUES (?, ?, ?, ?, ?, ?, datetime('now'))",
            (incident_id, stage, recipient, subject, status, detail),
        )
        connection.commit()
        return cursor.rowcount > 0
    except sqlite3.Error:
        return False