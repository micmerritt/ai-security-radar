# AI Security Radar

_Last updated (UTC): **2026-06-07**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Insurance of Agentic AI**  
- **Date:** 2026-06-03
- **Authors:** Quanyan Zhu
- **Link:** https://arxiv.org/abs/2606.05449v1
- **Security insight:** Agentic artificial intelligence (AI) systems are transforming the risk landscape by extending beyond information generation to autonomous planning, tool invocation, decision execution, and persistent modification of digital and physical environments. These…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**What If Prompt Injection Never Left? Exploring Cross-Session Stored Prompt Injection in Agentic Systems**  
- **Date:** 2026-06-03
- **Authors:** Yuanbo Xie, Tianyun Liu, Yingjie Zhang et al.
- **Link:** https://arxiv.org/abs/2606.04425v1
- **Security insight:** Modern agentic systems transform LLMs from session-bounded assistants into stateful systems that persist and evolve shared world state across sessions through memories, filesystems, tools, and other long-lived contextual artifacts. This shift fundamentally…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Domain-Conditioned Safety in Frontier Computer-Using Agents: A 793-Episode Browser Benchmark, a Coding-Domain Cross-Reference, and a Reproducibility Audit of Recent Red-Teaming**  
- **Date:** 2026-06-03
- **Authors:** Nicholas Saban
- **Link:** https://arxiv.org/abs/2606.05233v1
- **Security insight:** Recent computer-using-agent (CUA) red-teaming papers report prompt-injection attack success rates (ASR) of 42-98%, but these headline numbers cluster on retired models and on the most-vulnerable model in each paper's panel. We ask whether those techniques,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents**  
- **Date:** 2026-06-03
- **Authors:** Pritam Dash, Tongyu Ge, Aditi Jain et al.
- **Link:** https://arxiv.org/abs/2606.04329v1
- **Security insight:** Memory is a core component of AI agents, enabling them to accumulate knowledge across interactions and improve performance. However, persistent memory introduces the risk of memory poisoning, where a single adversarial memory write can exert long-term…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Caught in the Act(ivation): Toward Pre-Output and Multi-Turn Detection of Credential Exfiltration by LLM Agents**  
- **Date:** 2026-06-02
- **Authors:** Kargi Chauhan, Pratibha Revankar
- **Link:** https://arxiv.org/abs/2606.04141v1
- **Security insight:** LLM agents often place sensitive credentials in the same context window as untrusted retrieved content, creating a direct path for indirect prompt injection to induce credential exfiltration. We study this failure mode through three complementary defenses.…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**From Control Boundary to Insurance Claim: Reconstructing AI-Mediated Losses Through the CER Framework**  
- **Date:** 2026-06-02
- **Authors:** Alex Leung, Rex Zhang, Kentaroh Toyoda et al.
- **Link:** https://arxiv.org/abs/2606.03777v1
- **Security insight:** AI losses that arise through an insured organization's generative or agentic AI system require state reconstruction, not merely event reconstruction, because the relevant state changes as the system reasons, retrieves, calls tools, and acts. The relevant…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**GuardNet: Ensemble Strategies of Shallow Neural Networks for Robust Prompt Injection and Jailbreak Detection**  
- **Date:** 2026-06-04
- **Authors:** Paulo Ricardo Ferreira Neves, Edson Rodrigues da Cruz Filho, Paulo Henrique Eleuterio Falsetti et al.
- **Link:** https://arxiv.org/abs/2606.05566v1
- **Security insight:** Large Language Models (LLMs) have transformed natural language processing, but they remain vulnerable to Prompt Injection (PI) and Jailbreak (JB) attacks. In addition, benchmark evaluations may be affected by contamination and partial information leakage,…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Hybrid Adversarial Defence for Natural Language Understanding Tasks**  
- **Date:** 2026-06-03
- **Authors:** Manar Abouzaid, Yang Wang, Chenghua Lin et al.
- **Link:** https://arxiv.org/abs/2606.04612v1
- **Security insight:** Large Language Models (LLMs) are vulnerable both to hallucination and adversarial manipulation. Although these problems are closely related, existing defences typically address them separately. We investigate a hybrid defence framework that combines entropy-…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**An Embarrassingly Simple Detector for Model Extraction Attacks in Large Language Model API Traffic**  
- **Date:** 2026-06-04
- **Authors:** Shuze Liu, Qianwen Guo, Yushun Dong
- **Link:** https://arxiv.org/abs/2606.05725v1
- **Security insight:** Large language models (LLMs) are increasingly deployed through hosted APIs, making model extraction a practical threat to model ownership and service security. However, individual extraction queries often resemble benign requests, and existing evaluations…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Poisoning & Backdoors

**FlowGuard: Flow Matching for Identity-Independent Detection of Data-Free Model Stealing Attacks on Energy System Intrusion Detection Systems**  
- **Date:** 2026-06-02
- **Authors:** Maxime Schwarzer, Laurin Holz, Tobias Huerten et al.
- **Link:** https://arxiv.org/abs/2606.03430v1
- **Security insight:** Artificial Intelligence (AI)-based Intrusion Detection Systems (IDS) deployed in energy infrastructure are vulnerable to model theft attacks, which allow adversaries to create evasive traffic offline. Current defences against model extraction rely either on…
- **Build idea:** Build a minimal poisoning simulator plus simple detectors (trigger search, label flip tests, anomaly baselines).

### Model Extraction & Privacy

**AI Model Extraction Attacks: Bypassing Single-Client Assumptions in Defenses**  
- **Date:** 2026-06-02
- **Authors:** Maxime Schwarzer, Johannes F. Loevenich, Gustavo Sánchez et al.
- **Link:** https://arxiv.org/abs/2606.03381v1
- **Security insight:** Ensuring the protection of Artificial Intelligence (AI) models deployed in military Command and Control (C2) systems and critical infrastructure is essential for maintaining information superiority. Model Extraction Attacks (MEAs) pose a significant threat,…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

**BAHSD: Bridging the Long-tail Gap via Adaptive Distillation in Black-box Sequential Recommendation**  
- **Date:** 2026-06-02
- **Authors:** Xi Zhou, Famin Wu, Mingming Li et al.
- **Link:** https://arxiv.org/abs/2606.03091v2
- **Security insight:** Sequential recommendation systems are widely adopted but often deployed as black-box APIs, which has driven recent interest in model extraction to replicate their capabilities locally. However, the long-tail distribution induces severe signal heterogeneity:…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

### Adversarial ML

**Black-box, Adaptive, Efficient, Transferable, Harmful, Applicable... Attacks Are All You Need to Break LLMs**  
- **Date:** 2026-06-02
- **Authors:** Vincent Limbach, Jonas Dornbusch, David Lüdke et al.
- **Link:** https://arxiv.org/abs/2606.03647v1
- **Security insight:** Accurately evaluating adversarial robustness is a longstanding challenge. A flawed attack design can inflate robustness estimates, making deployment risk assessment and defense comparison unreliable. Historically, standardized attacks such as AutoAttack have…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

### Other (Review)

**Safety Paradox: How Enhanced Safety Awareness Leaves LLMs Vulnerable to Posterior Attack**  
- **Date:** 2026-06-04
- **Authors:** Long P. Hoang, Hai V. Le, Shaoyang Xu et al.
- **Link:** https://arxiv.org/abs/2606.05614v1
- **Security insight:** Large language models (LLMs) are rigorously aligned to refuse harmful requests, a process that inherently cultivates a latent capacity to evaluate and recognize unsafe content. In this work, we reveal that this advanced safety awareness inadvertently…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
