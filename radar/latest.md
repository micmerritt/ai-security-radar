# AI Security Radar

_Last updated (UTC): **2026-09-10**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

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

**From Review to Authorization: Key-Isolated Threshold Signing for LLM Agents**  
- **Date:** 2026-09-05
- **Authors:** Yu Zheng, Qizhi Zhang
- **Link:** https://arxiv.org/abs/2609.05901v1
- **Security insight:** Autonomous LLM agents can turn untrusted content into effectful actions such as payments and permission changes. If the same process interprets this content and controls a reusable signing credential, prompt injection can cross the judgment boundary and reach…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**CONTINUITY: Security-Context Contracts for Composable LLM Agent Controls**  
- **Date:** 2026-09-04
- **Authors:** Chris Zheng, Geng Yang
- **Link:** https://arxiv.org/abs/2609.05269v1
- **Security insight:** LLM agent systems increasingly combine provenance tracking, authorization, policy enforcement, protocol adapters, and execution controls. However, individually correct security mechanisms do not necessarily compose into an end-to-end secure system: security-…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Repeat-After-Me: Black-Box Adaptive Visual Prompt Injection**  
- **Date:** 2026-09-03
- **Authors:** Sizhe Chen, Yu-Lin Tsai, Ivan Evtimov et al.
- **Link:** https://arxiv.org/abs/2609.04533v1
- **Security insight:** Prompt injection is widely recognized as a major security threat to AI agents that interact with untrusted external data, such as websites, documents, and emails. Prior work has shown that, in the text domain, black-box prompt injection can achieve near-…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Towards a Resilience-Theoretic Foundation for Adversarial Robustness in Industrial Control System Anomaly Detection**  
- **Date:** 2026-09-07
- **Authors:** Branka Stojanović, Andreas Flatscher, Michael Somma
- **Link:** https://arxiv.org/abs/2609.07244v1
- **Security insight:** Anomaly-based intrusion detection systems in industrial control systems (ICS) and operational technology (OT) environments are increasingly required to meet formal resilience criteria: absorbed adversarial disturbances, graceful degradation under sustained…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Hierarchical Prompt Injector for Domain Generalization Segmentation**  
- **Date:** 2026-09-05
- **Authors:** Xin Kun Lin, Ruoyu Guo, Jiaqi Guo et al.
- **Link:** https://arxiv.org/abs/2609.05864v1
- **Security insight:** Domain Generalized Semantic Segmentation (DGSS) is a challenging task, as vision models often rely on low-level appearance cues that change across domains. In contrast, structural attributes exhibit cross-domain stability, motivating the use of structural…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Influence Score and Transformers interpretability: Measure of the Effective Impact of Attention Heads at inference time**  
- **Date:** 2026-09-04
- **Authors:** Lisa Bouger, Yannick Teglia, Philippe Loubet Moundi
- **Link:** https://arxiv.org/abs/2609.05074v1
- **Security insight:** We propose an influence score to quantify the contribution of attention heads to classification decisions in Transformer-based models designed for prompt injection detection. The score combines directional influence on the logits with structural contribution…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.
