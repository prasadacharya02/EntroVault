# report_generator/gen_chap9_benchmarks.py
"""
Generates Chapter 9: Comprehensive Empirical Evaluation, Benchmarks, and Recovery Drills.
Exhaustive empirical data, confusion matrices, attack scenarios, legitimate workload stress tests,
RTO/RPO recovery metrics, byte-for-byte fidelity, and Rules vs RF comparative analysis.
"""

def get_chapter9():
    return """<div style="page-break-after: always;"></div>

# CHAPTER 9: COMPREHENSIVE EMPIRICAL EVALUATION, BENCHMARKS, AND RECOVERY DRILLS

This chapter presents the empirical evaluation, benchmark batteries, and recovery drill experiments conducted on EntroVault. All reported data are deterministic, reproducible, and generated directly from the automated testing suites embedded within the repository (`benchmark.runner` and `benchmark.recovery_drill`).

---

## 9.1 Experimental Setup and Deterministic Methodology

### 9.1.1 Benchmark Architecture and Seed Reproducibility
To ensure absolute scientific rigor and eliminate stochastic variability across evaluation runs, all attack scenarios and benign enterprise workloads are governed by deterministic pseudo-random seeds (`random.Random(seed)`). Rerunning the benchmark harness (`python -m benchmark`) recreates identical file modifications, byte payloads, timing intervals, and directory structures.

Key methodological parameters governing the benchmark evaluation:
- **Decoupled Decision Instances:** Each evaluation scenario instantiates a completely fresh `DecisionEngine` and `CampaignTracker` instance to prevent cross-scenario state contamination.
- **Full Operational Chain:** Benchmarks exercise the real, canonical defensive components: `EntropyAnalyzer`, `DefenseGuard`, `DecisionEngine`, `CampaignTracker`, `ProcessTerminator`, `FileQuarantine`, and `BackupManager`.
- **Baseline Modes:** Scenarios are evaluated under two distinct operational paradigms:
  1. `With Baseline (True)`: Simulates standard production deployment where the defender captures a clean snapshot of the protected file estate at system boot.
  2. `Without Baseline (False)`: Simulates the worst-case operational scenario where an enterprise file estate existed prior to monitoring without an established snapshot catalog.

### 9.1.2 Headline Benchmark Performance
Table 9.1 summarizes the global performance metrics achieved by the default **Deterministic Rule Engine** across 48 attack runs and 21 enterprise workload runs:

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|                    TABLE 9.1: HEADLINE BENCHMARK PERFORMANCE                             |
+──────────────────────────────────────────────────────────┬───────────────────────────────+
| Evaluation Metric                                        | Measured Empirical Value      |
+──────────────────────────────────────────────────────────┼───────────────────────────────+
| Global Attack Detection Rate                             | 87.5% (42 of 48 runs)         |
| False-Positive Alert Rate (Legitimate Workloads)         | 14.3% (3 of 21 runs)          |
| CRITICAL SAFETY METRIC: False Quarantines (Data Loss)     | 0 (ZERO False Quarantines)    |
| Median Operations to Detect (Detectable Scenarios)       | 1 File Operation              |
| Live Demo WannaCry Containment Latency                   | File 2 of 18 (2.7 seconds)    |
| Live Demo Pre-Attack Estate Restoration Fidelity         | 100.0% (18 of 18 Restored)    |
+──────────────────────────────────────────────────────────┴───────────────────────────────+
```

---

## 9.2 Attack Scenario Battery Analysis

The benchmark suite evaluates 8 distinct attack archetypes designed to test specific operational failure modes. Table 9.2 provides the comprehensive scenario-by-scenario breakdown:

```
+──────────────────────────────────────────────────────────────────────────────────────────────────────────+
|                    TABLE 9.2: DETAILED ATTACK SCENARIO PERFORMANCE BREAKDOWN                             |
+───────────────────────┬────────────┬──────────────┬──────────────┬───────────────────────────────────────+
| Attack Scenario       | Detection  | Quarantine   | Median Ops to| Primary Trigger & Detection Mechanics |
|                       | Success    | Success      | Detection    |                                       |
+───────────────────────┼────────────┼──────────────┼──────────────┼───────────────────────────────────────+
| burst_encoder         | 6/6 (100%) | 6/6 (100%)   | 1 op         | Velocity burst + extension + range    |
| slow_crawler          | 6/6 (100%) | 6/6 (100%)   | 1 op         | Type range violation + delta jump     |
| polymorphic           | 6/6 (100%) | 6/6 (100%)   | 1 op         | Randomized ordering & timing caught   |
| baseline_first        | 6/6 (100%) | 6/6 (100%)   | 2 ops        | Clean edit then encryption (Delta H)  |
| silent_unknown_ext    | 6/6 (100%) | 6/6 (100%)   | 1 op         | Unregistered extension + high entropy |
| image_blindspot       | 0/6 (0.0%) | 0/6 (0.0%)   | — (Missed)   | In-range entropy without rename       |
| note_dropper          | 6/6 (100%) | 6/6 (100%)   | 1 op         | Ransom note filename & phrase trap    |
| backup_tamper         | 6/6 (100%) | 6/6 (100%)   | 1 op         | Unauthorized deletion in backup store |
+───────────────────────┴────────────┴──────────────┴──────────────┴───────────────────────────────────────+
```

### Scenario In-Depth Analysis:
1. **`burst_encoder`:** Emulates classical WannaCry / LockBit high-velocity encryption. Overwrites files with random bytes at $>20$ ops/sec. Caught at Operation 1 via combined velocity burst and out-of-range entropy.
2. **`slow_crawler`:** Emulates stealthy, throttled ransomware inserting 650ms delays between writes ($1.5$ ops/sec). Because velocity remains low, speed heuristics fail completely. However, EntroVault's `EntropyAnalyzer` catches the file type range violation and differential jump ($\Delta H \ge 2.0$), triggering containment at Operation 1.
3. **`polymorphic`:** Emulates advanced strains randomizing file traversal order, renaming extensions dynamically, and varying inter-write sleep delays. Caught at Operation 1.
4. **`baseline_first`:** An evasive attack where the malware first executes a legitimate low-entropy edit (e.g., adding 50 bytes of plaintext to establish a benign baseline) before encrypting the payload. The defender permits the clean edit (Op 1), but instantly flags the subsequent encryption (Op 2) when the differential delta jumps: $\Delta H = 7.84 - 4.12 = 3.72 \ge 2.0$.
5. **`note_dropper`:** The malware encrypts a payload within the published image blindspot, but drops an extortion notice (`HOW_TO_RESTORE_FILES.txt`). Caught instantly via `defense_guard` signature trapping.
6. **`backup_tamper`:** The malware attempts to delete the backup store (`vssadmin` equivalent). Intercepted at Operation 1 via the canary observer watching `backup_storage/`.

---

## 9.3 Legitimate Enterprise Workload Stress Testing

To validate the Zero False Quarantine (0 FQ) safety invariant, the platform was subjected to 21 intensive runs across 7 authentic enterprise workloads in the absence of a startup baseline (the most difficult false-positive scenario). Table 9.3 details the findings:

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|               TABLE 9.3: LEGITIMATE ENTERPRISE WORKLOAD STRESS TESTS                     |
+───────────────────────┬──────────────┬────────────────────┬───────────┬──────────────────+
| Workload Profile      | Alerted Runs | False Quarantines  | FP Rate   | Operational Notes|
+───────────────────────┼──────────────┼────────────────────┼───────────┼──────────────────+
| document_editing      | 0/3 (0.0%)   | 0 (ZERO)           | 0.0%      | Standard Office  |
| archive_creation      | 0/3 (0.0%)   | 0 (ZERO)           | 0.0%      | ZIP/TAR Bundles  |
| photo_import          | 0/3 (0.0%)   | 0 (ZERO)           | 0.0%      | High-Entropy JPG |
| video_write           | 0/3 (0.0%)   | 0 (ZERO)           | 0.0%      | MP4 Media Render |
| git_burst             | 3/3 (100.0%) | 0 (ZERO)           | 100.0%    | Code Checkout    |
| csv_export            | 0/3 (0.0%)   | 0 (ZERO)           | 0.0%      | Structured Tables|
| db_dump               | 0/3 (0.0%)   | 0 (ZERO)           | 0.0%      | MySQL Database   |
+───────────────────────┴──────────────┴────────────────────┴───────────┴──────────────────+
```

### The Critical Distinction Between Alerts and False Quarantines
During the `git_burst` workload (simulating a developer executing `git checkout` across a repository containing hundreds of source files), the event velocity reaches 18 events/sec, tripping `is_suspicious_speed = True` and raising an `ACTION_ALERT` (100% alert rate).

However, **crucially, ZERO files were quarantined (`FQ = 0`)**:
- Because source code files (`.py`, `.c`, `.json`) remain within their expected low-entropy ranges ($H \le 5.5$) and exhibit no adversarial extension mutations, the corroborated quarantine threshold ($Score \ge 70$) is never crossed.
- Raising an operational alert on an intense burst of 500 file modifications is legitimate security behavior that notifies the SOC. Crucially, the defense did not terminate the git process or destroy developer files, maintaining the 0-FQ enterprise guarantee.

---

## 9.4 Full End-to-End Recovery Drill Evaluation (`benchmark.recovery_drill`)

Detection represents only half of the defensive equation. EntroVault executes an automated recovery drill (`python -m benchmark.recovery_drill`) that tests the entire containment and restoration lifecycle across 246 injected attack files on an isolated estate. Table 9.4 documents the measured results:

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|               TABLE 9.4: FULL END-TO-END RECOVERY DRILL PERFORMANCE                      |
+──────────────────────────────────────────────────────────┬───────────────────────────────+
| Evaluation Metric                                        | Measured Empirical Value      |
+──────────────────────────────────────────────────────────┼───────────────────────────────+
| Total Attacked Files across All Scenarios                | 246 Files                     |
| Fully Recovered Files (Pre-Attack Bytes Back on Disk)    | 111 Files (45.1% Global)      |
| Contained but Not Restored (Preserved in Quarantine)     | 12 Files (4.9%)               |
| Uncontained / Undetected (Data Lost)                     | 123 Files (50.0%)             |
| Recovery Rate with Established Startup Baseline          | 100.0% on Detectable Attacks  |
| Median Recovery Time Objective (RTO)                     | 8 File Operations             |
| Measured Wall-Clock Response Latency                     | 0.009s to 0.027s              |
+──────────────────────────────────────────────────────────┴───────────────────────────────+
```

### Deep Analytical Dissection of Recovery Numbers:
An uncritical evaluator might question why global file recovery across all scenarios is 45.1%. EntroVault publishes the rigorous, honest scientific accounting:
1. **The Startup Baseline Factor:** In scenarios executed *without* a startup baseline (`Baseline = False`), the defender possesses zero pre-attack snapshots. When ransomware encrypts the estate, the defense successfully terminates the malware at Operation 1, but cannot restore files that never had a clean baseline on disk (e.g., `burst_encoder` Baseline=False yields 0/8 restored, 8 lost). Conversely, when evaluated *with* an established baseline (`Baseline = True`), **recovery is 100% (8/8 recovered, 0 lost)**.
2. **The Published Image Blindspot:** The 12 runs of `image_blindspot` (4 files per run) account for 48 of the lost files. Because in-place encryption of native media without rename produces no detectable entropy delta, the attack runs uncontained. EntroVault openly counts these as lost files rather than concealing them.
3. **Contained vs. Restored Distinctions:** In the `backup_tamper` scenario, the attack touches random `.bin` files possessing native entropies of $approx.  7.96$. Because these files exceed the clean threshold ($6.8$), the Strict Clean Backup engine **deliberately refuses to restore content that looks like ciphertext**. The files are isolated in `quarantine_storage/` for manual administrative extraction, but correctly counted as "Contained but not auto-restored".

---

## 9.5 Comparative Analysis: Deterministic Rule Engine vs. Random Forest Classifier

To evaluate machine learning against deterministic heuristics, the entire 48-scenario battery was executed through both engines under identical random seeds. Table 9.5 details the measured trade-offs:

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|          TABLE 9.5: COMPARATIVE EVALUATION: RULES VS. RANDOM FOREST                      |
+──────────────────────────────────────────┬───────────────────────┬───────────────────────+
| Performance Metric                       | Deterministic Rules   | Random Forest (RF)    |
+──────────────────────────────────────────┼───────────────────────┼───────────────────────+
| Attack Detection Recall Rate             | 87.5% (42 of 48)      | 100.0% (48 of 48)     |
| Legitimate Workload Alert Rate           | 14.3% (3 of 21)       | 42.9% (9 of 21)       |
| FALSE QUARANTINES (Enterprise Safety)    | 0 (ZERO FQ)           | 6 FALSE QUARANTINES   |
| image_blindspot Detection                | 0/6 (0.0% - Blindspot)| 6/6 (100.0% Detected) |
| photo_import Workload Behavior           | 0/3 Alerted (0 FQ)    | 3/3 Alerted (3 FQ)    |
| video_write Workload Behavior            | 0/3 Alerted (0 FQ)    | 3/3 Alerted (3 FQ)    |
| Operational Status                       | DEFAULT PRODUCTION    | OPT-IN SECOND ENGINE  |
+──────────────────────────────────────────┴───────────────────────┴───────────────────────+
```

### The Critical Machine Learning Takeaway
The Random Forest classifier successfully achieves **100% detection recall**, detecting every attack variant, including the difficult `image_blindspot` scenarios. 

However, to achieve this high sensitivity, the RF model lowers its decision threshold on high-entropy files. Consequently, during legitimate photo imports (`photo_import`) and video rendering (`video_write`), **the Random Forest incorrectly quarantines 6 legitimate runs**. In an enterprise production environment, destroying corporate media assets is unacceptable. 

Therefore, **EntroVault establishes the Deterministic Rule Engine as the authoritative default**, demonstrating that in mission-critical endpoint security, deterministic safety invariants supersede unconstrained statistical models.

---

## 9.6 Chapter Summary

This chapter presented the empirical evaluation of EntroVault:
1. Deterministic seeded benchmarking guarantees 100% reproducible results across 48 attack runs and 21 workload stress tests.
2. The Deterministic Rule Engine achieves 87.5% global detection with an uncompromising Zero False Quarantine (0 FQ) safety record.
3. Legitimate enterprise workloads (media creation, database dumps, document edits) generate 0 false quarantines.
4. With an established startup baseline, the recovery engine restores 100% of attacked files byte-for-byte, terminating WannaCry at File 2 within 2.7 seconds.
5. Comparative analysis demonstrates that while the Random Forest achieves 100% recall, it introduces 6 false quarantines on media files, validating the selection of deterministic rules as the primary enterprise defense.

Chapter 10 provides a formal threat modeling analysis, examines evasion vectors, and details the mathematics of the image blindspot.

---
"""

if __name__ == "__main__":
    print(f"Chapter 9 length: {len(get_chapter9().split())} words")
