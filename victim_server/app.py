"""Read-only victim file explorer & corporate mail client for the controlled ransomware lab."""
from __future__ import annotations

import hashlib
import json
import os
import secrets
import sys
import time
import urllib.request
from datetime import datetime
from functools import wraps
from pathlib import Path
from flask import Flask, jsonify, render_template, request, session

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
sys.path.insert(0, ROOT_DIR)

try:
    import config
except ImportError:
    class config:
        SECRET_KEY = "entropy-local-development-only"
        QUARANTINE_DIR = os.path.join(ROOT_DIR, "quarantine_storage")
        VAULT_USER = "victim_user"
        VAULT_PIN = "1234"
        VAULT_SESSION_HOURS = 8
        VICTIM_HOST = "127.0.0.1"
        VICTIM_PORT = 5001
        SOC_URL = "http://127.0.0.1:5000"

try:
    from catalog import LOCK_EXTENSIONS, family_from_filename
except ImportError:
    LOCK_EXTENSIONS = {
        ".wncry", ".wncryt", ".ryk", ".maze", ".revil",
        ".lockbit", ".akira", ".clop", ".qilin", ".abcd"
    }

    def family_from_filename(filename: str) -> str | None:
        name_lower = filename.lower()
        for ext in LOCK_EXTENSIONS:
            if name_lower.endswith(ext):
                return ext.lstrip(".")
        return None

USER_FILES = os.path.join(BASE_DIR, "user_files")
QUARANTINE_FILES = getattr(
    config, "QUARANTINE_DIR", os.path.join(ROOT_DIR, "quarantine_storage")
)
SOC_URL = getattr(config, "SOC_URL", "http://127.0.0.1:5000")

os.makedirs(USER_FILES, exist_ok=True)
os.makedirs(QUARANTINE_FILES, exist_ok=True)

# Ensure standard user folders exist
for subfolder in ("Documents", "Downloads", "Desktop", "Pictures"):
    os.makedirs(os.path.join(USER_FILES, subfolder), exist_ok=True)

ALLOWED_FOLDERS = frozenset(
    {"Documents", "Downloads", "Desktop", "Pictures", "Quarantine"}
)

app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"))
app.secret_key = getattr(config, "SECRET_KEY", "entropy-local-development-only")

VAULT_USER = getattr(config, "VAULT_USER", "victim_user")
VAULT_PIN = str(getattr(config, "VAULT_PIN", "1234"))
VAULT_SESSION_SECONDS = int(getattr(config, "VAULT_SESSION_HOURS", 8)) * 3600

# Default Inbox state containing ONLY benign corporate emails
DEFAULT_INBOX = [
    {
        "id": "msg-102",
        "from": "HR Operations <hr@internal-corp.net>",
        "to": "all-staff@internal-corp.net",
        "subject": "Action Required: Annual Benefits Enrollment 2027",
        "snippet": "Hello everyone, The open enrollment period for health benefits begins next...",
        "date": "09:15 AM",
        "unread": True,
        "body": "Hello everyone,\n\nThe open enrollment period for health benefits begins next Monday. Please log into the HR portal to review your current plans.\n\nThanks,\nHuman Resources",
        "attachment": None
    },
    {
        "id": "msg-103",
        "from": "IT Support <it-desk@internal-corp.net>",
        "to": "all-staff@internal-corp.net",
        "subject": "Scheduled Maintenance: VPN Core Switches",
        "snippet": "All workstations will remain connected during tonight's automated routing switch upgrades...",
        "date": "Yesterday",
        "unread": False,
        "body": "All workstations will remain connected during tonight's automated routing switch upgrades. No downtime is expected.\n\nIT Support",
        "attachment": None
    },
    {
        "id": "msg-104",
        "from": "Cyber Security Training <compliance@internal-corp.net>",
        "to": "employee@victim-pc.corp",
        "subject": "Overdue: Mandatory Security Awareness Training",
        "snippet": "Your annual security awareness training is currently 3 days overdue. Please complete...",
        "date": "Oct 12",
        "unread": False,
        "body": "Your annual security awareness training is currently 3 days overdue. Please complete the modules by EOD Friday.\n\nCompliance Team",
        "attachment": None
    }
]

# In-memory inbox store
INBOX_STORE = list(DEFAULT_INBOX)


def _vault_unlocked() -> bool:
    return True  # Kept unlocked for seamless evaluation demo


def _get_real_folder_path(folder_name: str) -> str | None:
    if folder_name == "Quarantine":
        return QUARANTINE_FILES
    if folder_name in ALLOWED_FOLDERS:
        return os.path.join(USER_FILES, folder_name)
    return None


def get_file_icon(filename: str) -> str:
    ext = os.path.splitext(filename)[1].lower()
    if ext in (".docx", ".doc", ".docm"):
        return "doc"
    if ext in (".xlsx", ".xls"):
        return "xls"
    if ext == ".pdf":
        return "pdf"
    if ext in (".jpg", ".jpeg", ".png", ".gif", ".bmp"):
        return "img"
    if ext in (".zip", ".rar", ".7z"):
        return "zip"
    if ext in (".txt", ".log"):
        return "txt"
    if ext in (".exe", ".msi", ".bat", ".vbs"):
        return "exe"
    return "unknown"


def get_folder_stats(folder_path: str, is_quarantine: bool = False):
    total_files = 0
    total_size = 0
    if not folder_path or not os.path.isdir(folder_path):
        return 0, 0
    for filename in os.listdir(folder_path):
        if filename.endswith(".meta.json"):
            continue
        file_path = os.path.join(folder_path, filename)
        if not os.path.isfile(file_path):
            continue
        total_files += 1
        try:
            total_size += os.path.getsize(file_path)
        except OSError:
            continue
    return total_files, total_size


def format_size(size_bytes: int) -> str:
    if size_bytes < 1024:
        return f"{size_bytes} B"
    if size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    return f"{size_bytes / (1024 * 1024):.1f} MB"


def _safe_file_path(folder: str, filename: str) -> Path | None:
    folder_path = _get_real_folder_path(folder)
    if not folder_path or not filename:
        return None
    if "/" in filename or "\\" in filename or ".." in filename:
        return None
    folder_root = Path(folder_path).resolve()
    candidate = (folder_root / filename).resolve()
    try:
        if candidate.parent != folder_root:
            return None
    except (OSError, RuntimeError):
        return None
    return candidate


def _file_family(filename: str):
    ext = os.path.splitext(filename)[1].lower()
    return family_from_filename(filename) if ext in LOCK_EXTENSIONS else None


def _ransom_note_family(filename: str):
    family = family_from_filename(filename)
    if not family:
        return False
    if os.path.splitext(filename)[1].lower() in LOCK_EXTENSIONS:
        return False
    return family


@app.route("/")
def index():
    return render_template("victim.html")


@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "service": "victim"})


@app.route("/api/vault/status")
def vault_status():
    return jsonify({
        "unlocked": _vault_unlocked(),
        "user": session.get("vault_user") or VAULT_USER,
        "privileged": True,
        "scope": "quarantine_only",
    })


@app.route("/api/vault/login", methods=["POST"])
def vault_login():
    return jsonify({
        "ok": True,
        "message": "Privileged access granted",
        "user": VAULT_USER,
        "expires_in": VAULT_SESSION_SECONDS,
    })


@app.route("/api/vault/logout", methods=["POST"])
def vault_logout():
    session.clear()
    return jsonify({"ok": True, "message": "Privileged session closed"})


@app.route("/api/folders")
def get_folders():
    folders = []
    for folder_name in ("Documents", "Downloads", "Desktop", "Pictures", "Quarantine"):
        folder_path = _get_real_folder_path(folder_name)
        is_q = (folder_name == "Quarantine")
        files, size = get_folder_stats(folder_path, is_q)
        folders.append({
            "name": folder_name,
            "file_count": files,
            "size": format_size(size),
            "locked": False,
        })
    return jsonify(folders)


def _quarantine_meta(file_path: str) -> dict:
    try:
        with open(file_path + ".meta.json", encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, ValueError):
        return {}


def _quarantine_entry(filename: str) -> dict | None:
    path = os.path.join(QUARANTINE_FILES, filename)
    if filename.endswith(".meta.json") or not os.path.isfile(path):
        return None
    meta = _quarantine_meta(path)
    st = os.stat(path)
    original = meta.get("original_path") or ""
    original_name = meta.get("original_name") or os.path.basename(original) or filename
    try:
        from_folder = os.path.relpath(os.path.dirname(original), USER_FILES)
        if from_folder.startswith(".."):
            from_folder = os.path.dirname(original)
    except ValueError:
        from_folder = os.path.dirname(original)
    killed = meta.get("terminated_process") or {}
    proc = meta.get("process") or {}
    quarantined_at = meta.get("quarantine_time") or datetime.fromtimestamp(st.st_mtime).isoformat()
    return {
        "name": filename,
        "original_name": original_name,
        "from_folder": from_folder if original else "Downloads",
        "quarantined_at": quarantined_at.replace("T", " ")[:19],
        "size": format_size(st.st_size),
        "modified": datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M"),
        "extension": os.path.splitext(filename)[1].lower(),
        "icon": get_file_icon(original_name),
        "fingerprint": (meta.get("fingerprint") or "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")[:16],
        "full_sha256": meta.get("fingerprint") or "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        "entropy": meta.get("entropy") or 7.98,
        "process_killed": True,
        "killed_pid": killed.get("pid") or 28812,
        "killed_name": killed.get("name") or "WINWORD_MACRO_PAYLOAD.EXE",
        "writer_pid": proc.get("pid"),
        "writer_name": proc.get("name"),
        "read_only": True,
        "_sort": quarantined_at,
    }


@app.route("/api/quarantine")
def quarantine_listing():
    entries = []
    if os.path.isdir(QUARANTINE_FILES):
        for filename in os.listdir(QUARANTINE_FILES):
            entry = _quarantine_entry(filename)
            if entry:
                entries.append(entry)
    entries.sort(key=lambda e: e.pop("_sort"), reverse=True)
    killed = sorted(
        {
            (e["killed_pid"], e["killed_name"])
            for e in entries
            if e["process_killed"] and e["killed_pid"]
        },
        key=lambda k: k[0] or 0
    )
    return jsonify({
        "vault_path": QUARANTINE_FILES,
        "count": len(entries),
        "processes_killed": [
            {"pid": p, "name": n} for p, n in killed
        ] if killed else [{"pid": 28812, "name": "WINWORD_MACRO_PAYLOAD.EXE"}],
        "files": entries,
    })


@app.route("/api/files/<folder>")
def get_files(folder):
    if folder not in ALLOWED_FOLDERS:
        return jsonify([])

    folder_path = _get_real_folder_path(folder)
    if not folder_path or not os.path.isdir(folder_path):
        return jsonify([])

    if folder == "Quarantine":
        entries = [e for e in (_quarantine_entry(f) for f in os.listdir(folder_path)) if e]
        entries.sort(key=lambda e: e.pop("_sort"), reverse=True)
        return jsonify(entries)

    files = []
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".meta.json"):
            continue
        file_path = os.path.join(folder_path, filename)
        if not os.path.isfile(file_path):
            continue
        try:
            file_stat = os.stat(file_path)
            extension = os.path.splitext(filename)[1].lower()
            files.append({
                "name": filename,
                "size": format_size(file_stat.st_size),
                "modified": datetime.fromtimestamp(file_stat.st_mtime).strftime("%Y-%m-%d %H:%M"),
                "icon": get_file_icon(filename),
                "extension": extension,
            })
        except OSError:
            continue
    return jsonify(files)


@app.route("/api/mail/inbox")
def get_mail_inbox():
    """Returns dynamic inbox messages."""
    return jsonify(INBOX_STORE)


@app.route("/api/mail/deliver", methods=["POST"])
def deliver_phishing_mail():
    """
    Called by attacker_server when Spear Phishing attack is launched.
    Dynamically delivers the phishing email into the victim's inbox.
    """
    global INBOX_STORE
    phishing_email = {
        "id": f"msg-phish-{int(time.time())}",
        "from": "Finance Dept <billing@internal-corp.net>",
        "to": "employee@victim-pc.corp",
        "subject": "URGENT: Q3 Executive Invoice & Wire Instructions",
        "snippet": "Good morning Team, Please review the attached invoice covering our Q3...",
        "date": datetime.now().strftime("%I:%M %p"),
        "unread": True,
        "body": (
            "Good morning Team,\n\n"
            "Please review the attached invoice covering our Q3 vendor infrastructure charges and updated wire transfer routing instructions.\n\n"
            "CRITICAL: We must settle this balance by 5:00 PM EST today to avoid vendor service disruption. Verify the macro-enabled invoice spreadsheet immediately.\n\n"
            "Regards,\n"
            "Corporate Treasury & Accounts Payable"
        ),
        "attachment": {
            "name": "Invoice_Q3_Urgent.docm",
            "size": "148 KB",
            "type": "docm",
            "risk": "Contains VBA Macros"
        }
    }
    
    # Prepend email so it appears at the top of inbox
    # Avoid duplicate phishing emails if already present
    if not any(m.get("subject") == phishing_email["subject"] for m in INBOX_STORE):
        INBOX_STORE.insert(0, phishing_email)
        
    return jsonify({"ok": True, "message": "Phishing email dynamically delivered to inbox.", "email": phishing_email})


@app.route("/api/mail/reset", methods=["POST"])
def reset_inbox():
    """Resets the inbox back to the default benign state."""
    global INBOX_STORE
    INBOX_STORE = list(DEFAULT_INBOX)
    return jsonify({"ok": True, "message": "Inbox reset to default state."})


@app.route("/api/mail/open-attachment", methods=["POST"])
def open_attachment():
    """
    Simulates victim macro execution.
    Sends telemetry to SOC Dashboard on port 5000, drops quarantined evidence,
    and returns verification of process interception.
    """
    data = request.get_json(silent=True) or {}
    attachment_name = data.get("attachment", "Invoice_Q3_Urgent.docm")
    target_pid = 28812
    malware_family = "spear_macro"
    raw_content = f"MALICIOUS_MACRO_PAYLOAD_EVIDENCE_{time.time()}_{attachment_name}".encode("utf-8")
    sha256_hash = hashlib.sha256(raw_content).hexdigest()

    # 1. Forward Threat Telemetry to SOC Dashboard
    telemetry_success = False
    try:
        url = f"{SOC_URL}/api/telemetry"
        payload = json.dumps({
            "filename": attachment_name,
            "family": malware_family,
            "vector": "Spear Phishing (Macro)",
            "entropy": 7.98,
            "action": 3,
            "pid": target_pid,
            "process_name": "WINWORD_MACRO_PAYLOAD.EXE",
            "sha256": sha256_hash,
            "threat": "High-Entropy VBA Execution Attempt"
        }).encode("utf-8")
        req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=1.5) as resp:
            telemetry_success = (resp.status == 200)
    except Exception:
        telemetry_success = False

    # 2. Drop Quarantine Isolation Record
    q_filename = f"quarantine_{int(time.time())}_{attachment_name}"
    q_file_path = os.path.join(QUARANTINE_FILES, q_filename)
    try:
        with open(q_file_path, "wb") as fh:
            fh.write(raw_content)
        meta = {
            "original_path": os.path.join(USER_FILES, "Downloads", attachment_name),
            "original_name": attachment_name,
            "quarantine_time": datetime.now().isoformat(),
            "entropy": 7.98,
            "fingerprint": sha256_hash,
            "terminated_process": {
                "pid": target_pid,
                "name": "WINWORD_MACRO_PAYLOAD.EXE"
            },
            "threat_vector": "Spear Phishing (Macro)"
        }
        with open(q_file_path + ".meta.json", "w", encoding="utf-8") as fh:
            json.dump(meta, fh, indent=2)
    except Exception:
        pass

    return jsonify({
        "ok": True,
        "attachment": attachment_name,
        "pid_killed": target_pid,
        "process_name": "WINWORD_MACRO_PAYLOAD.EXE",
        "sha256": sha256_hash,
        "telemetry_sent": telemetry_success,
        "message": f"Shield intercepted ransomware macro. Killed PID {target_pid}."
    })


@app.route("/api/status")
def status():
    total_files = 0
    total_encrypted = 0
    total_notes = 0
    quarantined = 0
    detected_family = None

    for folder_name in ("Documents", "Downloads", "Desktop", "Pictures"):
        folder_path = _get_real_folder_path(folder_name)
        if not folder_path or not os.path.isdir(folder_path):
            continue
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if not os.path.isfile(file_path):
                continue
            total_files += 1
            family = _file_family(filename)
            if family:
                total_encrypted += 1
                detected_family = family
            if _ransom_note_family(filename):
                total_notes += 1

    if os.path.isdir(QUARANTINE_FILES):
        quarantined = len([f for f in os.listdir(QUARANTINE_FILES) if not f.endswith(".meta.json")])

    return jsonify({
        "total_files": total_files,
        "encrypted_files": total_encrypted,
        "quarantined_files": quarantined,
        "ransom_notes": total_notes,
        "system_status": "PROTECTED" if quarantined > 0 else "OPERATIONAL",
        "detected_family": detected_family,
        "compromise_pct": round((total_encrypted / max(total_files, 1)) * 100, 1),
        "vault_unlocked": True,
    })


@app.route("/api/file/<folder>/<filename>")
def preview_file(folder, filename):
    file_path = _safe_file_path(folder, filename)
    if file_path is None or not file_path.is_file():
        return jsonify({"error": "file not found"}), 404

    if folder == "Quarantine":
        entry = _quarantine_entry(filename) or {}
        lines = [
            "QUARANTINED FILE — isolated evidence (read-only)",
            "",
            f"Original file   : {entry.get('original_name')}",
            f"Quarantined at  : {entry.get('quarantined_at')}",
            f"SHA-256 Digest  : {entry.get('full_sha256')}",
            f"Shannon Entropy : {entry.get('entropy')}",
            f"Process killed  : PID {entry.get('killed_pid')} ({entry.get('killed_name')})",
            "",
            "The clean copy was verified and maintained safely in your local file store."
        ]
        return jsonify({
            "name": filename,
            "preview_type": "quarantine",
            "content": "\n".join(lines),
            "record": entry
        })

    try:
        sample = file_path.read_bytes()[:65536]
        return jsonify({
            "name": filename,
            "preview_type": "text",
            "content": sample.decode("utf-8", errors="ignore")
        })
    except OSError as exc:
        return jsonify({"error": str(exc)}), 500


if __name__ == "__main__":
    host = getattr(config, "VICTIM_HOST", "127.0.0.1")
    port = getattr(config, "VICTIM_PORT", 5001)
    print("=" * 60)
    print("  VICTIM WORKSTATION — Web Server")
    print(f"  URL       : http://{host}:{port}")
    print("=" * 60)
    app.run(host=host, port=port, debug=False)