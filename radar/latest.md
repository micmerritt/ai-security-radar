# AI Security Radar

_Last updated (UTC): **2026-07-28**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

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
- **Link:** https://arxiv.org/abs/2607.23999v1
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

**Encoding Invisible Causation for Bridge Diagnostic Agents: Triple-Guided Retrieval-Augmented Fine-Tuning with QLoRA**  
- **Date:** 2026-07-23
- **Authors:** Takato Yasuno
- **Link:** https://arxiv.org/abs/2607.21680v1
- **Security insight:** Bridge infrastructure deteriorates gradually, yet its root causes---salt intrusion, freezing, fatigue cracking, and others---remain invisible to the naked eye. Expert diagnosis relies on tacit knowledge built over years of practice. We address the challenge…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**The Ethics of Autonomous AI Agents for Offensive Security**  
- **Date:** 2026-07-22
- **Authors:** Andreas Happe, Jürgen Cito, Jasmin Wachter
- **Link:** https://arxiv.org/abs/2607.20255v1
- **Security insight:** LLM-driven autonomous agents are reshaping offensive security. Unlike traditional penetration-testing tooling -- deterministic, narrowly scoped, and operated by trained practitioners -- agentic security tools exhibit \textit{indeterminacy} along three…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Know Your Agent: Reconnaissance-Driven Pentesting of AI Agents**  
- **Date:** 2026-07-22
- **Authors:** Or Zion Eliav, Eyal Lenga, Shir Bernstien et al.
- **Link:** https://arxiv.org/abs/2607.19837v1
- **Security insight:** Traditional pentesting uses reconnaissance at each step to uncover unseen weaknesses, build stronger attacks, and advance the objective; we argue that AI agents require the same treatment. We formalize agent reconnaissance by modeling the process and…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**V-DEAL: Diagnosing Video Safety De-Calibration as an Understanding-Refusal Coupling Failure**  
- **Date:** 2026-07-23
- **Authors:** Zhetong Zhang, Honghao Fu, Miao Xu et al.
- **Link:** https://arxiv.org/abs/2607.21151v2
- **Security insight:** As Video Large Language Models are increasingly deployed in real-world applications, ensuring their safety alignment has become critical. Counterintuitively, we find that harmful videos paired with benign queries achieve higher attack success rates than the…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### Other (Review)

**What AI Red-Team Evaluations Can and Cannot Prove**  
- **Date:** 2026-07-23
- **Authors:** Bandana Kaur
- **Link:** https://arxiv.org/abs/2607.21735v1
- **Security insight:** Red-team evaluations of AI models support some claims and not others, and the boundary between the two is calculable rather than merely a matter of judgment. We define the evidential ceiling of an evaluation as the largest factor by which one result can move…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
