# AI Security Radar

_Last updated (UTC): **2026-06-03**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

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

**From Prompt Injection to Persistent Control: Defending Agentic Harness Against Trojan Backdoors**  
- **Date:** 2026-05-29
- **Authors:** Jiejun Tan, Zhicheng Dou, Xinyu Yang et al.
- **Link:** https://arxiv.org/abs/2605.31042v1
- **Security insight:** LLM agents are evolving from conversational chatbots to operational tools in real-world workspaces. In local agentic harnesses, an LLM can read and write files, call tools, and reuse workspace state across sessions. While such capabilities enhance utility,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Send a SCOUT First: Pre-hoc Reasoning for Adaptive Detector Allocation in Prompt-Injection Defense**  
- **Date:** 2026-05-29
- **Authors:** Shuhao Zhang, Jiarui Li, Qi Cao et al.
- **Link:** https://arxiv.org/abs/2605.30837v1
- **Security insight:** Prompt-injection detectors are heterogeneous: each is strong on a different slice of attacks, and none is always reliable. Yet existing systems still treat detection as a fixed single-detector pipeline, committing every request to one detector's blind spots.…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

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

**Confused ChatGPT: Cross-App Context Poisoning via First-Party APIs**  
- **Date:** 2026-05-30
- **Authors:** Chao Wang, Somesh Jha, Zhiqiang Lin
- **Link:** https://arxiv.org/abs/2606.00485v1
- **Security insight:** ChatGPT Apps, launched by OpenAI on Oct. 6, 2025, introduce an app-in-app paradigm in which third-party applications share a single chat context with the user and with every other connected app. The ecosystem grew from 122 apps in Dec. 2025 to 888 by May…
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

**A Registry-Bound LLM Pipeline for Evidence-Grounded Trait Extraction across Tropical Plants, Aquatic Species, and Exotic Pets**  
- **Date:** 2026-05-31
- **Authors:** Jeff Wang
- **Link:** https://arxiv.org/abs/2606.00994v1
- **Security insight:** We describe a registry-bound large-language-model extraction pipeline producing evidence-grounded structured trait records at scale, on cultivated tropical plant, aquatic, and pet species. Four mechanisms render LLM-derived rows auditable: a versioned 39-key…
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
