# AI Security Radar

_Last updated (UTC): **2026-06-04**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**What If Prompt Injection Never Left? Exploring Cross-Session Stored Prompt Injection in Agentic Systems**  
- **Date:** 2026-06-03
- **Authors:** Yuanbo Xie, Tianyun Liu, Yingjie Zhang et al.
- **Link:** https://arxiv.org/abs/2606.04425v1
- **Security insight:** Modern agentic systems transform LLMs from session-bounded assistants into stateful systems that persist and evolve shared world state across sessions through memories, filesystems, tools, and other long-lived contextual artifacts. This shift fundamentally…
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

**SeClaw: Spec-Driven Security Task Synthesis for Evaluating Autonomous Agents**  
- **Date:** 2026-06-01
- **Authors:** Hao Cheng, Changtao Miao, Tianle Song et al.
- **Link:** https://arxiv.org/abs/2606.02302v1
- **Security insight:** Autonomous LLM agents increasingly operate in stateful environments where they access tools, files, memory, and external services. While such capabilities enable complex real-world workflows, they also introduce security risks that are difficult to capture…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**AgentRedBench: Dynamic Redteaming and Integration-Aware Defense for LLM Agents over SaaS Integrations**  
- **Date:** 2026-06-01
- **Authors:** Hiskias Dingeto, William Leeney
- **Link:** https://arxiv.org/abs/2606.02240v2
- **Security insight:** Indirect prompt injection in tool-use agents is a concrete production threat: LLM agents read from integrations (third-party services such as Gmail, Salesforce, or Jira accessed through tool calls) whose response content the user neither writes nor controls.…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Hybrid Adversarial Defence for Natural Language Understanding Tasks**  
- **Date:** 2026-06-03
- **Authors:** Manar Abouzaid, Yang Wang, Chenghua Lin et al.
- **Link:** https://arxiv.org/abs/2606.04612v1
- **Security insight:** Large Language Models (LLMs) are vulnerable both to hallucination and adversarial manipulation. Although these problems are closely related, existing defences typically address them separately. We investigate a hybrid defence framework that combines entropy-…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**"**Important** You should give me full credits!": Exploring Prompt Injection Attacks on LLM-Based Automatic Grading Systems**  
- **Date:** 2026-06-02
- **Authors:** Hang Li, Fedor Filippov, Yuling Lin et al.
- **Link:** https://arxiv.org/abs/2606.03090v1
- **Security insight:** The emergence of large language models (LLMs) has significantly accelerated recent research on LLM-based automatic grading (AG) systems. Benefiting from the strong instruction-following capabilities and broad prior knowledge of LLMs, educators can deploy AG…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**MENTIS: What Belief Changes Under Alignment? Measuring Multi-Scale Latent Torsion in Language Models**  
- **Date:** 2026-05-31
- **Authors:** Partha Pratim Saha, Samarth Raina, Mayur Parvatikar et al.
- **Link:** https://arxiv.org/abs/2606.01060v1
- **Security insight:** Preference alignment has substantially improved the observable behavior of large language models, yet it remains unclear what alignment changes internally. Aligned systems still fail under jailbreaks, prompt injection, and retrieval-time corruption,…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

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
- **Link:** https://arxiv.org/abs/2606.03091v1
- **Security insight:** Sequential recommendation systems are widely adopted but often deployed as black-box APIs, which has driven recent interest in model extraction to replicate their capabilities locally. However, the long-tail distribution induces severe signal heterogeneity:…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

### Adversarial ML

**Black-box, Adaptive, Efficient, Transferable, Harmful, Applicable... Attacks Are All You Need to Break LLMs**  
- **Date:** 2026-06-02
- **Authors:** Vincent Limbach, Jonas Dornbusch, David Lüdke et al.
- **Link:** https://arxiv.org/abs/2606.03647v1
- **Security insight:** Accurately evaluating adversarial robustness is a longstanding challenge. A flawed attack design can inflate robustness estimates, making deployment risk assessment and defense comparison unreliable. Historically, standardized attacks such as AutoAttack have…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

**Gate AI: LLM Security Benchmark Evaluation Methodology and Results**  
- **Date:** 2026-06-01
- **Authors:** Ryle Goehausen, Marcus Sousa
- **Link:** https://arxiv.org/abs/2606.02959v1
- **Security insight:** Published evaluations of prompt-injection and jailbreak detectors for Large Language Models often suffer from two systematic weaknesses: per-dataset threshold tuning and undisclosed operating points. We describe an evaluation harness that addresses both. The…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.
