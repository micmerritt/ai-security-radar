# AI Security Radar

_Last updated (UTC): **2026-09-12**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**The Agent Incident Registry: Toward Preventing Repeated AI Agent Failures**  
- **Date:** 2026-09-10
- **Authors:** Divyanshu Kumar, Rohith HN, Nitin Aravind Birur et al.
- **Link:** https://arxiv.org/abs/2609.11030v1
- **Security insight:** AI agents increasingly act through tools and delegated authority, but general incident repositories rarely capture the mechanisms needed to compare public failures with agent-security evaluations. We present the Agent Incident Registry (AIR), a source-linked…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**DriftNet: A Dual-Head Trajectory Transformer for Detecting and Localizing Prompt Injection in LLM Agents**  
- **Date:** 2026-09-09
- **Authors:** Asif Pinjari, Mithun Paul Saint-Germain
- **Link:** https://arxiv.org/abs/2609.10892v1
- **Security insight:** When an indirect prompt injection succeeds against an LLM agent, the compromise is visible in the agent's own behavior: a benign prefix of tool calls, a poisoned observation, and a suffix of actions that serve the attacker. An operator needs three facts:…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**No-Box Vulnerability Analysis: Description-only Detection of Indirect Prompt Injection Vulnerabilities in MCP Servers**  
- **Date:** 2026-09-09
- **Authors:** Zehua Zhang, Jie Hu, Pratham Hegde et al.
- **Link:** https://arxiv.org/abs/2609.10854v1
- **Security insight:** Conventional vulnerability analysis relies on either system access or dynamic interaction, all of which may be unavailable to third-party analysts auditing closed-source, remotely hosted, critical in situ systems, or commercially gated software. Therefore, we…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Kernel-Managed Shared Memory for System-Wide Personalization**  
- **Date:** 2026-09-09
- **Authors:** Ryan Lum, Yongfeng Zhang
- **Link:** https://arxiv.org/abs/2609.10144v1
- **Security insight:** AI systems become more useful when they can adapt to the people using them, but in multi-agent systems, useful context learned by one agent often remains unavailable to others. We present kernel-managed shared memory, a system-level abstraction in which…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**An Experimental Evaluation of Multimodal Prompt Injection Attacks on Agentic AI Frameworks**  
- **Date:** 2026-09-08
- **Authors:** Viet K. Nguyen, Mohammad I. Husain
- **Link:** https://arxiv.org/abs/2609.09404v1
- **Security insight:** Agentic AI frameworks let a language model plan, keep memory, and call tools that reach real files, mail, and services. Most of these agents also read images, which gives an attacker a way to put text into the agent's context without going through the user.…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Authority Is Not a String: A Capability-Scoped Harness for Prompt-Injection-Resistant Coding Agents**  
- **Date:** 2026-09-08
- **Authors:** Dimitrios Stamatios Bouras, Yihan Dai, Sergey Mechtaev
- **Link:** https://arxiv.org/abs/2609.08371v1
- **Security insight:** Coding agents use system-level tools to read files, execute commands, and modify source code. Within the agent's sandbox, these tools often carry ambient authority: naming a resource is sufficient to act on it. Indirect prompt injection exploits this…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**CoRL: Co-Evolutionary Reinforcement Learning for Adaptive Indirect Prompt-Injection Attacks and Defenses**  
- **Date:** 2026-09-07
- **Authors:** Boyang Zhang, Qingxin Xiao, Lingwei Dang et al.
- **Link:** https://arxiv.org/abs/2609.07529v1
- **Security insight:** Tool-augmented language agents are vulnerable to indirect prompt injection (IPI). Unlike direct prompt injection, IPI hides adversarial instructions in untrusted tool outputs and can covertly alter the execution of a legitimate task. Defenses trained on fixed…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**AgentDrift: A Step-Labeled Benchmark of Injection-Hijacked LLM Agent Trajectories**  
- **Date:** 2026-09-07
- **Authors:** Asif Pinjari, Mithun Paul Saint-Germain
- **Link:** https://arxiv.org/abs/2609.06972v1
- **Security insight:** LLM agents complete tasks by issuing sequences of tool calls, and every observation they read is a channel through which an indirect prompt injection can enter. A successful injection has a characteristic shape when the trajectory is read in order: a benign…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**MOLE: Detecting Insider Threats in AI Agents**  
- **Date:** 2026-09-07
- **Authors:** Aashiq Muhamed, Virginia Smith
- **Link:** https://arxiv.org/abs/2609.06966v1
- **Security insight:** Model misalignment, prompt injection, or operator misuse could lead AI agents operating frontier-lab accounts to exfiltrate model weights, poison training data, or weaken release gates. Existing benchmarks do not test whether defenders can detect this…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**SWE-Test: Benchmarking LLM Vulnerability Discovery via Input Prediction**  
- **Date:** 2026-09-05
- **Authors:** Yuanxiang Shi, Jiayi Lin, Xuanyong Lin et al.
- **Link:** https://arxiv.org/abs/2609.06229v1
- **Security insight:** Vulnerability discovery is becoming an important ability of large language model (LLM) agents: agents that silently miss real defects leave critical software exposed. Rigorously measuring this ability is therefore urgent, but existing benchmarks are gameable…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**EvoSafeHarness: Evolving Model- and Domain-Specific Harnesses for Securing Agents**  
- **Date:** 2026-09-05
- **Authors:** Nanxi Li, Yingzi Ma, Yulong Cao et al.
- **Link:** https://arxiv.org/abs/2609.05903v1
- **Security insight:** Large Language Model (LLM) agents are turning language into real-world effects, making safety necessary against both indirect prompt injections and direct harmful requests. System-level safety harnesses add an enforcement layer beyond model-level defenses,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Architecting the Secure AI-SOC: A Neurosymbolic Framework for Pipeline Integrity and Threat Mitigation**  
- **Date:** 2026-09-09
- **Authors:** Anna Gazani, Spyridon Kounoupidis, Panagiotis Katsaros et al.
- **Link:** https://arxiv.org/abs/2609.10707v1
- **Security insight:** The integration of Large Language Models (LLMs) into Security Operations Centers (SOCs) streamlines threat intelligence but introduces critical vulnerabilities, notably indirect prompt injection via log poisoning. Adversaries exploit this vector to execute…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Towards a Resilience-Theoretic Foundation for Adversarial Robustness in Industrial Control System Anomaly Detection**  
- **Date:** 2026-09-07
- **Authors:** Branka Stojanović, Andreas Flatscher, Michael Somma
- **Link:** https://arxiv.org/abs/2609.07244v1
- **Security insight:** Anomaly-based intrusion detection systems in industrial control systems (ICS) and operational technology (OT) environments are increasingly required to meet formal resilience criteria: absorbed adversarial disturbances, graceful degradation under sustained…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### Model Extraction & Privacy

**SoK: Privacy Attacks on Machine Learning via Explainable AI**  
- **Date:** 2026-09-09
- **Authors:** Abdullah Caglar Oksuz, Anisa Halimi, Erman Ayday
- **Link:** https://arxiv.org/abs/2609.10627v1
- **Security insight:** Machine learning explanations reveal model behavior beyond predictions, creating attack surfaces for model confidentiality and data privacy. We systematize 25 studies that exploit explanations for model extraction, membership inference, and model inversion,…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?
