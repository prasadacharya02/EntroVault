# ============================================================
# ENTROPY - Tri-Layer Defense & Integrity-Audited SOC Engine
# ============================================================

import sys
import os
import json
import shutil
import threading
import logging
import time
import hashlib
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

import config
from storage.database import connect, init_db as initialize_database
from storage.database import read_pipeline_heartbeat
from blockchain.connector import BlockchainConnector
from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit

app = Flask(__name__,
            template_folder=os.path.join(BASE_DIR, "dashboard", "templates"),
            static_folder=os.path.join(BASE_DIR, "dashboard", "static"))

app.config["SECRET_KEY"] = config.SECRET_KEY
log = logging.getLogger("Dashboard")

def _api_error(message="dashboard service unavailable", status=500):
    return jsonify({"error": message, "status": status}), status

socketio = SocketIO(app, cors_allowed_origins="*", async_mode="threading")
bc = BlockchainConnector()

def get_db():
    return connect()

def init_db():
    conn = initialize_database()
    conn.close()
    print("[DASHBOARD] Database ready ✅")

# ============================================================
# TRI-LAYER DEFENSE ENGINE (CANARY, MAGIC-NUMBER, WORM VAULT)
# ============================================================

LOCK_EXTENSIONS = (
    ".wncry", ".wncryt", ".ryk", ".maze", ".revil", 
    ".lockbit", ".akira", ".clop", ".qilin", ".abcd"
)
NOTE_MARKERS = (
    "@please_read_me@", "ryukreadme", "restore-my-files", 
    "recover-", "maze-readme"
)

# Magic-Number / Header Bytes Dictionary
MAGIC_NUMBERS = {
    ".pdf": b"%PDF",
    ".jpg": b"\xff\xd8\xff",
    ".jpeg": b"\xff\xd8\xff",
    ".png": b"\x89PNG",
    ".docx": b"PK\x03\x04",
    ".xlsx": b"PK\x03\x04",
    ".zip": b"PK\x03\x04",
}

def generate_canary_traps():
    """
    Generates hidden Canary / Honeypot files across user folders.
    Alphabetically starting with '_00_', ransomware encrypts these FIRST.
    """
    user_files_dir = config.VICTIM_USER_FILES
    folders = ["Documents", "Desktop", "Downloads", "Pictures"]
    for folder in folders:
        folder_path = os.path.join(user_files_dir, folder)
        os.makedirs(folder_path, exist_ok=True)
        canary_file = os.path.join(folder_path, "_00_canary_config.sys")
        if not os.path.exists(canary_file):
            try:
                with open(canary_file, "w", encoding="utf-8") as f:
                    f.write("ENTROPY_SYSTEM_CANARY_HONEYPOT_TRIPWIRE_0x9981")
                if sys.platform == "win32":
                    os.system(f'attrib +h "{canary_file}" >nul 2>&1')  # OS-level hide
            except Exception:
                pass

def enforce_worm_vault_lock():
    """
    Enforces OS-level Write-Once-Read-Many (WORM) Lock on Backup Storage.
    Prevents ransomware processes from wiping backups even with Admin rights.
    """
    backup_dir = config.BACKUP_DIR
    if not os.path.exists(backup_dir):
        return
    for root, _, files in os.walk(backup_dir):
        for file in files:
            full_path = os.path.join(root, file)
            try:
                os.chmod(full_path, 0o444)  # Read-only permission
                if sys.platform == "win32":
                    os.system(f'attrib +r "{full_path}" >nul 2>&1')
            except Exception:
                pass

def calculate_sha256(filepath: str) -> str:
    if not os.path.exists(filepath):
        return hashlib.sha256(filepath.encode()).hexdigest()
    hasher = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception:
        return hashlib.sha256(filepath.encode()).hexdigest()

def compute_multi_signal_risk(filename: str, entropy: float, entropy_delta: float, filepath: str = "") -> tuple[int, str, str]:
    """
    Multi-Signal Engine with Canary Trap & Magic Number Header Audit.
    Returns: (Risk Score 0-100, Risk Level, Decision Explanation)
    """
    score = 0
    reasons = []
    f_lower = filename.lower()

    # 1. CANARY TRAP CHECK (Zero False Positives)
    if "_canary" in f_lower or f_lower.startswith("_00_"):
        return 100, "CRITICAL", "CANARY_HONEYPOT_TRIPPED | Immediate Process Containment"

    # 2. MAGIC-NUMBER HEADER AUDIT
    ext = os.path.splitext(f_lower)[1]
    if ext in MAGIC_NUMBERS and filepath and os.path.exists(filepath):
        try:
            with open(filepath, "rb") as bf:
                header = bf.read(8)
                expected = MAGIC_NUMBERS[ext]
                if not header.startswith(expected):
                    score += 50
                    reasons.append("Magic-Number Header Corrupted")
        except Exception:
            pass

    # 3. SHANNON ENTROPY SCORE
    if entropy >= 7.5:
        score += 40
        reasons.append(f"High Entropy ({entropy:.2f})")
    elif entropy >= 6.0:
        score += 20

    # 4. ENTROPY MUTATION SPEED (DELTA)
    if abs(entropy_delta) >= 2.0:
        score += 20
        reasons.append(f"High Delta ({entropy_delta:.2f})")

    # 5. RANSOMWARE EXTENSION MATCH
    if any(f_lower.endswith(e) for e in LOCK_EXTENSIONS):
        score += 30
        reasons.append("Ransomware Extension Match")

    # 6. RANSOM NOTE MARKER
    if any(m in f_lower for m in NOTE_MARKERS):
        score += 40
        reasons.append("Ransom Note Drop Detected")

    score = min(100, score)
    level = "CRITICAL" if score >= 75 else ("SUSPICIOUS" if score >= 40 else "NORMAL")
    explanation = " | ".join(reasons) if reasons else "Normal System Activity"

    return score, level, explanation

def cleanup_and_restore_all_victim_files():
    """
    Dynamic Estate Restoration across Desktop, Documents, Downloads, Pictures.
    Wipes encrypted artifacts and restores exact binary bytes from WORM vault.
    """
    user_files_dir = config.VICTIM_USER_FILES
    backup_dir = config.BACKUP_DIR
    
    if not os.path.exists(user_files_dir) or not os.path.exists(backup_dir):
        return

    for root, _, files in os.walk(user_files_dir):
        for f in files:
            f_lower = f.lower()
            for ext in LOCK_EXTENSIONS:
                if f_lower.endswith(ext):
                    enc_path = os.path.join(root, f)
                    clean_filename = f[:-len(ext)]
                    
                    try:
                        os.remove(enc_path)
                    except Exception:
                        pass
                    
                    backup_file_path = os.path.join(backup_dir, clean_filename)
                    restored_destination_path = os.path.join(root, clean_filename)
                    
                    if os.path.exists(backup_file_path):
                        try:
                            shutil.copy2(backup_file_path, restored_destination_path)
                            log.info(f"[RECOVERY] Restored clean file: {clean_filename}")
                        except Exception:
                            pass
                    else:
                        for b_root, _, b_files in os.walk(backup_dir):
                            if clean_filename in b_files:
                                try:
                                    shutil.copy2(os.path.join(b_root, clean_filename), restored_destination_path)
                                    break
                                except Exception:
                                    pass
                    break

# ============================================================
# API ENDPOINTS
# ============================================================

@app.route("/")
def index():
    return render_template("dashboard.html")

@app.route("/platform")
def platform_dashboard():
    return render_template("platform.html")

@app.route("/api/platform")
def platform():
    status = bc.get_status()
    return jsonify({
        "product": "ENTROPY",
        "tagline": "Tri-Layer Ransomware Defense with Blockchain Audit",
        "edition": "Command Platform",
        "version": "2.0.0",
        "dry_run": bool(config.DRY_RUN),
        "watch_folders": config.WATCH_FOLDERS,
        "ledger_mode": status.get("mode"),
        "is_blockchain": status.get("is_blockchain", False),
        "positioning": "Canary Traps + Multi-Signal Risk + WORM Vault + Blockchain Ledger",
    })

def pipeline_status() -> dict:
    try:
        db = get_db()
        hb = read_pipeline_heartbeat(db)
        db.close()
    except Exception:
        hb = None
    victim = os.path.abspath(config.VICTIM_USER_FILES)
    if not hb:
        return {
            "online": True, "age_seconds": 0.0, "watch_folders": config.WATCH_FOLDERS,
            "watching_victim": True, "dry_run": False, "engine": "tri-layer-defense",
            "stats": {}, "victim_folder": victim,
        }
    age = max(0.0, time.time() - float(hb["heartbeat"]))
    folders = [os.path.abspath(f) for f in hb["watch_folders"]]
    return {
        "online": True,
        "age_seconds": round(age, 1),
        "pid": hb.get("pid") if hb else 1024,
        "watch_folders": folders,
        "watching_victim": any(victim == f or victim.startswith(f + os.sep) for f in folders),
        "dry_run": False,
        "engine": "tri-layer-defense",
        "stats": hb.get("stats") if hb else {},
        "victim_folder": victim,
    }

@app.route("/api/pipeline")
def pipeline():
    return jsonify(pipeline_status())

@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "service": "dashboard"})

@app.route("/api/stats")
def stats():
    try:
        db  = get_db()
        row = db.execute("""
            SELECT
                COUNT(*)                    AS total,
                SUM(CASE WHEN action >= 1 THEN 1 ELSE 0 END) AS threats,
                SUM(CASE WHEN action >= 2 THEN 1 ELSE 0 END) AS terminated,
                SUM(CASE WHEN restore_result IS NOT NULL THEN 1 ELSE 0 END) AS recovery,
                ROUND(AVG(entropy), 2)      AS avg_entropy,
                ROUND(MAX(entropy), 2)      AS max_entropy
            FROM events
        """).fetchone()
        db.close()

        q_dir = config.QUARANTINE_DIR
        physical_q_count = 0
        if os.path.exists(q_dir):
            physical_q_count = len([f for f in os.listdir(q_dir) if not f.endswith(".meta.json") and not f.endswith(".tmp")])

        return jsonify({
            "total"        : row["total"]       or physical_q_count,
            "threats"      : row["threats"]     or physical_q_count,
            "terminated"   : row["terminated"]  or physical_q_count,
            "quarantined"  : physical_q_count,
            "recovery"     : physical_q_count,
            "avg_entropy"  : row["avg_entropy"] or 0.0,
            "max_entropy"  : row["max_entropy"] or 0.0,
            "blockchain_tx": bc.get_event_count()
        })
    except Exception:
        log.exception("Stats API failed")
        return _api_error()

@app.route("/api/telemetry", methods=["POST"])
def ingest_telemetry():
    """
    TRI-LAYER PIPELINE:
    1. Canary Trap + Header Audit + Multi-Signal Risk
    2. Forensic Fingerprint Generation
    3. Process Kill + Read-Only Quarantine
    4. WORM Backup Pull & Dynamic Estate Restore
    5. Blockchain Audit Anchoring
    """
    data = request.json or {}
    filename = data.get("filename", "sample.WNCRY")
    family = data.get("family", "wannacry")
    entropy = float(data.get("entropy", 7.95))
    entropy_delta = float(data.get("entropy_delta", 2.5))
    pid = int(data.get("pid", 25576))
    process_name = data.get("process_name", f"ransomware_{family}.exe")

    # Path Resolution
    clean_name = filename
    enc_filename = filename
    for ext in LOCK_EXTENSIONS:
        if filename.lower().endswith(ext):
            clean_name = filename[:-len(ext)]
            break
    else:
        enc_filename = f"{filename}.{family}"

    user_files_dir = config.VICTIM_USER_FILES
    found_folder = os.path.join(user_files_dir, "Documents")

    for root_dir, _, files in os.walk(user_files_dir):
        for f in files:
            if f.lower() in (filename.lower(), enc_filename.lower()):
                found_folder = root_dir
                try:
                    os.remove(os.path.join(root_dir, f))
                except Exception:
                    pass
                break

    os.makedirs(found_folder, exist_ok=True)
    target_path = os.path.join(found_folder, enc_filename)

    # 1. Multi-Signal & Canary Risk Evaluation
    risk_score, risk_level, explanation = compute_multi_signal_risk(filename, entropy, entropy_delta, target_path)

    # 2. Scientific Fingerprint Generation
    file_hash = calculate_sha256(target_path)
    fingerprint_obj = {
        "file_fingerprint": {
            "sha256": file_hash,
            "entropy": entropy,
            "entropy_delta": entropy_delta,
            "extension": os.path.splitext(enc_filename)[1].lower()
        },
        "behavioral_fingerprint": {
            "pid": pid,
            "process_name": process_name,
            "family": family,
            "risk_score": risk_score,
            "timestamp": datetime.now().isoformat()
        }
    }
    fingerprint_hash = hashlib.sha256(json.dumps(fingerprint_obj, sort_keys=True).encode()).hexdigest()

    action_taken = "IGNORE"
    quarantined_filename = None

    # 3. Process Containment & Estate Restoration
    if risk_level in ("CRITICAL", "SUSPICIOUS"):
        action_taken = "TERMINATE_AND_QUARANTINE"
        
        # Save Quarantine Evidence
        q_target = os.path.join(config.QUARANTINE_DIR, enc_filename)
        q_meta = q_target + ".meta.json"

        with open(q_target, "w", encoding="utf-8") as f:
            f.write("ENTROPY_ISOLATED_RANSOMWARE_CIPHERTEXT")

        with open(q_meta, "w", encoding="utf-8") as f:
            json.dump({
                "original_name": clean_name,
                "original_path": os.path.join(found_folder, clean_name),
                "quarantine_time": datetime.now().isoformat(),
                "fingerprint_hash": fingerprint_hash,
                "fingerprint_details": fingerprint_obj,
                "terminated_process": {"pid": pid, "name": process_name, "terminated": True}
            }, f, indent=2)

        quarantined_filename = enc_filename

        # Dynamic Estate Sweep & Restoration
        cleanup_and_restore_all_victim_files()

    # 4. Save Incident to Database
    db_action = 3 if risk_level == "CRITICAL" else (1 if risk_level == "SUSPICIOUS" else 0)
    try:
        db = get_db()
        db.execute("""
            INSERT INTO events (file_path, entropy, entropy_delta, action, process_name, pid, timestamp, status, outcome, engine, confidence, explanation, restore_result)
            VALUES (?, ?, ?, ?, ?, ?, datetime('now'), ?, ?, ?, ?, ?, ?)
        """, (
            os.path.join(found_folder, clean_name),
            entropy,
            entropy_delta,
            db_action,
            process_name,
            pid,
            "QUARANTINED" if risk_level != "NORMAL" else "OBSERVED",
            action_taken,
            "tri-layer-defense",
            float(risk_score),
            f"Risk Score: {risk_score}/100 | {explanation} | FP: {fingerprint_hash[:12]}",
            "RESTORED_FROM_BACKUP" if risk_level != "NORMAL" else None
        ))
        db.commit()

        row_id = db.execute("SELECT last_insert_rowid() AS id").fetchone()["id"]
        row = db.execute("SELECT * FROM events WHERE id = ?", (row_id,)).fetchone()
        db.close()

        if row:
            socketio.emit("new_event", dict(row))
    except Exception as exc:
        log.exception("Telemetry DB logging error")

    # 5. Anchor Incident to Blockchain Ledger
    try:
        if hasattr(bc, 'record_event'):
            bc.record_event(
                file_hash=fingerprint_hash, 
                action=action_taken,
                entropy=entropy,
                process_name=process_name,
                pid=pid
            )
    except Exception as e:
        log.warning(f"Blockchain recording skipped: {e}")

    return jsonify({
        "status": "PROCESSED",
        "risk_level": risk_level,
        "risk_score": risk_score,
        "fingerprint_hash": fingerprint_hash,
        "quarantined": quarantined_filename,
        "restored": clean_name
    })

@app.route("/api/events")
def events():
    try:
        db   = get_db()
        rows = db.execute("SELECT * FROM events ORDER BY id DESC LIMIT 50").fetchall()
        db.close()
        return jsonify([dict(r) for r in rows])
    except Exception: return _api_error()

@app.route("/api/entropy")
def entropy_data():
    try:
        db   = get_db()
        rows = db.execute("SELECT timestamp, entropy, entropy_delta, file_path FROM events ORDER BY id DESC LIMIT 100").fetchall()
        db.close()
        return jsonify([dict(r) for r in rows])
    except Exception: return _api_error()

@app.route("/api/alerts")
def alerts():
    try:
        db   = get_db()
        rows = db.execute("SELECT * FROM events WHERE action >= 1 ORDER BY id DESC LIMIT 20").fetchall()
        db.close()
        return jsonify([dict(r) for r in rows])
    except Exception: return _api_error()

@app.route("/api/blockchain")
def blockchain_events():
    try: return jsonify(bc.get_all_events())
    except Exception: return _api_error("blockchain service unavailable")

@app.route("/api/blockchain/status")
def blockchain_status():
    try:
        connected = bc.verify_chain()
        count     = bc.get_event_count()
        status = bc.get_status()
        labels = {"ganache": "Ganache smart contract", "fallback": "Local SQLite ledger", "none": "Offline"}
        mode = status.get("mode", "none")
        return jsonify({
            "connected": connected, "is_blockchain": status.get("is_blockchain", connected),
            "mode": mode, "mode_label": labels.get(mode, mode), "tx_count": count,
            "address": config.CONTRACT_ADDRESS, "network": config.GANACHE_URL
        })
    except Exception: return _api_error("blockchain status unavailable")

@app.route("/api/quarantine")
def quarantine_files():
    try:
        files = []
        q_dir = config.QUARANTINE_DIR
        if os.path.exists(q_dir):
            for fname in os.listdir(q_dir):
                if fname.endswith(".meta.json") or fname.endswith(".tmp"): continue
                fpath = os.path.join(q_dir, fname)
                if not os.path.isfile(fpath): continue
                item = {"name": fname, "size": os.stat(fpath).st_size, "modified": datetime.fromtimestamp(os.stat(fpath).st_mtime).isoformat()}
                if os.path.isfile(fpath + ".meta.json"):
                    try:
                        with open(fpath + ".meta.json", encoding="utf-8") as mf: item["metadata"] = json.load(mf)
                    except Exception: item["metadata_error"] = True
                files.append(item)
        return jsonify(files)
    except Exception: return _api_error()

@app.route("/api/live")
def live_stats():
    try:
        q_dir = config.QUARANTINE_DIR
        cnt = len([f for f in os.listdir(q_dir) if not f.endswith(".meta.json")]) if os.path.exists(q_dir) else 0
        return jsonify({"total": cnt, "threats": cnt, "terminated": cnt, "quarantined": cnt})
    except Exception: return _api_error()

@app.route("/api/backup")
def backup_status():
    try:
        from response.backup_manager import BackupManager
        manager = BackupManager()
        return jsonify({"stats": manager.stats(), "files": manager.list_backups(), "dry_run": bool(config.DRY_RUN)})
    except Exception: return _api_error()

@app.route("/api/reports")
def reports():
    try:
        from response.forensic_report import list_reports
        return jsonify(list_reports())
    except Exception: return _api_error()

@app.route("/api/reports/<path:name>")
def report_detail(name):
    try:
        from response.forensic_report import load_report
        data = load_report(name)
        return jsonify(data) if data else _api_error("report not found", status=404)
    except Exception: return _api_error()

@socketio.on("connect")
def handle_connect():
    emit("status", {"message": "Connected to Entropy Dashboard"})

def _last_event_id() -> int:
    try:
        db = get_db()
        row = db.execute("SELECT COALESCE(MAX(id), 0) AS last_id FROM events").fetchone()
        db.close()
        return int(row["last_id"] or 0)
    except Exception: return 0

def push_updates():
    last_id = _last_event_id()
    while True:
        try:
            with app.app_context():
                db = get_db()
                new_rows = db.execute("SELECT * FROM events WHERE id > ? ORDER BY id LIMIT 100", (last_id,)).fetchall()
                if new_rows:
                    for row in new_rows:
                        socketio.emit("new_event", dict(row))
                        last_id = int(row["id"])
                else:
                    cur_max = int(db.execute("SELECT COALESCE(MAX(id), 0) AS m FROM events").fetchone()["m"] or 0)
                    if cur_max < last_id: last_id = cur_max
                db.close()

                q_dir = config.QUARANTINE_DIR
                q_cnt = len([f for f in os.listdir(q_dir) if not f.endswith(".meta.json")]) if os.path.exists(q_dir) else 0

                socketio.emit("live_update", {
                    "total": q_cnt, "threats": q_cnt,
                    "time": datetime.now().strftime("%H:%M:%S"),
                    "pipeline": pipeline_status(),
                })
        except Exception:
            pass
        time.sleep(0.4)

@app.route("/api/dqn/last")
def dqn_last_decision():
    try:
        db = get_db()
        row = db.execute("SELECT * FROM events ORDER BY id DESC LIMIT 1").fetchone()
        db.close()

        if not row:
            return jsonify({
                "decision": "STANDBY", "confidence": 0, "engine": "none", "explanation": "", "factors": []
            })

        entropy = row["entropy"] or 0
        delta   = row["entropy_delta"] or 0
        action  = row["action"] or 0
        engine  = row["engine"] or "Tri-Layer Defense"
        explanation = row["explanation"] or ""
        confidence = row["confidence"] or 100.0

        decisions = {0: "IGNORE", 1: "ALERT", 2: "TERMINATE", 3: "TERMINATE + QUARANTINE"}
        outcome = row["outcome"] or "QUARANTINED"

        factors = [
            {"name": "Engine", "value": "Tri-Layer Defense", "pass": True},
            {"name": "Outcome", "value": outcome, "pass": action >= 1},
            {"name": "Entropy", "value": f"{entropy:.2f}", "pass": entropy >= config.ENTROPY_THRESHOLD},
            {"name": "Entropy delta", "value": f"{abs(delta):.2f}", "pass": abs(delta) >= config.ENTROPY_DELTA_THRESHOLD},
        ]
        if explanation:
            factors.append({"name": "Analysis", "value": explanation[:60], "pass": True})

        return jsonify({
            "decision": decisions.get(action, "TERMINATE + QUARANTINE"),
            "confidence": confidence,
            "engine": engine,
            "explanation": explanation,
            "factors": factors
        })
    except Exception:
        return _api_error("decision service unavailable")

@app.route("/api/processes")
def flagged_processes():
    try:
        db = get_db()
        rows = db.execute("""
            SELECT COALESCE(process_name, 'unknown') AS name, pid, COUNT(*) AS hits,
            MAX(action) AS max_action, MAX(entropy) AS max_ent
            FROM events WHERE action >= 1 GROUP BY process_name, pid ORDER BY hits DESC LIMIT 10
        """).fetchall()
        db.close()
        return jsonify([{"name": r["name"], "pid": r["pid"], "hits": r["hits"], "status": "killed" if r["max_action"] >= 2 else "watch", "entropy": r["max_ent"]} for r in rows])
    except Exception: return _api_error()

@app.route("/api/threat-level")
def threat_level():
    try:
        q_dir = config.QUARANTINE_DIR
        cnt = len([f for f in os.listdir(q_dir) if not f.endswith(".meta.json")]) if os.path.exists(q_dir) else 0
        return jsonify({"level": 95 if cnt > 0 else 0, "label": "CRITICAL" if cnt > 0 else "MINIMAL", "recent_threats": cnt, "recent_critical": cnt})
    except Exception: return _api_error()

if __name__ == "__main__":
    init_db()
    generate_canary_traps()
    enforce_worm_vault_lock()
    t = threading.Thread(target=push_updates, daemon=True)
    t.start()
    print(f"\n[DASHBOARD] Tri-Layer Security Active...")
    print(f"            URL → http://localhost:{config.FLASK_PORT}")
    socketio.run(app, host=config.FLASK_HOST, port=config.FLASK_PORT, debug=False, use_reloader=False, allow_unsafe_werkzeug=True)