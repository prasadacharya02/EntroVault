# report_generator/gen_appendices.py
"""
Generates the comprehensive Appendices:
- Appendix A: Full ThreatLogger.sol source code
- Appendix B: Algorithms 1 to 10 in formal pseudocode
- Appendix C: Complete Benchmark Dataset Schemas
- Appendix D: Exhaustive 200-Mark Viva Voce Defense Guide (Questions & Model Answers)
"""

def get_appendices():
    return """<div style="page-break-after: always;"></div>

# APPENDIX A: COMPLETE SOLIDITY ThreatLogger.sol SMART CONTRACT SOURCE CODE

The complete, unabridged Solidity source code for the `ThreatLogger` decentralized forensic contract is presented below:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title ThreatLogger
 * @dev Autonomous decentralized forensic ledger for cryptoviral incident logging.
 * Implements immutable, non-repudiable audit trails for incident response.
 */
contract ThreatLogger {
    
    // Struct representing an immutable forensic threat record
    struct ThreatEvent {
        uint256 id;
        string  fingerprint;    // SHA3-256 + SHA-256 composite hash
        string  threatType;     // Categorical malware classification
        uint256 timestamp;      // EVM block timestamp
        uint256 pid;            // Attributing OS Process ID
        uint256 entropyScore;   // Measured Shannon entropy * 100
        string  processName;    // Attributed executable name
        string  filePath;       // Path to target filesystem object
        string  actionTaken;    // Defensive containment action
        string  status;         // Execution status token
    }

    // Dynamic storage array of recorded threat events
    ThreatEvent[] public events;
    
    // Contract deployer address possessing administrative authorization
    address public owner;

    // Indexed event emitted for real-time SOC Web3 subscription filters
    event ThreatLogged(
        uint256 indexed id,
        string fingerprint,
        string threatType,
        uint256 timestamp
    );

    // Event emitted upon ownership transfer
    event OwnershipTransferred(
        address indexed previousOwner,
        address indexed newOwner
    );

    /**
     * @dev Initializes contract deployer as owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Access control modifier restricting functions to contract deployer.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "ThreatLogger: Caller is not the authorized owner");
        _;
    }

    /**
     * @dev Transfers administrative ownership to a new account.
     * @param nextOwner The address of the new administrative account.
     */
    function transferOwnership(address nextOwner) public onlyOwner {
        require(nextOwner != address(0), "ThreatLogger: New owner cannot be zero address");
        emit OwnershipTransferred(owner, nextOwner);
        owner = nextOwner;
    }

    /**
     * @dev Appends an immutable threat event record to the blockchain.
     * @return id The monotonically increasing index of the committed record.
     */
    function logThreat(
        string memory fingerprint,
        string memory threatType,
        uint256 pid,
        uint256 entropyScore,
        string memory processName,
        string memory filePath,
        string memory actionTaken,
        string memory status
    ) public onlyOwner returns (uint256) {
        uint256 id = events.length;
        events.push(ThreatEvent(
            id,
            fingerprint,
            threatType,
            block.timestamp,
            pid,
            entropyScore,
            processName,
            filePath,
            actionTaken,
            status
        ));

        emit ThreatLogged(id, fingerprint, threatType, block.timestamp);
        return id;
    }

    /**
     * @dev Queries a discrete forensic threat record by index.
     */
    function getEvent(uint256 id) public view returns (
        uint256,
        string memory,
        string memory,
        uint256,
        uint256,
        uint256,
        string memory,
        string memory,
        string memory,
        string memory
    ) {
        require(id < events.length, "ThreatLogger: Event index out of bounds");
        ThreatEvent memory e = events[id];
        return (
            e.id,
            e.fingerprint,
            e.threatType,
            e.timestamp,
            e.pid,
            e.entropyScore,
            e.processName,
            e.filePath,
            e.actionTaken,
            e.status
        );
    }

    /**
     * @dev Returns the total number of committed incident records.
     */
    function getEventCount() public view returns (uint256) {
        return events.length;
    }

    /**
     * @dev Returns an array of recent event IDs for SOC telemetry polling.
     * @param count The maximum number of recent event IDs to retrieve.
     */
    function getRecentEvents(uint256 count) public view returns (uint256[] memory) {
        uint256 len = events.length;
        uint256 n = count < len ? count : len;
        uint256[] memory ids = new uint256[](n);
        for (uint256 i = 0; i < n; i++) {
            ids[i] = len - n + i;
        }
        return ids;
    }
}
```

---

<div style="page-break-after: always;"></div>

# APPENDIX B: CORE ALGORITHMIC FORMULATIONS IN FORMAL PSEUDOCODE

This appendix provides the formal algorithmic formulations (Algorithms 1 to 10) governing the core computational pipelines of EntroVault.

```
================================================================================
ALGORITHM 1: Shannon Information Entropy Vectorized Computation
================================================================================
INPUT: Raw byte sequence D of length N bytes
OUTPUT: Shannon entropy H in bits per byte (0.0000 to 8.0000)

1: if D is empty or N == 0 then
2:     return 0.0000
3: end if
4: Initialize frequency array Counts of size 256 with zeros
5: for each byte b in D do
6:     Counts[b] <- Counts[b] + 1
7: end for
8: Initialize H <- 0.0
9: for i from 0 to 255 do
10:    if Counts[i] > 0 then
11:        p_i <- Counts[i] / N
12:        H <- H - (p_i * log2(p_i))
13:    end if
14: end for
15: return Round(H, 4)
================================================================================
```

```
================================================================================
ALGORITHM 2: Tri-Segment Partial File Entropy Profiling
================================================================================
INPUT: File path P, Maximum sample size S (default 65536 bytes)
OUTPUT: Structured metadata map M containing overall and segmental entropies

1: Initialize M with default zeroed attributes and error <- null
2: Open file handle on P in binary read mode
3: Read buffer D of size min(FileSize(P), S)
4: M.bytes_read <- Length(D)
5: M.entropy_overall <- ALGORITHM_1(D)
6: third <- Length(D) // 3
7: if third > 0 then
8:     D_start  <- D[0 : third]
9:     D_middle <- D[third : 2 * third]
10:    D_end    <- D[2 * third : Length(D)]
11:    M.entropy_start  <- ALGORITHM_1(D_start)
12:    M.entropy_middle <- ALGORITHM_1(D_middle)
13:    M.entropy_end    <- ALGORITHM_1(D_end)
14: end if
15: M.file_hash <- SHA256(D)
16: return M
================================================================================
```

```
================================================================================
ALGORITHM 3: Temporal Event Ingestion, Deduplication, and Burst Normalization
================================================================================
INPUT: File system event E = (Path, Type, Timestamp), Window W = 1.0 second
OUTPUT: Boolean decision ProcessEvent (True if admitted, False if duplicate)

1: Normalize key K <- (NormalizePath(E.Path), E.Type)
2: Lock deduplication cache mutex
3: now <- CurrentSystemTime()
4: last_time <- Cache.Get(K, default=0.0)
5: if (now - last_time) < W then
6:     Unlock mutex
7:     return False  // Suppress duplicate intermediate write burst
8: end if
9: Cache.Set(K, now)
10: Evict entries from Cache older than 2 * W
11: Unlock mutex
12: return True
================================================================================
```

```
================================================================================
ALGORITHM 4: Anti-Tamper and Ransom Note Trap Inspection
================================================================================
INPUT: Normalized file event E, Path P, File content sample D
OUTPUT: Boolean flags: ransom_note, defense_tamper

1: Initialize ransom_note <- False, defense_tamper <- False
2: if E.Type == "DELETED" then
3:     if P is within BACKUP_DIR or P is within QUARANTINE_DIR then
4:         if not BaseName(P).StartsWith(".tmp") then
5:             defense_tamper <- True
6:             return (ransom_note, defense_tamper)
7:         end if
8:     end if
9: end if
10: if MatchRegex(BaseName(P), RANSOM_NOTE_REGEX_PATTERNS) then
11:    ransom_note <- True
12: else if Extension(P) in {".txt", ".html"} and Length(D) > 0 then
13:    if ContainsAnyPhrase(D[:4096], EXTORTION_SIGNATURE_CATALOG) then
14:        ransom_note <- True
15:    end if
16: end if
17: return (ransom_note, defense_tamper)
================================================================================
```

```
================================================================================
ALGORITHM 5: Multi-Tier Deterministic Threat Decision Logic
================================================================================
INPUT: Enriched file event E, Entropy H, Delta dH, Velocity V, Normal range [R_min, R_max]
OUTPUT: Categorical Action A in {0: IGNORE, 1: ALERT, 2: TERMINATE, 3: TERMINATE_QUARANTINE}

1: if E.ransom_note or E.defense_tamper or E.known_threat_confirmed then
2:     return 3  // Instant hard-confirmation containment
3: end if
4: delta_signal <- abs(dH) >= ENTROPY_DELTA_THRESHOLD (2.0)
5: ext_mutated  <- E.ext_changed
6: hi_speed     <- V >= FILES_PER_SECOND_THRESHOLD (3.0)
7: corroborated <- delta_signal or ext_mutated or hi_speed
8: if E.threat_score >= 70 and corroborated then
9:     return 3  // High risk with behavioral corroboration
10: end if
11: if E.threat_score >= 40 or hi_speed then
12:    return 1  // Alert only
13: end if
14: if H >= ENTROPY_THRESHOLD (6.8) and Extension(E.Path) not in NORMAL_RANGES then
15:    return 1  // Unknown high-entropy format
16: end if
17: return 0  // Ignore benign event
================================================================================
```

```
================================================================================
ALGORITHM 6: Temporal Cross-File Campaign Escalation Tracker
================================================================================
INPUT: Event E, Decision Action A, Sliding window W = 15.0 seconds
OUTPUT: Tuple (Escalate, SweepEvents, KillOverridePID)

1: now <- CurrentSystemTime()
2: Purge entries from Deque where (now - entry.timestamp) > W
3: if E.process.verified and E.process.pid not in DEFENDER_TOOLING then
4:     LastVerifiedPID <- E.process.pid
5: end if
6: if not (E.entropy >= 6.8 and (abs(E.delta) >= 2.0 or E.ext_changed)) then
7:     return (False, [], null)
8: end if
9: DistinctPaths <- Unique file paths in Deque with Action >= 1 and Path != E.Path
10: Escalate <- (A >= 1) and (Count(DistinctPaths) >= CAMPAIGN_MIN_FILES - 1)
11: Append (now, E.Path, E, A) to Deque
12: SweepEvents <- []
13: if Escalate then
14:    SweepEvents <- All events currently in Deque
15: end if
16: return (Escalate, SweepEvents, LastVerifiedPID)
================================================================================
```

```
================================================================================
ALGORITHM 7: Verified Process Attribution and Zombie-Safe Process Termination
================================================================================
INPUT: Target Process Identifier PID, Expected victim file path P
OUTPUT: Boolean Success, Status token

1: if PID <= 0 or PID is null then
2:     return (False, "Invalid PID")
3: end if
4: Query operating system process table for proc <- Process(PID)
5: if proc does not exist then
6:     return (True, "Already exited (zombie-safe rc=42)")
7: end if
8: if Any(marker in proc.cmdline for marker in DEFENDER_TOOLING_MARKERS) then
9:     return (False, "Self-kill blocked: Defender tooling")
10: end if
11: if proc.status in {ZOMBIE, DEAD} then
12:    return (True, "Terminated: Zombie reaped (rc=42)")
13: end if
14: Dispatch SIGTERM signal to proc
15: Wait for proc exit with timeout 0.2 seconds
16: if proc is still active then
17:    Dispatch SIGKILL signal to proc
18:    Wait for proc exit with timeout 0.5 seconds
19: end if
20: return (True, "Terminated cleanly via SIGTERM/SIGKILL")
================================================================================
```

```
================================================================================
ALGORITHM 8: Strict Clean Backup Qualification and Storage Ingestion
================================================================================
INPUT: File path P, Measured entropy H, StrictMode flag (True for event-time writes)
OUTPUT: Boolean IsClean (True if admitted as restore source, False if rejected)

1: ext <- Lowercase(Extension(P))
2: normal <- NORMAL_ENTROPY_RANGES.Get(ext)
3: if normal is null then
4:     if StrictMode then
5:         return False  // Unknown formats at runtime cannot be admitted as clean
6:     end if
7:     return H < ENTROPY_THRESHOLD (6.8)
8: end if
9: normal_max <- normal.max_bound if StrictMode else (normal.max_bound + 0.5)
10: if H > normal_max then
11:    return False  // Strictly above empirical baseline for this type
12: end if
13: last_clean <- QueryManifestLastCleanEntropy(P)
14: if last_clean is not null then
15:    if abs(H - last_clean) >= ENTROPY_DELTA_THRESHOLD (2.0) then
16:        return False  // Reject sudden jump: ciphertext contamination prevention
17:    end if
18: end if
19: return True
================================================================================
```

```
================================================================================
ALGORITHM 9: Content-Based Post-Kill Estate Verification and Rollback Remediation
================================================================================
INPUT: Monitored estate directory Path, BackupManager instance BM
OUTPUT: Integer RepairedFilesCount

1: RepairedFilesCount <- 0
2: for each File F in RecursiveDirectoryWalk(Path) do
3:     if Extension(F) in {".meta.json", ".txt"} or F is in DEFENDER_STORES then
4:         continue
5:     end if
6:     current_hash <- SHA256(F)
7:     clean_hash   <- BM.GetLastCleanHash(F)
8:     // Content-based comparison eliminates false positives on legitimate photos
9:     if clean_hash is not null and current_hash != clean_hash then
10:        BM.Restore(F)
11:        RepairedFilesCount <- RepairedFilesCount + 1
12:    end if
13: end for
14: return RepairedFilesCount
================================================================================
```

```
================================================================================
ALGORITHM 10: Byzantine-Fault-Tolerant Federated Threat Fingerprint Consensus
================================================================================
INPUT: Incoming File Fingerprint FP, Tenant Node ID N, Local Threat Score S
OUTPUT: Action Directive (CONFIRMED_QUARANTINE, CORROBORATE_ALERT, NONE)

1: Query ExchangeRegistry for Record R matching FP
2: if R is null then
3:     Create new Record R: FP <- FP, Sightings <- 1, Confirmed <- False, Nodes <- {N}
4:     return NONE
5: end if
6: if N not in R.Nodes then
7:     R.Nodes.Add(N)
8:     R.Sightings <- R.Sightings + 1
9: end if
10: if Count(R.Nodes) >= EXCHANGE_CONFIRM_THRESHOLD (2) then
11:    R.Confirmed <- True
12:    return CONFIRMED_QUARANTINE  // Multi-tenant quorum consensus reached
13: end if
14: if Count(R.Nodes) == 1 then
15:    // Poison-node defense: Single sighting only corroborates (+25 score)
16:    return CORROBORATE_ALERT
17: end if
18: return NONE
================================================================================
```

---

<div style="page-break-after: always;"></div>

# APPENDIX C: COMPLETE BENCHMARK DATASET SCHEMAS

The automated benchmark harness (`benchmark.runner` and `benchmark.scenarios`) and the Random Forest classifier (`ai.rf_model`) evaluate structured telemetry governed by strict JSON schemas:

### C.1 Runtime Ingested Event Schema
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "EntroVaultIngestedEvent",
  "type": "object",
  "properties": {
    "id": { "type": "integer" },
    "timestamp": { "type": "string", "format": "date-time" },
    "file_path": { "type": "string" },
    "event_type": { "type": "string", "enum": ["CREATED", "MODIFIED", "DELETED", "MOVED"] },
    "file_extension": { "type": "string" },
    "entropy_overall": { "type": "number", "minimum": 0.0, "maximum": 8.0 },
    "entropy_delta": { "type": "number", "minimum": -8.0, "maximum": 8.0 },
    "threat_score": { "type": "number", "minimum": 0.0, "maximum": 100.0 },
    "ext_changed": { "type": "boolean" },
    "is_suspicious_speed": { "type": "boolean" },
    "events_per_sec": { "type": "number", "minimum": 0.0 },
    "ransom_note": { "type": "boolean" },
    "defense_tamper": { "type": "boolean" },
    "known_threat": { "type": "boolean" },
    "known_threat_confirmed": { "type": "boolean" },
    "process": {
      "type": "object",
      "properties": {
        "pid": { "type": "integer" },
        "name": { "type": "string" },
        "cmdline": { "type": "string" },
        "identity_verified": { "type": "boolean" }
      },
      "required": ["pid", "name", "identity_verified"]
    }
  },
  "required": ["timestamp", "file_path", "event_type", "entropy_overall"]
}
```

### C.2 Forensic Incident Report Schema (`reports/incidents/`)
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "EntroVaultForensicIncidentReport",
  "type": "object",
  "properties": {
    "incident_id": { "type": "string" },
    "timestamp": { "type": "string", "format": "date-time" },
    "detection_summary": {
      "type": "object",
      "properties": {
        "primary_threat_type": { "type": "string" },
        "trigger_reason": { "type": "string" },
        "attributing_process": { "type": "object" }
      }
    },
    "impact_metrics": {
      "type": "object",
      "properties": {
        "files_alerted": { "type": "integer" },
        "files_quarantined": { "type": "integer" },
        "files_restored_clean": { "type": "integer" },
        "estate_integrity_score": { "type": "string" }
      }
    },
    "cryptographic_evidence": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "file_path": { "type": "string" },
          "ciphertext_sha3_256": { "type": "string" },
          "ciphertext_sha256": { "type": "string" },
          "restored_baseline_sha256": { "type": "string" },
          "blockchain_tx_receipt": { "type": "string" }
        }
      }
    }
  }
}
```

---

<div style="page-break-after: always;"></div>

# APPENDIX D: COMPREHENSIVE 200-MARK VIVA VOCE DEFENSE GUIDE

This appendix provides an authoritative preparation guide for the final year major project evaluation (200 marks). It covers the most challenging technical questions, architectural critiques, and potential examiner trap questions, providing rigorous, scientifically honest answers aligned with the delivered implementation.

---

### Question 1: "Why does your benchmark report 87.5% detection accuracy instead of 100%? Did your system fail?"
**Model Answer:**  
"No, the system did not fail; this 87.5% figure reflects scientific and engineering honesty. The 6 missed runs out of 48 correspond strictly to the `image_blindspot` scenario. In that scenario, an attacker encrypts already high-entropy compressed media (such as JPEGs or MP4s) in place without appending an extension like `.locked`. 

Because native JPEGs have a natural Shannon entropy between 7.2 and 7.8, and modern ciphertext is between 7.95 and 8.0, the differential delta ($\Delta H approx.  0.53$) is well below our corroboration threshold of 2.0. Mathematically, no pure entropy detector can distinguish in-place ciphertext from compressed media without structural parsing. 

If we aggressively tune our thresholds to catch it, our Random Forest classifier achieves 100% detection, but it destroys 6 legitimate media workloads (photo imports and video writes). In an enterprise security system, destroying user data is an unacceptable failure mode. Therefore, we deliberately maintain a strict Zero False Quarantine (0 FQ) standard and openly publish the image blindspot as an inherent physical limitation of Shannon entropy."

---

### Question 2: "Can a privileged administrator decrypt the quarantined files in your vault using a master key or PIN?"
**Model Answer:**  
"No, absolutely not. Quarantined files cannot be decrypted by anyone. Real-world ransomware uses hybrid envelope cryptography: symmetric AES session keys are generated in RAM, encrypt the files, and are immediately encapsulated under an attacker's remote RSA/ECC public key before being purged from memory. Without the attacker's private key, reversing AES-256 ciphertext is computationally infeasible ($\mathcal{O}(2^{256})$).

In our purple-team simulation engines, ciphertext is generated by overwriting files with operating system entropy (`os.urandom`). The original bytes are permanently destroyed. Our quarantine vault serves strictly as an isolated forensic locker to preserve ciphertext evidence and cryptographic hashes for incident response. 

Disaster recovery in EntroVault is achieved strictly by restoring uncorrupted, hash-verified clean baselines captured *before* the attack began. Any candidate who claims their software can decrypt ransomware ciphertext without the attacker's key is either presenting a toy cipher or fabricating claims."

---

### Question 3: "What is the 'Ciphertext Backup Poisoning' bug, and how does EntroVault solve it?"
**Model Answer:**  
"The ciphertext backup poisoning defect occurs in continuous backup architectures. When ransomware modifies `Financial_Report.xlsx` into ciphertext, naive backup monitors detect a file modification and snapshot the encrypted file as 'Version 2'. When the security system later initiates rollback, the backup manager restores Version 2—putting the encrypted file right back onto the disk, resulting in total data loss.

EntroVault solves this via our **Strict Clean Backup Admission Algorithm** (`_is_clean(strict=True)`). When an event-time snapshot is evaluated, the file must satisfy three non-negotiable criteria:
1. The extension must be in our known baseline catalog (unknown extensions at runtime are rejected).
2. The entropy must be strictly $\le$ the type's normal maximum bound, with **zero tolerance margin**.
3. The entropy must not exhibit a differential jump $\Delta H \ge 2.0$ from the previous clean version.

If an attacker encrypts an `.xlsx` file, its entropy jumps to $approx.  7.88$, violating the maximum bound of 7.50 and tripping the $\Delta H \ge 2.0$ cap. The snapshot is rejected from clean qualification, guaranteeing that our disaster recovery engine only restores genuine pre-attack plaintext."

---

### Question 4: "Why did you implement the Campaign Escalation Tracker? Why not just kill the process on the very first suspicious file?"
**Model Answer:**  
"Killing a process on the very first high-entropy file is extremely dangerous. Benign actions like a user saving a new encrypted ZIP archive, importing a RAW photo, or rendering a video clip immediately produce high-entropy writes. If we terminated processes on the first file, we would constantly crash video editors, compilers, and archiving utilities.

Furthermore, sophisticated ransomware operators use 'slow-crawlers', inserting delays between writes (e.g., 650ms per file, operating at 1.5 ops/sec), which evades write-burst speed counters. 

Ransomware is inherently a multi-file campaign. Our `CampaignTracker` maintains a 15-second sliding window. When File 1 is touched, the system raises an `ACTION_ALERT` (Score 60) and caches the verified PID. When File 2 qualifies within 15 seconds, the tracker confirms an active multi-file campaign and escalates to `ACTION_TERMINATE_QUARANTINE`. 

Crucially, it executes a **Campaign Sweep**, instantly rolling back File 1 as well. By doing this, we terminate WannaCry at File 2 of 18 within 2.7 seconds, achieve 100% estate recovery, and maintain a Zero False Quarantine record across all legitimate single-file media writes."

---

### Question 5: "What happens if Ganache or your Ethereum blockchain node goes offline during an attack?"
**Model Answer:**  
"The defensive pipeline continues running without interruption. In real incidents, malware frequently disables network cards, or incident response teams disconnect Ethernet cables to isolate endpoints. If our defensive pipeline relied synchronously on an online Ethereum node, the pipeline would hang waiting for RPC timeouts, allowing the malware to finish encrypting the disk.

To solve this, we engineered an **Autonomous LocalLedger Fallback Architecture**. If the `web3.py` connector fails to reach Ganache or encounters a timeout, it activates an embedded SQLite fallback ledger. The incident is committed locally with an explicit label: `MODE: FALLBACK (SQLite)`. 

We never fabricate fake blockchain transaction hashes; our SOC dashboard clearly displays whether records are on Ganache EVM or the local fallback. This ensures uninterrupted forensic logging and instantaneous process containment even during total network partitioning."

---

### Question 6: "How do you prevent the defensive agent from killing itself or critical system processes?"
**Model Answer:**  
"Our `ProcessTerminator` implements a multi-layered immunity whitelist. Before dispatching `SIGTERM` or `SIGKILL`, it inspects the process command line via `psutil.Process(pid).cmdline()`. 

If the command line contains any string from `DEFENDER_TOOLING_MARKERS` (`pipeline_runner`, `lab.py`, `victim_server`, `attacker_server`, `dashboard`, `app.py`), or belongs to `WHITELISTED_PROCESSES` (`System`, `explorer.exe`, `systemd`, `init`), process termination is strictly rejected.

Additionally, to prevent race condition delays during high-speed detonations where an attacker process exits immediately post-write, our terminator is **zombie-aware**. Defunct or dead processes are reaped instantly ($rc = 42$), completely avoiding the 3-second `SIGKILL` timeout that plagues naive process monitors."

---

### Question 7: "What is your federated threat exchange, and how do you protect against a poisoned node?"
**Model Answer:**  
"Our federated exchange allows multiple defensive tenants to share cryptographic threat fingerprints (SHA-256). However, open threat-sharing networks are vulnerable to Byzantine poisoned-node attacks, where a compromised or misconfigured node broadcasts a critical OS hash (like `kernel32.dll`) as malware, causing peer systems to destroy their own operating systems.

EntroVault enforces a **Quorum-Based Consensus Model ($K \ge 2$)**:
- A sighting reported by only **1 node** is treated as *corroborating intelligence*. It increments the threat score by $+25$ points but is **strictly barred from auto-quarantining alone**.
- Only when at least **2 independent nodes** have independently encountered and quarantined the identical fingerprint is the hash marked as `confirmed = 1`. 

Once confirmed by quorum, peer nodes can immediately execute zero-touch quarantine. This mathematically prevents any single poisoned node from inducing a denial-of-service across the federation."

---
"""

if __name__ == "__main__":
    print(f"Appendices length: {len(get_appendices().split())} words")
