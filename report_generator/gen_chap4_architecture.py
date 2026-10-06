# report_generator/gen_chap4_architecture.py
"""
Generates Chapter 4: System Architecture and Detailed Specification.
Comprehensive architectural blueprint of EntroVault, detailing the tripartite purple-team topology,
the 3 micro-services (SOC, Victim, Attacker), runtime data flows, hardware/software specifications,
and security boundary enforcement.
"""

def get_chapter4():
    return """<div style="page-break-after: always;"></div>

# CHAPTER 4: SYSTEM ARCHITECTURE AND DETAILED SPECIFICATION

This chapter articulates the complete architectural blueprint and engineering specification of EntroVault. It delineates the tripartite purple-team operational model, details the end-to-end data processing pipeline, defines hardware and software runtime constraints, and formalizes the security boundary invariants governing system containment.

---

## 4.1 Global Architectural Blueprint: The EntroVault Tripartite Topology

To satisfy the demanding requirements of enterprise-level cybersecurity validation and academic evaluation (200-mark final year specification), EntroVault abandons single-script host detection in favor of an integrated **Cyber-Physical Purple-Team Tripartite Topology**. 

As illustrated in Figure 4.1, the platform partitions functionality across three distinct operational surfaces running as decoupled micro-services, communicating over isolated HTTP REST interfaces and low-latency WebSocket transport channels:

```
+───────────────────────────────────────────────────────────────────────────────────────────+
|                           ENTROVAULT TRIPARTITE ARCHITECTURE                              |
+───────────────────────────────────────────────────────────────────────────────────────────+
|                                                                                           |
|  TIER 1: BLUE TEAM / SOC DASHBOARD (Port 5000)                                            |
|  +─────────────────────────────────────────────────────────────────────────────────────+  |
|  | Flask-SocketIO Server │ Real-Time Telemetry Push (400ms) │ Dynamic Entropy Graph    |  |
|  | Threat Log Matrix     │ Forensic Report Inspector        │ Blockchain Audit Viewer  |  |
|  +─────────────────────────────────────────▲───────────────────────────────────────────+  |
|                                            │ Telemetry Push                               |
|                                            │ (Sub-Second JSON)                            |
|  CORE DEFENSIVE PIPELINE                   │                                              |
|  +─────────────────────────────────────────┴───────────────────────────────────────────+  |
|  | [FileMonitor (0.2s)] ──> [EventDeduplicator] ──> [EventPipeline (Batch 50)]         |  |
|  |        │                                                                            |  |
|  |        ├──> [EntropyAnalyzer (Shannon + Tri-Segment + Delta H)]                     |  |
|  |        ├──> [DefenseGuard (Note Trapping + Protected Store Canary Watcher)]         |  |
|  |        ├──> [BackupManager (Strict Clean Admission: No Delta Jump, In-Range)]       |  |
|  |        └──> [DecisionEngine]                                                        |  |
|  |                  ├── Deterministic Rule Engine (0 False Quarantine Standard)        |  |
|  |                  ├── Campaign Escalation Tracker (15s Window, 2-File Multi-Kill)   |  |
|  |                  ├── Random Forest Classifier (Opt-in, 11 Features, SHAP XAI)      |  |
|  |                  └── Deep Q-Network Agent (Opt-in Reinforcement Learning)          |  |
|  |                                                                                     |  |
|  | [ResponseOrchestrator] ──> [ProcessTerminator (Verified PID, Zombie Reaping)]       |  |
|  |                        ──> [FileQuarantine (Install-Time Store, SHA3-256 Fingerprint|  |
|  |                        ──> [Post-Kill Verifier (Byte-Level Estate Hash Compare)]    |  |
|  |                        ──> [BlockchainConnector (Ganache EVM / SQLite Fallback)]   |  |
|  +─────────────────────────────────────────▲───────────────────────────────────────────+  |
|                                            │ OS File Notifications                        |
|                                            │ & Estate Rollback                            |
|  TIER 2: VICTIM WORKSTATION (Port 5001)    │          TIER 3: RED TEAM / ATTACKER (8001)  |
|  +─────────────────────────────────────────┴─────+    +────────────────────────────────+  |
|  | Neutral File Explorer ("This PC")             |    | Multi-Strain Detonation Engine |  |
|  | Protected Estate: victim_server/user_files/   |    | 10 Real-World Malware Profiles |  |
|  | Authenticated Quarantine Vault (PIN: 1234)    |    | (WannaCry, LockBit, Conti, ...)  |  |
|  | Non-Decryption Forensic Evidence Mode         |    | Throttled Speed Control Sliders|  |
|  +───────────────────────────────────────────────+    +────────────────────────────────+  |
+───────────────────────────────────────────────────────────────────────────────────────────+
```
*Figure 4.1: High-Level Cyber-Physical Purple-Team Architecture of EntroVault.*

---

## 4.2 Three-Tier Purple-Team Deployment Model

### 4.2.1 Tier 1: Real-Time SOC Telemetry and Forensic Dashboard (Port 5000)
The Security Operations Center (SOC) dashboard serves as the command interface for defensive security analysts:
- **Asynchronous Telemetry Push:** Operating on an independent daemon thread, the telemetry engine queries the SQLite event datastore every 400 milliseconds (`time.sleep(0.4)`), serializes newly inserted threat records into JSON frames, and broadcasts them across active WebSocket connections via `Flask-SocketIO`.
- **Dynamic Visual Instrumentation:** Security operators observe a live Chart.js entropy waveform plotting real-time file entropy against theoretical safety bounds ($H = 6.8$ and $H = 8.0$), an active threat counter tracking detected incidents, and an interactive ledger displaying process attributions, extracted digital signatures, and response status flags.
- **Forensic Drill-Down:** The SOC interface provides dedicated inspection portals for generated forensic reports, cryptographic smart contract transaction receipts, and federated intelligence sightings.

### 4.2.2 Tier 2: The Neutralized Victim Workstation and File Explorer (Port 5001)
A core engineering mandate of this project is the strict neutralization of the victim user interface. In an authentic corporate environment, an employee experiencing an endpoint infection must not be presented with alarming defensive telemetry, cryptoviral family attributions, or raw incident scores:
- **Clean File Explorer ("This PC"):** The victim web portal (`victim_server/app.py`) serves a neutral graphical file explorer displaying standard file system attributes: filename, file size, last modified timestamp, and format icons across standard user folders (`Documents/`, `Desktop/`, `Downloads/`, `Pictures/`).
- **Absence of Attack Telemetry:** During an active attack, the victim interface displays no encrypted file counters, no malware names, and no system warnings. Compromised files disappear seamlessly as they are quarantined, and reappear instantly as they are restored by the background defense.
- **PIN-Protected Administrative Vault:** The quarantine storage folder is physically and logically locked behind an authenticated vault interface (`/api/quarantine/auth`). Standard users cannot access quarantined artifacts. Security administrators authenticate via a secure PIN challenge (`victim_user` / `1234`), establishing an 8-hour scoped session (`quarantine_only`). In strict adherence to scientific honesty, the vault allows administrators to inspect encrypted evidence and JSON metadata, but explicitly bars decryption (as original plaintext is irreversibly overwritten by malware session keys).

### 4.2.3 Tier 3: The Multi-Strain Attacker Command-and-Control Console (Port 8001)
The Red Team detonation console (`attacker_server/app.py`) provides a controlled, sandboxed environment to launch weaponized ransomware simulations:
- **10 Canonical Cryptoviral Strains:** Security evaluators can select from 10 distinct malware archetypes: WannaCry, LockBit 3.0, REvil/Sodinokibi, Ryuk, BlackCat/ALPHV, Conti, Maze, Cerber, GandCrab, and Dharma.
- **Dynamic Speed Modulation:** An operational slider permits tuning attack velocity from rapid unthrottled bursts ($> 20$ files/sec) down to stealthy slow-crawlers ($1.0 - 1.6$ files/sec) designed to defeat velocity-based heuristics.
- **Path Sandboxing:** To prevent accidental host corruption, the attacker server enforces strict path normalization checks (`safe_path()`), restricting all destructive write operations strictly to the `victim_server/user_files/` directory.

---

## 4.3 End-to-End Runtime Pipeline Data Flow

The global operational lifecycle of an event passing through EntroVault is formalized in Figure 4.2 and described across ten sequential runtime stages:

```
 [Victim Files: user_files/]
           │
           │ (1) OS File System Event (Modified / Created / Renamed)
           ▼
 [watchdog.Observer (0.2s Polling)]
           │
           │ (2) Raw FileModifiedEvent
           ▼
 [monitoring.event_deduplicator (1.0s Window)]
           │
           │ (3) De-duplicated Event Token
           ▼
 [monitoring.event_pipeline.EventPipeline (Queue: 10,000 | Batch: 50)]
           │
           ├───────────────────────────────┬───────────────────────────────┐
           ▼                               ▼                               ▼
 [entropy.entropy_calculator]    [monitoring.defense_guard]      [response.backup_manager]
  - Shannon Entropy (H)           - Ransom Note Pattern Match     - Strict Clean Check:
  - Tri-Segment Partial Entropy   - Backup/Quarantine Tamper        * In normal type range
  - Delta Jump vs History         - Federated Registry Lookup       * No delta jump >= 2.0
  - Threat Score (0 - 100)                                          * Snapshot clean v1
           │                               │                               │
           └───────────────────────────────┼───────────────────────────────┘
                                           ▼
 [monitoring.pipeline_runner.DecisionEngine]
  ├── Hard Confirmation Check (Note Dropped? Store Tampered? Quorum >= 2?)
  ├── Corroboration Invariant (Score >= 70 AND (Delta >= 2.0 OR ExtChanged OR Speed))
  └── CampaignTracker Evaluation (Distinct qualifying files in 15s >= 2?)
                                           │
                                           │ Decision Action: ACTION_TERMINATE_QUARANTINE
                                           ▼
 [response.response_module.ResponseExecutor]
  ├── (4) ProcessTerminator: Extract verified PID via psutil, reap zombie tree
  ├── (5) FileQuarantine: Dual-hash SHA3-256 + SHA-256, isolate into install-time folder
  ├── (6) Campaign Sweep: Recursively quarantine & restore all files in campaign window
  ├── (7) Post-Kill Verifier: Walk estate, compare current SHA-256 vs last clean, repair
  ├── (8) BackupManager: Restore clean byte-for-byte baseline, reverse-rename extensions
  ├── (9) Forensic Report Generator: Serialize JSON incident record to disk
  └── (10) BlockchainConnector: Commit immutable transaction to Ganache EVM / LocalLedger
                                           │
           ┌───────────────────────────────┴───────────────────────────────┐
           ▼                                                               ▼
 [SQLite Database: entropy.db]                                   [Real-Time SocketIO Push]
  - Persisted event telemetry                                     - Broadcast to SOC (5000)
  - 400ms polling worker                                          - Neutral victim update
```
*Figure 4.2: Comprehensive End-to-End Runtime Pipeline Sequence Diagram.*

---

## 4.4 Hardware, Software, and Environment Requirements

### 4.4.1 Laboratory Hardware Topology
The evaluation environment is deployed on an isolated hypervisor host configured according to the parameters specified in Table 4.1:

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|                    TABLE 4.1: HARDWARE EVALUATION TOPOLOGY                               |
+──────────────────────────┬───────────────────────────────────────────────────────────────+
| Hardware Component       | Laboratory Specification                                      |
+──────────────────────────┼───────────────────────────────────────────────────────────────+
| Host CPU Architecture    | x86_64 / AMD64 (8 Physical Cores, 16 Threads @ 3.60 GHz)      |
| Host Physical RAM        | 32,768 MB (32 GB) DDR4 @ 3200 MHz                             |
| Storage Subsystem        | 1 TB NVMe M.2 Solid State Drive (PCIe Gen 4, 5000 MB/s Read)  |
| Virtual Sandbox Hyperv.  | KVM / QEMU Isolated Guest Container                           |
| Guest Allocated vCPUs    | 4 vCPUs (Pinned, 1 Socket, 4 Cores)                           |
| Guest Allocated Memory   | 8,192 MB (8 GB) High-Performance vRAM                         |
| Network Isolation        | Host-Only Isolated Virtual Bridge (No External WAN Routing)   |
+──────────────────────────┴───────────────────────────────────────────────────────────────+
```

### 4.4.2 Software Dependencies and Python Subsystem Configuration
The software stack is built using Python 3.10+ running on an enterprise Linux / POSIX base. Table 4.2 documents the core software components and dependencies:

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|                      TABLE 4.2: CORE SOFTWARE DEPENDENCIES                               |
+──────────────────────────┬──────────────┬────────────────────────────────────────────────+
| Package / Subsystem      | Version      | Functional Role in Architecture                |
+──────────────────────────┼──────────────┼────────────────────────────────────────────────+
| Python Runtime           | >= 3.10.12   | Core Pipeline Execution Environment            |
| watchdog                 | >= 3.0.0     | Asynchronous File System Event Notification    |
| Flask                    | >= 2.3.0     | Web Micro-Framework for SOC, Victim, Attacker  |
| Flask-SocketIO           | >= 5.3.0     | Sub-Second WebSocket Streaming Infrastructure  |
| python-socketio          | >= 5.8.0     | Client/Server Bi-directional Transport         |
| psutil                   | >= 5.9.0     | Process Table Inspection & Handle Extraction   |
| web3.py                  | >= 6.0.0     | JSON-RPC Client for Ethereum EVM / Ganache     |
| pycryptodome             | >= 3.18.0    | NIST FIPS Compliant SHA3-256 Hashing Primitives|
| scikit-learn (Optional)  | >= 1.3.0     | Random Forest Second-Classifier Training       |
| shap (Optional)          | >= 0.42.0    | Local SHAP Feature Attribution Explanations    |
| torch (Optional)         | >= 2.0.0     | Deep Q-Network Tensor Evaluation (Graceful Fall)|
| Ganache CLI / UI         | >= 7.9.0     | Local Ethereum Virtual Machine Testnet          |
+──────────────────────────┴──────────────┴────────────────────────────────────────────────+
```

---

## 4.5 Security Boundaries, Threat Isolation, and Path Containment

To guarantee absolute safety during live malware detonations and prevent denial-of-service against the operating system, EntroVault enforces four rigid security boundary invariants:

### 1. Attacker Containment Invariant (`safe_path`)
The attacker console interacts strictly through the `safe_path()` containment validator:
```python
def safe_path(target: str) -> bool:
    resolved = Path(target).resolve()
    sandbox = Path(config.VICTIM_USER_FILES).resolve()
    return resolved == sandbox or sandbox in resolved.parents
```
Any execution attempting directory traversal (e.g., `../../etc/passwd` or `..\Windows\System32`) raises an immediate fatal security exception, preventing malicious file system escapes.

### 2. Defender Self-Kill Immunity Whitelist (`DEFENDER_TOOLING_MARKERS`)
When the `ProcessTerminator` receives an instruction to terminate an offending PID, it inspects the complete command line and executable path via `psutil.Process(pid).cmdline()`. If the command line contains any string belonging to `DEFENDER_TOOLING_MARKERS`:
```python
DEFENDER_TOOLING_MARKERS = (
    "pipeline_runner", "entropy_system", "lab.py",
    "victim_server", "attacker_server", "dashboard",
    "app.py", "main.py"
)
```
or appears in `config.WHITELISTED_PROCESSES` (`System`, `explorer.exe`, `systemd`, `init`), process termination is strictly rejected. This prevents the defender from accidentally terminating its own event pipeline, web servers, or critical OS processes during high-load attacks.

### 3. Installation-Time Physical Store Provisioning
In compliance with enterprise deployment specifications, the quarantine vault directory (`quarantine_storage/`) and backup snapshot directory (`backup_storage/`) are physically created during the initial setup script execution (`install.py`). The paths are strictly managed out-of-band and shielded from user manipulation.

### 4. Honest Non-Decryption Invariant
The platform establishes an unbreakable security boundary regarding file decryption: **ciphertext held within the quarantine vault cannot be decrypted by any user or administrator**. Because simulated and real-world cryptoviral engines destroy the original plaintext by overwriting bytes with pseudo-random streams (`os.urandom`) or encrypting with unreachable remote asymmetric keys, EntroVault recovers assets exclusively by rolling back to pre-attack clean baseline snapshots.

---

## 4.6 Architectural Resilience and Compatibility Facades

To ensure robust interoperability across diverse research testbeds and legacy evaluation harnesses, EntroVault incorporates compatibility facades:
- `entropy_system.py`: Emits a standard `DeprecationWarning` while seamlessly routing legacy calls into the canonical `entropy.entropy_calculator.EntropyAnalyzer` engine.
- `blockchain/blockchain_logger.py`: Provides backward-compatible wrappers around the modern `blockchain.connector.BlockchainConnector` module.
- **Graceful Optional Imports:** If advanced dependencies (`torch` for Deep Q-Networks, `scikit-learn` or `shap` for Random Forest explanations, or `web3` for Ganache EVM connections) are absent from the host Python environment, the system gracefully degrades to its deterministic rule engine and local SQLite ledger without raising unhandled exceptions or crashing the pipeline.

---

## 4.7 Chapter Summary

This chapter detailed the structural architecture of EntroVault:
1. The tripartite purple-team deployment isolates SOC monitoring (Port 5000), neutral victim exploration (Port 5001), and attacker detonation (Port 8001).
2. The runtime pipeline processes file events across ten synchronized stages, linking watchdog observation, entropy calculation, strict backup, campaign escalation, and blockchain logging.
3. Strict security invariants prevent directory traversal escapes, defender self-termination, and ciphertext recovery poisoning.
4. Resilient architectural facades ensure continuous execution regardless of optional dependency availability.

Chapter 5 examines the low-level software engineering mechanics and implementation details of the monitoring and entropy subsystems.

---
"""

if __name__ == "__main__":
    print(f"Chapter 4 length: {len(get_chapter4().split())} words")
