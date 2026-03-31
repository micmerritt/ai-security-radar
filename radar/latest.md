# AI Security Radar

_Last updated (UTC): **2026-03-31**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Evaluating Privilege Usage of Agents on Real-World Tools**  
- **Date:** 2026-03-30
- **Authors:** Quan Zhang, Lianhang Fu, Lvsi Lian et al.
- **Link:** https://arxiv.org/abs/2603.28166v1
- **Security insight:** Equipping LLM agents with real-world tools can substantially improve productivity. However, granting agents autonomy over tool use also transfers the associated privileges to both the agent and the underlying LLM. Improper privilege usage may lead to serious…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Kill-Chain Canaries: Stage-Level Tracking of Prompt Injection Across Attack Surfaces and Model Safety Tiers**  
- **Date:** 2026-03-30
- **Authors:** Haochuan Kevin Wang
- **Link:** https://arxiv.org/abs/2603.28013v1
- **Security insight:** We present a stage-decomposed analysis of prompt injection attacks against five frontier LLM agents. Prior work measures task-level attack success rate (ASR); we localize the pipeline stage at which each model's defense activates. We instrument every run with…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**A Systematic Taxonomy of Security Vulnerabilities in the OpenClaw AI Agent Framework**  
- **Date:** 2026-03-29
- **Authors:** Surada Suwansathit, Yuxuan Zhang, Guofei Gu
- **Link:** https://arxiv.org/abs/2603.27517v1
- **Security insight:** AI agent frameworks connecting large language model (LLM) reasoning to host execution surfaces--shell, filesystem, containers, and messaging--introduce security challenges structurally distinct from conventional software. We present a systematic taxonomy of…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs**  
- **Date:** 2026-03-25
- **Authors:** Alexander Panfilov, Peter Romov, Igor Shilov et al.
- **Link:** https://arxiv.org/abs/2603.24511v1
- **Security insight:** LLM agents like Claude Code can not only write code but also be used for autonomous AI research and engineering \citep{rank2026posttrainbench, novikov2025alphaevolve}. We show that an \emph{autoresearch}-style pipeline \citep{karpathy2026autoresearch} powered…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Invisible Threats from Model Context Protocol: Generating Stealthy Injection Payload via Tree-based Adaptive Search**  
- **Date:** 2026-03-25
- **Authors:** Yulin Shen, Xudong Pan, Geng Hong et al.
- **Link:** https://arxiv.org/abs/2603.24203v1
- **Security insight:** Recent advances in the Model Context Protocol (MCP) have enabled large language models (LLMs) to invoke external tools with unprecedented ease. This creates a new class of powerful and tool augmented agents. Unfortunately, this capability also introduces an…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Crossing the NL/PL Divide: Information Flow Analysis Across the NL/PL Boundary in LLM-Integrated Code**  
- **Date:** 2026-03-30
- **Authors:** Zihao Xu, Xiao Cheng, Ruijie Meng et al.
- **Link:** https://arxiv.org/abs/2603.28345v1
- **Security insight:** LLM API calls are becoming a ubiquitous program construct, yet they create a boundary that no existing program analysis can cross: runtime values enter a natural-language prompt, undergo opaque processing inside the LLM, and re-emerge as code, SQL, JSON, or…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Hidden Ads: Behavior Triggered Semantic Backdoors for Advertisement Injection in Vision Language Models**  
- **Date:** 2026-03-29
- **Authors:** Duanyi Yao, Changyue Li, Zhicong Huang et al.
- **Link:** https://arxiv.org/abs/2603.27522v1
- **Security insight:** Vision-Language Models (VLMs) are increasingly deployed in consumer applications where users seek recommendations about products, dining, and services. We introduce Hidden Ads, a new class of backdoor attacks that exploit this recommendation-seeking behavior…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Prompt Attack Detection with LLM-as-a-Judge and Mixture-of-Models**  
- **Date:** 2026-03-26
- **Authors:** Hieu Xuan Le, Benjamin Goh, Quy Anh Tang
- **Link:** https://arxiv.org/abs/2603.25176v1
- **Security insight:** Prompt attacks, including jailbreaks and prompt injections, pose a critical security risk to Large Language Model (LLM) systems. In production, guardrails must mitigate these attacks under strict low-latency constraints, resulting in a deployment gap in which…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**PIDP-Attack: Combining Prompt Injection with Database Poisoning Attacks on Retrieval-Augmented Generation Systems**  
- **Date:** 2026-03-26
- **Authors:** Haozhen Wang, Haoyue Liu, Jionghao Zhu et al.
- **Link:** https://arxiv.org/abs/2603.25164v1
- **Security insight:** Large Language Models (LLMs) have demonstrated remarkable performance across a wide range of applications. However, their practical deployment is often hindered by issues such as outdated knowledge and the tendency to generate hallucinations. To address these…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**Poisoning the Genome: Targeted Backdoor Attacks on DNA Foundation Models**  
- **Date:** 2026-03-29
- **Authors:** Charalampos Koilakos, Ioannis Mouratidis, Ilias Georgakopoulos-Soares
- **Link:** https://arxiv.org/abs/2603.27465v1
- **Security insight:** Genomic foundation models trained on DNA sequences have demonstrated remarkable capabilities across diverse biological tasks, from variant effect prediction to genome design. These models are typically trained on massive, publicly sourced genomic datasets…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**AI Security in the Foundation Model Era: A Comprehensive Survey from a Unified Perspective**  
- **Date:** 2026-03-25
- **Authors:** Zhenyi Wang, Siyu Luan
- **Link:** https://arxiv.org/abs/2603.24857v1
- **Security insight:** As machine learning (ML) systems expand in both scale and functionality, the security landscape has become increasingly complex, with a proliferation of attacks and defenses. However, existing studies largely treat these threats in isolation, lacking a…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Poisoning & Backdoors

**On the Vulnerability of Deep Automatic Modulation Classifiers to Explainable Backdoor Threats**  
- **Date:** 2026-03-26
- **Authors:** Younes Salmi, Hanna Bogucka
- **Link:** https://arxiv.org/abs/2603.25310v1
- **Security insight:** Deep learning (DL) has been widely studied for assisting applications of modern wireless communications. One of the applications is automatic modulation classification (AMC). However, DL models are found to be vulnerable to adversarial machine learning (AML)…
- **Build idea:** Build a minimal poisoning simulator plus simple detectors (trigger search, label flip tests, anomaly baselines).

**Physical Backdoor Attack Against Deep Learning-Based Modulation Classification**  
- **Date:** 2026-03-26
- **Authors:** Younes Salmi, Hanna Bogucka
- **Link:** https://arxiv.org/abs/2603.25304v1
- **Security insight:** Deep Learning (DL) has become a key technology that assists radio frequency (RF) signal classification applications, such as modulation classification. However, the DL models are vulnerable to adversarial machine learning threats, such as data manipulation…
- **Build idea:** Build a minimal poisoning simulator plus simple detectors (trigger search, label flip tests, anomaly baselines).

### Model Extraction & Privacy

**A Public Theory of Distillation Resistance via Constraint-Coupled Reasoning Architectures**  
- **Date:** 2026-03-26
- **Authors:** Peng Wei, Wesley Shu
- **Link:** https://arxiv.org/abs/2603.25022v1
- **Security insight:** Knowledge distillation, model extraction, and behavior transfer have become central concerns in frontier AI. The main risk is not merely copying, but the possibility that useful capability can be transferred more cheaply than the governance structure that…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?
