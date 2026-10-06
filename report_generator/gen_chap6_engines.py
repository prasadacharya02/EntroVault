# report_generator/gen_chap6_engines.py
"""
Generates Chapter 6: Multi-Tier Decision Engines and AI Classifiers.
In-depth academic dissection of the Deterministic Rule Engine, the Campaign Escalation Tracker,
the Random Forest classifier with SHAP explainability, the Deep Q-Network agent,
and the Byzantine-resilient federated threat exchange.
"""

def get_chapter6():
    return """<div style="page-break-after: always;"></div>

# CHAPTER 6: MULTI-TIER DECISION ENGINES AND AI CLASSIFIERS

This chapter details the decision logic and classification architectures powering EntroVault. It analyzes how the platform balances aggressive cryptoviral containment with an uncompromising Zero False Quarantine (0 FQ) safety standard across enterprise workloads.

---

## 6.1 Multi-Tier Decision Architecture Overview

The detection topology of EntroVault operates as a cascading multi-tier hierarchy. Rather than delegating critical process termination decisions to an opaque, monolithic neural network, the system enforces a defense-in-depth decision flow:

```
                  Incoming Ingested File System Event
                                   │
                                   ▼
             [ TIER 0: Hard-Confirmation Signal Interceptor ]
             - Dropped Ransom Note Detected?
             - Defensive Backup / Quarantine Store Tampered?
             - Threat Fingerprint Confirmed by Quorum (K >= 2)?
                                   │
                    YES ───────────┴─────────── NO
                     │                           │
                     ▼                           ▼
        [ ACTION_TERMINATE_QUARANTINE ]  [ TIER 1: Statistical & Behavioral Evaluator ]
                                         - Shannon Entropy >= 6.8?
                                         - Differential Delta |Delta H| >= 2.0?
                                         - Extension Mutated? High Speed Burst?
                                                 │
                                                 ▼
                                         [ TIER 2: Temporal Campaign Escalation ]
                                         - Distinct qualifying files in 15s >= 2?
                                                 │
                                  YES ───────────┴─────────── NO
                                   │                           │
                                   ▼                           ▼
                      [ ESCALATE TO TERMINATE ]     [ Optional AI Classifiers ]
                      [   & CAMPAIGN SWEEP    ]     - Random Forest + SHAP (Opt-in)
                                                    - Deep Q-Network Agent (Opt-in)
                                                    - Deterministic Rule Fallback
```
*Figure 6.1: Multi-Tier Cascading Threat Decision Topology.*

---

## 6.2 Deterministic Rule Engine: The Zero-False-Quarantine Standard

The baseline operational engine deployed by default in EntroVault is the **Deterministic Rule Engine** (`monitoring.pipeline_runner.make_decision`). In commercial enterprise operations, a security agent that destroys or locks legitimate corporate files (such as database dumps, active video transcodes, or compressed source archives) inflicts an operational denial-of-service equivalent to malware. Consequently, the rule engine is engineered to maintain a strict **Zero False Quarantine (0 FQ)** invariant across all standard workloads.

### 6.2.1 Hard Confirmation Triggers
The engine first evaluates non-statistical, high-confidence indicators of malicious intent:
```python
def make_decision(event: dict) -> int:
    # Hard-confirmation signals bypass statistical scoring
    if (event.get("ransom_note") 
            or event.get("defense_tamper")
            or event.get("known_threat_confirmed")):
        return config.ACTION_TERMINATE_QUARANTINE
```
These signals represent definitive adversarial presence: dropping extortion instructions, attempting to delete backup repositories, or matching a threat hash confirmed by independent consensus across enterprise peers.

### 6.2.2 Behavioral Corroboration Primitives
If no hard confirmation exists, the engine interrogates information-theoretic metrics:
- Absolute Entropy: $H(D) \\ge 6.8$ bits/byte.
- Differential Jump: $|\\Delta H| \\ge 2.0$ bits/byte.
- Threat Score: $S \\in [0, 100]$.
- Extension Mutation: `ext_changed = True` (e.g., `.docx` to `.docx.WNCRY`).
- Suspicious Velocity: `is_suspicious_speed = True` ($> 3.0$ events/sec).

The engine enforces the fundamental **Corroboration Constraint**:
```python
    entropy      = event.get("entropy_overall") or 0.0
    delta        = abs(event.get("entropy_delta") or 0.0)
    score        = event.get("threat_score")     or 0.0
    ext_chg      = event.get("ext_changed", False)
    hi_speed     = event.get("is_suspicious_speed", False)
    delta_signal = delta >= config.ENTROPY_DELTA_THRESHOLD

    corroborated = ext_chg or hi_speed or delta_signal

    # Strong score plus corroborating behavioral anomaly
    if score >= 70 and corroborated:
        return config.ACTION_TERMINATE_QUARANTINE

    # High score without behavioral corroboration is alert-only
    if score >= 40:
        return config.ACTION_ALERT

    if hi_speed:
        return config.ACTION_ALERT

    # Unknown high-entropy formats trigger alert, not quarantine
    extension = (event.get("file_extension") or "").lower()
    if entropy >= config.ENTROPY_THRESHOLD and (
        extension not in config.NORMAL_ENTROPY_RANGES
    ):
        return config.ACTION_ALERT

    return config.ACTION_IGNORE
```

Table 6.1 defines the formal action space and operational semantics:

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|                    TABLE 6.1: DECISION ENGINE ACTION SPACE                               |
+────────┬─────────────────────────────┬───────────────────────────────────────────────────+
| Action | Identifier                  | Operational Action Taken by Pipeline              |
+────────┼─────────────────────────────┼───────────────────────────────────────────────────+
| 0      | ACTION_IGNORE               | Allow write; update historical entropy baseline   |
| 1      | ACTION_ALERT                | Log suspicious event to SOC; no destructive action|
| 2      | ACTION_TERMINATE            | Forcibly kill verified process tree (PID)         |
| 3      | ACTION_TERMINATE_QUARANTINE | Kill PID, isolate ciphertext, initiate rollback   |
+────────┴─────────────────────────────┴───────────────────────────────────────────────────+
```

---

## 6.3 Campaign Escalation Tracker (`monitoring.pipeline_runner.CampaignTracker`)

### 6.3.1 The Slow-Crawler Evasion Problem
The primary theoretical vulnerability of per-file heuristic detectors is the **Slow-Crawler Attack Vector**. A sophisticated ransomware strain (such as modernized LockBit or BlackCat builds) can introduce sleep pauses between successive file encryptions (e.g., waiting 650 milliseconds between files, operating at $1.5 - 1.6$ files/sec). Under this velocity, the attack never trips write-burst thresholds. Furthermore, by encrypting files without appending suspicious extensions, each individual file operation produces an isolated `ACTION_ALERT` (score $approx. .  60$) that never crosses the destructive containment threshold ($70 + \\text{corroboration}$). The adversary can slowly encrypt an entire disk estate over several hours without triggering automated mitigation.

### 6.3.2 Temporal Window Correlation and State Automaton
To neutralize this evasion technique, EntroVault introduces the **Campaign Escalation Tracker** (`CampaignTracker`). The tracker recognizes that cryptoviral extortion is intrinsically an aggregate, multi-file campaign.

The tracker maintains an in-memory chronological deque of recent events occurring within a rolling temporal window $\\tau$:
$$\\tau = \\text{CAMPAIGN\\_WINDOW\\_SECONDS} = 15.0 \\text{ seconds}$$

An event qualifies for campaign tracking if and only if it satisfies the qualification predicate:
$$\\text{Qualifies}(e) \\iff \\left( H(e) \\ge 6.8 \\right) \\land \\left( |\\Delta H(e)| \\ge 2.0 \\;\\lor\\; \\text{ExtChanged}(e) \\right)$$

When a newly ingested file event triggers an alert ($a \\ge \\text{ACTION\\_ALERT}$), the tracker interrogates its sliding window:
$$\\text{CountDistinctPaths}(\\text{qualifying events in } [t - \\tau, t]) \\ge \\text{CAMPAIGN\\_MIN\\_FILES} - 1$$

where `CAMPAIGN_MIN_FILES = 2`. 

If at least 2 distinct files exhibit cryptoviral characteristics within 15 seconds, the tracker **escalates the decision immediately to `ACTION_TERMINATE_QUARANTINE`**:

```python
class CampaignTracker:
    def check_and_record(self, event: dict, action: int):
        now = time.time()
        window = config.CAMPAIGN_WINDOW_SECONDS
        
        # Evict stale entries older than 15 seconds
        while self.entries and now - self.entries[0][0] > window:
            self.entries.popleft()

        # Cache verified process holding open file handles
        verified = self._verified_process(event)
        if verified is not None:
            self.last_verified = (now, verified)

        if not self._qualifies(event):
            return False, [], None

        path = os.path.normpath(event.get("file_path") or "")
        others = [e for (_t, p, e, a) in self.entries 
                  if p != path and a >= config.ACTION_ALERT]

        # Escalation condition: 2 or more distinct files in 15 seconds
        escalate = (action >= config.ACTION_ALERT 
                    and len(others) >= config.CAMPAIGN_MIN_FILES - 1)

        self.entries.append((now, path, event, action))

        sweep_events = []
        if escalate:
            # Aggregate all campaign files for active rollback sweep
            sweep_events = [e for (_t, _p, e, _a) in self.entries]

        kill_override = self.last_verified[1] if self.last_verified else None
        return escalate, sweep_events, kill_override
```

### 6.3.3 The Kill-Override and Campaign Sweep Primitives
The `CampaignTracker` incorporates two critical operational innovations:
1. **Kill-Override Attribution:** In rapid or asynchronous attacks, by the time the second file triggers campaign confirmation, the offending process may have already released the second file handle. However, the tracker records the `last_verified` PID from File 1. On escalation, `kill_override` provides the verified malware PID, ensuring that process termination executes reliably even if the current event lacks handle attribution.
2. **Campaign Rollback Sweep:** When campaign escalation trips at File 2, File 1 has already been modified on disk (having only received an alert during its initial ingestion). The escalation engine returns `sweep_events`, causing the response orchestrator to immediately sweep back to File 1, isolating its ciphertext into quarantine and restoring its original clean version. Consequently, **zero files are left damaged on disk**.

---

## 6.4 Random Forest Classifier with SHAP Local Explainability (`ai.rf_model`)

For environments requiring probabilistic risk scoring and transparent threat attribution, EntroVault provides an opt-in **Random Forest Classifier** coupled with **SHAP (SHapley Additive exPlanations)**.

### 6.4.1 11-Dimensional Feature Vector Architecture
The Random Forest model evaluates an 11-dimensional continuous and categorical feature vector extracted directly from runtime telemetry, as detailed in Table 6.2:

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|                    TABLE 6.2: 11-DIMENSIONAL FEATURE SCHEMA                              |
+────┬──────────────────┬───────────────┬──────────────────────────────────────────────────+
| ID | Feature Name     | Domain / Range| Physical Semantics                               |
+────┼──────────────────┼───────────────┼──────────────────────────────────────────────────+
| 0  | entropy_score    | [0.0, 8.0]    | Measured Shannon entropy of the file payload     |
| 1  | entropy_delta    | [-8.0, +8.0]  | Differential jump vs historical clean baseline   |
| 2  | files_per_sec    | [0.0, 50.0+]  | Rolling 10-second file modification velocity     |
| 3  | ext_changed      | {0.0, 1.0}    | Binary flag indicating file extension mutation   |
| 4  | process_age_sec  | [0.0, 3600+]  | Elapsed uptime of the modifying process in sec   |
| 5  | is_signed        | {0.0, 1.0}    | Operating system cryptographic signature status  |
| 6  | files_affected   | [0.0, 200+]   | Cumulative file modifications by this process    |
| 7  | avg_entropy_hist | [0.0, 8.0]    | Mean historical entropy across the local estate  |
| 8  | is_known_process | {0.0, 1.0}    | Binary flag for standard OS processes            |
| 9  | time_hour        | [0.0, 23.0]   | Diurnal hour of execution (off-hours weighting)  |
| 10 | in_normal_range  | {-1.0, 0, 1.0}| +1.0 within normal range, -1.0 out, 0.0 unknown  |
+────┴──────────────────┴───────────────┴──────────────────────────────────────────────────+
```

### 6.4.2 Training Topology and Evaluation Splits
The classifier (`ai.rf_model.RFEngine`) is trained via `ai.train_rf` using an ensemble of 100 decision trees (`n_estimators=100`, `max_depth=10`, `random_state=42`) on versioned synthetic dataset schemas (`schema_version=2`). The training pipeline enforces an 80/20 train/test stratified split, achieving a training ROC-AUC of $0.998$ and an evaluation ROC-AUC of $0.994$.

### 6.4.3 SHAP Local Explainability in SOC Operations
To provide interpretable telemetry for human analysts, the RF engine integrates `shap.TreeExplainer`. For every classified incident, the system computes the exact Shapley attribution values, identifying the top three positive (risk-increasing) and negative (risk-decreasing) feature drivers:

```python
# Sample SHAP Attribution Output rendered on SOC Dashboard:
"Risk Score: 94% | Drivers: entropy_delta (+0.38), in_normal_range (-0.22), ext_changed (+0.19)"
```

### 6.4.4 The Accuracy-Safety Trade-Off (Why RF is Opt-In)
As established in the empirical benchmarks (Chapter 9), the Random Forest achieves **100% attack detection recall (48 of 48 attacks detected)**, successfully closing the image blindspot that evades the rule engine. However, this high recall comes at a severe operational cost: **the RF model triggers 6 false quarantines** on benign high-entropy workloads (`photo_import` and `video_write`).

Because destroying legitimate user files violates EntroVault's core safety mandate, **the Deterministic Rule Engine remains the default operational engine**. The Random Forest is maintained as an explicit opt-in module (`ENTROPY_AI_ENGINE=rf`), illustrating the classic machine-learning precision-recall trade-off in mission-critical cybersecurity systems.

---

## 6.5 Deep Q-Network Reinforcement Learning Engine (`ai.dqn_model`)

EntroVault incorporates an experimental Deep Q-Network agent (`ai.dqn_model.DQNAgent`) designed to explore adaptive mitigation policies in dynamic adversarial environments:
- **Neural Network Topology:** A multi-layer perceptron (MLP) consisting of an input layer ($10$ normalized inputs), two fully connected hidden layers with 64 neurons each utilizing Rectified Linear Unit (ReLU) activations, and a linear output layer producing Q-values across the 4 discrete actions:
  $$10 \\xrightarrow{\\text{Dense}} 64 \\xrightarrow{\\text{ReLU}} 64 \\xrightarrow{\\text{ReLU}} 4 \\quad [Q(s, a_0), Q(s, a_1), Q(s, a_2), Q(s, a_3)]$$
- **Experience Replay Memory:** A cyclic replay buffer (`deque(maxlen=10000)`) storing transition tuples $(s_t, a_t, r_t, s_{t+1}, d_t)$. Minibatches of size $B = 64$ are randomly sampled to decorrelate consecutive training observations.
- **Epsilon-Greedy Exploration Policy:** Initial exploration rate $\\epsilon_{start} = 1.0$ decays exponentially at rate $\\lambda = 0.995$ per episode down to $\\epsilon_{end} = 0.01$.
- **Target Network Synchronization:** To stabilize the regression target in temporal difference learning, a target network $\\hat{Q}(s, a; \\theta^-)$ is synchronized with the online policy network $\\theta$ every 10 episodes.

In compliance with architectural resilience standards, if PyTorch is absent or model weights (`ai/dqn_weights.pth`) are missing, the pipeline logs a warning and automatically activates the deterministic rule engine without interruption.

---

## 6.6 Federated Threat-Fingerprint Exchange Simulation (`blockchain.fingerprint_exchange`)

To facilitate collaborative cyber defense across multi-tenant enterprise environments, EntroVault includes a federated threat intelligence exchange engine (`blockchain.fingerprint_exchange.ThreatExchange`):
- **Cross-Node Threat Memory:** Participating nodes broadcast the cryptographic fingerprints (SHA-256) of confirmed cryptoviral payloads to a synchronized SQLite registry (`blockchain/exchange.db`).
- **The Byzantine Poisoned-Node Defense:** A primary threat to federated intelligence networks is the compromised or malicious peer node. If a single corrupted node broadcasts the hash of a legitimate system binary (such as `cmd.exe` or `svchost.exe`) as malware, peer systems that automatically execute destructive quarantine would experience immediate operational failure.

To prevent this attack, EntroVault implements a **Quorum-Based Verification Threshold ($K \ge 2$)**:
1. **Single-Node Sighting ($K = 1$):** A fingerprint reported by only one node is classified as *Corroborating Intelligence*. It increments the local threat score by $+25$ points but **is strictly barred from triggering automated quarantine alone**.
2. **Quorum Consensus ($K \ge 2$):** Only when at least two independent, uncoordinated tenant nodes have independently quarantined and reported the identical fingerprint does the status transition to `confirmed = 1`. Upon reaching quorum, peer nodes treat incoming matching files as pre-confirmed threats, enabling instantaneous zero-touch quarantine.

---

## 6.7 Chapter Summary

This chapter detailed the multi-tier decision hierarchy of EntroVault:
1. The Deterministic Rule Engine enforces an uncompromising Zero False Quarantine (0 FQ) standard by requiring corroborating behavioral flags before initiating containment.
2. The Campaign Escalation Tracker correlates qualifying cryptoviral events across a sliding 15-second window, neutralizing slow-crawling attacks at File 2 of execution while sweeping previously alerted files.
3. The Random Forest classifier provides 11-dimensional feature evaluation with local SHAP interpretability, operating as an opt-in high-recall model.
4. The Deep Q-Network models adaptive containment within a Markov Decision Process framework with graceful rule fallbacks.
5. The Federated Threat Exchange implements a Byzantine-fault-tolerant quorum model ($K \ge 2$) that prevents poisoned nodes from inducing denial-of-service across peer tenants.

Chapter 7 details the automated response orchestration, process termination mechanics, and strict clean backup restoration engine.

---
"""

if __name__ == "__main__":
    print(f"Chapter 6 length: {len(get_chapter6().split())} words")
