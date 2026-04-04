# AI Security Radar

_Last updated (UTC): **2026-04-04**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**ClawSafety: "Safe" LLMs, Unsafe Agents**  
- **Date:** 2026-04-01
- **Authors:** Bowen Wei, Yunbei Zhang, Jinhao Pan et al.
- **Link:** https://arxiv.org/abs/2604.01438v1
- **Security insight:** Personal AI agents like OpenClaw run with elevated privileges on users' local machines, where a single successful prompt injection can leak credentials, redirect financial transactions, or destroy files. This threat goes well beyond conventional text-level…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Safety, Security, and Cognitive Risks in World Models**  
- **Date:** 2026-04-01
- **Authors:** Manoj Parmar
- **Link:** https://arxiv.org/abs/2604.01346v1
- **Security insight:** World models -- learned internal simulators of environment dynamics -- are rapidly becoming foundational to autonomous decision-making in robotics, autonomous vehicles, and agentic AI. Yet this predictive power introduces a distinctive set of safety,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**AgentWatcher: A Rule-based Prompt Injection Monitor**  
- **Date:** 2026-04-01
- **Authors:** Yanting Wang, Wei Zou, Runpeng Geng et al.
- **Link:** https://arxiv.org/abs/2604.01194v1
- **Security insight:** Large language models (LLMs) and their applications, such as agents, are highly vulnerable to prompt injection attacks. State-of-the-art prompt injection detection methods have the following limitations: (1) their effectiveness degrades significantly as…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Architecting Secure AI Agents: Perspectives on System-Level Defenses Against Indirect Prompt Injection Attacks**  
- **Date:** 2026-03-31
- **Authors:** Chong Xiang, Drew Zagieboylo, Shaona Ghosh et al.
- **Link:** https://arxiv.org/abs/2603.30016v1
- **Security insight:** AI agents, predominantly powered by large language models (LLMs), are vulnerable to indirect prompt injection, in which malicious instructions embedded in untrusted data can trigger dangerous agent actions. This position paper discusses our vision for system-…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

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

**SafeClaw-R: Towards Safe and Secure Multi-Agent Personal Assistants**  
- **Date:** 2026-03-28
- **Authors:** Haoyu Wang, Zibo Xiao, Yedi Zhang et al.
- **Link:** https://arxiv.org/abs/2603.28807v1
- **Security insight:** LLM-based multi-agent systems (MASs) are transforming personal productivity by autonomously executing complex, cross-platform tasks. Frameworks such as OpenClaw demonstrate the potential of locally deployed agents integrated with personal data and services,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Adversarial Prompt Injection Attack on Multimodal Large Language Models**  
- **Date:** 2026-03-31
- **Authors:** Meiwen Ding, Song Xia, Chenqi Kong et al.
- **Link:** https://arxiv.org/abs/2603.29418v1
- **Security insight:** Although multimodal large language models (MLLMs) are increasingly deployed in real-world applications, their instruction-following behavior leaves them vulnerable to prompt injection attacks. Existing prompt injection methods predominantly rely on textual…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

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

### RAG & Retrieval Attacks

**Poisoning the Genome: Targeted Backdoor Attacks on DNA Foundation Models**  
- **Date:** 2026-03-29
- **Authors:** Charalampos Koilakos, Ioannis Mouratidis, Ilias Georgakopoulos-Soares
- **Link:** https://arxiv.org/abs/2603.27465v1
- **Security insight:** Genomic foundation models trained on DNA sequences have demonstrated remarkable capabilities across diverse biological tasks, from variant effect prediction to genome design. These models are typically trained on massive, publicly sourced genomic datasets…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Model Extraction & Privacy

**Loop-Checking and Counter-Model Extraction for Intuitionistic Tense Logics via Nested Sequents**  
- **Date:** 2026-03-31
- **Authors:** Tim S. Lyon
- **Link:** https://arxiv.org/abs/2603.29424v1
- **Security insight:** This paper develops a novel nested sequent proof-search methodology for intuitionistic tense logics (ITLs), supporting finite counter-model extraction. We introduce a new loop-checking method that detects repeating nested sequents using homomorphisms, thereby…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

### Adversarial ML

**Performative Scenario Optimization**  
- **Date:** 2026-03-31
- **Authors:** Quanyan Zhu, Zhengye Han
- **Link:** https://arxiv.org/abs/2603.29982v1
- **Security insight:** This paper introduces a performative scenario optimization framework for decision-dependent chance-constrained problems. Unlike classical stochastic optimization, we account for the feedback loop where decisions actively shape the underlying data-generating…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.
