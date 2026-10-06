"""Attacker C2 orchestration panel and MITRE ATT&CK attack launcher."""
from __future__ import annotations

import hmac
import ipaddress
import json
import os
import re
import signal
import sqlite3
import subprocess
import sys
import threading
import time
import urllib.request
from collections import deque
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
VICTIM_DIR = os.path.join(ROOT_DIR, "victim_server")
USER_FILES = os.path.join(VICTIM_DIR, "user_files")

HTML_PATH = os.path.join(BASE_DIR, "templates", "attacker.html")

sys.path.insert(0, ROOT_DIR)
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, VICTIM_DIR)

try:
    import config
except ImportError:
    class config:
        DB_PATH = os.path.join(ROOT_DIR, "entropy.db")
        QUARANTINE_DIR = os.path.join(ROOT_DIR, "quarantine_storage")
        CONTROL_TOKEN = "entropy-lab"

try:
    import ransomware_engines as engines
except ImportError:
    class engines:
        @staticmethod
        def list_families():
            return [
                "wannacry", "ryuk", "lockbit", "revil",
                "maze", "akira", "clop", "qilin", "macro_spearphish"
            ]

try:
    from create_fake_files import restore_all_files
except Exception:
    restore_all_files = None

_proc_lock = threading.Lock()
_proc = None
_proc_family = None
_stream = deque(maxlen=300)
_control_path = os.path.join(ROOT_DIR, "attacker_control.json")

_KILLED_EXIT = 42

_SCAN_RE = re.compile(r"scan complete:\s*(\d+)\s*targets,\s*(\d+)\s*skipped")
_HIT_RE = re.compile(r"encrypted\s+(\d+)/(\d+)")
_NOTE_RE = re.compile(r"Note dropped:")
_BYTES_RE = re.compile(r"\((\d+)\s*bytes\)")


def send_cors_headers(handler):
    handler.send_header("Access-Control-Allow-Origin", "*")
    handler.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    handler.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization, X-Requested-With")


def _relay_telemetry(filename: str, family: str, pid: int = 28812):
    try:
        url = "http://127.0.0.1:5000/api/telemetry"
        payload = json.dumps({
            "filename": filename,
            "family": family,
            "entropy": 7.98,
            "action": 3,
            "pid": pid,
            "process_name": f"ransomware_{family}.exe"
        }).encode("utf-8")
        req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
        urllib.request.urlopen(req, timeout=1.0)
    except Exception:
        pass


def _deliver_phishing_email():
    """Dynamically sends the Spear Phishing Email to the Victim Workstation on port 5001."""
    try:
        url = "http://127.0.0.1:5001/api/mail/deliver"
        req = urllib.request.Request(url, data=b"{}", headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=2.0) as resp:
            return resp.status == 200
    except Exception as e:
        sys.stderr.write(f"[ATTACKER] Could not deliver email to victim: {e}\n")
        return False


def _write_control(payload):
    current = {}
    try:
        with open(_control_path, encoding="utf-8") as fh:
            current = json.load(fh)
    except (OSError, ValueError):
        pass
    current.update(payload)
    try:
        with open(_control_path, "w", encoding="utf-8") as fh:
            json.dump(current, fh)
    except OSError:
        pass


def _append_log(text: str):
    timestamp = time.strftime("%H:%M:%S")
    entry = {
        "time": timestamp,
        "timestamp": timestamp,
        "msg": text,
        "text": text,
        "line": text
    }
    with _proc_lock:
        _stream.append(entry)


def _simulate_initial_access(family_id: str, vector: str):
    """
    Simulates the MITRE ATT&CK Initial Access vector dynamically 
    before deploying or staging the ransomware payload.
    """
    if vector in ("phishing", "spear_phishing_macro", "macro"):
        _append_log(f"[SPEAR-PHISHING] Crafting weaponized document: 'Invoice_Q3_Urgent.docm' (VBA Stager)...")
        time.sleep(0.7)
        _append_log(f"[SPEAR-PHISHING] Sending targeted email to: employee@victim-pc.corp (Subject: 'URGENT: Q3 Executive Invoice')...")
        
        # DYNAMIC EMAIL DELIVERY TO VICTIM
        success = _deliver_phishing_email()
        if success:
            _append_log(f"[SPEAR-PHISHING] SUCCESS: Phishing email delivered to victim workstation inbox (port 5001).")
        else:
            _append_log(f"[SPEAR-PHISHING] WARNING: Victim mail server endpoint unreachable, continuing offline mode.")

        time.sleep(0.6)
        _append_log(f"[SPEAR-PHISHING] Email delivered to inbox. Awaiting victim macro interaction on workstation...")

    elif vector == "usb":
        _append_log(f"[ROGUE USB] Malicious BadUSB inserted into victim-pc workstation by insider.")
        time.sleep(0.7)
        _append_log(f"[ROGUE USB] HID Keyboard injection initiated. Injecting obfuscated keystrokes...")
        time.sleep(0.5)
        _append_log(f"[ROGUE USB] Spawning hidden PowerShell terminal session...")
        time.sleep(0.6)
        _append_log(f"[ROGUE USB] Executing living-off-the-land script. Dropping payload ({family_id})...")

    else:  # zero_click (default)
        _append_log(f"[ZERO-CLICK] Scanning subnet for active hosts... Target: victim-pc (192.168.1.105)")
        time.sleep(0.7)
        _append_log(f"[ZERO-CLICK] Probing open ports: 135/tcp (RPC), 139/tcp (NetBIOS), 445/tcp (SMB)...")
        time.sleep(0.5)
        _append_log(f"[ZERO-CLICK] VULNERABILITY DETECTED: Windows SMBv1 Memory Corruption (MS17-010 EternalBlue)")
        time.sleep(0.6)
        _append_log(f"[ZERO-CLICK] Transmitting SMB buffer overflow packet. Remote Code Execution achieved!")

    time.sleep(0.5)
    _append_log(f"[PAYLOAD] Triggering ransomware execution cycle. Escalating to SYSTEM privileges...")


def _stream_reader(proc):
    try:
        for line in proc.stdout:
            text = line.rstrip("\n")
            if text:
                _append_log(text)
                if "encrypt" in text.lower() or "note" in text.lower() or "." in text:
                    filename = f"sample_{int(time.time() * 1000)}.{_proc_family or 'wncry'}"
                    parts = text.split()
                    for p in parts:
                        if "." in p and len(p) > 3:
                            filename = os.path.basename(p.strip("():,"))
                            break
                    _relay_telemetry(filename, _proc_family or "wannacry", proc.pid or 28812)
    except (OSError, ValueError):
        pass


def _spawn(family_id, vector="zero_click"):
    global _proc, _proc_family
    with _proc_lock:
        if _proc is not None and _proc.poll() is None:
            return False, f"{_proc_family} already running"
        _stream.clear()
        _write_control({"factor": 1.0, "paused": False})

        def _async_launch():
            global _proc
            # Trigger the attack narrative in the logs
            _simulate_initial_access(family_id, vector)
            
            command = [
                sys.executable,
                "-m",
                "attacker_server.ransomware_engines",
                family_id,
                "--control",
                _control_path,
            ]
            try:
                _proc = subprocess.Popen(
                    command,
                    cwd=ROOT_DIR,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1,
                )
                threading.Thread(target=_stream_reader, args=(_proc,), daemon=True).start()
            except Exception as e:
                _append_log(f"[ENGINE ERROR] Could not spawn local binary: {e}")

        threading.Thread(target=_async_launch, daemon=True).start()
        _proc_family = family_id

    return True, "ok"


def _child_state():
    with _proc_lock:
        proc = _proc
        family = _proc_family
        lines = list(_stream)

    if proc is None:
        return {
            "active": False, "family": family or None, "phase": "IDLE",
            "progress": 0, "log": lines, "pid": 28812 if lines else None,
            "defender_killed": False,
        }

    alive = proc.poll() is None
    last_entry = lines[-1] if lines else ""
    last_text = last_entry["msg"] if isinstance(last_entry, dict) else str(last_entry)

    targets = skipped = hit = total = notes = 0
    bytes_encrypted = 0
    for entry in lines:
        line = entry["msg"] if isinstance(entry, dict) else str(entry)
        m = _SCAN_RE.search(line)
        if m:
            targets, skipped = int(m.group(1)), int(m.group(2))
        m = _HIT_RE.search(line)
        if m:
            hit, total = int(m.group(1)), int(m.group(2))
        if _NOTE_RE.search(line):
            notes += 1
        m = _BYTES_RE.search(line)
        if m and "encrypting" in line:
            bytes_encrypted += int(m.group(1))

    defender_killed = ("TERMINATED BY DEFENSE" in last_text) or (
        (not alive) and proc.returncode == _KILLED_EXIT
    )

    if defender_killed:
        phase = "KILLED_BY_DEFENDER"
    elif alive:
        phase = "PAUSED" if _read_control_or_default().get("paused") else "ENCRYPTING"
    elif proc.returncode == 0:
        phase = "COMPLETED" if total else "STOPPED"
    else:
        phase = "STOPPED"

    return {
        "active": alive,
        "family": family,
        "phase": phase,
        "progress": round(min(100, hit / max(total, 1) * 100), 1) if total else 0,
        "targets": targets,
        "files_hit": hit,
        "files_skipped": skipped,
        "notes_dropped": notes,
        "bytes_encrypted": bytes_encrypted,
        "pid": proc.pid if alive else 28812,
        "returncode": proc.returncode if proc else None,
        "defender_killed": defender_killed,
        "log": lines,
    }


def _read_control_or_default():
    try:
        with open(_control_path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return {}


def _stop_child(operator: bool):
    global _proc
    with _proc_lock:
        proc = _proc
    if proc is None or proc.poll() is not None:
        return False
    try:
        proc.send_signal(signal.SIGINT if operator else signal.SIGTERM)
    except (OSError, ProcessLookupError):
        return False
    return True


def _reset_lab_estate():
    """Triggered when user clicks 'restore target'."""
    _stop_child(operator=True)
    
    # 1. Restore victim fake files
    try:
        if restore_all_files is not None:
            restore_all_files()
        else:
            fixtures_script = os.path.join(VICTIM_DIR, "create_fake_files.py")
            if os.path.exists(fixtures_script):
                subprocess.run([sys.executable, fixtures_script, "--clean"], cwd=ROOT_DIR, capture_output=True)
    except Exception as exc:
        sys.stderr.write(f"[reset] Restore error: {exc}\n")

    # 2. Reset victim mail inbox
    try:
        url = "http://127.0.0.1:5001/api/mail/reset"
        req = urllib.request.Request(url, data=b"{}", headers={"Content-Type": "application/json"}, method="POST")
        urllib.request.urlopen(req, timeout=1.5)
    except Exception:
        pass

    # 3. WIPE ALL SOC DATABASE TABLES to reset SOC Dashboard to 0000
    db_path = getattr(config, "DB_PATH", os.path.join(ROOT_DIR, "entropy.db"))
    if os.path.exists(db_path):
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            # Fetch all tables
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            for table_name in tables:
                t_name = table_name[0]
                if t_name != "sqlite_sequence": # don't delete internal sqlite tables
                    cursor.execute(f"DELETE FROM {t_name};")
            conn.commit()
            conn.close()
            sys.stderr.write("[RESET] SOC database tables cleared successfully.\n")
        except Exception as e:
            sys.stderr.write(f"[RESET ERROR] Could not wipe DB: {e}\n")

    # 4. Clear quarantine storage
    q_dir = getattr(config, "QUARANTINE_DIR", os.path.join(ROOT_DIR, "quarantine_storage"))
    if os.path.exists(q_dir):
        for item in os.listdir(q_dir):
            try:
                os.remove(os.path.join(q_dir, item))
            except Exception:
                pass


def victim_snapshot():
    total = 0
    locked = 0
    notes = 0
    lock_extensions = (
        ".wncry", ".wncryt", ".ryk", ".maze", ".revil",
        ".lockbit", ".akira", ".clop", ".qilin", ".abcd"
    )
    note_markers = (
        "@please_read_me@", "ryukreadme", "restore-my-files",
        "recover-", "maze-readme"
    )

    if not os.path.isdir(USER_FILES):
        return {"exists": True, "total": 10, "locked": 0, "notes": 0}

    for directory, _, filenames in os.walk(USER_FILES):
        for filename in filenames:
            total += 1
            extension = os.path.splitext(filename)[1].lower()
            lowercase_name = filename.lower()
            if extension in lock_extensions:
                locked += 1
            if any(marker in lowercase_name for marker in note_markers):
                notes += 1

    return {"exists": True, "total": max(total, 1), "locked": locked, "notes": notes}


def read_json(handler):
    content_length = int(handler.headers.get("Content-Length") or 0)
    if content_length <= 0:
        return {}
    raw = handler.rfile.read(content_length)
    try:
        return json.loads(raw.decode("utf-8"))
    except Exception:
        return {}


def send_json(handler, payload, status=200):
    body = json.dumps(payload).encode("utf-8")
    handler.send_response(status)
    send_cors_headers(handler)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.send_header("Cache-Control", "no-store")
    handler.end_headers()
    handler.wfile.write(body)


def send_text(handler, text):
    body = text.encode("utf-8")
    handler.send_response(200)
    send_cors_headers(handler)
    handler.send_header("Content-Type", "text/plain; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


def send_html(handler):
    if not os.path.exists(HTML_PATH):
        handler.send_error(404, "attacker.html not found")
        return

    with open(HTML_PATH, "r", encoding="utf-8") as file:
        html = file.read()

    host_header = handler.headers.get("Host", "127.0.0.1:8001")
    host = host_header.split(":", 1)[0]
    scheme = "http"

    victim_url = f"{scheme}://{host}:5001"
    dashboard_url = f"{scheme}://{host}:5000"
    attacker_url = f"{scheme}://{host}:8001"

    html = html.replace("__VICTIM_URL__", victim_url)
    html = html.replace("__DASHBOARD_URL__", dashboard_url)
    html = html.replace("__ATTACKER_URL__", attacker_url)
    html = html.replace("__CONTROL_TOKEN__", getattr(config, "CONTROL_TOKEN", "entropy-lab"))

    body = html.encode("utf-8")
    handler.send_response(200)
    send_cors_headers(handler)
    handler.send_header("Content-Type", "text/html; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


class Handler(SimpleHTTPRequestHandler):
    def log_message(self, format_string, *args):
        sys.stderr.write("[attacker] " + (format_string % args) + "\n")

    def do_OPTIONS(self):
        self.send_response(200)
        send_cors_headers(self)
        self.send_header("Content-Length", "0")
        self.end_headers()

    def do_GET(self):
        path = urlparse(self.path).path
        if path in {"/", "/index.html", "/attacker.html"}:
            send_html(self)
            return
        if path == "/api/families":
            send_json(self, engines.list_families())
            return
        if path == "/api/stats":
            stats = _child_state()
            stats["victim"] = victim_snapshot()
            send_json(self, stats)
            return
        if path == "/api/log":
            stats = _child_state()
            lines = [entry.get("msg", "") if isinstance(entry, dict) else str(entry) for entry in stats.get("log", [])]
            send_text(self, "\n".join(lines) + "\n")
            return
        self.send_error(404, "not found")

    def do_POST(self):
        path = urlparse(self.path).path
        data = read_json(self)

        if path == "/api/launch":
            family = (data.get("family") or "wannacry").strip().lower()
            vector = (data.get("vector") or "spear_phishing_macro").strip().lower()
            
            ok, message = _spawn(family, vector)
            
            if not ok:
                send_json(self, {"ok": False, "error": message}, status=200)
                return
            send_json(self, {"ok": True, "family": family, "vector": vector, "pid": 28812, "stats": _child_state()})
            return

        if path == "/api/stop":
            stopped = _stop_child(operator=True)
            send_json(self, {"ok": True, "stopped": bool(stopped)})
            return

        if path == "/api/pause":
            _write_control({"paused": True})
            send_json(self, {"ok": True, "paused": True})
            return

        if path == "/api/resume":
            _write_control({"paused": False})
            send_json(self, {"ok": True, "paused": False})
            return

        if path == "/api/speed":
            factor = float(data.get("factor", 1.0))
            _write_control({"factor": factor})
            send_json(self, {"ok": True, "speed_factor": factor})
            return

        if path == "/api/reset":
            _reset_lab_estate()
            send_json(self, {"ok": True, "victim": victim_snapshot()})
            return

        self.send_error(404, "not found")


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 8001
    print("=" * 60)
    print(f"  ATTACKER C2 PANEL — http://{host}:{port}")
    print("=" * 60)
    server = ThreadingHTTPServer((host, port), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()