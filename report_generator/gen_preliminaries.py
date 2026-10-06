# report_generator/gen_preliminaries.py
"""
Generates the front matter and preliminary pages for the 100-page IEEE Major Project Report.
Includes Title Page, Certificate, Declaration, Acknowledgements, Abstract,
Table of Contents, List of Figures, List of Tables, List of Algorithms, and Acronyms.
"""

def get_preliminaries():
    return """# PROACTIVE RANSOMWARE DEFENCE USING ENTROPY FINGERPRINTING, CAMPAIGN ESCALATION, AND IMMUTABLE BLOCKCHAIN AUDIT TRAILS
## A Purple-Team Cyber-Physical Architecture for Sub-Second Cryptoviral Detection, Zero-Data-Loss Containment, and Cryptographic Forensic Integrity

---

**A MAJOR PROJECT DISSERTATION REPORT (200 MARKS)**  
*Submitted in Partial Fulfillment of the Requirements for the Degree of*  
**BACHELOR OF TECHNOLOGY / MASTER OF SCIENCE**  
*IN*  
**COMPUTER SCIENCE & CYBERSECURITY ENGINEERING**  

---

**Academic Year:** 2025–2026  
**Document Classification:** Standard IEEE University Dissertation & Technical Specification  
**Document Series:** ENTROVAULT-ENG-THESIS-REV-4.2  
**Target Venue:** IEEE Transactions on Information Forensics and Security / IEEE Transactions on Dependable and Secure Computing  
**Code Repository & Verified Lab Build:** `prasadacharya02/EntroVault`  
**Distribution:** Unrestricted Academic & Research Release  

---

<div style="page-break-after: always;"></div>

## CERTIFICATE OF APPROVAL AND EVALUATION

This is to certify that the Major Project Dissertation entitled:

> **"Proactive Ransomware Defence using Entropy Fingerprinting, Campaign Escalation, and Immutable Blockchain Audit Trails: A Purple-Team Cyber-Physical Architecture for Sub-Second Cryptoviral Detection, Zero-Data-Loss Containment, and Cryptographic Forensic Integrity"**

submitted by the project candidate team in partial fulfillment of the requirements for the award of the Degree of **Bachelor of Technology / Master of Science in Computer Science and Engineering (Cybersecurity)**, is an authentic record of original research and engineering carried out under our supervision and guidance during the academic period 2025–2026.

The technical designs, empirical benchmarks, mathematical formulations, and source code implementations described in this thesis have been rigorously evaluated, subjected to controlled purple-team malware detonations, and defended against adversarial vectors in the cybersecurity research laboratory. To the best of our knowledge, the results, models, and empirical findings presented in this report have not formed the basis for the award of any other degree, diploma, or title in this or any other university.

<br><br>

--------------------------------------------- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ---------------------------------------------  
**Internal Project Supervisor / Advisor** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Head of Department (CSE & Cybersecurity)**  
Department of Computer Science & Engineering &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Faculty of Information Technology  
Date: October 6, 2026 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Date: October 6, 2026  

<br><br>

--------------------------------------------- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ---------------------------------------------  
**External Board Examiner (Industry Expert)** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **External Board Examiner (Academic Chair)**  
Senior SOC Architect / Security Evaluator &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Professor of Information Security  
Date: October 6, 2026 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Date: October 6, 2026  

---

<div style="page-break-after: always;"></div>

## CANDIDATE DECLARATION OF ORIGINALITY

We hereby declare that the research, architecture, mathematical derivations, software engineering, and experimental evaluations presented in this major project report titled **"Proactive Ransomware Defence using Entropy Fingerprinting, Campaign Escalation, and Immutable Blockchain Audit Trails"** are the sole outcome of our individual and joint engineering investigations. 

We explicitly affirm the following academic and ethical commitments:
1. **Academic Integrity & Plagiarism Standard:** The prose, analysis, diagrams, and algorithmic implementations contained herein have been composed independently. All external literature, algorithmic concepts, and foundational cryptographic primitives (including Shannon Information Entropy, NIST Secure Hash Standards, Ethereum Virtual Machine specifications, and scikit-learn architectures) are strictly attributed and cited in accordance with IEEE referencing standards.
2. **Empirical Authenticity:** No benchmark figures, detection rates, false quarantine statistics, or recovery times have been fabricated or artificially inflated. Where the defensive architecture experiences physical limitations—such as the mathematical indistinguishability of in-place encryption on previously compressed media (the *image blindspot*) or the impossibility of decrypting ciphertext encrypted with destroyed asymmetric session keys—these limitations are explicitly documented and published with mathematical proofs.
3. **Reproducibility Guarantee:** All experimental findings reported across Chapter 8 and Chapter 9 are deterministic, governed by pseudorandom seeds, and directly regenerable using the embedded benchmarking and recovery drill test suites included in the root codebase (`python -m benchmark` and `python -m benchmark.recovery_drill`).

Candidate Signature(s):  
`[Candidate Name / Roll No. / Signature Line]`  
`[Candidate Name / Roll No. / Signature Line]`  
`Department of Computer Science & Engineering, College of Engineering & Technology`  

---

<div style="page-break-after: always;"></div>

## ACKNOWLEDGEMENTS

The design, implementation, and rigorous stress testing of an end-to-end autonomous cryptoviral defense pipeline—spanning sub-second operating system kernel event ingestion, information-theoretic entropy modeling, temporal campaign correlation, strict cryptographic rollback, and distributed ledger smart contract deployment—would not have been feasible without the intellectual guidance, technical support, and structural resources provided by our academic institution and the broader cybersecurity research community.

First and foremost, we express our profound gratitude to our internal research supervisor and the faculty members of the Department of Computer Science and Engineering. Their insistence on engineering honesty—specifically mandating that detection limitations and recovery constraints be transparently quantified rather than obscured behind fabricated claims—fundamentally shaped the rigor of this project. Their critical critiques during the architectural review and interim evaluation stages challenged us to abandon naive per-file heuristics and develop the multi-event temporal escalation engine that defines our production-grade defense.

We extend our sincere thanks to the Systems and Networking Laboratory staff who provisioned the isolated hardware environments, hypervisor sandboxes, and virtual LAN topologies necessary to detonate weaponized ransomware strains safely. Conducting real-time purple-team simulations involving simulated WannaCry, LockBit, REvil, and Ryuk encryptions without risking institutional network integrity demanded specialized containment policies and strict operational safeguards.

We also recognize the open-source software and security research communities. The creators and maintainers of the Python `watchdog` framework, the Ethereum `web3.py` client, the Ganache local EVM testnet, `scikit-learn`, `psutil`, `Flask-SocketIO`, and the MITRE ATT&CK knowledge base have produced tools of exceptional utility, upon which our research pipeline is constructed.

Finally, we express our deepest appreciation to our families, peers, and fellow researchers whose patience, technical debates, and steady encouragement sustained us through the exhaustive debugging sessions, live socket latency tuning, and rigorous benchmark runs required to produce this comprehensive 200-mark dissertation report.

---

<div style="page-break-after: always;"></div>

## EXECUTIVE ABSTRACT

Cryptoviral extortion, commonly known as ransomware, remains one of the most destructive asymmetric threats confronting contemporary enterprise infrastructure and critical cyber-physical systems. Traditional signature-based Anti-Virus (AV) solutions and modern behavioral Endpoint Detection and Response (EDR) platforms demonstrate catastrophic latency when confronting zero-day, polymorphic, or slow-crawling cryptoviral variants. Furthermore, commercial endpoint security agents frequently corrupt disaster recovery workflows by capturing in-progress ciphertext as valid baseline backups, or fail to preserve tamper-evident forensic chains of custody acceptable in legal and regulatory proceedings.

This dissertation presents **EntroVault (codenamed ENTROPY)**, an enterprise-grade, purple-team-validated proactive defense ecosystem designed to achieve sub-second ransomware detection, zero-false-quarantine containment, automated byte-for-byte pre-attack estate restoration, and tamper-proof forensic logging. Built on a tripartite purple-team architecture comprising a live Security Operations Center (SOC) dashboard, an isolated victim workstation with a neutral file explorer, and a multi-strain attacker command-and-control detonation console, EntroVault replaces brittle static heuristics with a multi-tiered information-theoretic and behavioral pipeline.

The core detection engine combines block-level Shannon information entropy analysis, per-file-type empirical distribution boundaries, and sliding-window entropy delta thresholds ($\Delta H \ge 2.0$) with an innovative **Campaign Escalation Tracker**. By identifying multi-file encryption campaigns across a sliding 15-second window, the system neutralizes slow-crawling, realistic attacks (operating at 1.6 operations per second) at file 2 of execution, preventing estate-wide data compromise. An integrated **Strict Clean Backup Engine** eliminates the catastrophic defect of ciphertext-as-baseline poisoning by enforcing boundary validation and delta caps prior to snapshot admission. For forensic integrity, EntroVault deploys a dual-mode ledger coupling an Ethereum Virtual Machine (EVM) Solidity smart contract (`ThreatLogger.sol`) on a local Ganache network with an autonomous, crash-resilient SQLite fallback ledger.

The entire architecture is verified across 126 unit and integration test suites, deterministic multi-seed attack benchmarks across 8 adversarial scenarios and 7 legitimate enterprise workloads, and full end-to-end recovery drills. In live purple-team detonations of simulated WannaCry payloads, EntroVault reliably terminates malicious execution trees within 2.7 seconds at file 2 of 18, achieving **100% byte-for-byte recovery (18 of 18 files restored)**, leaving 0 unencrypted `.WNCRY` artifacts on disk, and recording 0 false quarantines across legitimate document editing, database exports, and archive routines. In an honest scientific assessment, this report analyzes the physical boundaries of Shannon entropy detection—specifically the mathematical indistinguishability of in-place encryption on previously compressed media (*image blindspots*)—and establishes an empirical foundation for multi-signal kernel-level defenses.

**Index Terms:** Ransomware Mitigation, Shannon Information Entropy, Campaign Escalation, Strict Disaster Recovery, Ethereum Smart Contracts, Immutable Audit Trails, Endpoint Detection & Response (EDR), Purple-Team Testing.

---

<div style="page-break-after: always;"></div>

## TABLE OF CONTENTS

- **Certificate of Approval and Evaluation** ............................................................. ii
- **Candidate Declaration of Originality** ............................................................. iii
- **Acknowledgements** .................................................................................... iv
- **Executive Abstract** .................................................................................... v
- **Table of Contents** .................................................................................... vi
- **List of Figures** .......................................................................................... ix
- **List of Tables** ........................................................................................... xi
- **List of Algorithms** ..................................................................................... xiii
- **List of Abbreviations and Acronyms** ................................................................ xiv

---

### CHAPTER 1: INTRODUCTION AND PROBLEM CONTEXT
- 1.1 The Ransomware Epidemic: Evolution, Modus Operandi, and Asymmetry
- 1.2 Analysis of MITRE ATT&CK Technique T1486 (Data Encrypted for Impact)
- 1.3 Critical Deficiencies in State-of-the-Art Anti-Virus and EDR Solutions
  - 1.3.1 Inefficacy of Signature-Based Hash Matching against Polymorphism
  - 1.3.2 Heuristic Brittleness and the High False-Positive Dilemma
  - 1.3.3 The Ciphertext Backup Contamination Vulnerability
  - 1.3.4 Forensic Volatility and Log Tampering in Host Environments
- 1.4 Problem Statement and Formal Project Mandate
- 1.5 Project Aim and Core Technical Objectives (200-Mark Specification)
- 1.6 Scope and Operational Boundaries of Research
- 1.7 Summary of Key Novel Engineering Contributions
- 1.8 Dissertation Structural Roadmap

---

### CHAPTER 2: COMPREHENSIVE LITERATURE SURVEY AND RELATED WORK
- 2.1 Information-Theoretic Techniques in Malware Analysis
  - 2.1.1 Historical Evolution of Entropy in Cryptanalysis and File Identification
  - 2.1.2 Block-Based vs. File-Wide Entropy in Crypto-Ransomware Detection
- 2.2 File System Monitoring Architectures: Userspace vs. Kernel Drivers
  - 2.2.1 Operating System Notification Hooks: `inotify`, `kqueue`, and `ReadDirectoryChangesW`
  - 2.2.2 Latency vs. Portability Trade-offs in Python `watchdog` Implementation
- 2.3 Machine Learning and Deep Reinforcement Learning in Cryptoviral Mitigation
  - 2.3.1 Supervised Classifiers and the Risk of False Quarantines
  - 2.3.2 Explainable AI (XAI) and SHAP Value Integration in Security Operations
  - 2.3.3 Markov Decision Processes and Deep Q-Networks for Automated Mitigation
- 2.4 Distributed Ledger Technology and Cryptographic Integrity in Forensics
  - 2.4.1 EVM Smart Contracts for Non-Repudiable Incident Logging
  - 2.4.2 Federated Threat Intelligence Exchanges and the Poisoned Node Problem
- 2.5 Critical Comparative Matrix: EntroVault vs. Academic and Commercial SOTA
- 2.6 Summary of Identified Research Gaps

---

### CHAPTER 3: MATHEMATICAL AND THEORETICAL FOUNDATIONS
- 3.1 Information-Theoretic Foundations of Shannon Entropy
  - 3.1.1 Discrete Memoryless Source Modeling
  - 3.1.2 Shannon's Entropy Formula and Byte Frequency Distributions
  - 3.1.3 Maximum Entropy Theorem for Uniform Distributions
- 3.2 Sliding Window and Multi-Segment Entropy Dynamics
  - 3.2.1 Partial-Encryption Detection via Tri-Segment Sampling
  - 3.2.2 Sliding Window Step Functions and Boundary Artifacts
- 3.3 Statistical Hypothesis Testing and Chi-Square Goodness-of-Fit
  - 3.3.1 Chi-Square ($\chi^2$) Distribution of Native vs. Ciphertext Payloads
  - 3.3.2 Monte Carlo Approximations for Large-File Sub-Sampling
- 3.4 Per-File-Type Empirical Probability Density Functions (PDFs)
  - 3.4.1 Plaintext, Structured Office Documents, Executables, and Compressed Media
  - 3.4.2 The Differential Entropy Threshold ($\Delta H$) Formulation
- 3.5 Markov Chain Modeling of File System Transformation Sequences
- 3.6 Reinforcement Learning Formulation: MDP, Bellman Optimality, and Q-Convergence
- 3.7 Dual Cryptographic Hashing and Collision Resistance Bounds (SHA3-256 and SHA-256)
- 3.8 Chapter Summary

---

### CHAPTER 4: SYSTEM ARCHITECTURE AND DETAILED SPECIFICATION
- 4.1 Global Architectural Blueprint: The EntroVault Tripartite Topology
- 4.2 Three-Tier Purple-Team Deployment Model
  - 4.2.1 Tier 1: Real-Time SOC Telemetry and Forensic Dashboard (Port 5000)
  - 4.2.2 Tier 2: The Neutralized Victim Workstation and File Explorer (Port 5001)
  - 4.2.3 Tier 3: The Multi-Strain Attacker Command-and-Control Console (Port 8001)
- 4.3 End-to-End Runtime Pipeline Data Flow
- 4.4 Hardware, Software, and Environment Requirements
  - 4.4.1 Laboratory Hardware Topology
  - 4.4.2 Software Dependencies and Python Subsystem Configuration
- 4.5 Security Boundaries, Threat Isolation, and Path Containment
- 4.6 Architectural Resilience and Compatibility Facades
- 4.7 Chapter Summary

---

### CHAPTER 5: CORE ENGINEERING AND IMPLEMENTATION MECHANICS
- 5.1 Real-Time File System Observer Subsystem (`monitoring.watchdog_monitor`)
  - 5.1.1 Recursive Directory Traversal and Observer Thread Management
  - 5.1.2 Temporal Event Deduplication Engine (`monitoring.event_deduplicator`)
- 5.2 High-Throughput Ingestion Queue and Batching Pipeline (`monitoring.event_pipeline`)
- 5.3 Defense Guard: Anti-Tamper and Signature Trapping (`monitoring.defense_guard`)
  - 5.3.1 Ransom Note Trapping via Filename Heuristics and Phrase Catalogs
  - 5.3.2 Protected Store Anti-Tampering Engine (Canary Monitoring)
- 5.4 High-Performance Entropy Calculation Engine (`entropy.entropy_calculator`)
  - 5.4.1 Optimized Byte Frequency Vectorization
  - 5.4.2 Tri-Segment Partial File Decomposition (Head, Body, Tail)
- 5.5 Dual-Layer Cryptographic Fingerprinting Engine (`storage.hashing`)
- 5.6 SQLite Storage Architecture and Transactional Schema (`storage.database`)
- 5.7 Chapter Summary

---

### CHAPTER 6: MULTI-TIER DECISION ENGINES AND AI CLASSIFIERS
- 6.1 Multi-Tier Decision Architecture Overview
- 6.2 Deterministic Rule Engine: The Zero-False-Quarantine Standard
  - 6.2.1 Hard Confirmation Triggers (Notes, Tamper, Quorum Consensus)
  - 6.2.2 Corroboration Primitives: $\Delta H$, Extension Mutation, and Velocity
  - 6.2.3 Scoring Thresholds and Action Mapping
- 6.3 Campaign Escalation Tracker (`monitoring.pipeline_runner.CampaignTracker`)
  - 6.3.1 The Slow-Crawler Evasion Problem
  - 6.3.2 Temporal Window Correlation (15-Second Sliding Window)
  - 6.3.3 Multi-File Escalation Automaton and State Machine
- 6.4 Random Forest Classifier with SHAP Local Explainability (`ai.rf_model`)
  - 6.4.1 11-Dimensional Feature Vector Architecture
  - 6.4.2 Training Topology, Hyperparameter Tuning, and Evaluation Splits
  - 6.4.3 SHAP Feature Importance and SOC Attribution Rendering
- 6.5 Deep Q-Network Reinforcement Learning Engine (`ai.dqn_model`)
  - 6.5.1 State Vector Representation and Normalization
  - 6.5.2 Discrete Action Space and Penalty-Biased Reward Engineering
  - 6.5.3 Experience Replay, Target Network Updating, and Fallback Grace
- 6.6 Federated Threat-Fingerprint Exchange Simulation (`blockchain.fingerprint_exchange`)
  - 6.6.1 Multi-Tenant Cross-Node Memory
  - 6.6.2 The Byzantine Poisoned Node Defense (Quorum Threshold $K \ge 2$)
- 6.7 Chapter Summary

---

### CHAPTER 7: AUTOMATED RESPONSE, STRICT BACKUP, AND BYTE-LEVEL RECOVERY
- 7.1 Autonomous Response Orchestration Subsystem (`response.response_module`)
- 7.2 Verified Process Attribution and Process Termination Mechanics
  - 7.2.1 Handle Extraction via `psutil` and Verification Challenges
  - 7.2.2 The Zombie Process Problem and Instant Clean Reaping
  - 7.2.3 Defender Tooling Whitelist and Self-Kill Immunity
- 7.3 Install-Time Isolated Quarantine Vault Subsystem
  - 7.3.1 Installation-Time Physical Provisioning Mandate
  - 7.3.2 Dual-Hash File Encapsulation and JSON Metadata Serialization
  - 7.3.3 The Cryptographic Non-Decryption Proof (Honest Viva Defense)
- 7.4 Strict Clean Backup Engine (`response.backup_manager`)
  - 7.4.1 The Ciphertext Backup Contamination Defect
  - 7.4.2 The Strict Clean Verification Algorithm
  - 7.4.3 Bounded Versioning, Pruning, and Tamper Resistance
- 7.5 Post-Kill Estate Verification and Active Remediation
  - 7.5.1 Content-Based Estate Walking vs. Blind Entropy Sampling
  - 7.5.2 Atomic In-Place Rollback and Reverse-Rename Mechanics
- 7.6 Automated Forensic Incident Reporting (`response.forensic_report`)
- 7.7 Chapter Summary

---

### CHAPTER 8: BLOCKCHAIN LEDGER, SMART CONTRACTS, AND FORENSIC IMMUTABILITY
- 8.1 The Forensic Requirement for Decentralized Non-Repudiation
- 8.2 EVM Smart Contract Architecture (`contracts/ThreatLogger.sol`)
  - 8.2.1 ThreatEvent Struct and State Storage Model
  - 8.2.2 Function Modifiers, Access Control, and Reentrancy Safety
  - 8.2.3 Log Threat Event Dispatch and Gas Optimization
- 8.3 EVM Gas Consumption Dynamics and Transaction Costs
- 8.4 Ganache Ethereum Deployment and Web3 Integration (`blockchain.connector`)
- 8.5 Resilient Dual-Mode Architecture: Autonomous LocalLedger Fallback
- 8.6 Forensic Chain of Custody and Audit Trail Schema
- 8.7 Chapter Summary

---

### CHAPTER 9: COMPREHENSIVE EMPIRICAL EVALUATION, BENCHMARKS, AND RECOVERY DRILLS
- 9.1 Experimental Setup and Deterministic Methodology
  - 9.1.1 Sandboxed Laboratory Environment Specifications
  - 9.1.2 Deterministic Seed Generation and Reproducibility
- 9.2 Attack Scenario Battery Analysis
  - 9.2.1 Burst Encoder Scenario
  - 9.2.2 Slow Crawler Scenario
  - 9.2.3 Polymorphic Payload Scenario
  - 9.2.4 Baseline-First Deceptive Scenario
  - 9.2.5 Silent Unknown Extension Scenario
  - 9.2.6 Image Blindspot Scenario (Honest Limitation Analysis)
  - 9.2.7 Note Dropper Scenario
  - 9.2.8 Backup Tamper Scenario
- 9.3 Legitimate Enterprise Workload Stress Testing
  - 9.3.1 Document Editing, Archive Creation, and Compaction
  - 9.3.2 High-Entropy Media Ingestion: Photo Imports and Video Transcoding
  - 9.3.3 Software Engineering Workloads: Git Burst Operations
  - 9.3.4 Enterprise Data Pipeline: CSV Exports and Database Dumps
- 9.4 Full End-to-End Recovery Drill Evaluation (`benchmark.recovery_drill`)
  - 9.4.1 Recovery Time Objective (RTO) Metrics: Operations and Clock Seconds
  - 9.4.2 Recovery Point Objective (RPO) and Data Preservation Ratios
  - 9.4.3 Byte-for-Byte Checksum Verification Results
- 9.5 Comparative Analysis: Deterministic Rule Engine vs. Random Forest Classifier
  - 9.5.1 Detection Recall vs. False Quarantine Safety Bar
  - 9.5.2 Receiver Operating Characteristic (ROC) and Confusion Matrices
- 9.6 Chapter Summary

---

### CHAPTER 10: ATTACK SURFACE MODELING, LIMITATIONS, AND BLINDSPOT MITIGATION
- 10.1 Formal STRIDE Threat Model Applied to EntroVault
- 10.2 In-Depth Analysis of the Image Blindspot Phenomenon
  - 10.2.1 Mathematical Indistinguishability Proof
  - 10.2.2 Potential Mitigation Vectors: Magic Bytes, Structural Parsing, and Size Ratios
- 10.3 Adversarial Evasion Vectors and Defensive Countermeasures
  - 10.3.1 Sub-Threshold Partial File Interleaving
  - 10.3.2 Timing Jitter and Extended Dwell-Time Attacks
  - 10.3.3 Direct Kernel Object Manipulation (DKOM) and Process Spoofing
- 10.4 Authentication and Vault PIN Security Architecture
- 10.5 Chapter Summary

---

### CHAPTER 11: REAL-TIME SOC INTERFACE, NEUTRAL VICTIM EXPLORER, AND ATTACKER SIMULATION
- 11.1 Real-Time Telemetry Push Architecture (`app.py` via Flask-SocketIO)
  - 11.1.1 WebSocket Frame Serialization and 400ms Heartbeat Pushes
  - 11.1.2 Dynamic Entropy Visualizer and Threat Level Instrumentation
- 11.2 The Neutral Victim Workstation Experience (`victim_server/app.py`)
  - 11.2.1 Human-Factors Rationale: Concealing Cryptoviral Threat Details
  - 11.2.2 Secure Vault Access Protocol and PIN Authentication
- 11.3 Multi-Strain Attacker Command-and-Control Console (`attacker_server/app.py`)
  - 11.3.1 Synthetic Detonation of 10 Real-World Ransomware Archetypes
  - 11.3.2 Variable Encryption Delays and Polymorphic Payloads
- 11.4 End-to-End Live Purple-Team Demonstration Workflow (200-Mark Script)
- 11.5 Chapter Summary

---

### CHAPTER 12: CONCLUSIONS, LESSONS LEARNED, AND FUTURE RESEARCH DIRECTIONS
- 12.1 Project Retrospective and Milestone Summary
- 12.2 Critical Engineering Trade-offs and Lessons Learned
- 12.3 Production Hardening Roadmap: Kernel Drivers, eBPF, and Minifilters
- 12.4 Concluding Remarks

---

### REFERENCES (IEEE FORMAT)
### APPENDIX A: ThreatLogger.sol Complete Smart Contract Source Code
### APPENDIX B: Core Algorithmic Formulations in Formal Pseudocode (Algorithms 1–10)
### APPENDIX C: Full Benchmark and Dataset Feature Schemas
### APPENDIX D: Comprehensive 200-Mark Viva Voce Defense Guide (Questions & Model Answers)

---

<div style="page-break-after: always;"></div>

## LIST OF FIGURES

- **Figure 1.1:** The Asymmetric Cryptoviral Attack Lifecycle and Mean-Time-to-Encrypt Timeline
- **Figure 1.2:** MITRE ATT&CK Enterprise Matrix Mapping for Cryptoviral Campaign T1486
- **Figure 3.1:** Shannon Entropy $H(X)$ of a Binary Source as a Function of Symbol Probability $p$
- **Figure 3.2:** Empirical Byte Frequency Histograms: Plaintext Text vs. AES-256 Ciphertext
- **Figure 3.3:** Sliding-Window Tri-Segment Entropy Profiling for Partial-File Encryption
- **Figure 3.4:** State Transition Diagram of File System Transformation as a Markov Process
- **Figure 4.1:** EntroVault High-Level Tripartite Architecture (SOC, Victim, Attacker)
- **Figure 4.2:** Complete End-to-End Runtime Pipeline Sequence Diagram
- **Figure 5.1:** Watchdog Multi-Path Recursive Observer Event Ingestion Topology
- **Figure 5.2:** Temporal Event Deduplication Sliding Time Window Filter
- **Figure 5.3:** Dual-Layer Cryptographic Hashing Architecture (SHA3-256 and SHA-256)
- **Figure 6.1:** Deterministic Decision Engine Multi-Stage Threshold Cascade
- **Figure 6.2:** Campaign Escalation Tracker State Machine and 15-Second Window Evaluation
- **Figure 6.3:** Random Forest Decision Trees and SHAP Feature Importance Attribution
- **Figure 6.4:** Deep Q-Network Agent Architecture with Experience Replay Buffer
- **Figure 6.5:** Federated Threat-Fingerprint Exchange Quorum Consensus ($K \ge 2$)
- **Figure 7.1:** Autonomous Response Execution Flow: Kill, Isolate, Sweep, Verify, and Restore
- **Figure 7.2:** Strict Clean Backup Filtering Flowchart: Rejecting Ciphertext Contamination
- **Figure 7.3:** In-Place File Restoration and Reverse-Rename Mechanical Flow
- **Figure 8.1:** EVM ThreatLogger Smart Contract Storage Layout and Event Dispatch
- **Figure 8.2:** Dual-Mode Blockchain Architecture: Ganache Provider with LocalLedger Fallback
- **Figure 9.1:** Attack Detection Rates Across 8 Experimental Scenarios: Rules vs. Random Forest
- **Figure 9.2:** False Quarantine Comparison: Deterministic Zero-Bar vs. Probabilistic Classifier
- **Figure 9.3:** Live WannaCry Purple-Team Detonation Timeline: Detection and Kill at File 2
- **Figure 10.1:** STRIDE Threat Model Applied to EntroVault Host Defense Architecture
- **Figure 10.2:** The In-Place Compressed Media Blindspot: Entropy Invariance Illustration
- **Figure 11.1:** SOC Dashboard User Interface Layout and Real-Time Telemetry Graphs
- **Figure 11.2:** Neutral Victim File Explorer vs. Authenticated Forensic Vault View
- **Figure 11.3:** Attacker Detonation Console Configuration and Attack Trigger Interface

---

<div style="page-break-after: always;"></div>

## LIST OF TABLES

- **Table 2.1:** Systematic Comparative Feature Matrix: EntroVault vs. Academic and Commercial SOTA
- **Table 3.1:** Theoretical and Empirical Shannon Entropy Ranges for Enterprise File Formats
- **Table 4.1:** Hardware Specifications of Purple-Team Evaluation Environment
- **Table 4.2:** Core Software Components, Versions, and Operational Dependencies
- **Table 5.1:** File Extension Baseline Probability Ranges (`NORMAL_ENTROPY_RANGES`)
- **Table 5.2:** Relational Database Table Definitions and Schema Mappings (`entropy.db`)
- **Table 6.1:** Decision Engine Action Space Definitions and Operational Semantics
- **Table 6.2:** 11-Dimensional Feature Vector Schema for Random Forest and DQN Agents
- **Table 6.3:** Federated Threat Exchange Multi-Tenant Simulation Matrix
- **Table 7.1:** Strict Clean Backup Verification Parameters and Safety Constraints
- **Table 8.1:** Solidity `ThreatLogger.sol` Gas Consumption Profile Across EVM Operations
- **Table 8.2:** Forensic JSON Incident Report Data Schema
- **Table 9.1:** Headline Benchmark Detection Results Across 48 Attack Runs
- **Table 9.2:** Detailed Attack Scenario Performance Breakdown (Deterministic Rule Engine)
- **Table 9.3:** Legitimate Enterprise Workload Stress Test Results (False Positive Evaluation)
- **Table 9.4:** Random Forest Classifier vs. Deterministic Rule Engine Performance Matrix
- **Table 9.5:** Comprehensive End-to-End Recovery Drill Results across 246 Injected Files
- **Table 9.6:** Measured RTO and Wall-Clock Response Latencies under Live WannaCry Detonation
- **Table 10.1:** Formal STRIDE Security Analysis and Mitigation Strategies
- **Table 11.1:** Attacker Console Ransomware Strain Profiles and Synthetic Mutation Parameters

---

<div style="page-break-after: always;"></div>

## LIST OF ALGORITHMS

- **Algorithm 1:** Shannon Information Entropy Vectorized Computation (`calculate_entropy`)
- **Algorithm 2:** Tri-Segment Partial File Entropy Profiling (`calculate_file_entropy`)
- **Algorithm 3:** Temporal Event Ingestion, Deduplication, and Burst Normalization
- **Algorithm 4:** Anti-Tamper and Ransom Note Trap Inspection (`collect_threat_flags`)
- **Algorithm 5:** Multi-Tier Deterministic Threat Decision Logic (`make_decision`)
- **Algorithm 6:** Temporal Cross-File Campaign Escalation Tracker (`check_and_record`)
- **Algorithm 7:** Verified Process Attribution and Zombie-Safe Process Termination
- **Algorithm 8:** Strict Clean Backup Qualification and Storage Ingestion (`_is_clean`)
- **Algorithm 9:** Content-Based Post-Kill Estate Verification and Rollback Remediation
- **Algorithm 10:** Byzantine-Fault-Tolerant Federated Threat Fingerprint Consensus

---

<div style="page-break-after: always;"></div>

## LIST OF ABBREVIATIONS AND ACRONYMS

| Acronym | Expanded Terminology |
| :--- | :--- |
| **AES** | Advanced Encryption Standard (NIST FIPS 197) |
| **API** | Application Programming Interface |
| **AV** | Anti-Virus Software |
| **BFT** | Byzantine Fault Tolerance |
| **CBC** | Cipher Block Chaining |
| **CPU** | Central Processing Unit |
| **DDoS** | Distributed Denial of Service |
| **DKOM** | Direct Kernel Object Manipulation |
| **DQN** | Deep Q-Network (Reinforcement Learning) |
| **CTR** | Counter Mode (Symmetric Encryption) |
| **EDR** | Endpoint Detection and Response |
| **EVM** | Ethereum Virtual Machine |
| **FIPS** | Federal Information Processing Standards |
| **FN** | False Negative |
| **FP** | False Positive |
| **FQ** | False Quarantine (Defensive File Destruction) |
| **GBC** | Gini Impurity Based Criterion |
| **GUI** | Graphical User Interface |
| **HTTP** | Hypertext Transfer Protocol |
| **IEEE** | Institute of Electrical and Electronics Engineers |
| **I/O** | Input / Output |
| **JSON** | JavaScript Object Notation |
| **LAN** | Local Area Network |
| **MB** | Megabyte ($10^6$ or $2^{20}$ bytes) |
| **MDP** | Markov Decision Process |
| **MITRE** | MITRE Corporation ATT&CK Framework |
| **NIST** | National Institute of Standards and Technology |
| **OS** | Operating System |
| **PDF** | Portable Document Format / Probability Density Function |
| **PID** | Process Identifier (Operating System Kernel) |
| **RAM** | Random Access Memory |
| **REST** | Representational State Transfer |
| **RF** | Random Forest Classifier |
| **ROC** | Receiver Operating Characteristic |
| **RPC** | Remote Procedure Call |
| **RPO** | Recovery Point Objective |
| **RTO** | Recovery Time Objective |
| **SHA** | Secure Hash Algorithm (NIST FIPS 180-4 / 202) |
| **SHAP** | SHapley Additive exPlanations |
| **SOC** | Security Operations Center |
| **SOTA** | State of the Art |
| **SQLite** | Structured Query Language Embedded Relational Database |
| **SSL/TLS** | Secure Sockets Layer / Transport Layer Security |
| **UI** | User Interface |
| **URI** | Uniform Resource Identifier |
| **URL** | Uniform Resource Locator |
| **UUID** | Universally Unique Identifier |
| **VLAN** | Virtual Local Area Network |
| **VM** | Virtual Machine |
| **XAI** | Explainable Artificial Intelligence |

---
"""

if __name__ == "__main__":
    print(f"Preliminaries length: {len(get_preliminaries().split())} words")
