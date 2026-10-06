"""Single-process launcher for the ENTROPY ransomware lab.

Starts the detection pipeline, SOC dashboard, victim explorer, and attacker
console together, then shuts them down on Ctrl+C.

This is the industry-level entry point for final year demo.
"""

from __future__ import annotations

import os
import signal
import subprocess
import sys
import time
import threading
import urllib.request
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PYTHON = sys.executable

SERVICES = (
    ("dashboard", [PYTHON, str(ROOT / "app.py")]),
    ("pipeline", [PYTHON, str(ROOT / "monitoring" / "pipeline_runner.py")]),
    ("victim", [PYTHON, str(ROOT / "victim_server" / "app.py")]),
    ("attacker", [PYTHON, str(ROOT / "attacker_server" / "app.py")]),
)

VICTIM_FOLDER = "victim_server/user_files"

def clean_demo_environment():
    """Wipes the database and quarantine folder before starting for a pure 0000 baseline."""
    print("[lab] Performing pre-demo cleanup (wiping old DB & quarantine)...")
    
    # 1. Delete SQLite history database & temp files
    for ext in ["", "-journal", "-wal", "-shm"]:
        db_file = ROOT / f"entropy.db{ext}"
        if db_file.exists():
            try:
                db_file.unlink()
            except Exception:
                pass
                
    # 2. Clear quarantine storage
    q_dir = ROOT / "quarantine_storage"
    if q_dir.exists():
        for f in q_dir.iterdir():
            if f.is_file():
                try:
                    f.unlink()
                except Exception:
                    pass

def pre_initialize_db():
    """Initializes SQLite schema ONCE serially before spawning sub-processes to prevent DB locking."""
    try:
        sys.path.insert(0, str(ROOT))
        from storage.database import init_db
        conn = init_db()
        if conn:
            conn.close()
        print("[lab] Database schema pre-initialized cleanly (WAL mode enabled) ✅")
    except Exception as exc:
        print(f"[lab] DB pre-init notice: {exc}")

def wait_and_open_browsers():
    """Waits for all 3 Flask apps to boot, then opens browser tabs simultaneously."""
    urls = [
        "http://127.0.0.1:8001",  # Attacker
        "http://127.0.0.1:5001",  # Victim
        "http://127.0.0.1:5000"   # SOC (Takes longest due to pipeline init)
    ]
    
    print("\n[lab] Waiting for all services to become fully active...")
    for url in urls:
        while True:
            try:
                # Ping the health/home endpoint
                urllib.request.urlopen(url, timeout=1.0)
                break
            except Exception:
                time.sleep(0.5)
                
    print("[lab] All services are ONLINE! Opening browser dashboards...")
    time.sleep(1.5)  # Brief pause to ensure rendering is ready
    
    # Open tabs
    webbrowser.open("http://127.0.0.1:8001")
    webbrowser.open("http://127.0.0.1:5001")
    webbrowser.open("http://127.0.0.1:5000")


def _set_default(env: dict[str, str], key: str, value: str) -> None:
    if not (env.get(key) or "").strip():
        env[key] = value

def _env(dry_run: bool | None = None) -> dict[str, str]:
    env = os.environ.copy()
    _set_default(env, "ENTROPY_DASHBOARD_HOST", "0.0.0.0")
    _set_default(env, "ENTROPY_VICTIM_HOST", "0.0.0.0")
    if dry_run is not None:
        env["ENTROPY_DRY_RUN"] = "true" if dry_run else "false"
    _set_default(env, "ENTROPY_DRY_RUN", "false")
    _set_default(env, "ENTROPY_CONTROL_TOKEN", "entropy-lab")
    _set_default(env, "ENTROPY_BLOCKCHAIN_FALLBACK", "true")
    _set_default(env, "PYTHONUNBUFFERED", "1")

    folders = [
        part.strip()
        for part in (env.get("ENTROPY_WATCH_FOLDERS") or "").split(",")
        if part.strip()
    ]
    victim_abs = (ROOT / VICTIM_FOLDER).resolve()
    if not any((ROOT / f).resolve() == victim_abs for f in folders):
        folders.insert(0, VICTIM_FOLDER)
    env["ENTROPY_WATCH_FOLDERS"] = ",".join(folders)
    return env

def _ensure_quarantine():
    import config
    q_dir = config.QUARANTINE_DIR
    b_dir = config.BACKUP_DIR
    os.makedirs(q_dir, exist_ok=True)
    os.makedirs(b_dir, exist_ok=True)
    os.makedirs(config.LOG_DIR, exist_ok=True)
    os.makedirs(config.REPORTS_DIR, exist_ok=True)

def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    
    # 1. Clean environment
    clean_demo_environment()
    _ensure_quarantine()
    
    # 2. Pre-initialize DB to stop sqlite concurrency crash
    pre_initialize_db()

    fixtures = ROOT / "victim_server" / "create_fake_files.py"
    victim_files = ROOT / "victim_server" / "user_files"
    if not victim_files.exists() or not any(victim_files.iterdir()):
        print("[lab] Creating victim fixtures...")
        subprocess.check_call([PYTHON, str(fixtures), "--clean"], cwd=ROOT)

    print("=" * 70)
    print("  ENTROPY - Ransomware Shield | Final Year Major Project")
    print("  Industry Level - Proactive Defence with Blockchain Audit")
    print("=" * 70)
    print("  SOC Dashboard   : http://127.0.0.1:5000  (real-time feed)")
    print("  Victim PC       : http://127.0.0.1:5001  (neutral explorer)")
    print("  Attacker Console: http://127.0.0.1:8001  (launch attacks)")
    env = _env(dry_run="--dry-run" in argv)
    dry_run = env["ENTROPY_DRY_RUN"].strip().lower() in {"1", "true", "yes", "on"}
    print(f"  Watching        : {env['ENTROPY_WATCH_FOLDERS']}")
    print("  Dry-run         : " + ("ON" if dry_run else "OFF - real kill+quarantine active"))
    print("=" * 70)

    processes: list[subprocess.Popen] = []
    try:
        for name, command in SERVICES:
            proc = subprocess.Popen(command, cwd=ROOT, env=env)
            processes.append(proc)
            print(f"[lab] started {name:12s} pid={proc.pid}")
            # ADDED: Stagger process execution by 0.6 seconds so they don't fight for DB locks
            time.sleep(0.6) 

        # Start the background thread to open browsers once everything is fully ready
        threading.Thread(target=wait_and_open_browsers, daemon=True).start()

        while True:
            for (svc_name, _), proc in zip(SERVICES, processes):
                code = proc.poll()
                if code is not None:
                    print(f"[lab] {svc_name} exited with {code} - shutting down")
                    return code or 1
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n[lab] shutting down...")
        return 0
    finally:
        for proc in processes:
            if proc.poll() is None:
                try:
                    proc.send_signal(signal.SIGINT)
                except Exception:
                    pass
        deadline = time.time() + 8
        for proc in processes:
            remaining = max(0.1, deadline - time.time())
            try:
                proc.wait(timeout=remaining)
            except subprocess.TimeoutExpired:
                try:
                    proc.kill()
                except Exception:
                    pass
        print("[lab] stopped - estate preserved for forensics")

if __name__ == "__main__":
    raise SystemExit(main())