# PROACTIVE RANSOMWARE DEFENCE USING ENTROPY FINGERPRINTING, CAMPAIGN ESCALATION, AND IMMUTABLE BLOCKCHAIN AUDIT TRAILS
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


<div style="page-break-after: always;"></div>

# CHAPTER 1: INTRODUCTION AND PROBLEM CONTEXT

## 1.1 The Ransomware Epidemic: Evolution, Modus Operandi, and Asymmetry

In the contemporary taxonomy of cyber warfare and enterprise security threats, cryptoviral extortion—colloquially designated as ransomware—constitutes the single most damaging asymmetric threat to modern digital infrastructure. Unlike traditional espionage malware, which prioritizes stealth, credential harvesting, and persistent exfiltration over extended dwell times, ransomware executes an active, destructive payload designed to deny availability to mission-critical data assets. The economic impact of ransomware attacks has escalated exponentially over the past decade, transitioning from opportunistic, low-yield consumer extortions into multi-million-dollar "Big Game Hunting" campaigns targeting critical healthcare networks, government municipal systems, energy utilities, and multinational corporate estates.

The foundational paradigm of ransomware hinges on mathematical asymmetry. Under modern symmetric-key cryptosystems—specifically the National Institute of Standards and Technology (NIST) Federal Information Processing Standard (FIPS) 197 Advanced Encryption Standard (AES) operating in Cipher Block Chaining (CBC) or Galois/Counter Mode (GCM), as well as ChaCha20-Poly1305—an adversary can compute an irreversible transformation over an enterprise file estate in a matter of seconds. By generating an ephemeral 256-bit symmetric session key ($K_{sym}$), encrypting user files in place, and subsequently encapsulating $K_{sym}$ under an asymmetric public key ($K_{pub}$) whose corresponding private key ($K_{priv}$) remains strictly under adversarial control on remote Command and Control (C2) servers, the attacker achieves an insurmountable computational barrier:

$$\text{Decryption Complexity} = \mathcal{O}(2^{256})$$

This brute-force search complexity exceeds the thermodynamics of the observable universe. Consequently, unless an organization possesses pristine, uncorrupted, off-site immutable backups, recovery without ransom payment is mathematically impossible. 

The historical trajectory of cryptoviral strains reveals three distinct operational generations:
1. **First-Generation Bulk Encryptors (e.g., CryptoLocker, WannaCry):** Characterized by high-velocity, multi-threaded recursive directory traversals. These strains execute rapid file overwrites using broad wildcard patterns across all logical drives, appending distinctive file extensions (such as `.WNCRY` or `.locked`) and aggressively terminating system services. While destructive, their sheer velocity and standardized IOCs make them susceptible to basic threshold detectors.
2. **Second-Generation Targeted Extortionists (e.g., Ryuk, REvil, Conti):** These campaigns operate via human-driven lateral movement following corporate domain compromise. Adversaries systematically disable endpoint protections, enumerate shadow copies via administrative utilities (`vssadmin delete shadows /all /quiet`), and execute coordinated night-time or weekend detonations across thousands of endpoints simultaneously.
3. **Third-Generation Evasive and Interleaved Strains (e.g., LockBit 3.0/Black, BlackCat/ALPHV):** The cutting edge of cryptoviral weaponry. These strains utilize intermittent or partial encryption—encrypting only every $N$-th block or merely the header and footer of a file—to evade I/O burst monitors. Furthermore, they incorporate low-velocity "slow-crawling" execution loops, thread-throttling, file renaming evasions, and in-place high-entropy camouflage to defeat signature-based and naive behavioral Endpoint Detection and Response (EDR) platforms.

The fundamental operational asymmetry lies in the **Mean-Time-to-Detect (MTTD)** versus the **Mean-Time-to-Encrypt (MTTE)**. Modern ransomware engines can encrypt a standard 100-megabyte enterprise document tree in less than 3.5 seconds. If defensive detection, human SOC escalation, and process containment require tens of minutes or hours, the defense has failed prior to intervention. True mitigation necessitates automated, sub-second autonomous endpoint reaction.

```
       ADVERSARIAL ATTACK TIMELINE (MTTE: ~3.5s - 15.0s)
[Initial Access] ──> [Privilege Escalation] ──> [Shadow Copy Deletion] ──> [Execution Burst: 18 Files Encrypted]
                                                                                      │
                                                                       Traditional AV/EDR Window
                                                                       (Alert generated after 15-45 mins)
                                                                                      │
                                                                               DATA LOSS OCCURS

       ENTROVAULT AUTONOMOUS DEFENSIVE TIMELINE (MTTD: <0.4s | MTTC: 2.7s)
[File 1 Modified] ──> [Entropy Delta & Sigma Check] ──> [File 2 Modified] ──> [Campaign Escalation Triggered]
         │                                                      │
    Strict Clean                                            Process Tree Terminated (PID 3101 Reaped)
   Backup Ingested                                          Dual-Hash Quarantine Vault Isolation
                                                            Estate Restored Byte-for-Byte (18/18)
```
*Figure 1.1: The Asymmetric Cryptoviral Attack Lifecycle and EntroVault Sub-Second Mitigation.*

---

## 1.2 Analysis of MITRE ATT&CK Technique T1486 (Data Encrypted for Impact)

To establish an enterprise-level engineering framework, this project explicitly models its threat mechanics against the MITRE ATT&CK Enterprise Matrix, focusing primarily on **Technique T1486: Data Encrypted for Impact**, along with its associated precursor and defense evasion sub-techniques:

```
+──────────────────────────────────────────────────────────────────────────────────+
|                    MITRE ATT&CK ENTERPRISE MATRIX MAPPING                        |
+──────────────────────────────────────────────────────────────────────────────────+
|  Tactic            | Technique ID | Description                                  |
+────────────────────+──────────────+──────────────────────────────────────────────+
|  Defense Evasion   | T1562.001    | Impair Defenses: Disable or Modify Tools     |
|  Defense Evasion   | T1070.004    | Indicator Removal: File Deletion             |
|  Impact            | T1490        | Inhibit System Recovery (Shadow Copy Delete) |
|  Impact            | T1486        | Data Encrypted for Impact                    |
|  Command & Control | T1071.001    | Application Layer Protocol: Web Protocols    |
+──────────────────────────────────────────────────────────────────────────────────+
```

Under Technique T1486, an adversary utilizes system cryptographic APIs (such as the Microsoft CryptoAPI/CNG on Windows, or OpenSSL/libcrypto on POSIX systems) or statically links embedded cryptographic libraries to encrypt user files. Key technical manifestations include:
- **In-Place File Overwrite:** The malware opens a file handle with write privileges (`GENERIC_WRITE`), reads the file content into memory, performs symmetric encryption, rewrites the buffer starting at offset 0, and flushes the buffer to disk.
- **Copy-Replace Mechanics:** The malware reads the target file, writes an encrypted clone with a temporary extension (`.tmp`), deletes the original unencrypted file, and renames the temporary clone to append a proprietary extension (e.g., `Financial_Report_2024.xlsx.WNCRY`).
- **Cryptographic Header Injection:** The malware prefixes the newly generated ciphertext with a structured binary header containing the encrypted session key, initialization vectors (IVs), and a magic marker (e.g., `WANACRY!`) to facilitate decryption should the victim pay the extortion fee.

In modern multi-stage campaigns, T1486 is invariably preceded by **Technique T1490 (Inhibit System Recovery)**, wherein scripts invoke:
```cmd
vssadmin.exe delete shadows /all /quiet
wbadmin.exe delete catalog -quiet
bcdedit.exe /set {default} bootstatuspolicy ignoreallfailures
bcdedit.exe /set {default} recoveryenabled no
```
By systematically stripping the operating system of local snapshot capabilities, the adversary invalidates native Volume Shadow Copy Service (VSS) restoration mechanisms. Consequently, an independent, tamper-proof, out-of-band backup architecture is a non-negotiable prerequisite for survivability.

---

## 1.3 Critical Deficiencies in State-of-the-Art Anti-Virus and EDR Solutions

Despite massive enterprise investments in endpoint security suites, cryptoviral campaigns continue to inflict catastrophic downtime. An exhaustive technical evaluation of commercial and open-source Anti-Virus (AV) and Endpoint Detection and Response (EDR) solutions reveals four critical systemic failure modes:

### 1.3.1 Inefficacy of Signature-Based Hash Matching against Polymorphism
Legacy AV platforms rely heavily on cryptographic hashes (MD5, SHA-1, SHA-256) of executable binaries compiled into static signature catalogs. Adversaries trivially neutralize this layer through **automated polymorphism and metamorphism**:
- Modifying binary junk code, reordering basic blocks, or altering compiler optimization flags changes the binary hash entirely on every single compilation.
- Utilizing legitimate native administrative tools ("Living off the Land" binaries, or LotL), such as executing PowerShell scripts or abusing legitimate debugging utilities, bypasses binary blacklists completely.
- Employing runtime crypters and memory-only staging means the malicious payload never touches disk in an unencrypted state prior to process execution.

### 1.3.2 Heuristic Brittleness and the High False-Positive Dilemma
To counter polymorphism, modern EDR solutions incorporate behavioral heuristics that monitor file creation velocity (e.g., detecting processes modifying $>20$ files per second) and API call sequences (`FindFirstFileW`, `CreateFileW`, `WriteFile`, `MoveFileExW`). However, these heuristics suffer from high false-positive rates:
- **Benign Developer and IT Workloads:** Legitimate developer routines (such as executing `git checkout` or `git pull` across large repositories), archiving large document sets via `7-Zip` or `tar`, database backup dumping (`mysqldump`), and video rendering pipelines all exhibit identical behavioral signatures: rapid file modifications, massive disk write bursts, and outputting compressed data that appears structurally random.
- **The False Quarantine Catastrophe:** If an EDR agent misidentifies an active database dump or a multi-gigabyte virtual disk image as ransomware and forcibly quarantines or terminates it, it induces the exact operational denial of service the defense was deployed to prevent. Consequently, enterprise security administrators routinely tune EDR heuristics down to prevent operational disruptions, inadvertently creating blind spots that ransomware operators exploit.

### 1.3.3 The Ciphertext Backup Contamination Vulnerability
Perhaps the most catastrophic flaw uncovered in commercial endpoint backup architectures is **the ciphertext backup ingestion flaw**:
- Backup software operating on file-system change notifications (such as Windows Change Journal or Linux `inotify`) detects that a user file has been modified.
- If the ransomware modifies a critical enterprise spreadsheet (`Financial_Report_2024.xlsx`) into high-entropy ciphertext, an unsophisticated backup manager immediately ingests the newly modified file as "Version 2 (Latest)".
- When the security team finally terminates the ransomware process hours later and initiates disaster recovery, the backup software dutifully restores the "latest" version—which is the encrypted ciphertext. If backup storage policies enforce strict snapshot limits or overwrite baselines, the uncorrupted plaintext is permanently erased.

### 1.3.4 Forensic Volatility and Log Tampering in Host Environments
During post-incident forensic investigations, incident response teams require non-repudiable logs to establish the initial infection vector, timeline of compromise, affected file estate, and precise malware attributions for cyber insurance and legal compliance. However:
- Operating system event logs (such as Windows Event Logs or Linux syslog) are stored locally in standard formats (`.evtx`, `/var/log`) and can be cleared or truncated by adversaries possessing local administrative privileges (`wevtutil cl System`).
- Attackers regularly deploy wiper routines to overwrite log directories prior to ransom note presentation, preventing forensic reconstruction and rendering root-cause analysis speculative.

---

## 1.4 Problem Statement and Formal Project Mandate

Given the systemic failure modes of perimeter defenses, signature matching, naive behavioral heuristics, and volatile local logging, there exists an urgent requirement for an autonomous, host-based proactive ransomware defense ecosystem capable of:
1. Detecting zero-day and polymorphic cryptoviral execution independent of binary hashes or static code signatures.
2. Operating with an uncompromising **Zero False Quarantine (0 FQ)** safety standard across legitimate high-entropy enterprise workloads (e.g., media compression, software development bursts, database exports).
3. Neutralizing slow-crawling, stealthy cryptoviral campaigns that intentionally throttle file modification speeds to evade conventional velocity thresholds.
4. Ensuring that active cryptoviral ciphertext can never poison disaster recovery baselines, while guaranteeing automated byte-for-byte rollback to pre-attack states without human operator intervention.
5. Establishing an immutable, decentralized, non-repudiable audit trail of all detected events, cryptographic hashes, and process attributions that resists local administrative tampering.

---

## 1.5 Project Aim and Core Technical Objectives (200-Mark Specification)

The overarching aim of this project is to architect, engineer, empirically validate, and defend **EntroVault (ENTROPY)**—an industry-grade, purple-team-validated cyber-physical defense platform engineered to satisfy the rigorous criteria of a final-year major engineering project (200-mark evaluation). 

The formal engineering specifications dictate three mandatory operational mandates:

### Mandate 1: Real-Time SOC Operational Visibility via Sub-Second Push
The defense platform must provide a dedicated Security Operations Center (SOC) dashboard operating independently of the victim endpoint. The SOC interface must ingest file system modifications recursively in real time, calculate information-theoretic entropy metrics on the fly, extract process attribution data, and push updates to security analysts via WebSocket streaming with a latency profile under 500 milliseconds.

### Mandate 2: Neutralized Victim Workstation Experience
In a genuine enterprise incident, a victim workstation must not display internal threat intelligence, cryptoviral family attributions, or panic-inducing security telemetry that could compromise forensic preservation or cause user panic. The victim file explorer interface must present a clean, neutral operating system file directory view (displaying standard names, sizes, icons, and timestamps). Quarantined ciphertext artifacts and detailed incident reports must remain isolated behind an authenticated, PIN-protected administrative vault inaccessible to standard users.

### Mandate 3: Autonomous Background Intervention, Containment, and Restoration
Upon detecting cryptoviral activity, the defensive pipeline must autonomously intervene in the background without requiring analyst confirmation. The system must:
- Terminate the malicious execution tree safely, verifying process identifiers (PIDs) while avoiding defender self-termination or system deadlock.
- Isolate compromised files into a dedicated quarantine store physically provisioned at installation time.
- Restore the entire compromised estate byte-for-byte from verified clean baseline snapshots, leaving zero encrypted artifacts on disk.
- Guarantee containment within a maximum threshold of **file 2 of the attack execution**, achieving an empirical recovery rate of 100% on active estates.

---

## 1.6 Scope and Operational Boundaries of Research

To ensure scientific honesty and rigorous academic integrity, the scope and operational boundaries of this dissertation are explicitly defined:
- **Purple-Team Laboratory Focus:** The system is engineered as an end-to-end, multi-tier cyber-physical laboratory consisting of three coordinated micro-services: a SOC Telemetry Dashboard (Port 5000), a Neutral Victim Workstation (Port 5001), and a Multi-Strain Attacker Command-and-Control Detonation Console (Port 8001).
- **Userspace File System Monitoring:** The primary monitoring implementation utilizes the cross-platform Python `watchdog` framework, polling the protected estate at 200-millisecond intervals. While enterprise commercial products deploy kernel-mode minifilter drivers (`FltRegisterFilter`) or Extended Berkeley Packet Filters (eBPF), this userspace architecture demonstrates canonical algorithmic validity while maintaining portability across Windows, Linux, and macOS host platforms.
- **Honest Decryption Impossibility:** The platform explicitly does **not** claim the capability to decrypt ransomware ciphertext files. As mathematically demonstrated in Section 1.1, real-world ransomware ciphertext generated via modern symmetric-asymmetric envelope cryptography cannot be decrypted without the adversary's private key. EntroVault's recovery mechanism relies strictly on out-of-band, pre-attack clean snapshot restoration.
- **The In-Place High-Entropy Blindspot:** As formally documented and evaluated in Chapter 9 and Chapter 10, any pure entropy-based detector faces an information-theoretic limitation when confronted with in-place encryption of previously compressed or encrypted file formats (such as JPEG, PNG, MP4, or ZIP archives) where no file renaming occurs. EntroVault openly documents this physical boundary, maintaining a 0-FQ bar rather than fabricating false-positive-laden claims.

---

## 1.7 Summary of Key Novel Engineering Contributions

The original research and engineering contributions delivered in this dissertation encompass:
1. **Multi-Stage Information-Theoretic Threat Calculus:** Development of an optimized Shannon entropy calculator combining whole-file entropy, sliding-window block entropy, empirical per-file-type baseline boundaries, and a calibrated differential jump metric ($\Delta H \ge 2.0$).
2. **Temporal Campaign Escalation Tracker (`CampaignTracker`):** An algorithmic state machine that correlates multi-file modifications over a sliding 15-second window. By recognizing that ransomware is intrinsically a multi-file campaign, the tracker escalates isolated alerts into immediate termination directives upon identifying 2 qualifying files, successfully neutralizing stealthy slow-crawler attacks operating at 1.6 ops/sec.
3. **Strict Clean Backup Admission Control:** Formulation and implementation of a strict snapshot filtering algorithm that prevents ciphertext from ever contaminating disaster recovery stores by validating post-modification files against strict type boundaries and delta jumps prior to ingestion.
4. **Resilient Dual-Hash Quarantine and Forensic Packaging:** An isolated quarantine subsystem utilizing dual-layer cryptographic fingerprinting (SHA3-256 primary + SHA-256 secondary) along with automated JSON forensic metadata serialization compliant with digital evidence chain-of-custody standards.
5. **Decentralized Dual-Mode Blockchain Audit Trail:** Design and deployment of an Ethereum Virtual Machine smart contract (`ThreatLogger.sol`) compiled for Ganache testnets, integrated with an autonomous, crash-resilient SQLite fallback ledger ensuring unbroken forensic logging even during network partitions or offline operations.
6. **Exhaustive Empirical Benchmarking and Recovery Drills:** Construction of a fully deterministic, reproducible benchmark battery testing 8 distinct attack archetypes against 7 legitimate enterprise workloads, accompanied by a full byte-for-byte recovery drill verifying post-incident file integrity down to individual cryptographic checksums.

---

## 1.8 Dissertation Structural Roadmap

The remainder of this dissertation is organized as follows:
- **Chapter 2 (Literature Survey and Related Work):** Examines historical and contemporary research in entropy-based malware detection, file system interception hooks, machine learning classifiers, and blockchain forensic logging, providing a comprehensive comparative feature matrix.
- **Chapter 3 (Mathematical and Theoretical Foundations):** Establishes the formal mathematical foundations of Shannon entropy, sliding-window sampling, Chi-Square goodness-of-fit testing, Markov chain modeling, and reinforcement learning Bellman equations.
- **Chapter 4 (System Architecture and Detailed Specification):** Details the global high-level architecture, 3-tier purple-team laboratory topology, runtime data flows, and security boundary constraints.
- **Chapter 5 (Core Engineering and Implementation Mechanics):** Dissects the low-level code mechanics of the watchdog file observer, event deduplication engine, DefenseGuard tamper-resistance subsystem, and dual-layer hashing primitives.
- **Chapter 6 (Multi-Tier Decision Engines and AI Classifiers):** Provides an in-depth analysis of the Deterministic Rule Engine, the Campaign Escalation Tracker, the Random Forest model with SHAP explanations, the Deep Q-Network agent, and the Byzantine-resistant federated exchange.
- **Chapter 7 (Automated Response, Strict Backup, and Byte-Level Recovery):** Explains process termination mechanics, zombie process reaping, install-time quarantine vaulting, strict clean backup algorithms, and post-kill estate restoration.
- **Chapter 8 (Blockchain Ledger, Smart Contracts, and Forensic Immutability):** Evaluates the Solidity `ThreatLogger` smart contract, EVM gas dynamics, Ganache deployment, and the resilient LocalLedger fallback architecture.
- **Chapter 9 (Comprehensive Empirical Evaluation, Benchmarks, and Recovery Drills):** Presents empirical data, confusion matrices, RTO/RPO calculations, and comparative evaluations across 48 attack runs and 21 workload stress tests.
- **Chapter 10 (Attack Surface Modeling, Limitations, and Blindspot Mitigation):** Delivers a formal STRIDE security model, a mathematical dissection of the image blindspot phenomenon, and evasion mitigation analyses.
- **Chapter 11 (Real-Time SOC Interface, Neutral Victim Explorer, and Attacker Simulation):** Documents the WebSocket streaming architecture, neutral victim explorer psychology, and multi-strain attacker simulation console.
- **Chapter 12 (Conclusions, Lessons Learned, and Future Research Directions):** Summarizes technical achievements, engineering trade-offs, and outlines future kernel-mode driver implementations.
- **References & Appendices:** Contains complete bibliographic citations, full smart contract source code, formal pseudocode algorithms, benchmark schemas, and a 200-mark examiner defense guide.

---


<div style="page-break-after: always;"></div>

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

Following this foundation, early host-based ransomware detection frameworks attempted to apply global file entropy thresholds to identify malicious writes. When a user document transitioned from a low-entropy state (e.g., ASCII text at $H approx. .  4.2$) to high entropy ($H \ge 7.8$), the file was flagged as encrypted. However, early implementations (such as those surveyed by Kharraz et al. in the UNVEIL study, 2016) demonstrated unacceptable false-positive rates when confronted with benign user actions involving compression algorithms (e.g., generating `.zip`, `.tar.gz`, or `.docx` archives).

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

$$\phi_i(x) = \sum_{S \subseteq F \setminus \{i\}} rac{|S|!(|F| - |S| - 1)!}{|F|!} \left[ f_x(S \cup \{i\}) - f_x(S) 
ight]$$

By decomposing a predicted cryptoviral threat score into discrete, signed feature contributions (e.g., $+0.42$ due to `entropy_delta \ge 2.0`, $+0.28$ due to `files_per_sec \ge 12`, $-0.35$ due to `in_normal_range`), SHAP provides the human SOC operator with immediate, actionable attribution telemetry.

### 2.3.3 Markov Decision Processes and Deep Q-Networks for Automated Mitigation
In dynamic attack scenarios where ransomware variants adapt their encryption velocity or payload chunking, static classification models fail to optimize multi-step responses. To address this, researchers have modeled cryptoviral defense as a **Markov Decision Process (MDP)** governed by Reinforcement Learning (RL):
- In an MDP formulation $(S, A, P, R, \gamma)$, the state space $S$ represents system telemetry (current entropy, historical entropy delta, event velocity, process age, signature validation), the action space $A$ defines mitigation postures (Ignore, Alert, Terminate Process, Terminate and Quarantine), and the reward function $R$ penalizes both undetected damage and false-positive interventions.
- Mnih et al. (2015) introduced **Deep Q-Networks (DQN)**, combining Q-learning with deep convolutional/dense neural networks to approximate the optimal action-value function:
  $$Q^*(s, a) = \mathbb{E} \left[ r + \gamma \max_{a'} Q^*(s', a') \;\middle|\; s, a 
ight]$$
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


<div style="page-break-after: always;"></div>

# CHAPTER 3: MATHEMATICAL AND THEORETICAL FOUNDATIONS

The detection, classification, and mitigation mechanisms embodied within EntroVault are grounded in rigorous mathematical formulations spanning information theory, discrete statistics, Markovian state analysis, reinforcement learning dynamics, and cryptographic complexity theory. This chapter details the formal mathematical framework underpinning the architecture.

---

## 3.1 Information-Theoretic Foundations of Shannon Entropy

### 3.1.1 Discrete Memoryless Source Modeling
In information theory, a digital file or binary data stream can be formally modeled as the output of a **Discrete Memoryless Source (DMS)**, denoted as $\mathcal{S}$. The source emits discrete symbols from a finite alphabet $\Sigma$ consisting of all possible 8-bit byte values:

$$\Sigma = \{ x_0, x_1, x_2, \dots, x_{255} \} = \{ 0\text{x}00, 0\text{x}01, \dots, 0\text{xFF} \}, \quad |\Sigma| = 256$$

Let $X$ be a discrete random variable representing the observation of a symbol emitted by source $\mathcal{S}$, characterized by an empirical probability mass function (PMF) $p(x_i) = P(X = x_i)$, satisfying the fundamental Kolmogorov probability axioms:

$$\sum_{i=0}^{255} p(x_i) = 1, \quad \text{where } 0 \le p(x_i) \le 1 \quad \forall i \in \{0, 1, \dots, 255\}$$

### 3.1.2 Shannon's Entropy Formula and Byte Frequency Distributions
Following the seminal theorem established by Claude E. Shannon (1948), the average uncertainty or information content per symbol emitted by source $\mathcal{S}$—termed the **Shannon Information Entropy** $H(X)$—is quantified in bits per byte as:

$$H(X) = - \sum_{i=0}^{255} p(x_i) \log_2 p(x_i)$$

Where, by analytical convention in information theory:
$$\lim_{p(x_i) \to 0^+} p(x_i) \log_2 p(x_i) = 0$$

For a concrete file buffer $D$ composed of $N$ contiguous bytes, where $C(x_i)$ represents the empirical occurrence count of byte value $x_i$ within $D$, the empirical probability is estimated via maximum likelihood estimation (MLE):

$$\hat{p}(x_i) = \frac{C(x_i)}{N} = \frac{1}{N} \sum_{j=1}^N \mathbb{I}(D[j] = x_i)$$

where $\mathbb{I}(\cdot)$ denotes the indicator function. The operational Shannon entropy is therefore computed as:

$$\hat{H}(D) = - \sum_{i=0}^{255} \left( \frac{C(x_i)}{N} \right) \log_2 \left( \frac{C(x_i)}{N} \right) = \log_2(N) - \frac{1}{N} \sum_{i=0}^{255} C(x_i) \log_2 C(x_i)$$

This vectorized formulation permits high-speed linear computation: $\mathcal{O}(N)$ to construct the 256-element frequency histogram, followed by $\mathcal{O}(1)$ to evaluate the 256-element summation.

```
   H(X) [bits/byte]
    8.0 ┼─────────────────────────────────────────────● Perfect AES/ChaCha Ciphertext (7.99 - 8.00)
        │                                             │
    7.5 ┼───────────────────────────────● Compressed Media (JPEG, MP4, ZIP: 7.00 - 7.80)
        │                               │
    6.5 ┼────────────────● Compiled Binaries & Formatted Docs (PDF, DOCX: 6.00 - 7.50)
        │                │
    4.5 ┼──● Plaintext English Text & Source Code (ASCII, UTF-8: 3.50 - 5.00)
        │  │
    0.0 ┴──┴────────────────────────────────────────── Byte Uniformity / Predictability
```
*Figure 3.1: Information Entropy Spectrum across Computing Asset Classes.*

### 3.1.3 Maximum Entropy Theorem for Uniform Distributions
The theoretical upper bound of the entropy metric governs its utility in cryptoviral detection. Applying Jensen's inequality to the strictly concave function $f(t) = \log_2(t)$:

$$H(X) = \mathbb{E} \left[ \log_2 \frac{1}{p(X)} \right] \le \log_2 \left( \mathbb{E} \left[ \frac{1}{p(X)} \right] \right) = \log_2 \left( \sum_{i=0}^{255} p(x_i) \frac{1}{p(x_i)} \right) = \log_2(256) = 8.0 \text{ bits/byte}$$

Equality $H(X) = H_{max} = 8.0$ holds if and only if the byte distribution is strictly uniform:
$$p(x_i) = \frac{1}{256} = 0.00390625 \quad \forall i \in \{0, 1, \dots, 255\}$$

Conversely, the theoretical lower bound occurs when the source emits a constant deterministic byte sequence (e.g., a file filled entirely with null bytes `0x00`):
$$p(x_k) = 1, \quad p(x_i) = 0 \quad \forall i \ne k \implies H(X) = H_{min} = 0.0 \text{ bits/byte}$$

Under Kerckhoffs's principle and modern cryptographic design, robust symmetric ciphers (e.g., AES-256-CBC, ChaCha20) produce pseudo-random bitstreams indistinguishable from independent and identically distributed (i.i.d.) uniform noise. Consequently, cryptoviral encryption inexorably drives a file's empirical byte distribution toward uniform equiprobability, yielding $\hat{H}(D) approx. .  7.95 - 8.00$.

---

## 3.2 Sliding Window and Multi-Segment Entropy Dynamics

### 3.2.1 Partial-Encryption Detection via Tri-Segment Sampling
Modern evasive ransomware strains (such as LockBit 3.0 and BlackCat) frequently implement intermittent or partial encryption. Rather than encrypting the entire file, the malware encrypts only the initial 10% (containing file headers and magic numbers) or alternating 4KB blocks, leaving the remainder untouched. A whole-file entropy calculation on a 50MB file undergoing partial header encryption will dilute the high-entropy block across the massive low-entropy body, resulting in a false-negative classification.

To resolve this evasion vector, EntroVault introduces a **Tri-Segment Partitioning Function**. Given an ingested sample buffer $D$ of size $N$ bytes (where $N = \min(\text{file\_size}, 65536)$), the buffer is partitioned into three non-overlapping contiguous slices:

$$D_{start} = D\left[0 : \left\lfloor \frac{N}{3} \right\rfloor\right], \quad D_{middle} = D\left[\left\lfloor \frac{N}{3} \right\rfloor : \left\lfloor \frac{2N}{3} \right\rfloor\right], \quad D_{end} = D\left[\left\lfloor \frac{2N}{3} \right\rfloor : N\right]$$

The system calculates individual sub-entropies:
$$H_{start} = \hat{H}(D_{start}), \quad H_{middle} = \hat{H}(D_{middle}), \quad H_{end} = \hat{H}(D_{end})$$

The partial-encryption anomaly metric $\Delta H_{seg}$ is defined as:
$$\Delta H_{seg} = \max(H_{start}, H_{middle}, H_{end}) - \min(H_{start}, H_{middle}, H_{end})$$

If $\Delta H_{seg} \ge 2.5$ and $\max(H_{start}, H_{middle}, H_{end}) \ge 7.8$, the file displays localized cryptographic distortion indicative of header-targeted or partial cryptoviral corruption.

```
  +─────────────────────── Buffer Sample: 65,536 Bytes ───────────────────────+
  │                                                                           │
  │   [ Segment 1: Head ]        [ Segment 2: Body ]       [ Segment 3: Tail ]│
  │   H_start = 7.98 bits        H_middle = 4.21 bits      H_end = 4.19 bits  │
  │   (Encrypted Header)         (Plaintext Payload)       (Plaintext Payload)│
  +───────────────────────────────────────────────────────────────────────────+
       Delta H_seg = 7.98 - 4.19 = 3.79 bits/byte  ===> FLAG: PARTIAL ENCRYPTION
```
*Figure 3.2: Tri-Segment Sliding Entropy Analysis Uncovering Header-Only Cryptoviral Corruption.*

---

## 3.3 Statistical Hypothesis Testing and Chi-Square Goodness-of-Fit

### 3.3.1 Chi-Square ($\chi^2$) Distribution of Native vs. Ciphertext Payloads
To complement Shannon entropy, EntroVault establishes a statistical test of hypothesis to determine whether an observed byte sequence deviates significantly from a theoretical uniform distribution. We formulate the null and alternative hypotheses:
- $\mathcal{H}_0$: The byte sequence is drawn from a discrete uniform distribution $\mathcal{U}(0, 255)$ (Indicative of Strong Cryptographic Ciphertext).
- $\mathcal{H}_1$: The byte sequence deviates significantly from uniformity (Indicative of Native Structured Data).

The Pearson Chi-Square Goodness-of-Fit test statistic is defined as:

$$\chi^2 = \sum_{i=0}^{255} \frac{\left( O_i - E_i \right)^2}{E_i}$$

where:
- $O_i = C(x_i)$ is the observed frequency count of byte $x_i$ in sample $D$.
- $E_i = \frac{N}{256}$ is the theoretically expected count under the uniform null hypothesis $\mathcal{H}_0$.

Under $\mathcal{H}_0$, the test statistic asymptotically follows a central Chi-Square distribution with $k - 1 = 256 - 1 = 255$ degrees of freedom ($df = 255$). The critical values at standard significance levels are:
- $\chi^2_{0.05, 255} approx. .  293.25$
- $\chi^2_{0.01, 255} approx. .  310.46$
- $\chi^2_{0.001, 255} approx. .  330.52$

For structured text, executable binaries, and formatted office documents, $O_i$ deviates massively from $E_i$ (e.g., spaces `0x20` and common ASCII characters exhibit enormous positive deviations, while non-printable control characters remain near zero), driving $\chi^2 > 10,000$. Conversely, true cryptographic ciphertext yields $\chi^2 \le 310.46$, confirming failure to reject the uniform null hypothesis $\mathcal{H}_0$.

### 3.3.2 Monte Carlo Approximations for Large-File Sub-Sampling
Evaluating every byte of multi-gigabyte virtual hard disks (`.vmdk`) or database stores (`.mdf`) introduces prohibitive CPU cache invalidation and disk I/O bottlenecks. EntroVault employs a bounded sub-sampling strategy. By default, the sampling size is configured to $N_{sample} = 65,536$ bytes ($64$ KB).

By Hoeffding's inequality for bounded random variables, the probability that the empirical sample mean byte probability $\hat{p}(x_i)$ deviates from the true population probability $p(x_i)$ by more than an error bound $\epsilon$ satisfies:

$$P\left( |\hat{p}(x_i) - p(x_i)| \ge \epsilon \right) \le 2 \exp\left( -2 N_{sample} \epsilon^2 \right)$$

For $N_{sample} = 65,536$ and $\epsilon = 0.005$:
$$2 \exp\left( -2 \times 65536 \times (0.005)^2 \right) = 2 \exp(-3.2768) approx. .  0.0754$$

This ensures that a 64KB sample provides an accurate, statistically robust approximation of whole-file entropy with minimal computation time ($< 1.2$ milliseconds per evaluation).

---

## 3.4 Per-File-Type Empirical Probability Density Functions (PDFs)

### 3.4.1 Empirical Distribution Bands across Formats
A major flaw in naive entropy detectors is enforcing a single global threshold (e.g., $H \ge 7.0$). In modern operating systems, diverse file formats possess drastically different native entropy ranges due to internal Huffman coding, Lempel-Ziv-Welch (LZW) compression, and binary serialization.

To eliminate false-positive alerts, EntroVault maps each file extension $ext$ to an empirically calibrated interval:

$$\Omega(ext) = [H_{min}(ext), H_{max}(ext)]$$

Table 3.1 details the formal empirical boundaries established within `config.NORMAL_ENTROPY_RANGES`:

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|           TABLE 3.1: EMPIRICAL SHANNON ENTROPY DISTRIBUTION BANDS                        |
+───────────────────┬─────────────────────┬─────────────────────┬──────────────────────────+
| File Extension    | Lower Bound H_min   | Upper Bound H_max   | Structural Description   |
+───────────────────┼─────────────────────┼─────────────────────┼──────────────────────────+
| .txt              | 3.00 bits/byte      | 5.50 bits/byte      | Uncompressed ASCII / UTF8|
| .doc, .docx       | 6.00 bits/byte      | 7.50 bits/byte      | Compressed XML Container |
| .xlsx             | 6.00 bits/byte      | 7.50 bits/byte      | OpenXML ZIP Archive      |
| .pdf              | 6.50 bits/byte      | 7.80 bits/byte      | FlateDecode Streams      |
| .jpg, .jpeg       | 7.00 bits/byte      | 7.80 bits/byte      | DCT & Huffman Compressed |
| .png              | 6.50 bits/byte      | 7.50 bits/byte      | Deflate Bitmaps          |
| .mp4              | 7.00 bits/byte      | 7.90 bits/byte      | H.264 / AAC Codec Streams|
| .zip              | 7.50 bits/byte      | 8.00 bits/byte      | DEFLATE Compressed Store |
| .exe              | 5.00 bits/byte      | 7.20 bits/byte      | PE x86/x64 Binary Blocks |
| .py, .csv, .dat   | 4.00 bits/byte      | 6.50 bits/byte      | Structured Code & Tables |
+───────────────────┴─────────────────────┴─────────────────────┴──────────────────────────+
```

### 3.4.2 The Differential Entropy Threshold ($\Delta H$) Formulation
Rather than evaluating absolute entropy in isolation, EntroVault tracks the historical trajectory of each file across successive modifications. Let $H_t(f)$ denote the current measured entropy of file $f$ at timestamp $t$, and let $H_{t-1}(f)$ represent the immediately preceding clean entropy stored in the historical register.

The **Differential Entropy Delta** $\Delta H(f)$ is formally defined as:

$$\Delta H(f) = H_t(f) - H_{t-1}(f)$$

A legitimate document modification (e.g., adding several paragraphs to a corporate memo or updating financial entries in a spreadsheet) induces small continuous shifts:
$$|\Delta H_{benign}| \le 0.45 \text{ bits/byte}$$

In contrast, cryptoviral overwrite produces an abrupt, non-linear phase shift:
$$\Delta H_{ransomware} \ge 2.00 \text{ bits/byte}$$

EntroVault establishes the fundamental **Corroboration Invariant**:
An event is classified as potentially cryptoviral if and only if:
$$\left( H_t(f) \ge H_{thresh} \right) \land \left( \left( |\Delta H(f)| \ge \Delta H_{thresh} \right) \lor \text{ExtensionChanged}(f) \lor \text{VelocityExceeded} \right)$$

where $H_{thresh} = 6.8$ and $\Delta H_{thresh} = 2.0$. This invariant mathematically guarantees that a file that was *already* high-entropy prior to the event (such as a photo import or video transcode) generates $\Delta H approx. .  0.0$, preventing false quarantine.

---

## 3.5 Markov Chain Modeling of File System Transformation Sequences

The sequence of operational transformations occurring within a monitored file estate can be modeled as a discrete-time stochastic process possessing the Markov property. Let $S_t \in \mathcal{S}_{state}$ represent the system defensive state at time step $t$:

$$\mathcal{S}_{state} = \{ S_0: \text{Normal}, S_1: \text{Alert}, S_2: \text{Campaign Confirmed}, S_3: \text{Containment}, S_4: \text{Restored} \}$$

The state transition probability matrix $\mathbf{P}$ is governed by conditional observation vectors:

$$\mathbf{P} = \begin{bmatrix}
P(S_0 | S_0) & P(S_1 | S_0) & 0 & 0 & 0 \\
P(S_0 | S_1) & P(S_1 | S_1) & P(S_2 | S_1) & 0 & 0 \\
0 & 0 & 0 & P(S_3 | S_2) & 0 \\
0 & 0 & 0 & 0 & P(S_4 | S_3) \\
P(S_0 | S_4) & 0 & 0 & 0 & 0
\end{bmatrix}$$

Under benign background operations, transition $P(S_0 | S_0) approx. .  0.999$. An isolated high-entropy write moves the system to $S_1$ (Alert). If no subsequent qualifying events occur within the campaign window $\tau = 15$ seconds, the temporal decay function transitions the system back:
$$P(S_0 | S_1, \Delta t > \tau) = 1.0$$

However, if a second qualifying event occurs within $\tau$, the campaign escalation automaton executes:
$$P(S_2 | S_1, \Delta t \le \tau) = 1.0$$

State $S_2$ represents an absorbing intermediate state that deterministically transitions to $S_3$ (Process Termination and File Quarantine) and $S_4$ (Byte-for-Byte Restoration), before resetting to $S_0$.

---

## 3.6 Reinforcement Learning Formulation: MDP, Bellman Optimality, and Q-Convergence

For environments opting into adaptive reinforcement learning, the defensive agent is formalized as an optimal control policy within a **Markov Decision Process (MDP)** defined by the 5-tuple $(\mathcal{S}, \mathcal{A}, \mathcal{P}, \mathcal{R}, \gamma)$:
- **State Space $\mathcal{S} \subset \mathbb{R}^{10}$:** An 10-dimensional continuous normalized feature vector representing the file operation and process context (entropy score, entropy delta, event velocity, extension mutation flag, process age, digital signature status, affected file count, historical mean entropy, known process status, and time of day).
- **Action Space $\mathcal{A} = \{0, 1, 2, 3\}$:**
  - $a_0$: `ACTION_IGNORE` (Permit file write)
  - $a_1$: `ACTION_ALERT` (Log alert to SOC telemetry)
  - $a_2$: `ACTION_TERMINATE` (Forcibly terminate offending PID)
  - $a_3$: `ACTION_TERMINATE_QUARANTINE` (Kill PID, isolate ciphertext, initiate rollback)
- **Reward Function $\mathcal{R}(s, a, s')$:** The reward structure is heavily asymmetric to penalize false quarantines and catastrophic breaches:
  $$\mathcal{R}(s, a) = \begin{cases}
  +5.0 & \text{if } a = a_0 \text{ and event is Benign} \\
  +50.0 & \text{if } a = a_3 \text{ and event is True Cryptoviral Attack} \\
  -100.0 & \text{if } a = a_3 \text{ and event is Benign (False Quarantine Penalty)} \\
  -250.0 & \text{if } a = a_0 \text{ and event is Ransomware (Breach Penalty)} \\
  -2.0 & \text{if } a = a_1 \text{ and event is Benign (Noise Penalty)}
  \end{cases}$$
- **Discount Factor $\gamma = 0.95$:** Models the temporal weighting of future estate preservation.

The optimal action-value function $Q^*(s, a)$ satisfies the fundamental **Bellman Optimality Equation**:

$$Q^*(s, a) = \mathcal{R}(s, a) + \gamma \sum_{s' \in \mathcal{S}} \mathcal{P}_{ss'}^a \max_{a' \in \mathcal{A}} Q^*(s', a')$$

The parameterized Deep Q-Network $Q(s, a; \theta)$ is trained by minimizing the Mean Squared Bellman Error (MSBE) loss function over mini-batches sampled from an experience replay buffer $\mathcal{D}$:

$$L_i(\theta_i) = \mathbb{E}_{(s, a, r, s') \sim \mathcal{D}} \left[ \left( r + \gamma \max_{a'} Q(s', a'; \theta_i^-) - Q(s, a; \theta_i) \right)^2 \right]$$

where $\theta_i^-$ denotes the parameter vector of the target network, updated periodically every $C = 10$ steps to ensure mathematical convergence and prevent divergence oscillations.

---

## 3.7 Dual Cryptographic Hashing and Collision Resistance Bounds (SHA3-256 and SHA-256)

To guarantee the non-repudiation of forensic evidence and ensure that backup verification cannot be defeated by adversarial hash collisions, EntroVault enforces a **Dual-Layer Cryptographic Fingerprinting Architecture** combining:
1. **SHA-256 (NIST FIPS 180-4):** Merkle-Damgård construction with a 512-bit block size and 256-bit internal state.
2. **SHA3-256 (NIST FIPS 202):** Keccak permutation-based sponge construction with a capacity $c = 512$ bits and rate $r = 1088$ bits.

Let $H_{SHA2}(M)$ and $H_{SHA3}(M)$ denote the respective hash digests of message $M$. The composite fingerprint is defined as the concatenation:

$$\Phi(M) = H_{SHA3}(M) \;\Vert\; H_{SHA2}(M) \in \{0, 1\}^{512}$$

### Collision Resistance Bound
Under the generalized Birthday Paradox, the number of chosen messages $k$ required to locate a collision with probability $P_{coll} \ge 0.5$ in an $n$-bit cryptographic hash function is bounded by:

$$k approx. .  1.1774 \sqrt{2^n} = 1.1774 \times 2^{n/2}$$

For a single 256-bit hash:
$$k_{256} approx. .  1.1774 \times 2^{128} approx. .  4.005 \times 10^{38} \text{ operations}$$

By pairing two cryptographically orthogonal constructions (Merkle-Damgård compression vs. Keccak sponge permutation), an adversary seeking a simultaneous preimage or second-preimage collision must break both mathematical structures simultaneously. Even if an unforeseen algorithmic vulnerability were discovered in SHA-256's Davies-Meyer compression function, the Keccak-f[1600] permutation remains completely impervious. This guarantees mathematical immutability for all forensic artifacts committed to the blockchain and backup stores.

---

## 3.8 Chapter Summary

This chapter established the rigorous theoretical and mathematical foundations of EntroVault:
1. Shannon information entropy provides the core information-theoretic discriminator, mapping byte distributions to an interval $[0.0, 8.0]$.
2. Tri-segment partitioning and Pearson Chi-Square goodness-of-fit testing enable the detection of localized and partial encryption patterns.
3. Per-type empirical bands and differential delta metrics ($\Delta H \ge 2.0$) eliminate false alarms on natively compressed media.
4. Markov chain state modeling establishes the deterministic progression of defensive alerts into containment states.
5. Bellman optimality equations govern reinforcement learning policies, ensuring penalty-biased containment.
6. Dual cryptographic hashing (SHA3-256 + SHA-256) guarantees an insurmountable collision boundary ($2^{256} 	imes 2^{256} = 2^{512}$) for all persistent forensic ledgers.

These theoretical formulations directly drive the architectural blueprints and low-level code mechanics presented in Chapter 4 and Chapter 5.

---


<div style="page-break-after: always;"></div>

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


<div style="page-break-after: always;"></div>

# CHAPTER 5: CORE ENGINEERING AND IMPLEMENTATION MECHANICS

This chapter delivers a comprehensive code-level inspection of the core engineering mechanics powering EntroVault's monitoring, event ingestion, anti-tampering, entropy analysis, and storage subsystems. Specific attention is devoted to concurrency controls, race condition mitigations, and performance optimizations.

---

## 5.1 Real-Time File System Observer Subsystem (`monitoring.watchdog_monitor`)

### 5.1.1 Recursive Directory Traversal and Observer Thread Management
File system observation is orchestrated by `monitoring.watchdog_monitor.FileMonitor`. Rather than running synchronous blocking checks, the module deploys an asynchronous daemon thread wrapping the `watchdog.observers.Observer` engine. 

The observer registers recursive file system hooks across all configured watch directories (`config.WATCH_FOLDERS`), which by default includes the victim user files estate (`victim_server/user_files/`) and testing fixtures (`data/testing/`):

```python
class FileMonitor:
    def __init__(self, watch_folders=None, callback=None):
        self.watch_folders = watch_folders or config.WATCH_FOLDERS
        self.callback = callback
        self.observer = Observer()
        self.handler = FileChangeEventHandler(self._on_event)
        self.deduplicator = EventDeduplicator(
            window_seconds=config.EVENT_DEDUP_WINDOW_SECONDS
        )

    def start(self):
        for folder in self.watch_folders:
            if os.path.exists(folder):
                self.observer.schedule(self.handler, folder, recursive=True)
                log.info(f"[MONITOR] Watching recursively: {folder}")
        self.observer.start()
```

The underlying observer polls directory handles at a tuned 200-millisecond cycle (`0.2s`). This frequency guarantees that file modifications are captured prior to subsequent malware operations while maintaining negligible CPU utilization ($< 1.5\%$ on multi-core hosts).

### 5.1.2 Temporal Event Deduplication Engine (`monitoring.event_deduplicator`)
A notorious operational challenge in operating-system-level file monitoring is **event storming**. When a process modifies a 100KB file in chunks, the OS triggers separate notifications for handle opening, write buffering, size truncation, and handle closing. In rapid succession, a single file write can produce $15 - 50$ discrete `FileModifiedEvent` notifications within 50 milliseconds. Processing each event through the cryptographic entropy calculator would saturate CPU queues and cause severe pipeline lag.

To resolve this, EntroVault implements an in-memory temporal sliding-window deduplicator:

```python
class EventDeduplicator:
    def __init__(self, window_seconds: float = 1.0):
        self.window = window_seconds
        self.last_seen = {}  # (file_path, event_type) -> timestamp
        self._lock = threading.Lock()

    def should_process(self, file_path: str, event_type: str) -> bool:
        now = time.time()
        key = (os.path.normpath(file_path), event_type)
        with self._lock:
            last = self.last_seen.get(key, 0.0)
            if now - last < self.window:
                return False  # Suppress duplicate event
            self.last_seen[key] = now
            # Evict stale entries older than 2x window
            if len(self.last_seen) > 2000:
                self.last_seen = {
                    k: t for k, t in self.last_seen.items() 
                    if now - t <= (self.window * 2)
                }
            return True
```

By enforcing `config.EVENT_DEDUP_WINDOW_SECONDS = 1.0`, redundant intermediate write notifications are suppressed. Only the initial write and subsequent distinct operations pass into the ingestion pipeline, reducing queue congestion by over $85\%$ during mass write bursts.

---

## 5.2 High-Throughput Ingestion Queue and Batching Pipeline (`monitoring.event_pipeline`)

The transition between raw OS file system notifications and defensive threat analysis is decoupled using a thread-safe, bounded, multi-producer single-consumer FIFO queue (`monitoring.event_pipeline.EventPipeline`):
- **Bounded Queue Size (`EVENT_QUEUE_SIZE = 10000`):** Prevents memory exhaustion attacks where an adversary attempts to exhaust host RAM by generating millions of micro-file events.
- **Batch Processing (`EVENT_BATCH_SIZE = 50`):** Events are drained from the queue in discrete batches, enabling bulk relational database transactions and amortizing thread context-switching overhead.
- **Velocity Estimation:** The pipeline calculates real-time event rates using a rolling 10-second deque of timestamps:
  $$\text{Rate}(t) = \frac{\sum_{i=1}^M \mathbb{I}(t - t_i \le 10.0)}{10.0} \quad [\text{events/sec}]$$
  If $\text{Rate}(t) \ge 3.0$ events/second, the event is flagged with `is_suspicious_speed = True`.

---

## 5.3 Defense Guard: Anti-Tamper and Signature Trapping (`monitoring.defense_guard`)

Prior to passing an event to mathematical entropy scoring, `monitoring.defense_guard.collect_threat_flags()` interrogates the event for hard, non-statistical indicators of adversarial behavior:

### 5.3.1 Ransom Note Trapping via Filename Heuristics and Phrase Catalogs
Adversaries operating cryptoviral payloads inevitably drop ransom instructions to facilitate extortion payments. The defense guard matches created filenames against regular expression patterns:
- Filenames containing `readme`, `how_to_decrypt`, `how_to_recover`, `restore_files`, `help_decrypt`, or `decrypt_notes` paired with `.txt`, `.html`, or `.hta` extensions.
- Regex pattern: `r"(!?[a-zA-Z0-9_-]*(?:readme|decrypt|restore|recover)[a-zA-Z0-9_-]*\.(txt|html|hta))$"`.

Furthermore, if a newly created text file is detected, `response.ransom_note` scans the first 4,096 bytes for signature phrases:
- `"your personal files are encrypted"`
- `"send bitcoin to the following address"`
- `"all your documents, photos, databases have been locked"`
- `"tor browser"` / `"onion address"`

Detecting any matching phrase instantly sets `ransom_note = True`, bypassing all statistical thresholds and triggering immediate process termination.

### 5.3.2 Protected Store Anti-Tampering Engine (Canary Monitoring)
Ransomware frequently attempts to inhibit system recovery (MITRE ATT&CK T1490) by deleting local backup files and clearing quarantine directories. EntroVault protects its own storage directories (`backup_storage/` and `quarantine_storage/`) by scheduling active watchdog observers across them.

If a `DELETED` event is intercepted within `backup_storage/` or `quarantine_storage/`, the pipeline immediately invokes `defense_guard`:
```python
def check_defense_tampering(event: dict) -> bool:
    file_path = event.get("file_path", "")
    event_type = event.get("event_type", "")
    if event_type == "DELETED":
        for protected in (config.BACKUP_DIR, config.QUARANTINE_DIR):
            if os.path.commonpath([file_path, protected]) == protected:
                # Exclude internal housekeeping files (manifests, temp files)
                if not os.path.basename(file_path).startswith(".tmp"):
                    log.critical(f"[TAMPER] Defensive store deletion: {file_path}")
                    return True
    return False
```
An unauthorized deletion within a protected defensive directory trips the `defense_tamper = True` flag, which constitutes an immediate hard-confirmation signal requiring instant containment.

---

## 5.4 High-Performance Entropy Calculation Engine (`entropy.entropy_calculator`)

The mathematical core of the detection pipeline is implemented within `entropy.entropy_calculator`. Listing 5.1 details the vectorized byte-frequency calculation and Shannon formula evaluation:

```python
def calculate_entropy(data: bytes) -> float:
    if not data:
        return 0.0

    # Step 1: Count byte frequencies across 256 bins
    byte_counts = [0] * 256
    for byte in data:
        byte_counts[byte] += 1

    # Step 2: Vectorized Shannon entropy evaluation
    total_bytes = len(data)
    entropy = 0.0
    for count in byte_counts:
        if count == 0:
            continue
        probability = count / total_bytes
        entropy -= probability * math.log2(probability)

    return round(entropy, 4)
```
*Listing 5.1: Vectorized Shannon Entropy Computation in Python.*

### Tri-Segment Sampling Implementation
To capture partial and header encryption without reading multi-megabyte files into memory, `calculate_file_entropy()` reads up to `config.SAMPLE_SIZE_BYTES` ($65,536$ bytes) and computes three non-overlapping segmental entropies:

```python
def calculate_file_entropy(file_path: str, sample_size: int = None) -> dict:
    if sample_size is None:
        sample_size = config.SAMPLE_SIZE_BYTES

    # Default metadata structure
    result = {
        'file_path': file_path,
        'timestamp': datetime.now().isoformat(),
        'entropy_overall': 0.0,
        'entropy_start': 0.0,
        'entropy_middle': 0.0,
        'entropy_end': 0.0,
        'file_size': 0,
        'is_readable': False,
        'file_hash': ''
    }

    try:
        result['file_size'] = os.path.getsize(file_path)
        with open(file_path, 'rb') as f:
            data = f.read(sample_size)
        
        result['bytes_read'] = len(data)
        result['is_readable'] = True
        if len(data) == 0:
            return result

        result['entropy_overall'] = calculate_entropy(data)

        # Segmental partition
        third = len(data) // 3
        if third > 0:
            result['entropy_start']  = calculate_entropy(data[:third])
            result['entropy_middle'] = calculate_entropy(data[third:2*third])
            result['entropy_end']    = calculate_entropy(data[2*third:])

        # SHA-256 baseline fingerprint
        result['file_hash'] = hashlib.sha256(data).hexdigest()
    except (PermissionError, FileNotFoundError) as e:
        result['error'] = str(e)

    return result
```
*Listing 5.2: Tri-Segment Sliding Entropy and Metadata Extraction.*

---

## 5.5 Dual-Layer Cryptographic Fingerprinting Engine (`storage.hashing`)

To ensure collision-resistant forensic tracking, `storage.hashing` exposes low-level cryptographic hashing primitives supporting dual-algorithm fingerprint generation:

```python
def sha3_256_file(path: str) -> str:
    # Compute NIST FIPS 202 SHA3-256 digest in 64KB blocks
    h = hashlib.sha3_256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def sha256_file(path: str) -> str:
    # Compute NIST FIPS 180-4 SHA-256 digest in 64KB blocks
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def dual_hash_file(path: str) -> tuple[str, str]:
    # Compute both digests in a single I/O pass
    h3 = hashlib.sha3_256()
    h2 = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h3.update(chunk)
            h2.update(chunk)
    return h3.hexdigest(), h2.hexdigest()
```
Computing both hashes in a single sequential I/O pass minimizes NVMe disk read cycles while providing cryptographic security against theoretical single-algorithm hash collision attacks.

---

## 5.6 SQLite Storage Architecture and Transactional Schema (`storage.database`)

Persistent telemetry and defensive audit records are managed via an embedded SQLite database (`entropy.db`). Table 5.1 outlines the primary schema definitions across core relational tables:

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|                        TABLE 5.1: RELATIONAL DATABASE SCHEMAS                            |
+───────────────────┬──────────────────────────────────────────────────────────────────────+
| Table Name        | Schema Fields and Data Types                                         |
+───────────────────┼──────────────────────────────────────────────────────────────────────+
| events            | id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp TEXT,                |
|                   | file_path TEXT, event_type TEXT, entropy REAL, entropy_delta REAL,   |
|                   | pid INTEGER, process_name TEXT, action INTEGER, status TEXT,         |
|                   | outcome TEXT, restore_result TEXT, dry_run INTEGER, engine TEXT,     |
|                   | confidence REAL, explanation TEXT, q_values TEXT                     |
+───────────────────┼──────────────────────────────────────────────────────────────────────+
| blockchain_log    | id INTEGER PRIMARY KEY AUTOINCREMENT, event_id INTEGER,              |
|                   | tx_hash TEXT, block_number INTEGER, fingerprint TEXT,                |
|                   | threat_type TEXT, pid INTEGER, process_name TEXT, file_path TEXT,    |
|                   | action_taken TEXT, status TEXT, timestamp TEXT, mode TEXT            |
+───────────────────┼──────────────────────────────────────────────────────────────────────+
| backup_manifest   | file_path TEXT, version INTEGER, backup_path TEXT,                   |
|                   | sha256_hash TEXT, entropy REAL, timestamp TEXT, is_clean INTEGER,    |
|                   | PRIMARY KEY (file_path, version)                                     |
+───────────────────┼──────────────────────────────────────────────────────────────────────+
| threat_exchange   | fingerprint TEXT PRIMARY KEY, sightings INTEGER, confirmed INTEGER,  |
|                   | threat_type TEXT, first_seen TEXT, last_seen TEXT, nodes_json TEXT   |
+───────────────────┴──────────────────────────────────────────────────────────────────────+
```

To prevent database contention between high-velocity watchdog worker threads and the asynchronous SocketIO push loop, all database connections enable SQLite Write-Ahead Logging (WAL) mode:
```sql
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;
PRAGMA busy_timeout = 5000;
```
This configuration permits concurrent readers without locking the active pipeline writer thread.

---

## 5.7 Chapter Summary

This chapter detailed the low-level implementation mechanics of EntroVault's operational core:
1. The watchdog file monitor polls directory handles every 200ms and utilizes an event deduplicator to eliminate redundant write events within a 1.0-second sliding window.
2. DefenseGuard traps explicit indicators of compromise, including ransom notes and unauthorized deletions of protected backup/quarantine stores.
3. The entropy calculator evaluates Shannon entropy via a vectorized 256-bin histogram and computes tri-segment sub-entropies to detect localized partial encryption.
4. The storage subsystem enforces dual-layer cryptographic hashing (SHA3-256 + SHA-256) and logs relational telemetry into a WAL-enabled SQLite database.

Chapter 6 evaluates the multi-tier decision engines, the Campaign Escalation Tracker, and the machine learning classifiers.

---


<div style="page-break-after: always;"></div>

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
- Absolute Entropy: $H(D) \ge 6.8$ bits/byte.
- Differential Jump: $|\Delta H| \ge 2.0$ bits/byte.
- Threat Score: $S \in [0, 100]$.
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
The primary theoretical vulnerability of per-file heuristic detectors is the **Slow-Crawler Attack Vector**. A sophisticated ransomware strain (such as modernized LockBit or BlackCat builds) can introduce sleep pauses between successive file encryptions (e.g., waiting 650 milliseconds between files, operating at $1.5 - 1.6$ files/sec). Under this velocity, the attack never trips write-burst thresholds. Furthermore, by encrypting files without appending suspicious extensions, each individual file operation produces an isolated `ACTION_ALERT` (score $approx. .  60$) that never crosses the destructive containment threshold ($70 + \text{corroboration}$). The adversary can slowly encrypt an entire disk estate over several hours without triggering automated mitigation.

### 6.3.2 Temporal Window Correlation and State Automaton
To neutralize this evasion technique, EntroVault introduces the **Campaign Escalation Tracker** (`CampaignTracker`). The tracker recognizes that cryptoviral extortion is intrinsically an aggregate, multi-file campaign.

The tracker maintains an in-memory chronological deque of recent events occurring within a rolling temporal window $\tau$:
$$\tau = \text{CAMPAIGN\_WINDOW\_SECONDS} = 15.0 \text{ seconds}$$

An event qualifies for campaign tracking if and only if it satisfies the qualification predicate:
$$\text{Qualifies}(e) \iff \left( H(e) \ge 6.8 \right) \land \left( |\Delta H(e)| \ge 2.0 \;\lor\; \text{ExtChanged}(e) \right)$$

When a newly ingested file event triggers an alert ($a \ge \text{ACTION\_ALERT}$), the tracker interrogates its sliding window:
$$\text{CountDistinctPaths}(\text{qualifying events in } [t - \tau, t]) \ge \text{CAMPAIGN\_MIN\_FILES} - 1$$

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
  $$10 \xrightarrow{\text{Dense}} 64 \xrightarrow{\text{ReLU}} 64 \xrightarrow{\text{ReLU}} 4 \quad [Q(s, a_0), Q(s, a_1), Q(s, a_2), Q(s, a_3)]$$
- **Experience Replay Memory:** A cyclic replay buffer (`deque(maxlen=10000)`) storing transition tuples $(s_t, a_t, r_t, s_{t+1}, d_t)$. Minibatches of size $B = 64$ are randomly sampled to decorrelate consecutive training observations.
- **Epsilon-Greedy Exploration Policy:** Initial exploration rate $\epsilon_{start} = 1.0$ decays exponentially at rate $\lambda = 0.995$ per episode down to $\epsilon_{end} = 0.01$.
- **Target Network Synchronization:** To stabilize the regression target in temporal difference learning, a target network $\hat{Q}(s, a; \theta^-)$ is synchronized with the online policy network $\theta$ every 10 episodes.

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


<div style="page-break-after: always;"></div>

# CHAPTER 7: AUTOMATED RESPONSE, STRICT BACKUP, AND BYTE-LEVEL RECOVERY

This chapter details the autonomous containment, forensic preservation, and disaster recovery subsystems of EntroVault. It analyzes how the platform achieves verified process termination, prevents ciphertext backup poisoning, eliminates false positives during estate recovery, and guarantees byte-for-byte restoration of attacked files.

---

## 7.1 Autonomous Response Orchestration Subsystem (`response.response_module`)

Upon receiving an actionable directive (`ACTION_TERMINATE` or `ACTION_TERMINATE_QUARANTINE`) from the decision layer, the defensive pipeline transitions from passive monitoring to active containment. The execution workflow is coordinated by `response.response_module.execute_response` across six atomic phases:

```
                  Trigger: ACTION_TERMINATE_QUARANTINE
                                   │
                                   ▼
          [ Phase 1: Verified Process Tree Termination ]
          - Interrogate PID via psutil; verify open handles
          - Validate immunity whitelist (DEFENDER_TOOLING_MARKERS)
          - Execute SIGTERM -> instant zombie reap (rc=42)
                                   │
                                   ▼
          [ Phase 2: Dual-Hash Quarantine Vault Isolation ]
          - Compute SHA3-256 + SHA-256 dual fingerprint
          - Atomic move to install-time quarantine_storage/
          - Serialize forensic metadata manifest (.meta.json)
                                   │
                                   ▼
          [ Phase 3: Multi-File Campaign Sweep ]
          - Iterate across all files recorded in 15s campaign window
          - Quarantine and restore intermediate alerted files
                                   │
                                   ▼
          [ Phase 4: Content-Based Post-Kill Verification ]
          - Recursively walk monitored estate (victim_server/user_files/)
          - Compare current SHA-256 vs last known clean baseline
          - Remediate partially corrupted or mid-write files
                                   │
                                   ▼
          [ Phase 5: Atomic Byte-Level In-Place Restoration ]
          - Retrieve hash-verified clean blob from backup_storage/
          - Restore original content byte-for-byte
          - Reverse-rename mutated extensions (e.g., .WNCRY -> .xlsx)
                                   │
                                   ▼
          [ Phase 6: Immutable Forensic Record Commit ]
          - Generate RFC-compliant incident JSON report
          - Broadcast transaction to Ganache EVM / LocalLedger
```
*Figure 7.1: Multi-Phase Autonomous Response Execution Lifecycle.*

---

## 7.2 Verified Process Attribution and Process Termination Mechanics

### 7.2.1 Handle Extraction and Attribution Verification
In an asynchronous userspace architecture, terminating arbitrary processes based on statistical file events carries catastrophic risk. If an innocent background utility (e.g., an antivirus scanner, indexer, or cloud sync agent) touches a file immediately after ransomware encrypts it, naive process attribution would terminate the innocent utility while leaving the active malware process intact.

To resolve this attribution challenge, `response.response_module.ProcessTerminator` performs **handle-level verification**:
```python
def terminate_process(pid: int, expected_path: str = None) -> tuple[bool, str]:
    if not pid or pid <= 0:
        return False, "Invalid PID"

    try:
        proc = psutil.Process(pid)
    except psutil.NoSuchProcess:
        return True, "Process already exited (zombie-safe)"

    # Security Whitelist Enforcement
    cmdline = " ".join(proc.cmdline()).lower()
    if any(marker in cmdline for marker in config.DEFENDER_TOOLING_MARKERS):
        log.warning(f"[TERMINATOR] Self-kill blocked for defender marker: {cmdline}")
        return False, "Process is defender tooling (whitelisted)"

    if proc.name() in config.WHITELISTED_PROCESSES:
        return False, "Process is operating system core binary"
```

### 7.2.2 The Zombie Process Problem and Instant Clean Reaping
In high-speed malware detonations, a critical race condition emerges: the malicious child process (such as a CLI encryption script) may complete its write operation, exit its main loop, and enter the operating system **Zombie (defunct)** state before the terminator thread executes `proc.terminate()`. 

In unoptimized defensive platforms, attempting to send `SIGTERM` or `SIGKILL` to a zombie process fails with `NoSuchProcess` or hangs waiting for process disappearance, triggering a fallback 3-second force-kill timeout. This induces unacceptable pipeline latency, delaying file restoration by several seconds.

EntroVault implements **Zombie-Aware Process Reaping**:
```python
    try:
        # Check process status prior to signal dispatch
        status = proc.status()
        if status in (psutil.STATUS_ZOMBIE, psutil.STATUS_DEAD):
            log.info(f"[TERMINATOR] Process PID {pid} is already zombie/dead.")
            return True, "Terminated (zombie reaped rc=42)"

        # Graceful SIGTERM dispatch
        proc.terminate()
        try:
            proc.wait(timeout=0.2)
            return True, "Terminated cleanly via SIGTERM (rc=42)"
        except psutil.TimeoutExpired:
            # Forceful SIGKILL fallback if process ignores SIGTERM
            proc.kill()
            proc.wait(timeout=0.5)
            return True, "Forcefully killed via SIGKILL"
    except psutil.NoSuchProcess:
        return True, "Process exited before termination signal"
```
By recognizing defunct process states and polling with a tight 200ms timeout, the terminator achieves instantaneous containment ($rc = 42$), completely eliminating the 3-second penalty.

---

## 7.3 Install-Time Isolated Quarantine Vault Subsystem

### 7.3.1 Installation-Time Physical Provisioning Mandate
A core requirement of the 200-mark final year specification mandates that **the quarantine folder must be created by the user at installation time**. In enterprise environments, quarantine storage cannot be an ad-hoc directory dynamically spawned during an attack, as administrative restrictions or disk quota limits could cause runtime provisioning failure.

EntroVault enforces install-time provisioning within `install.py`:
```python
def setup_environment():
    q_dir = Path(config.QUARANTINE_DIR) # quarantine_storage/
    b_dir = Path(config.BACKUP_DIR)     # backup_storage/
    q_dir.mkdir(parents=True, exist_ok=True)
    b_dir.mkdir(parents=True, exist_ok=True)
    print(f"[INSTALL] Quarantine folder created by user at install: {q_dir}")
```
Runtime safeguards in `config.py` and `lab.py` (`_ensure_quarantine()`) assert the physical existence of this store prior to booting the monitoring observers.

### 7.3.2 Dual-Hash File Encapsulation and Metadata Serialization
When `FileQuarantine.quarantine()` isolates an infected file, it performs an atomic filesystem move from the protected victim directory into `quarantine_storage/`. To prevent filename collisions during multi-strain attacks, the file is renamed using a composite token:
$$	ext{quarantined\_filename} = 	ext{base\_name} + 	ext{"\_"} + 	ext{timestamp} + 	ext{"\_"} + 	ext{UUID4}[:8]$$

Simultaneously, the engine generates an accompanying forensic metadata file (`<quarantined_filename>.meta.json`) containing cryptographic evidence:
```json
{
  "original_path": "victim_server/user_files/Financial_Report_2024.xlsx.WNCRY",
  "quarantine_time": "2026-10-06T14:22:01.104231",
  "entropy_score": 7.8841,
  "sha3_256": "8a3f9e2b1c4d...e7f1",
  "sha256": "5c2d8a1e9b3f...4a0c",
  "attributing_pid": 3101,
  "attributing_process": "python3 (ransomware_engines.py)",
  "detection_engine": "rules + campaign_escalation",
  "decryption_possible": false
}
```

### 7.3.3 The Cryptographic Non-Decryption Invariant (Viva Defense Assurance)
A frequent point of academic failure during oral defense (viva voce) is candidates falsely asserting that their defensive software can "decrypt" quarantined files once the administrator enters a master password. 

EntroVault publishes an explicit, mathematically sound policy:
**Quarantined files cannot be decrypted by anyone, including privileged administrators.**
- In real-world ransomware, the adversary encrypts files with an ephemeral symmetric key ($K_{sym}$) and encapsulates it using their remote asymmetric public key ($K_{pub}$). Without the adversary's private key ($K_{priv}$), decryption is computationally infeasible ($\mathcal{O}(2^{256})$).
- In EntroVault's purple-team simulation engines, ciphertext is generated via irreversible operating system entropy streams (`os.urandom`) overwrite. The original bytes are permanently destroyed.
- The quarantine vault serves strictly as an **isolated forensic evidence locker** to preserve malware artifacts for threat intelligence analysis. Disaster recovery is achieved strictly via clean backup rollback, not decryption.

---

## 7.4 Strict Clean Backup Engine (`response.backup_manager`)

### 7.4.1 The Ciphertext Backup Contamination Defect
In conventional backup architectures, file monitoring agents automatically snapshot modified files to maintain current version histories. Under a ransomware attack, this behavior produces catastrophic **disaster recovery poisoning**:
1. Clean file `Financial_Report_2024.xlsx` (Entropy: 6.84) is monitored by the backup agent.
2. Ransomware overwrites the file with ciphertext, raising its entropy to 7.88.
3. The backup agent detects a `FileModifiedEvent` and ingests the encrypted file as "Version 2".
4. When the response engine terminates the ransomware and requests a rollback, the backup manager restores "Version 2"—restoring ciphertext over disk, resulting in total permanent data loss.

### 7.4.2 The Strict Clean Verification Algorithm
To eradicate this vulnerability, EntroVault introduces the **Strict Clean Ingestion Algorithm** (`response.backup_manager.BackupManager._is_clean(strict=True)`), illustrated in Figure 7.2:

```
              Ingested Event-Time Snapshot Candidate
                                 │
                                 ▼
           [ Rule 1: Extension Known in Baseline Catalog? ]
           - Is ext in NORMAL_ENTROPY_RANGES?
                                 │
                  NO ────────────┴──────────── YES
                   │                            │
                   ▼                            ▼
            [ REJECT: NOT CLEAN ]      [ Rule 2: Strict Upper Boundary Check ]
            (Unknown ext at event      - Is Entropy <= normal_max?
             time cannot be clean)     (Strict check: NO +0.5 margin permitted!)
                                                │
                                 NO ────────────┴──────────── YES
                                  │                            │
                                  ▼                            ▼
                           [ REJECT: NOT CLEAN ]     [ Rule 3: Differential Delta Cap ]
                                                     - |Entropy - Last_Clean_Entropy| >= 2.0?
                                                               │
                                                YES ───────────┴─────────── NO
                                                 │                           │
                                                 ▼                           ▼
                                          [ REJECT: NOT CLEAN ]     [ ADMIT AS CLEAN V1 ]
                                          (Sudden phase shift       (Eligible as Disaster
                                           indicates encryption)     Recovery Rollback Source)
```
*Figure 7.2: Strict Clean Backup Verification and Admission Control.*

The Python implementation in `response/backup_manager.py` enforces these constraints:
```python
def _is_clean(self, path: str, entropy: float, strict: bool = False) -> bool:
    _, ext = os.path.splitext(path)
    ext = ext.lower()
    normal = config.NORMAL_ENTROPY_RANGES.get(ext)

    # Constraint 1: Unknown extensions at runtime are never admitted as clean
    if normal is None:
        if strict:
            return False
        return entropy < config.ENTROPY_THRESHOLD

    # Constraint 2: Strict upper boundary check (zero tolerance margin)
    normal_max = normal[1] if strict else (normal[1] + 0.5)
    if entropy > normal_max:
        return False

    # Constraint 3: Differential delta jump cap
    last_clean_entropy = self._get_last_clean_entropy(path)
    if last_clean_entropy is not None:
        if abs(entropy - last_clean_entropy) >= config.ENTROPY_DELTA_THRESHOLD:
            log.warning(f"[BACKUP] Rejecting capture: Delta jump {abs(entropy - last_clean_entropy):.2f} >= 2.0")
            return False

    return True
```
This multi-layered validation guarantees that encrypted files (such as an `.xlsx` file modified to 7.88 bits/byte) are rejected from clean backup qualification. Disaster recovery rollback is strictly restricted to pre-attack baseline snapshots (`is_clean == 1`).

---

## 7.5 Post-Kill Estate Verification and Active Remediation

### 7.5.1 Content-Based Estate Walking vs. Blind Entropy Sampling
Following process termination, a critical operational requirement is verifying that no partially encrypted files or modified remnants remain across the estate. A naive approach would walk the directory tree and flag any file with entropy exceeding $6.8$ bits/byte. 

However, **entropy-only post-kill verification causes severe false positives on legitimate media**:
- In a standard corporate directory, legitimate JPEG photos (`.jpg`) and MPEG-4 videos (`.mp4`) exhibit native entropies between $7.2$ and $7.8$ bits/byte.
- A blind entropy check would misidentify all enterprise photos and videos as ransomware ciphertext, triggering unnecessary and destructive rollbacks.

EntroVault solves this via **Content-Based Cryptographic Verification**:
```python
def post_kill_verification(estate_dir: str, backup_manager: BackupManager):
    repaired_count = 0
    for root, _, files in os.walk(estate_dir):
        for file in files:
            full_path = os.path.join(root, file)
            # Skip ransom notes and defender artifacts
            if full_path.endswith((".meta.json", ".txt")):
                continue

            current_hash = sha256_file(full_path)
            clean_hash = backup_manager.get_last_clean_hash(full_path)

            # Verification based strictly on cryptographic content equality
            if clean_hash and current_hash != clean_hash:
                log.warning(f"[POST-KILL] Hash mismatch detected for {file} -> Initiating Repair")
                backup_manager.restore(full_path)
                repaired_count += 1
    return repaired_count
```
By comparing SHA-256 hashes against known-good baselines, legitimate high-entropy photos ($H = 7.4$, identical pre- and post-attack hash) remain completely untouched, while partially encrypted documents are precisely repaired.

### 7.5.2 Atomic In-Place Rollback and Reverse-Rename Mechanics
Ransomware strains regularly append proprietary extensions to target files (e.g., renaming `Client_Meeting_Notes.docx` to `Client_Meeting_Notes.docx.WNCRY`). When restoring an estate, restoring content into the `.WNCRY` path leaves a corrupted filename, whereas creating a new file while the `.WNCRY` file exists leaves duplicate artifacts.

EntroVault coordinates atomic in-place rollback and reverse-renaming:
1. The quarantine module removes `Client_Meeting_Notes.docx.WNCRY` from disk into `quarantine_storage/`.
2. The backup manager queries the historical manifest to identify the original un-mutated file path (`Client_Meeting_Notes.docx`).
3. The clean blob is read from `backup_storage/` and written directly to the original path.
4. Cryptographic checksums are re-verified on disk.

This workflow guarantees that the estate is restored **byte-for-byte and name-for-name**, leaving 0 `.WNCRY` files on disk.

---

## 7.6 Automated Forensic Incident Reporting (`response.forensic_report`)

For every contained incident, `response.forensic_report.generate_report()` aggregates forensic telemetry into a structured JSON incident dossier saved to `reports/incidents/`:

```json
{
  "incident_id": "INC-20261006-3101",
  "timestamp": "2026-10-06T14:22:03.891042",
  "detection_summary": {
    "primary_threat_type": "WannaCry_Simulation",
    "trigger_reason": "CAMPAIGN_ESCALATION (2 files in 15s)",
    "attributing_process": {
      "pid": 3101,
      "name": "python3",
      "cmdline": "python3 attacker_server/ransomware_engines.py --strain wannacry"
    }
  },
  "impact_metrics": {
    "files_alerted": 1,
    "files_quarantined": 2,
    "files_restored_clean": 2,
    "estate_integrity_score": "100.0% (18/18 files verified)"
  },
  "cryptographic_evidence": [
    {
      "file_path": "victim_server/user_files/Financial_Report_2024.xlsx",
      "ciphertext_sha3_256": "8a3f9e...e7f1",
      "ciphertext_sha256": "5c2d8a...4a0c",
      "restored_baseline_sha256": "3d9e4a...1b2c",
      "blockchain_tx_receipt": "0x4b7c8f...9a12"
    }
  ]
}
```
This automated dossier provides complete, legally admissible technical documentation for insurance claims and post-incident digital forensics.

---

## 7.7 Chapter Summary

This chapter detailed the response, quarantine, and recovery architecture of EntroVault:
1. Process termination leverages handle verification and zombie process reaping, achieving instant execution ($rc = 42$) without force-kill latency.
2. The install-time quarantine vault encapsulates infected artifacts using dual SHA3-256 + SHA-256 hashes, strictly enforcing non-decryption policies.
3. The Strict Clean Backup algorithm eliminates disaster recovery poisoning by rejecting candidates with out-of-range entropies or delta jumps $\ge 2.0$.
4. Post-kill verification relies on cryptographic SHA-256 hash comparison rather than blind entropy checks, eliminating false positives on legitimate media.
5. In-place recovery restores damaged files byte-for-byte and reverses adversarial renames, achieving 100% pre-attack estate fidelity.

Chapter 8 details the blockchain ledger, smart contract architecture, and cryptographic immutability guarantees.

---


<div style="page-break-after: always;"></div>

# CHAPTER 8: BLOCKCHAIN LEDGER, SMART CONTRACTS, AND FORENSIC IMMUTABILITY

This chapter analyzes the cryptographic integrity and decentralized audit architecture of EntroVault. It details the Solidity smart contract implementation (`ThreatLogger.sol`), evaluates Ethereum Virtual Machine (EVM) gas dynamics, and analyzes the autonomous local fallback mechanism engineered to preserve forensic logging during network partitioning.

---

## 8.1 The Forensic Requirement for Decentralized Non-Repudiation

In contemporary enterprise breach investigations and legal proceedings, the integrity of digital evidence is governed by strict chain-of-custody standards (e.g., ISO/IEC 27037). When responding to an advanced ransomware intrusion, digital forensics and incident response (DFIR) teams encounter a fundamental challenge: **host log volatility and administrative tampering**.

Adversaries possessing local administrative or `NT AUTHORITY\SYSTEM` privileges systematically neutralize local audit mechanisms:
```cmd
wevtutil.exe cl Security
wevtutil.exe cl System
wevtutil.exe cl Application
```
On Linux hosts, rootkits regularly truncate `/var/log/audit/audit.log` or modify disk timestamps (`touch -r`) to conceal malware drop times. Furthermore, centralized remote logging protocols (such as standard unauthenticated Syslog over UDP/514) are susceptible to network packet injection, eavesdropping, and truncation if lateral movement compromises network routers.

To guarantee non-repudiation, EntroVault integrates an immutable decentralized ledger. By committing cryptographic fingerprints of detected threats, attributing process metadata, and exact block timestamps to an Ethereum Virtual Machine (EVM) smart contract, the system produces a permanent, cryptographically tamper-proof audit trail that cannot be modified, deleted, or retroactively falsified by any host-level adversary.

---

## 8.2 EVM Smart Contract Architecture (`contracts/ThreatLogger.sol`)

The decentralized logging subsystem is governed by the custom Solidity smart contract `ThreatLogger.sol`, deployed to an Ethereum-compatible network. Listing 8.1 provides the complete contract implementation:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ThreatLogger {
    struct ThreatEvent {
        uint256 id;
        string  fingerprint;
        string  threatType;
        uint256 timestamp;
        uint256 pid;
        uint256 entropyScore;
        string  processName;
        string  filePath;
        string  actionTaken;
        string  status;
    }

    ThreatEvent[] public events;
    address public owner;

    event ThreatLogged(
        uint256 indexed id,
        string fingerprint,
        string threatType,
        uint256 timestamp
    );

    constructor() { 
        owner = msg.sender; 
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "not owner");
        _;
    }

    function transferOwnership(address nextOwner) public onlyOwner {
        require(nextOwner != address(0), "zero owner");
        owner = nextOwner;
    }

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
            id, fingerprint, threatType, block.timestamp,
            pid, entropyScore, processName, filePath, actionTaken, status
        ));
        emit ThreatLogged(id, fingerprint, threatType, block.timestamp);
        return id;
    }

    function getEvent(uint256 id) public view returns (
        uint256, string memory, string memory, uint256,
        uint256, uint256, string memory, string memory, string memory, string memory
    ) {
        ThreatEvent memory e = events[id];
        return (e.id, e.fingerprint, e.threatType, e.timestamp,
                e.pid, e.entropyScore, e.processName, e.filePath, e.actionTaken, e.status);
    }

    function getEventCount() public view returns (uint256) { 
        return events.length; 
    }

    function getRecentEvents(uint256 count) public view returns (uint256[] memory) {
        uint256 len = events.length;
        uint256 n = count < len ? count : len;
        uint256[] memory ids = new uint256[](n);
        for (uint256 i = 0; i < n; i++) ids[i] = len - n + i;
        return ids;
    }
}
```
*Listing 8.1: Complete ThreatLogger.sol Smart Contract.*

### 8.2.1 Structural Analysis and Access Control
- **`ThreatEvent` Data Structure:** Encapsulates the complete digital forensic vector, binding the SHA-256 fingerprint of the ciphertext, the attributed operating system PID, the process executable name, the target file path, and the action taken.
- **`onlyOwner` Modifier Security:** The `logThreat()` entrypoint enforces strict access control. Only the designated defensive agent account (`owner = msg.sender` initialized during deployment) possesses authorization to append records. Malicious processes running on the host cannot inject fraudulent records or overwrite existing state.
- **Event Emission for SOC Telemetry:** Committing an event triggers the EVM log instruction `emit ThreatLogged(...)`. Remote SOC visualizers and enterprise SIEM aggregators can monitor these indexed logs via standard JSON-RPC WebSocket filters (`eth_subscribe("logs")`) without polling contract storage.

---

## 8.3 EVM Gas Consumption Dynamics and Transaction Costs

A frequent operational criticism of blockchain-based security architectures is prohibitive gas consumption. In EntroVault, storage layout and variable encodings were optimized to minimize computational overhead within the EVM.

Table 8.1 details the measured gas consumption profile across contract functions executed on Ganache:

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|                    TABLE 8.1: EVM GAS CONSUMPTION PROFILE                                |
+───────────────────────┬──────────────┬───────────────┬───────────────────────────────────+
| Operational Function  | Gas Used     | Cost @ 20 Gwei| Operational Role in Pipeline      |
+───────────────────────┼──────────────┼───────────────┼───────────────────────────────────+
| Contract Deployment   | 842,190 gas  | 0.0168 ETH    | One-time setup during install.py  |
| transferOwnership     | 28,412 gas   | 0.0005 ETH    | Administrative key rotation       |
| logThreat (Short Path)| 94,520 gas   | 0.0018 ETH    | Committing standard incident      |
| logThreat (Long Path) | 118,740 gas  | 0.0023 ETH    | Incident with long directory path |
| getEvent (View Call)  | 0 gas (Free) | 0.0000 ETH    | Read-only SOC query via JSON-RPC  |
| getEventCount (View)  | 0 gas (Free) | 0.0000 ETH    | Read-only telemetry health check  |
+───────────────────────┴──────────────┴───────────────┴───────────────────────────────────+
```

Because defensive containment executes only upon confirming a ransomware campaign or detecting hard indicators (e.g., at File 2 of an attack), the system commits an average of only $2 - 4$ transactions per attack scenario. On enterprise private Ethereum networks (e.g., Hyperledger Besu or Quorum), transaction fees are negligible or zero, making this architecture viable for high-throughput enterprise deployment.

---

## 8.4 Ganache Ethereum Deployment and Web3 Integration (`blockchain.connector`)

Integration between the Python runtime pipeline and the Ethereum node is managed via `blockchain.connector.BlockchainConnector`, wrapping the `web3.py` library:
- **Deployment Script (`blockchain/deploy.py`):** Compiles `ThreatLogger.sol` using `py-solc-x`, connects to the Ganache RPC provider (`http://127.0.0.1:7545`), deploys the compiled bytecode from account index 0, and persists the deployed contract address and ABI to `config.CONTRACT_ADDRESS` and `blockchain/contract_abi.json`.
- **Transaction Assembly:** `BlockchainConnector.log_threat()` dynamically builds the transaction dictionary, queries the current account nonce via `w3.eth.get_transaction_count()`, estimates gas limits, signs the transaction with the defensive wallet private key, and broadcasts via `w3.eth.send_raw_transaction()`.
- **Receipt Confirmation:** The connector awaits transaction receipt confirmation (`w3.eth.wait_for_transaction_receipt(timeout=5.0)`), extracting the mined transaction hash (`tx_hash`) and block number for persistent storage in `entropy.db`.

---

## 8.5 Resilient Dual-Mode Architecture: Autonomous LocalLedger Fallback

### 8.5.1 The Network Partition Reality
In an authentic cyber attack, defensive endpoints face severe network disruption:
- Adversaries regularly execute network interface denial commands (e.g., `netsh interface set interface "Ethernet" disable`).
- Enterprise SOC incident responders often execute rapid network quarantine, severing all WAN and LAN traffic to contain lateral infection.
- In academic evaluation and demonstration environments, evaluators may execute tests on offline laptops without running local Ganache nodes.

If a security agent binds its logging pipeline synchronously to a remote blockchain, network failure induces pipeline crashes or blocking timeouts, halting process termination and causing total data loss.

### 8.5.2 Dual-Mode Architecture and Transparent Labeling
To resolve this engineering vulnerability, EntroVault incorporates an **Autonomous LocalLedger Fallback Architecture**:

```
                       Incident Containment Event
                                   │
                                   ▼
             [ BlockchainConnector.log_threat(...) ]
                                   │
              Is Ganache EVM Available & Connected?
                                   │
                    YES ───────────┴─────────── NO
                     │                           │
                     ▼                           ▼
        [ MODE: GANACHE EVM ]         [ MODE: FALLBACK LEDGER ]
        - web3.py JSON-RPC            - Local SQLite Transaction
        - Transact to ThreatLogger    - Hash-Chained Audit Table
        - Mined Block Receipt         - Labeled: "FALLBACK (SQLite)"
                     │                           │
                     └─────────────┬─────────────┘
                                   ▼
              [ Persisted to entropy.db & SOC Feed ]
```
*Figure 8.2: Dual-Mode Blockchain Architecture with Resilient LocalLedger Fallback.*

The implementation in `blockchain/connector.py` handles this transition gracefully:
```python
class BlockchainConnector:
    def __init__(self, fallback_enabled: bool = True):
        self.mode = "ganache"
        self.fallback = LocalLedger() if fallback_enabled else None
        
        # Connect to EVM provider
        try:
            self.w3 = Web3(Web3.HTTPProvider(config.GANACHE_URL, request_kwargs={'timeout': 1.0}))
            if not self.w3.is_connected():
                self._activate_fallback("Ganache node offline")
        except Exception as e:
            self._activate_fallback(f"RPC connection failed: {e}")

    def log_threat(self, **kwargs) -> dict:
        if self.mode == "ganache":
            try:
                # Transact to smart contract
                receipt = self._send_contract_tx(**kwargs)
                return {"mode": "ganache", "tx_hash": receipt.transactionHash.hex(), ...}
            except Exception as e:
                log.warning(f"[BLOCKCHAIN] EVM transaction failed ({e}) -> Activating fallback")
                self._activate_fallback(str(e))

        # Autonomous Fallback Path
        return self.fallback.log_threat(**kwargs)
```

### 8.5.3 Academic and Operational Honesty
EntroVault enforces absolute transparency regarding ledger status:
- When operating in fallback mode, all forensic reports, database records, and SOC dashboard banners explicitly display the label:  
  **`MODE: FALLBACK (Local SQLite Ledger - Offline Mode)`**
- The platform never misrepresents a local SQLite database as an immutable distributed ledger. Evaluators and examiners can clearly distinguish between live Ganache EVM blocks and local fallback records, preserving academic integrity during examination.

---

## 8.6 Forensic Chain of Custody and Audit Trail Schema

Each committed transaction produces an immutable cryptographic receipt containing:
1. `tx_hash`: 256-bit Keccak transaction hash generated by the EVM.
2. `block_number`: Monotonically increasing block height confirming temporal order.
3. `fingerprint`: Combined SHA3-256 + SHA-256 hash of the quarantined file.
4. `threat_type`: Categorical malware classification (e.g., `WannaCry_Simulation`).
5. `timestamp`: Operating system Unix epoch timestamp cross-verified against EVM `block.timestamp`.

This record forms an unalterable bridge linking physical disk artifacts in `quarantine_storage/` to immutable on-chain blocks, establishing an unbroken chain of custody admissible in legal forensics.

---

## 8.7 Chapter Summary

This chapter detailed the decentralized forensic architecture of EntroVault:
1. Traditional host logging mechanisms are vulnerable to local administrative tampering and erasure during cryptoviral campaigns.
2. The Solidity `ThreatLogger.sol` contract provides non-repudiable on-chain incident storage, governed by `onlyOwner` access control and gas-optimized structs.
3. Gas consumption averages $94,000 - 118,000$ gas per logged incident, representing negligible operational overhead.
4. The resilient dual-mode architecture guarantees unbroken logging continuity via an autonomous LocalLedger fallback, maintaining clear operational labeling during offline execution.
5. Dual cryptographic fingerprinting binds physical forensic artifacts directly to immutable blockchain receipts.

Chapter 9 presents the comprehensive empirical evaluations, deterministic benchmark batteries, and recovery drill results.

---


<div style="page-break-after: always;"></div>

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


<div style="page-break-after: always;"></div>

# CHAPTER 10: ATTACK SURFACE MODELING, LIMITATIONS, AND BLINDSPOT MITIGATION

This chapter provides a rigorous security analysis of EntroVault. It applies the formal STRIDE threat model to the architecture, delivers an information-theoretic proof of the in-place compressed media blindspot, analyzes adversarial evasion vectors, and documents defensive mitigations.

---

## 10.1 Formal STRIDE Threat Model Applied to EntroVault

To evaluate the defensive robustness of EntroVault against sophisticated threat actors, the architecture was subjected to formal threat modeling using the Microsoft STRIDE methodology. Table 10.1 details the identified threats, attack vectors, and engineering countermeasures:

```
+──────────────────────────────────────────────────────────────────────────────────────────────────────────+
|                    TABLE 10.1: FORMAL STRIDE THREAT ANALYSIS AND MITIGATIONS                            |
+─────────────────────┬────────────────────────────────┬───────────────────────────────────────────────────+
| STRIDE Category     | Adversarial Attack Vector      | Defensive Mitigation in EntroVault                |
+─────────────────────┼────────────────────────────────┼───────────────────────────────────────────────────+
| Spoofing Identity   | Malware process renames its    | ProcessTerminator interrogates OS process table;  |
|                     | executable to svchost.exe to   | handle verification checks open file descriptors; |
|                     | evade termination.             | whitelist only exempts verified system paths.     |
+─────────────────────┼────────────────────────────────┼───────────────────────────────────────────────────+
| Tampering with Data | Ransomware deletes backup      | DefenseGuard schedules active canary observers    |
|                     | manifests or clears quarantine | across backup_storage/ and quarantine_storage/;   |
|                     | directories (T1490).           | unauthorized deletions trip instant kill signal.  |
+─────────────────────┼────────────────────────────────┼───────────────────────────────────────────────────+
| Repudiation         | Adversary wipes local syslog   | Cryptographic fingerprints and block timestamps   |
|                     | and event logs (T1070.004) to  | committed immutably to EVM ThreatLogger contract  |
|                     | destroy forensic evidence.     | and hash-chained SQLite LocalLedger.              |
+─────────────────────┼────────────────────────────────┼───────────────────────────────────────────────────+
| Information Discl.  | Unauthorized user attempts to  | Quarantine store locked behind SHA-256 hashed PIN |
|                     | view quarantined malware       | challenge (victim_user / 1234); constant-time     |
|                     | evidence or private data.      | comparison prevents side-channel timing leaks.    |
+─────────────────────┼────────────────────────────────┼───────────────────────────────────────────────────+
| Denial of Service   | Adversary generates millions of| EventPipeline enforces 10,000-event queue bound;  |
|                     | micro-events to saturate RAM;  | EventDeduplicator suppresses bursts (1.0s window);|
|                     | attempts to force false quaran.| Rule Engine enforces Zero False Quarantine bar.   |
+─────────────────────┼────────────────────────────────┼───────────────────────────────────────────────────+
| Elevation of Priv.  | Attacker attempts directory    | safe_path() containment validator strictly asserts|
|                     | traversal escape (../../)      | all operations remain confined within target      |
|                     | to encrypt host root files.    | victim_server/user_files/ estate boundary.        |
+─────────────────────┴────────────────────────────────┴───────────────────────────────────────────────────+
```

---

## 10.2 In-Depth Analysis of the Image Blindspot Phenomenon

### 10.2.1 Mathematical Indistinguishability Proof
In scientific evaluation, engineering credibility requires candid documentation of physical limitations. Across the benchmark battery (Chapter 9), EntroVault recorded a 0% detection rate on the `image_blindspot` scenario when using the Deterministic Rule Engine. This section delivers the formal mathematical proof establishing why **pure Shannon entropy cannot distinguish in-place encryption of previously compressed media from native content**.

Let $F_{jpg}$ denote a native JPEG image file. Due to the discrete cosine transform (DCT) and subsequent Huffman entropy coding inherent in the JPEG ISO/IEC 10918-1 specification, byte symbols within native images exhibit near-uniform statistical distributions:

$$p_{jpg}(x_i) approx.  rac{1}{256} \pm \epsilon_i \implies H(F_{jpg}) \in [7.20, 7.80] 	ext{ bits/byte}$$

Now, let $F_{cipher} = 	ext{AES-256-CBC}(F_{jpg}, K)$ denote the ciphertext generated by encrypting the image in place without modifying the file extension (`.jpg`). Modern symmetric block ciphers satisfy the strict avalanche criterion (SAC), producing an ideal pseudo-random byte stream:

$$p_{cipher}(x_i) approx.  rac{1}{256} \implies H(F_{cipher}) \in [7.95, 8.00] 	ext{ bits/byte}$$

Under EntroVault's calibrated baseline catalog, the allowable normal entropy range for `.jpg` is:
$$\Omega(	ext{.jpg}) = [7.00, 7.80] 	ext{ bits/byte}$$

Applying the measurement noise tolerance margin ($\Delta_{margin} = 0.5$ bits/byte) established to prevent false positives on highly compressed graphics, the upper detection ceiling becomes:
$$H_{ceiling}(	ext{.jpg}) = H_{max}(	ext{.jpg}) + \Delta_{margin} = 7.80 + 0.50 = 8.30 	ext{ bits/byte}$$

Since theoretical maximum Shannon entropy over 8-bit bytes is mathematically bounded by $H_{max} = 8.00$:
$$H(F_{cipher}) \le 8.00 < 8.30 = H_{ceiling}(	ext{.jpg})$$

Furthermore, because the baseline file was already high-entropy prior to encryption ($H_{t-1} approx.  7.45$), the differential delta jump is:
$$\Delta H = H(F_{cipher}) - H(F_{jpg}) approx.  7.98 - 7.45 = 0.53 	ext{ bits/byte}$$

Since $\Delta H = 0.53 < 2.00$ (`ENTROPY_DELTA_THRESHOLD`), and no extension mutation occurred, **the operation satisfies all mathematical criteria for a legitimate image file modification**. Consequently, the deterministic rule engine correctly refuses to quarantine the file, avoiding false positives during photo editing at the expense of an in-place encryption blindspot.

```
  H(X) [bits/byte]
   8.30 ┼──────────────────────────────────────────────────────── Theoretical Ceiling (7.80 + 0.5)
   8.00 ┼─────────────────────────────────────────────● Ciphertext (H = 7.98)
        │                                             ▲
        │                                  Delta H = 0.53 < 2.00 (Fails Delta Bar!)
        │                                             ▼
   7.45 ┼───────────────────────────────● Native JPEG Image (H = 7.45)
   7.00 ┼──────────────────────────────────────────────────────── Normal Range Minimum for .jpg
   0.00 ┴────────────────────────────────────────────────────────
```
*Figure 10.1: Information Entropy Invariance in Compressed Media Overwrites.*

### 10.2.2 Potential Mitigation Vectors
To close this blindspot in future production revisions without compromising the 0-FQ standard, three complementary signals are planned:
1. **Magic-Byte Header Validation:** Native JPEG images must begin with the 3-byte start-of-image (SOI) marker `0xFF 0xD8 0xFF` and terminate with end-of-image (EOI) `0xFF 0xD9`. Cryptoviral encryption destroys these magic markers. Checking header structural validity can detect encryption instantly without relying on entropy.
2. **Partial-Front Encryption Trapping:** Ransomware optimizing for speed often encrypts only the first 4KB of a media file. Inspecting the $\Delta H_{seg}$ variance across the initial 4KB block can expose destroyed headers.
3. **File Size and Compression Incompressibility:** Encrypted payloads cannot be compressed further (Kolmogorov complexity is maximal). Attempting a fast in-memory Deflate pass on the payload: if the compression ratio is $1.000$, the file is almost certainly encrypted.

---

## 10.3 Adversarial Evasion Vectors and Defensive Countermeasures

Sophisticated ransomware developers continually refine evasion techniques to bypass behavioral EDR agents. This section evaluates three primary adversarial evasion vectors:

### 10.3.1 Sub-Threshold Partial File Interleaving
An adversary can encrypt only every 16th byte of a file or interleave blocks of null bytes (`0x00`) into the ciphertext stream. By diluting the high-entropy ciphertext with zero bytes, the calculated whole-file Shannon entropy is artificially depressed below $6.8$.
- **Mitigation:** EntroVault's **Tri-Segment Entropy Profiling** decomposes samples into Head, Middle, and Tail segments. While global entropy may drop, localized segmental variance ($\Delta H_{seg} \ge 2.5$) trips partial-encryption alarms.

### 10.3.2 Timing Jitter and Extended Dwell-Time Attacks
To evade velocity counters ($>3.0$ events/sec), adversaries insert randomized sleep intervals (e.g., waiting 12 seconds between target files), spreading an attack over several hours.
- **Mitigation:** EntroVault's **Campaign Escalation Tracker** enforces a 15-second sliding window that correlates events across distinct file paths. Even if an adversary slows encryption to 1 file every 7 seconds, 2 distinct qualifying files within the 15-second window trigger immediate escalation to `ACTION_TERMINATE_QUARANTINE`, halting the attack at File 2.

### 10.3.3 Direct Kernel Object Manipulation (DKOM) and Process Spoofing
Advanced threat actors operating at kernel privilege levels (Ring 0) can alter the `ActiveProcessLinks` doubly-linked list in the Windows Executive Process block (`EPROCESS`) to conceal active PIDs from userspace enumeration APIs like `psutil`.
- **Mitigation:** While userspace monitors cannot prevent Ring 0 DKOM, EntroVault's **Kill-Override Attribution** records all processes that previously held file handles. If current process enumeration returns null, the terminator falls back to the last verified malware PID cached within the campaign window.

---

## 10.4 Authentication and Vault PIN Security Architecture

Access to the quarantined evidence vault (`victim_server/app.py`) is restricted via an authenticated administrative API (`/api/quarantine/auth`).

To prevent authentication bypass and side-channel timing attacks, the authentication subsystem enforces two security controls:
1. **Constant-Time Comparison:** User PIN verification utilizes `hmac.compare_digest()`:
   ```python
   def verify_vault_pin(user_input: str) -> bool:
       correct_pin = config.VAULT_PIN # "1234"
       return hmac.compare_digest(user_input.strip(), correct_pin.strip())
   ```
   Standard string equality (`==`) exits early upon encountering the first non-matching character, leaking timing information that allows an attacker to deduce the PIN via microsecond timing analysis. Constant-time evaluation completely eliminates this side-channel leak.
2. **Cryptographic Session Scoping:** Successful authentication generates a signed session token restricted to an 8-hour validity window (`config.VAULT_SESSION_HOURS = 8`) with a hard-coded scope of `quarantine_only`. This token confers read-only access to forensic manifests and explicitly bars administrative access to host command execution.

---

## 10.5 Chapter Summary

This chapter delivered a rigorous threat analysis of EntroVault:
1. The STRIDE security model confirms robust defensive controls across spoofing, tampering, repudiation, information disclosure, denial-of-service, and elevation of privilege.
2. An information-theoretic proof demonstrated why in-place encryption of previously compressed media (the image blindspot) is mathematically indistinguishable from legitimate edits under pure Shannon entropy.
3. Tri-segment profiling and temporal campaign tracking neutralize sophisticated evasion vectors, including entropy padding and slow-crawler timing jitter.
4. Vault PIN authentication utilizes constant-time digest comparison to prevent side-channel timing attacks, establishing strict cryptographic access controls.

Chapter 11 details the real-time SOC interface, the neutral victim explorer, and the attacker simulation console.

---


<div style="page-break-after: always;"></div>

# CHAPTER 11: REAL-TIME SOC INTERFACE, NEUTRAL VICTIM EXPLORER, AND ATTACKER SIMULATION

This chapter details the operational implementation of the three user-facing micro-services comprising EntroVault: the real-time SOC dashboard, the neutral victim workstation explorer, and the multi-strain attacker detonation console. It concludes with the formal live purple-team demonstration script engineered for academic evaluation.

---

## 11.1 Real-Time Telemetry Push Architecture (`app.py` via Flask-SocketIO)

The Security Operations Center (SOC) dashboard (`app.py`, hosted at `http://127.0.0.1:5000`) provides defensive analysts with real-time operational visibility into file system transformations, information-theoretic telemetry, active threat indicators, and blockchain transaction receipts.

### 11.1.1 WebSocket Frame Serialization and 400ms Heartbeat Loop
To satisfy Mandate 1 of the engineering specification (sub-second real-time telemetry streaming), EntroVault decouples database ingestion from client communication using `Flask-SocketIO` operating in multi-threaded asynchronous mode.

A dedicated background daemon thread (`push_updates()`) continuously polls the SQLite relational datastore at tuned 400-millisecond intervals:

```python
def push_updates():
    last_id = 0
    while True:
        try:
            with connect_database() as db:
                # Query newly committed events since last push cycle
                new_rows = db.execute(
                    "SELECT * FROM events WHERE id > ? ORDER BY id ASC LIMIT 100",
                    (last_id,)
                ).fetchall()

                for row in new_rows:
                    event_data = dict(row)
                    # Broadcast discrete event frame to all active SOC WebSockets
                    socketio.emit("new_event", event_data)
                    last_id = max(last_id, row["id"])

                # Broadcast global aggregate system heartbeat
                total_events = db.execute("SELECT COUNT(*) FROM events").fetchone()[0]
                total_threats = db.execute(
                    "SELECT COUNT(*) FROM events WHERE action >= 2"
                ).fetchone()[0]
                
                socketio.emit("live_update", {
                    "total_events": total_events,
                    "threat_count": total_threats,
                    "timestamp": datetime.now().isoformat()
                })
        except Exception as e:
            log.error(f"[DASHBOARD] SocketIO push failed: {e}")

        time.sleep(0.4)
```

By leveraging WebSocket transport (`io({transports: ['websocket', 'polling']})`), telemetry frames reach connected browser sessions in under 420 milliseconds from the physical disk write, achieving verified sub-second operational monitoring.

### 11.1.2 Dynamic Entropy Visualizer and Threat Instrumentation
The frontend dashboard interface incorporates dynamic graphical instrumentation:
- **Real-Time Entropy Waveform:** A live Chart.js time-series graph plotting the Shannon entropy of incoming file operations against the warning threshold ($H = 6.8$) and the cryptographic ceiling ($H = 8.0$).
- **Threat Event Feed:** A scrollable tabular ledger detailing file paths, operating system PIDs, attributing process names, action taken (`IGNORED`, `ALERTED`, `TERMINATED+QUARANTINED`), and engine classification metadata.
- **Incident Inspector Modal:** Selecting an event renders the full forensic JSON record, displaying extracted cryptographic hashes (SHA3-256 and SHA-256), SHAP feature attribution drivers, and Ethereum smart contract transaction receipts.

---

## 11.2 The Neutral Victim Workstation Experience (`victim_server/app.py`)

### 11.2.1 Human-Factors Rationale: Concealing Threat Details
A primary design mandate (Mandate 2) is the complete neutralization of the victim workstation (`victim_server/app.py`, hosted at `http://127.0.0.1:5001`). In operational enterprise incidents, displaying alarming threat telemetry (such as "WannaCry Ransomware Detected on Your PC!") induces panic, prompts unauthorized user reboots that corrupt volatile RAM evidence, or tips off adversaries conducting human-operated intrusions.

The victim interface must function as a **neutral operating system file explorer ("This PC")**:
- The API endpoint `/api/files` strictly sanitizes file system metadata, returning only filename, file size in bytes, last modified date, and standard format icons across user folders (`Documents/`, `Desktop/`, `Downloads/`, `Pictures/`).
- The endpoint **strictly excludes** internal threat scores, detected malware families, encryption flags, or campaign counters.

### 11.2.2 Secure Vault Access Protocol and PIN Authentication
To inspect quarantined evidence, administrative security personnel access the protected Vault modal:
- **Authentication Challenge:** Users must submit credentials to `/api/quarantine/auth`. The backend validates the username (`victim_user`) and performs constant-time PIN verification (`1234`) using `hmac.compare_digest()`.
- **Administrative Quarantine View:** Upon successful authentication, an 8-hour scoped session token is issued, granting access to `/api/quarantine/files`. Administrators can inspect quarantined ciphertext artifacts, view associated `.meta.json` dossiers, and review forensic reports.
- **Strict Non-Decryption Boundary:** The interface contains no "Decrypt Files" button. As established in Section 7.3.3, real cryptoviral ciphertext cannot be decrypted without the adversary's private key; recovery is achieved strictly via pre-attack clean baseline rollback.

---

## 11.3 Multi-Strain Attacker Command-and-Control Console (`attacker_server/app.py`)

The Red Team attacker console (`attacker_server/app.py`, hosted at `http://127.0.0.1:8001`) provides an isolated detonation harness to trigger realistic cryptoviral simulations.

### 11.3.1 Emulation of 10 Real-World Malware Archetypes
The underlying simulation engine (`attacker_server/ransomware_engines.py`) implements synthetic execution profiles modeling 10 notorious ransomware strains, as summarized in Table 11.1:

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|                    TABLE 11.1: SYNTHETIC RANSOMWARE STRAIN PROFILES                      |
+───────────────────┬───────────────────┬─────────────────┬────────────────────────────────+
| Malware Strain    | Extension Appended| Inter-Write Lag | Structural Encryption Payload  |
+───────────────────┼───────────────────┼─────────────────┼────────────────────────────────+
| WannaCry          | .WNCRY            | 0.05s (Fast)    | Full overwrite + WANACRY! hdr  |
| LockBit 3.0       | .lockbit          | 0.02s (Burst)   | Interleaved block encryption   |
| REvil / Sodinokibi| .revil            | 0.15s (Moderate)| Full overwrite + random ext    |
| Ryuk              | .RYK              | 0.10s (Moderate)| Full overwrite + RYK header    |
| BlackCat / ALPHV  | .alphv            | 0.35s (Throttled| Header-only partial encryption |
| Conti             | .CONTI            | 0.08s (Fast)    | Multi-threaded bulk overwrite  |
| Maze              | .maze             | 0.20s (Moderate)| Double-extension append        |
| Cerber            | .cerber           | 0.12s (Moderate)| Triple-extension mutation      |
| GandCrab          | .GDCB             | 0.18s (Moderate)| Full overwrite + ransom note   |
| Dharma            | .dharma           | 0.25s (Throttled| Appended contact email in name |
+───────────────────┴───────────────────┴─────────────────┴────────────────────────────────+
```

### 11.3.2 Speed Modulation and Safety Sandboxing
The attacker console interface provides an interactive velocity slider, allowing evaluators to throttle detonation speeds between:
- Unthrottled Burst Encryptions ($> 25$ files/sec).
- Realistic Slow Crawlers ($1.0 - 1.6$ files/sec) designed to defeat speed thresholds.

All execution engines are strictly bound to `victim_server/user_files/` via `safe_path()` assertion, preventing accidental corruption of host operating system directories.

---

## 11.4 End-to-End Live Purple-Team Demonstration Workflow (200-Mark Script)

To achieve maximum marks during academic evaluation and examiner viva voce defense, the project incorporates a validated one-command demonstration harness (`python lab.py`). Evaluators execute the following end-to-end verification sequence:

### Step 1: Environment Initialization
The evaluator provisions directories and resets test estates:
```bash
python install.py
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python lab.py
```
`lab.py` automatically initializes 18 clean enterprise files across 4 user directories (`victim_server/user_files/`), snapshots clean baselines into `backup_storage/`, boots the watchdog monitoring pipeline, and starts all three web servers.

### Step 2: Workstation Inspection (Examiner Baseline)
1. Navigate to **Victim PC** (`http://127.0.0.1:5001`): The explorer displays 18 clean files (spreadsheets, source code, presentations, and photos). The Quarantine Vault indicates **"Locked [LOCKED]"**.
2. Navigate to **SOC Dashboard** (`http://127.0.0.1:5000`): Threat counter reads **0**, the dynamic entropy waveform displays a flat baseline ($approx.  4.2$), and the heartbeat indicates active sub-second polling.

### Step 3: Red Team Malware Detonation
1. Navigate to **Attacker Console** (`http://127.0.0.1:8001`).
2. Select **WannaCry** strain simulation and click **"Launch Attack"**.

### Step 4: Real-Time Defensive Intervention
Within 2.7 seconds, the SOC Dashboard dynamically streams the containment sequence:
- **File 1 (`Financial_Report_2024.xlsx`):** Overwritten with random bytes ($H = 7.88$). Decision Engine registers `ACTION_ALERT` (Score 60). CampaignTracker records File 1 into the 15-second sliding window.
- **File 2 (`Client_Meeting_Notes.docx.WNCRY`):** Overwritten and renamed ($H = 7.81$). CampaignTracker confirms $\ge 2$ distinct files with cryptoviral signatures within 15 seconds. Escalates immediately to `ACTION_TERMINATE_QUARANTINE`.
- **Process Termination:** `ProcessTerminator` identifies PID 3101, verifies open handle attribution, asserts whitelist immunity, and executes `SIGTERM` / zombie reap ($rc = 42$).
- **Campaign Rollback Sweep:** Response orchestrator sweeps File 1 and File 2, moves ciphertext into `quarantine_storage/`, and restores pre-attack clean baselines.
- **Post-Kill Verification:** System walks the estate, compares SHA-256 checksums against clean baselines, and verifies zero unencrypted `.WNCRY` files remain.

### Step 5: Post-Attack Integrity Verification
1. Refresh **Victim PC** (`http://127.0.0.1:5001`): The directory continues to display **18 clean files**; zero `.WNCRY` files exist.
2. Authenticate to Quarantine Vault using PIN `1234`: The administrator inspects the 2 isolated ciphertext evidence files and accompanying JSON metadata, confirming forensic chain of custody.
3. Refresh **SOC Dashboard** (`http://127.0.0.1:5000`): Threat counter records 1 confirmed incident, displaying mined transaction hashes and SHA3-256 fingerprints.

**Demo Outcome:** Attack terminated at File 2 of 18; 100% of files restored byte-for-byte; 0 false quarantines; 0 data loss.

---

## 11.5 Chapter Summary

This chapter detailed the user-facing operational surfaces of EntroVault:
1. The SOC Dashboard streams real-time telemetry at 400ms intervals via Flask-SocketIO WebSockets, rendering live entropy charts and threat feeds.
2. The Victim Workstation maintains a neutral file explorer interface, concealing cryptoviral threat details while isolating quarantined evidence behind a PIN-authenticated administrative vault.
3. The Attacker Console emulates 10 real-world ransomware families with variable velocity throttling.
4. The live purple-team demonstration workflow verifies sub-second containment at File 2 of 18 with 100% byte-for-byte recovery.

Chapter 12 presents the conclusions, academic reflections, and future engineering roadmap.

---


<div style="page-break-after: always;"></div>

# CHAPTER 12: CONCLUSIONS, LESSONS LEARNED, AND FUTURE RESEARCH DIRECTIONS

This chapter synthesizes the primary findings and engineering contributions delivered by EntroVault. It reviews the fulfillment of the core project mandates, critically evaluates key architectural trade-offs, outlines a production-grade kernel roadmap, and concludes with final reflections on proactive cryptoviral resilience.

---

## 12.1 Project Retrospective and Milestone Summary

The EntroVault (ENTROPY) project was undertaken to resolve the critical operational deficiencies plaguing contemporary ransomware defense architectures: the inefficacy of signature matching against polymorphic binaries, the high false-quarantine rate of statistical heuristics, the catastrophic vulnerability of ciphertext backup contamination, and the volatility of host forensic logs.

Through the engineering designs and empirical evaluations documented across this dissertation, all three primary mandates established in the 200-mark final year specification were definitively fulfilled:

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|                    TABLE 12.1: PROJECT MANDATE FULFILLMENT AUDIT                         |
+─────────────────────┬─────────────────────────────────┬──────────────────────────────────+
| Specification       | Formal Engineering Requirement  | Delivered Empirical Status       |
+─────────────────────┼─────────────────────────────────┼──────────────────────────────────+
| Mandate 1:          | Continuous file monitoring;     | FULFILLED: Watchdog observer +   |
| SOC Real-Time Push  | real-time telemetry streaming   | 400ms Flask-SocketIO push loop;  |
|                     | with sub-second update latency. | sub-420ms verified socket push.  |
+─────────────────────┼─────────────────────────────────┼──────────────────────────────────+
| Mandate 2:          | Neutral victim file explorer;   | FULFILLED: Clean "This PC" UI;   |
| Neutral Workstation | no attack details shown; vault  | no encrypted counts; PIN vault   |
|                     | locked behind authentication.   | (victim_user / 1234, 8h scope).  |
+─────────────────────┼─────────────────────────────────┼──────────────────────────────────+
| Mandate 3:          | Background auto-response; kill  | FULFILLED: WannaCry killed at    |
| Auto-Response &     | process + quarantine to install | File 2/18 in 2.7s; 18/18 files   |
| Recovery            | folder + 100% clean restore.    | restored byte-for-byte; 0 FQ.    |
+─────────────────────┴─────────────────────────────────┴──────────────────────────────────+
```

Across an exhaustive testing suite of **126 automated unit and integration tests**, deterministic multi-seed benchmarks across 48 attack runs and 21 enterprise workloads, and full end-to-end recovery drills, EntroVault demonstrated:
- **Zero False Quarantines (0 FQ):** Complete preservation of legitimate enterprise workloads (media creation, archive compaction, database exports, and source code checkouts).
- **Sub-Second Containment:** Neutralization of weaponized ransomware at File 2 of 18 within 2.7 seconds of detonation.
- **Byte-for-Byte Restoration:** 100% pre-attack estate restoration on active baselines, leaving 0 encrypted artifacts on disk.
- **Decentralized Immutability:** Dual-mode blockchain logging combining EVM smart contracts with resilient offline SQLite fallback ledgers.

---

## 12.2 Critical Engineering Trade-offs and Lessons Learned

The design and implementation of EntroVault yielded five vital engineering insights regarding the realities of autonomous endpoint defense:

### 1. The Primacy of Zero False Quarantines over Unconstrained Detection
In academic literature, researchers routinely chase "100% detection accuracy" using aggressive machine learning models. However, our empirical findings (Chapter 9) revealed that while a Random Forest classifier achieves 100% detection recall, it induces **6 false quarantines** on benign photo imports and video writes. In enterprise IT, an EDR platform that autonomously locks corporate media assets causes an operational denial-of-service equivalent to ransomware. **Zero False Quarantine must remain an inviolable safety invariant**; deterministic behavioral rules must supersede statistical models when executing destructive containment.

### 2. Scientific Honesty Regarding Information-Theoretic Blindspots
Pure Shannon entropy possesses a physical limitation: it cannot differentiate between native compressed media (JPEGs, MP4s, ZIPs at $H approx.  7.4 - 7.8$) and symmetric ciphertext ($H approx.  7.95$) when encrypted in place without extension renaming. Rather than fabricating inflated claims or tuning thresholds into high false-positive territory, EntroVault openly documents the **image blindspot** as an inherent physical boundary of entropy analysis, establishing a benchmark for multi-signal fusion.

### 3. Multi-File Campaign Escalation vs. Isolated Per-File Triggers
Ransomware is intrinsically a multi-file campaign. Attempting to make irrevocable process termination decisions on a single file modification inevitably produces false positives or misses slow-crawling attacks. By introducing the **Campaign Escalation Tracker** with a 15-second sliding window, EntroVault allows the first suspicious file to raise an alert, and uses the second corroborating file to trigger immediate termination and sweep rollback. This correlates stealthy attacks operating at 1.5 ops/sec without risking single-file false alarms.

### 4. Strict Clean Backup Admission Control
Disaster recovery cannot be decoupled from threat detection. Standard continuous backup solutions blindly snapshot ciphertext, corrupting baseline catalogs. By enforcing strict file-type upper bounds (with zero tolerance margins) and differential jump caps ($\Delta H < 2.0$), EntroVault ensures that **corrupted files are never admitted into clean backup stores**, preserving restore integrity.

### 5. Resilient Dual-Mode Architectural Design
Academic blockchain solutions regularly fail under real-world conditions where malware disables network interfaces. EntroVault's dual-mode architecture—coupling Ganache EVM smart contracts with an autonomous SQLite fallback ledger—guarantees unbroken forensic continuity during offline network partitioning while preserving academic transparency via explicit mode labeling.

---

## 12.3 Production Hardening Roadmap: Kernel Drivers, eBPF, and Minifilters

While EntroVault provides a fully operational, industry-level purple-team laboratory, transitioning the architecture into a commercial enterprise endpoint agent requires migrating from userspace polling into operating system kernel drivers:

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|                    PRODUCTION KERNEL IMPLEMENTATION ROADMAP                              |
+─────────────────────┬─────────────────────────────────┬──────────────────────────────────+
| Architectural Phase | Target Engineering Technology   | Operational Benefit Achieved     |
+─────────────────────┼─────────────────────────────────┼──────────────────────────────────+
| Phase 1:            | Windows Minifilter Driver       | Synchronous pre-operation I/O    |
| Kernel Interception | (FltRegisterFilter) & Linux     | interception (IRP_MJ_CREATE);    |
|                     | eBPF (sys_enter_write tracep.)  | zero-delay PID handle trapping.  |
+─────────────────────┼─────────────────────────────────┼──────────────────────────────────+
| Phase 2:            | Magic-Byte Header Parsing &     | Complete elimination of the      |
| Structural Parsing  | Partial Incompressibility Tests | compressed media image blindspot |
|                     | (Fast Deflate Pass)             | without inducing false alarms.   |
+─────────────────────┼─────────────────────────────────┼──────────────────────────────────+
| Phase 3:            | Hardware SIMD Vectorization     | Sub-microsecond Shannon entropy  |
| Hardware AVX-512    | (Intel AVX-512 / ARM NEON)      | calculation across multi-gigabyte|
| Acceleration        |                                 | virtual disks and databases.     |
+─────────────────────┼─────────────────────────────────┼──────────────────────────────────+
| Phase 4:            | Production Consortium EVM       | Decentralized, multi-enterprise  |
| Consortium Ledger   | (Hyperledger Besu / Quorum with | threat exchange with automated   |
|                     | IBFT 2.0 Consensus)             | Byzantine quorum consensus.      |
+─────────────────────┴─────────────────────────────────┴──────────────────────────────────+
```

---

## 12.4 Concluding Remarks

Ransomware remains a formidable asymmetric threat, but it is not invulnerable. By exploiting an unavoidable physical characteristic of symmetric cryptography—the collapse of structured information into maximum Shannon entropy—and correlating behavioral transformations across temporal campaign windows, autonomous defense systems can detect and neutralize attacks at the earliest stages of execution.

EntroVault proves that proactive, host-based cryptoviral defense does not require sacrificing legitimate enterprise productivity to false alarms, nor does it require brittle signature feeds. Through rigorous mathematical modeling, strict disaster recovery engineering, and immutable decentralized forensic logging, EntroVault establishes a reproducible, production-grade paradigm for next-generation cyber resilience.

---


<div style="page-break-after: always;"></div>

# REFERENCES

[1] C. E. Shannon, "A mathematical theory of communication," *The Bell System Technical Journal*, vol. 27, no. 3, pp. 379–423, Jul. 1948.

[2] R. Lyda and J. Hamrock, "Using entropy analysis to find encrypted and packed malware," *IEEE Security & Privacy*, vol. 5, no. 2, pp. 40–45, Mar./Apr. 2007.

[3] N. Scaife, H. Carter, P. Traynor, and K. R. B. Butler, "CryptoLock (and Drop It): Stopping Ransomware at Endpoints," in *Proc. 36th IEEE Int. Conf. on Distributed Computing Systems (ICDCS)*, Nara, Japan, 2016, pp. 303–312.

[4] A. Continella, A. Guagnelli, F. Zingales, S. De Carli, M. Monga, and S. Zanero, "ShieldFS: A Self-healing, Ransomware-aware Filesystem," in *Proc. 32nd Annual Computer Security Applications Conf. (ACSAC)*, Los Angeles, CA, USA, 2016, pp. 336–347.

[5] A. Kharraz, W. Robertson, D. Balzarotti, L. Bilge, and E. Kirda, "UNVEIL: A Large-Scale, Automated Approach to Detecting Ransomware," in *Proc. 25th USENIX Security Symp. (USENIX Security 16)*, Austin, TX, USA, 2016, pp. 757–772.

[6] D. Sgandurra, L. Muñoz-González, R. Mohsen, and E. C. Lupu, "Automated dynamic analysis of ransomware: Benefits, limitations and use for detection," *arXiv preprint arXiv:1609.03020*, 2016.

[7] C. Wressnegger, F. Yamaguchi, A. Arp, and K. Rieck, "Comprehensive analysis of entropy-based malware detection," *ACM Transactions on Privacy and Security (TOPS)*, vol. 23, no. 2, pp. 1–32, 2020.

[8] T. McIntosh, A. Kayes, Y. P. P. Chen, A. Ng, and P. Watters, "Ransomware mitigation in the modern era: A comprehensive survey," *ACM Computing Surveys (CSUR)*, vol. 54, no. 9, pp. 1–36, 2021.

[9] National Institute of Standards and Technology (NIST), "Advanced Encryption Standard (AES)," *Federal Information Processing Standards Publication (FIPS PUB) 197*, Nov. 2001.

[10] National Institute of Standards and Technology (NIST), "Secure Hash Standard (SHS)," *Federal Information Processing Standards Publication (FIPS PUB) 180-4*, Aug. 2015.

[11] National Institute of Standards and Technology (NIST), "SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions," *Federal Information Processing Standards Publication (FIPS PUB) 202*, Aug. 2015.

[12] MITRE Corporation, "Data Encrypted for Impact: Technique T1486," *MITRE ATT&CK Enterprise Matrix*, 2024. [Online]. Available: https://attack.mitre.org/techniques/T1486/

[13] MITRE Corporation, "Inhibit System Recovery: Technique T1490," *MITRE ATT&CK Enterprise Matrix*, 2024. [Online]. Available: https://attack.mitre.org/techniques/T1490/

[14] MITRE Corporation, "Impair Defenses: Disable or Modify Tools: Technique T1562.001," *MITRE ATT&CK Enterprise Matrix*, 2024. [Online]. Available: https://attack.mitre.org/techniques/T1562/001/

[15] S. M. Lundberg and S.-I. Lee, "A unified approach to interpreting model predictions," in *Advances in Neural Information Processing Systems (NeurIPS 2017)*, Long Beach, CA, USA, 2017, pp. 4765–4774.

[16] V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Veness, M. G. Bellemare, et al., "Human-level control through deep reinforcement learning," *Nature*, vol. 518, no. 7540, pp. 529–533, Feb. 2015.

[17] L. Breiman, "Random Forests," *Machine Learning*, vol. 45, no. 1, pp. 5–32, Oct. 2001.

[18] S. Nakamoto, "Bitcoin: A Peer-to-Peer Electronic Cash System," Decentralized Business Review, 2008.

[19] V. Buterin, "A next-generation smart contract and decentralized application platform," *Ethereum White Paper*, vol. 3, no. 37, pp. 2–1, 2014.

[20] G. Liang, S. R. Weller, F. Luo, Z. Y. Dong, and J. Ma, "Distributed blockchain-based data protection framework for modern power systems," *IEEE Transactions on Smart Grid*, vol. 10, no. 3, pp. 3104–3113, 2018.

[21] M. Cebe, E. Erdin, K. Akkaya, H. Aksu, and S. Uluagac, "Block-4-filter: A blockchain-based framework for secure and trustable vehicle data forensics," *IEEE Internet of Things Journal*, vol. 5, no. 6, pp. 4330–4341, 2018.

[22] M. Castro and B. Liskov, "Practical Byzantine fault tolerance and proactive recovery," *ACM Transactions on Computer Systems (TOCS)*, vol. 20, no. 4, pp. 398–461, 2002.

[23] W. Meng, E. W. Tischhauser, Q. Wang, Y. Wang, and J. Han, "When intrusion detection meets blockchain technology: A review," *IEEE Access*, vol. 6, pp. 10179–10188, 2018.

[24] International Organization for Standardization, "Information technology — Security techniques — Guidelines for identification, collection, acquisition and preservation of digital evidence," *ISO/IEC Standard 27037:2012*, Oct. 2012.

[25] C. Adams, P. Cain, D. Pinkas, and R. Zuccherato, "Internet X.509 Public Key Infrastructure Time-Stamp Protocol (TSP)," *IETF Request for Comments (RFC) 3161*, Aug. 2001.

[26] P. Chen, S. C. Desmet, and C. D. Huygens, "A study on advanced ransomware detection using machine learning," in *Proc. 9th Int. Conf. on Dependable Systems and Networks*, 2018, pp. 112–121.

[27] R. Vinayakumar, K. Soman, K. S. Velan, and S. Ganorkar, "Evaluating shallow and deep learning models for ransomware detection," *IEEE Access*, vol. 7, pp. 78023–78040, 2019.

[28] K. Hampton, Z. Baig, and S. Zeadally, "Ransomware behavioral analysis on Windows endpoints," *Computers & Security*, vol. 93, p. 101789, 2020.

[29] S. Alam, S. Bhattacharya, and P. Sharma, "Reinforcement learning for endpoint detection and automated ransomware containment," in *Proc. IEEE Security and Privacy Workshops (SPW)*, 2021, pp. 204–213.

[30] C. Morato, M. Falcone, and S. Zanero, "Userspace file system event monitoring: Bottlenecks and optimization strategies," in *Proc. ACM Symposium on Applied Computing*, 2018, pp. 1654–1661.

[31] D. Boneh and V. Shoup, *A Graduate Course in Applied Cryptography*, Version 0.5, Stanford University, 2023.

[32] A. J. Menezes, P. C. van Oorschot, and S. A. Vanstone, *Handbook of Applied Cryptography*, CRC Press, 1996.

[33] R. S. Sutton and A. G. Barto, *Reinforcement Learning: An Introduction*, 2nd ed., MIT Press, Cambridge, MA, 2018.

[34] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, et al., "Scikit-learn: Machine learning in Python," *Journal of Machine Learning Research (JMLR)*, vol. 12, pp. 2825–2830, 2011.

[35] G. van Rossum and F. L. Drake, *Python 3 Reference Manual*, CreateSpace, Scotts Valley, CA, 2009.

[36] M. Grinberg, *Flask Web Development: Developing Web Applications with Python*, 2nd ed., O'Reilly Media, Sebastopol, CA, 2018.

[37] G. Giandomenico, "Watchdog: Python API and shell utilities to monitor file system events," *GitHub Repository*, 2023. [Online]. Available: https://github.com/gorakhargosh/watchdog

[38] G. Rodola, "psutil: Cross-platform process and system monitoring in Python," *GitHub Repository*, 2023. [Online]. Available: https://github.com/giampaolo/psutil

[39] Ethereum Foundation, "Web3.py: A Python interface for interacting with the Ethereum blockchain," *Ethereum Docs*, 2024. [Online]. Available: https://web3py.readthedocs.io/

[40] Truffle Suite, "Ganache: Personal Ethereum blockchain for development," *ConsenSys*, 2024. [Online]. Available: https://trufflesuite.com/ganache/

[41] D. R. Cox, *The Analysis of Binary Data*, Chapman and Hall, London, 1970.

[42] W. Feller, *An Introduction to Probability Theory and Its Applications*, vol. 1, 3rd ed., John Wiley & Sons, New York, 1968.

[43] J. L. Hodges and E. L. Lehmann, "The efficiency of some nonparametric competitors of the t-test," *The Annals of Mathematical Statistics*, vol. 27, no. 2, pp. 324–335, 1956.

[44] K. Pearson, "On the criterion that a given system of deviations from the probable in the case of a correlated system of variables is such that it can be reasonably supposed to have arisen from random sampling," *The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science*, vol. 50, no. 302, pp. 157–175, 1900.

[45] W. Hoeffding, "Probability inequalities for sums of bounded random variables," *Journal of the American Statistical Association*, vol. 58, no. 301, pp. 13–30, 1963.

[46] G. J. Woo, "Windows Internals, Part 1: System architecture, processes, threads, memory management, and more," 7th ed., Microsoft Press, Redmond, WA, 2017.

[47] R. Love, *Linux Kernel Development*, 3rd ed., Addison-Wesley Professional, Boston, MA, 2010.

[48] B. Gregg, *BPF Performance Tools: Deep Analysis and Solving Problems on OS and Applications*, Addison-Wesley Professional, 2019.

[49] G. Bertoni, J. Daemen, M. Peeters, and G. Van Assche, "The Keccak reference," *Submission to NIST (Round 3)*, 2011.

[50] R. C. Merkle, "A certified digital signature," in *Proc. Advances in Cryptology — CRYPTO '89*, Santa Barbara, CA, USA, 1989, pp. 218–238.

[51] I. Damgård, "A design principle for hash functions," in *Proc. Advances in Cryptology — CRYPTO '89*, Santa Barbara, CA, USA, 1989, pp. 416–427.

[52] D. E. Knuth, *The Art of Computer Programming, Volume 2: Seminumerical Algorithms*, 3rd ed., Addison-Wesley, Reading, MA, 1997.

---


<div style="page-break-after: always;"></div>

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
