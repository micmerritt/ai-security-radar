# AI Security Radar

_Last updated (UTC): **2026-08-02**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Piggybacking on Perception: Stealthy Concurrent Audio Prompt Injections against Multimodal LLM Agents**  
- **Date:** 2026-07-30
- **Authors:** Mingxiao Liu, Yitong Li, Haoren Zhao et al.
- **Link:** https://arxiv.org/abs/2607.28165v1
- **Security insight:** Large Language Model (LLM)-driven multimodal agents are increasingly deployed to execute autonomous tasks via continuous audio interaction. While this paradigm enhances interaction naturalness, it introduces a critical yet under-explored attack surface, as…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**GPT-Red: Automated Red Teaming via Self-Play at Scale**  
- **Date:** 2026-07-28
- **Authors:** Eric Wallace, Christopher A. Choquette-Choo, Nikhil Kandpal et al.
- **Link:** https://arxiv.org/abs/2607.26115v1
- **Security insight:** We introduce \textbf{GPT-Red}, an automated red-teaming agent that is trained to discover novel prompt injection attacks against frontier LLMs. The goal of this model is to evaluate and improve the robustness of our production systems. To this end, we use it…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**SafeFlow: Semantic Information-Flow Control for Blocking Malicious Propagation in Multi-Agent Systems**  
- **Date:** 2026-07-28
- **Authors:** Haowen Dai, Zonghao Ying, Wenfeng Li et al.
- **Link:** https://arxiv.org/abs/2607.25255v2
- **Security insight:** Multi-agent systems improve capability through task decomposition and role specialization, but these same mechanisms introduce an important safety blind spot: a harmful objective can be fragmented into locally plausible subtasks, allowing malicious intent to…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Agentic Permissions Policy Algebra for Taint Confinement in LLM Agents**  
- **Date:** 2026-07-27
- **Authors:** Arseny Kravchenko, Vadim Liventsev, Innokentii Konstantinov et al.
- **Link:** https://arxiv.org/abs/2607.24625v1
- **Security insight:** Autonomous LLM agents processing mixed-confidentiality data face severe security risks from prompt injection attacks and reasoning errors. While dynamic Information Flow Control (IFC) provides structural security guarantees, traditional taint tracking…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Just Testing, Move Along: Evasion of LLM-based System Log Interpretation by Prompt Injection**  
- **Date:** 2026-07-27
- **Authors:** Max Landauer, Florian Skopik, Markus Wurzenberger et al.
- **Link:** https://arxiv.org/abs/2607.24174v1
- **Security insight:** Large Language Models (LLMs) are increasingly integrated into Security Operations Center (SOC) workflows, where they support analysts in tasks such as the interpretation of system logs. However, the ability of LLMs to directly process untrusted textual input…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Agentic Cloud Decoys: A Deception-Driven Framework for Autonomous Intrusion Investigation**  
- **Date:** 2026-07-27
- **Authors:** Mohan Manivannan, Dalal Alharthi
- **Link:** https://arxiv.org/abs/2607.24006v1
- **Security insight:** Cloud telemetry arrives at a scale that, paradoxically, makes intrusion understanding harder rather than easier. Attackers operate through legitimate identity, federated session tokens, and cloud native APIs indistinguishable from routine administration, and…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**ContainmentBench: Trace-Based Evaluation of Post-Injection Containment in Tool-Using LLM Agents**  
- **Date:** 2026-07-27
- **Authors:** Wenhao Lan, Shan Li, Xinhua Lai et al.
- **Link:** https://arxiv.org/abs/2607.23999v2
- **Security insight:** Tool-using LLM agents process untrusted content, maintain memory, delegate across agents, and invoke side-effecting tools. Existing prompt-injection evaluations typically summarize security with terminal attack or policy outcomes, but equal endpoints can…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Are You Still the Agent I Authorized? Earned Authority under a Fixed Ceiling for Evolving Agents**  
- **Date:** 2026-07-26
- **Authors:** Zhaoxi Zhang, Xiaomei Zhang
- **Link:** https://arxiv.org/abs/2607.23586v1
- **Security insight:** Long-lived AI agents increasingly evolve after deployment by retaining experience, acquiring skills and tools, revising workflows, delegating work, and moving across task phases. This improves adaptation but creates a distinct authorization problem. Tool-…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Mission-Level Runtime Assurance for LLM-Assisted ISR Swarms over a Verification-Aware Fabric**  
- **Date:** 2026-07-26
- **Authors:** Nikolaos Kekatos, Stylianos Basagiannis, Panagiotis Katsaros et al.
- **Link:** https://arxiv.org/abs/2607.23532v1
- **Security insight:** Swarms of LLM-assisted autonomous robots are increasingly proposed for cooperative intelligence, surveillance, and reconnaissance (ISR) in contested environments. A growing class of their assurance failures arises not within any single platform but across the…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Poster: Rethinking Security in LLM Code Generation through Real-World Risk Scenarios**  
- **Date:** 2026-07-25
- **Authors:** Lixun Ma, Ruolong Ma, Bei Wang et al.
- **Link:** https://arxiv.org/abs/2607.23088v1
- **Security insight:** Large Language Models (LLMs) are widely used for code generation, yet their security behavior in realistic development workflows remains underexplored. Existing benchmarks often rely on explicitly specified security requirements, failing to capture real-world…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Agent Security Needs Redefinition through a Holistic Framework**  
- **Date:** 2026-07-24
- **Authors:** Vincent Siu, Jingxuan He, Kyle Montgomery et al.
- **Link:** https://arxiv.org/abs/2607.22024v1
- **Security insight:** Agent security is widely treated as a question about action content. Defenses ask whether an instruction looks malicious. Benchmarks ask whether an agent performs a harmful sounding action. \textbf{We argue that agent security is fundamentally a contextual…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Protocol-Level Attacks on Agentic Commerce Platforms: A Cross-Platform Taxonomy, AIP-Bench, and Unified Defense**  
- **Date:** 2026-07-23
- **Authors:** Yedidel Louck
- **Link:** https://arxiv.org/abs/2607.21824v1
- **Security insight:** Agentic commerce platforms let AI agents autonomously discover services, move payments, and wield user credentials on their users' behalf, and they already handle real money. Their security has so far been studied almost entirely at the level of the AI model,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Security of World-Model-Based Embodied AI: A Lifecycle of Threats, Defenses, and Evaluation**  
- **Date:** 2026-07-30
- **Authors:** Fazhong Liu, Zhuoyan Chen, Haozhen Tan et al.
- **Link:** https://arxiv.org/abs/2607.28226v1
- **Security insight:** World models give embodied AI a predictive core: they compress observations into states, simulate action-conditioned futures, and enable planning beyond reactive control. This predictive layer, however, opens a new security boundary-compromise can propagate…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### Other (Review)

**What AI Red-Team Evaluations Can and Cannot Prove**  
- **Date:** 2026-07-23
- **Authors:** Bandana Kaur
- **Link:** https://arxiv.org/abs/2607.21735v2
- **Security insight:** Red-team evaluations of AI models support some claims and not others, and the boundary between the two is calculable rather than merely a matter of judgment. We define the evidential ceiling of an evaluation as the largest factor by which one result can move…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
