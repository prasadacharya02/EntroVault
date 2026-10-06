# report_generator/gen_chap2_literature.py
"""
Generates Chapter 2: Comprehensive Literature Survey and Related Work.
Exhaustive, critical review of prior academic literature on entropy analysis,
filesystem monitoring, machine learning in ransomware detection, blockchain forensics,
and a comprehensive comparative matrix against state-of-the-art solutions.
"""

def get_chapter2():
    return """<div style="page-break-after: always;"></div>

# CHAPTER 2: COMPREHENSIVE LITERATURE SURVEY AND RELATED WORK

The challenge of detecting and mitigating cryptoviral extortion has motivated substantial academic and industrial investigation over the past decade. This chapter establishes the scholarly context of this dissertation by critically surveying the state of the art (SOTA) across four foundational domains:
1. Information-theoretic entropy methods for encrypted payload discrimination.
2. Operating system file-system interception architectures.
3. Machine learning and reinforcement learning paradigms in host-based behavioral mitigation.
4. Distributed ledger technology and cryptographic mechanisms for forensic chain-of-custody preservation.

The survey concludes with a detailed comparative matrix delineating the technical capabilities and limitations of existing systems relative to EntroVault, formalizing the specific research gaps addressed in this engineering research.

---

## 2.1 Information-Theoretic Techniques in Malware Analysis

### 2.1.1 Historical Evolution of Entropy in Cryptanalysis and File Identification
The application of Claude E. Shannon's mathematical theory of communication (1948) to computer security originated in binary analysis and cryptanalysis. In their seminal work, Lyda and Hamrock (2007) demonstrated that Shannon entropy could reliably distinguish between native compiled machine code, packed executables, and encrypted payloads within portable executable (PE) binaries. Native compiled x86/x64 binaries typically exhibit an overall entropy between $4.5$ and $6.2$ bits per byte due to the non-uniform frequency distribution of operational codes (opcodes), whereas compressed and encrypted code sections routinely exceed $7.2$ bits per byte, approaching the theoretical maximum of $8.0$.

Following this foundation, early host-based ransomware detection frameworks attempted to apply global file entropy thresholds to identify malicious writes. When a user document transitioned from a low-entropy state (e.g., ASCII text at $H approx. .  4.2$) to high entropy ($H \\ge 7.8$), the file was flagged as encrypted. However, early implementations (such as those surveyed by Kharraz et al. in the UNVEIL study, 2016) demonstrated unacceptable false-positive rates when confronted with benign user actions involving compression algorithms (e.g., generating `.zip`, `.tar.gz`, or `.docx` archives).

### 2.1.2 Block-Based vs. File-Wide Entropy in Crypto-Ransomware Detection
To overcome the limitations of global whole-file entropy, Scaife et al. (2016) introduced **CryptoDrop**, an early-warning detection architecture deployed on Microsoft Windows. CryptoDrop tracked three primary indicators across active file operations:
1. Changes in file entropy across discrete blocks.
2. Structural byte frequency changes measured via Chi-Square ($\chi^2$) goodness-of-fit tests.
3. Rapid mass deletions and file type transformations.

CryptoDrop demonstrated that evaluating entropy across sliding discrete blocks (e.g., 4,096-byte blocks) permitted the identification of partially encrypted files before the entire file handle was closed. However, CryptoDrop required the accumulation of several damaged files before reaching a decision threshold, resulting in a median loss of 10 user files prior to process suspension.

Continella et al. (2016) advanced this paradigm with **ShieldFS**, an autonomous add-on file system driver capable of intercepting I/O requests. ShieldFS monitored low-level file system transactions and extracted behavioral features, including the entropy of write buffers, file renaming patterns, and directory traversal sequences. ShieldFS incorporated a self-healing copy-on-write mechanism that buffered disk writes until an activity profile was classified as benign. While ShieldFS significantly reduced data loss, its reliance on heavy kernel-level write shadowing introduced severe I/O throughput degradation (up to 40% performance overhead on write-intensive database workloads) and struggled to differentiate between encrypted file writes and high-entropy media manipulation.

More recently, Wressnegger et al. (2020) and McIntosh et al. (2021) highlighted the vulnerability of sliding-window entropy to adversarial manipulation. Attackers can deliberately interleave unencrypted, zero-padded, or repetitive byte sequences into ciphertext streams to artificially depress the calculated Shannon entropy below standard detection thresholds ($approx.  6.8$), a technique known as **entropy padding**. This finding underscored that entropy cannot serve as an isolated, monolithic detection heuristic; it must be coupled with behavioral delta metrics, extension mutation tracking, and multi-file campaign correlation.

---

## 2.2 File System Monitoring Architectures: Userspace vs. Kernel Drivers

A fundamental architectural divergence in host-based cryptoviral defense centers on the operational layer at which file system operations are intercepted.

### 2.2.1 Operating System Notification Hooks: `inotify`, `kqueue`, and `ReadDirectoryChangesW`
Operating systems provide native event-driven asynchronous APIs that notify registered processes when directory trees undergo modification:
- **Microsoft Windows (`ReadDirectoryChangesW`):** Allows an application to monitor a directory handle for buffer modifications, file additions, deletions, and attribute alterations. While efficient, the underlying buffer can overflow during high-velocity write bursts, leading to dropped event notifications.
- **Linux (`inotify` / `fanotify`):** Linux provides file-descriptor-based monitoring. `inotify` delivers asynchronous path-level notifications (`IN_MODIFY`, `IN_CREATE`, `IN_MOVED_TO`), but does not natively provide process attribution (the PID executing the write). `fanotify` operates at the virtual file system (VFS) layer, allowing synchronous event interception and process identification, but requires root capabilities and kernel-level configuration.
- **macOS (`kqueue` / `FSEvents`):** BSD-derived kernel queues and CoreServices `FSEvents` provide lightweight directory-level coalescing, but exhibit notification latencies that can exceed several hundred milliseconds under load.

### 2.2.2 Latency vs. Portability Trade-offs in Python `watchdog` Implementation
To achieve cross-platform operability without binding the defensive codebase to a single proprietary OS kernel API, cross-platform frameworks such as Python `watchdog` wrap native notification subsystems (`ReadDirectoryChangesW` on Windows, `inotify` on Linux, and `kqueue` on macOS) under a unified event dispatch loop.

However, literature by Morato et al. (2018) notes significant engineering challenges in userspace monitoring:
- **Event Bursting and Duplication:** A single file overwrite operation (e.g., opening, truncating, writing 64KB chunks, and closing) frequently triggers dozens of discrete `FileModifiedEvent` notifications within milliseconds. Without a high-performance temporal deduplication engine, the detection queue becomes rapidly backlogged, introducing multi-second detection delays.
- **Out-of-Band Process Attribution:** Unlike kernel minifilters that synchronously intercept the exact Process ID (PID) initiating an `IRP_MJ_CREATE` I/O request packet, userspace monitors receive notifications *asynchronously after the disk modification has been committed*. Consequently, identifying the offending process requires immediate interrogation of operating system open file handles via system diagnostic interfaces (such as `psutil` or `/proc`), introducing race conditions if ephemeral malware processes close file handles immediately post-write.

---

## 2.3 Machine Learning and Deep Reinforcement Learning in Cryptoviral Mitigation

### 2.3.1 Supervised Classifiers and the Risk of False Quarantines
To surpass rigid heuristic thresholds, numerous researchers have deployed supervised machine learning models to classify process behavior and file transformations:
- Chen et al. (2018) and Vinayakumar et al. (2019) trained deep neural networks (DNNs), Random Forests (RF), and Support Vector Machines (SVM) on dynamic API call traces and file entropy vectors.
- While these models regularly report academic classification accuracies exceeding 98%, their operational deployment in enterprise environments is plagued by the **base-rate fallacy**. In an enterprise environment processing millions of benign file writes daily, a 1% false-positive rate yields hundreds of daily false alarms.
- More critically, in an automated defense platform with active mitigation, a false positive translates directly into a **False Quarantine (FQ)**—the automated destruction, encryption, or isolation of legitimate enterprise assets. As demonstrated by Hampton et al. (2020), defensive platforms that enforce automated process termination on probabilistic model outputs frequently corrupt enterprise software builds, video rendering, and database backups.

### 2.3.2 Explainable AI (XAI) and SHAP Value Integration in Security Operations
A primary impediment to adopting machine learning within Security Operations Centers (SOCs) is the "black-box" dilemma. Security analysts cannot trust an opaque probability score when making containment decisions. 

To resolve this opacity, recent cybersecurity literature has integrated Explainable AI (XAI) frameworks, predominantly **SHAP (SHapley Additive exPlanations)**, formulated by Lundberg and Lee (2017) based on cooperative game theory. SHAP calculates the marginal Shapley contribution of each individual feature to the final risk classification:

$$\phi_i(x) = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|!(|F| - |S| - 1)!}{|F|!} \left[ f_x(S \cup \{i\}) - f_x(S) \right]$$

By decomposing a predicted cryptoviral threat score into discrete, signed feature contributions (e.g., $+0.42$ due to `entropy_delta \ge 2.0`, $+0.28$ due to `files_per_sec \ge 12`, $-0.35$ due to `in_normal_range`), SHAP provides the human SOC operator with immediate, actionable attribution telemetry.

### 2.3.3 Markov Decision Processes and Deep Q-Networks for Automated Mitigation
In dynamic attack scenarios where ransomware variants adapt their encryption velocity or payload chunking, static classification models fail to optimize multi-step responses. To address this, researchers have modeled cryptoviral defense as a **Markov Decision Process (MDP)** governed by Reinforcement Learning (RL):
- In an MDP formulation $(S, A, P, R, \gamma)$, the state space $S$ represents system telemetry (current entropy, historical entropy delta, event velocity, process age, signature validation), the action space $A$ defines mitigation postures (Ignore, Alert, Terminate Process, Terminate and Quarantine), and the reward function $R$ penalizes both undetected damage and false-positive interventions.
- Mnih et al. (2015) introduced **Deep Q-Networks (DQN)**, combining Q-learning with deep convolutional/dense neural networks to approximate the optimal action-value function:
  $$Q^*(s, a) = \mathbb{E} \left[ r + \gamma \max_{a'} Q^*(s', a') \;\middle|\; s, a \right]$$
- In ransomware mitigation literature (e.g., Alam et al., 2021), DQNs have demonstrated the ability to learn nuanced defensive policies that delay aggressive quarantine until multiple corroborating behavioral flags appear, minimizing false quarantines while preserving endpoint containment speed.

---

## 2.4 Distributed Ledger Technology and Cryptographic Integrity in Forensics

### 2.4.1 EVM Smart Contracts for Non-Repudiable Incident Logging
Digital forensics and incident response (DFIR) frameworks require strict adherence to evidence preservation standards (such as ISO/IEC 27037). In severe ransomware incidents, adversaries frequently compromise local administrative accounts, enabling them to wipe system event logs (`wevtutil`), alter file access timestamps, and purge local security records to conceal their initial entry vectors and lateral movement paths.

To establish non-repudiation, researchers (e.g., Liang et al., 2017; Cebe et al., 2018) have proposed logging cryptographic evidence hashes to distributed ledgers. The **Ethereum Virtual Machine (EVM)** provides a decentralized, immutable execution environment:
- Once an incident record (containing the SHA-256 fingerprint of the ciphertext, the operating system process identifier, and an RFC-compliant timestamp) is committed via a smart contract transaction, it cannot be altered, rolled back, or deleted by any host administrator.
- However, prior academic proposals often fail in operational engineering: deploying smart contract transactions to public or enterprise Ethereum testnets introduces network latency (12–15 seconds per block) and financial transaction costs (gas fees), and causes complete forensic failure if the host experiences network isolation or off-line containment. A production-grade architecture requires a resilient local fallback ledger that preserves transactional integrity even during total network partitioning.

### 2.4.2 Federated Threat Intelligence Exchanges and the Poisoned Node Problem
Modern security platforms rely on threat intelligence exchanges (such as MISP or AlienVault OTX) to share Indicators of Compromise (IOCs) across corporate tenants. If Endpoint $A$ encounters a novel polymorphic cryptoviral hash, it broadcasts the fingerprint to Endpoint $B$ to preemptively quarantine the file upon arrival.

However, as highlighted in Byzantine fault tolerance research (Castro & Liskov, 2002; Meng et al., 2018), open threat-sharing networks are vulnerable to **Poisoned Node / Sybil Attacks**:
- A single compromised or misconfigured node could broadcast the cryptographic hash of a critical operating system binary (e.g., `kernel32.dll` or `explorer.exe`) as a confirmed ransomware threat.
- If receiving peer endpoints automatically enforce destructive quarantine on single-sighting reports, the poisoned node achieves a distributed denial-of-service (DDoS) across the entire defensive federation.
- Consequently, multi-tenant exchanges must implement strict quorum-based consensus constraints: a sighting from a single node must only serve as corroborating intelligence (+25 score weighting), while automated quarantine execution must strictly require independent verification from at least $K \ge 2$ uncoordinated nodes.

---

## 2.5 Critical Comparative Matrix: EntroVault vs. Academic and Commercial SOTA

To illustrate the technical differentiators of the architecture developed in this dissertation, Table 2.1 provides a systematic comparative feature matrix evaluating EntroVault against prominent academic frameworks and commercial enterprise security suites.

```
+──────────────────────────────────────────────────────────────────────────────────────────────────────────+
|                       TABLE 2.1: SYSTEMATIC COMPARATIVE FEATURE MATRIX                                   |
+──────────────────────────┬──────────────┬────────────┬──────────────┬──────────────────┬─────────────────+
| Evaluation Parameter     | CryptoDrop   | ShieldFS   | Sophos       | RansomCare       | EntroVault      |
|                          | (Scaife '16) | (Cont. '16)| Intercept X  | (AirGap '22)     | (This Thesis)   |
+──────────────────────────┼──────────────┼────────────┼──────────────┼──────────────────┼─────────────────+
| Primary Detection Model  | Block-level  | VFS I/O    | Deep Learning| Canary Decoy     | Shannon Entropy |
|                          | Entropy      | Profiling  | & Signatures | Trapping         | + Campaign Trk. |
+──────────────────────────┼──────────────┼────────────┼──────────────┼──────────────────┼─────────────────+
| File Containment Latency | ~10 Files    | 3–5 Files  | 2–4 Files    | Variable (Canary)| File 2 of Estate|
|                          | (High Loss)  | (Moderate) | (Moderate)   | Dependent        | (Sub-Second)    |
+──────────────────────────┼──────────────┼────────────┼──────────────┼──────────────────┼─────────────────+
| False Quarantine (FQ)    | High on      | Low-Medium | Low          | Zero (Canaries   | ZERO (0 FQ) on  |
| Safety Standard          | Media Files  | (Tuned)    | (Proprietary)| Only)            | Rule Engine     |
+──────────────────────────┼──────────────┼────────────┼──────────────┼──────────────────┼─────────────────+
| Slow-Crawler Evasion     | Vulnerable   | Vulnerable | Partially    | Resistant        | MITIGATED via   |
| Resistance (<2 ops/sec)  | (Speed Bar)  | (Heuristic)| Effective    | (Passive)        | CampaignTracker |
+──────────────────────────┼──────────────┼────────────┼──────────────┼──────────────────┼─────────────────+
| Disaster Recovery        | None         | In-Memory  | VSS Shadow   | Out-of-band      | Strict Clean    |
| Mechanism                | (Detection   | Shadow Copy| Copy Restore | Snapshot         | Pre-Attack Ver. |
|                          | Only)        | (Heavy I/O)| (T1490 Fail) | Integration      | (Byte-for-Byte) |
+──────────────────────────┼──────────────┼────────────┼──────────────┼──────────────────┼─────────────────+
| Backup Poisoning         | Not          | Not        | Vulnerable   | Partially        | ELIMINATED via  |
| Prevention               | Addressed    | Addressed  | (Overwrites) | Addressed        | Delta & Type Cap|
+──────────────────────────┼──────────────┼────────────┼──────────────┼──────────────────┼─────────────────+
| Forensic Audit           | Volatile OS  | Local Log  | Cloud SOC    | Syslog Export    | EVM Smart Cont. |
| Immutability             | Text Files   | Files      | Centralized  | (Local Tamper)   | + Local Fallback|
+──────────────────────────┼──────────────┼────────────┼──────────────┼──────────────────┼─────────────────+
| Byzantine-Safe Federated | None         | None       | Proprietary  | None             | Quorum (K >= 2) |
| Threat Exchange          |              |            | Cloud Sync   |                  | Consensus Model |
+──────────────────────────┼──────────────┼────────────┼──────────────┼──────────────────┼─────────────────+
| Explainable AI (XAI)     | None         | None       | None         | None             | Local SHAP      |
| Telemetry                |              |            | (Opaque)     |                  | Feature Drivers |
+──────────────────────────┼──────────────┼────────────┼──────────────┼──────────────────┼─────────────────+
| Tripartite Purple-Team   | No           | No         | No           | No               | FULL INTEGRATED |
| Lab Harness              | (Host Only)  | (Host Only)| (Enterprise) | (Enterprise)     | (SOC/Vic/Atk)   |
+──────────────────────────┼──────────────┼────────────┼──────────────┼──────────────────┼─────────────────+
```

---

## 2.6 Summary of Identified Research Gaps

The literature survey exposes five critical research and engineering gaps in existing cryptoviral mitigation literature:

1. **The Campaign Correlation Blindspot:** Existing detection systems predominantly evaluate file modifications as isolated, stateless events or rely on coarse global write-rate counters. Stealthy adversaries deliberately throttle execution below velocity thresholds (e.g., encrypting 1 file every 1.5 seconds). There is an absence of architectures that correlate subtle, multi-file behavioral changes across rolling temporal windows to achieve early-stage containment.
2. **Disaster Recovery Backup Poisoning:** Existing continuous backup engines blindly ingest modified files into version histories without validating whether the modified payload represents legitimate edits or cryptoviral ciphertext. Under active attack, legitimate baselines are overwritten or evicted, rendering subsequent recovery impossible.
3. **The Unrealistic "100% Detection / Perfect Decryption" Myth:** Commercial vendors and academic papers frequently claim 100% detection accuracy while concealing high false-positive rates on media workloads, or imply that privileged administrators can magically decrypt ciphertext without the attacker's private key. There is a lack of rigorous, scientifically honest research that formally publishes physical detection limits (such as the in-place compressed media blindspot) and recovery constraints.
4. **Fragile Forensic Persistence:** Proposed blockchain-based forensic logging systems rely on continuous connectivity to public or private Ethereum testnets. In operational reality, ransomware frequently severs network interfaces or security teams isolate endpoints off-network, causing total transaction failure and evidence loss in the absence of an autonomous local ledger fallback.
5. **Lack of Integrated Purple-Team Testing Topology:** Most academic evaluations detonate malware on single hosts without modeling the multi-tier operational realities of modern enterprise defense, specifically neglecting the human-factors requirement of keeping victim user interfaces clean and neutral while streaming live, sub-second telemetry to an isolated SOC.

EntroVault directly bridges each of these identified research gaps through the formal mathematical models, multi-tier decision engines, strict backup algorithms, and immutable logging architectures presented in the subsequent chapters of this dissertation.

---
"""

if __name__ == "__main__":
    print(f"Chapter 2 length: {len(get_chapter2().split())} words")
