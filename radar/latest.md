# AI Security Radar

_Last updated (UTC): **2026-07-07**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Untrusted Content Masking for Web Agents with Security Guarantees**  
- **Date:** 2026-07-06
- **Authors:** Kristina Nikolić, Egor Zverev, Javier Rando et al.
- **Link:** https://arxiv.org/abs/2607.05277v1
- **Security insight:** Defenses that provide security guarantees against prompt injection attacks rely on strict isolation between trusted instructions and untrusted data. In text-based environments such as tool-use APIs, this separation arises naturally: agents can reason from…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Agent Data Injection Attacks are Realistic Threats to AI Agents**  
- **Date:** 2026-07-06
- **Authors:** Woohyuk Choi, Juhee Kim, Taehyun Kang et al.
- **Link:** https://arxiv.org/abs/2607.05120v1
- **Security insight:** AI agents act on behalf of user prompts, consuming external data and taking actions based on the agent context. Prior research on AI agent security has primarily focused on indirect prompt injection (IPI). Its most well-studied category is instruction…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Biological Motifs for Agentic Control**  
- **Date:** 2026-07-05
- **Authors:** Bogdan Banu
- **Link:** https://arxiv.org/abs/2607.04240v1
- **Security insight:** The transition of Large Language Models (LLMs) from passive generators to autonomous agents has introduced significant challenges in reliability, security, and state management. Current agentic architectures are often constructed ad-hoc, prone to…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**DualView: Preventing Indirect Prompt Injection in Personal AI Agents**  
- **Date:** 2026-07-04
- **Authors:** Juhee Kim, Woohyuk Choi, Taehyun Kang et al.
- **Link:** https://arxiv.org/abs/2607.03821v1
- **Security insight:** Personal AI agents that run on the user's local machine, such as OpenClaw, automate daily tasks including web search, email, and file management. Their access to computer resources, including the network, file system, and shell, exposes them to indirect…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Distributed Attacks in Persistent-State AI Control**  
- **Date:** 2026-07-02
- **Authors:** Josh Hills, Ida Caspary, Asa Cooper Stickland
- **Link:** https://arxiv.org/abs/2607.02514v1
- **Security insight:** As AI coding agents become more autonomous, they increasingly ship code iteratively, with the codebase persisting across sessions. This persistence creates a new attack surface: a misaligned or prompt-injected agent can distribute attacks across pull requests…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Adversarial Pragmatics for AI Safety Evaluation: A Benchmark for Instruction Conflict, Embedded Commands, and Policy Ambiguity**  
- **Date:** 2026-07-01
- **Authors:** Brett Reynolds
- **Link:** https://arxiv.org/abs/2607.01153v1
- **Security insight:** Safety evaluations for language models increasingly depend on judgments about ambiguous natural-language behaviour: whether a model has followed an instruction, refused appropriately, complied with a policy, resisted an embedded command, or misreported…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Securing the AI Agent: A Unified Framework for Multi-Layer Agent Red Teaming**  
- **Date:** 2026-06-30
- **Authors:** Yong Yang, Xing Zheng, Huiyu Wu et al.
- **Link:** https://arxiv.org/abs/2606.31227v1
- **Security insight:** The fast growth of open-source AI infrastructure, from model serving engines and agent platforms to the Model Context Protocol (MCP) ecosystem and the language models themselves, has outpaced the security tooling available to defend it. We present AI-Infra-…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Understanding and Evaluating Claw-like Agent Security Through a Computer-Systems Lens**  
- **Date:** 2026-06-29
- **Authors:** Peizhi Niu, Wenjie Qu, Shangding Gu et al.
- **Link:** https://arxiv.org/abs/2606.30755v1
- **Security insight:** Claw-like AI agents (e.g., OpenClaw) are always-on processes with persistent access to credentials, files, tools, and external services. They take on system-level responsibilities -- installing packages, maintaining state, scheduling subtasks, and mediating…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Forensic Trajectory Signatures for Agent Memory Poisoning Detection**  
- **Date:** 2026-06-29
- **Authors:** Jun Wen Leong
- **Link:** https://arxiv.org/abs/2606.30566v1
- **Security insight:** We discover a behavioral invariant in LLM agents under persistent memory poisoning: in architectures where routing information is retrieved through observable memory-tool invocations, successful attacks require calling memory_recall_fact before…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Beyond Wireless Security: Covert Communications in Large Language Model-enabled Edge Networks**  
- **Date:** 2026-06-30
- **Authors:** Yuanai Xie, Jiaxin Chen, Zhaozhi Liu
- **Link:** https://arxiv.org/abs/2606.31016v1
- **Security insight:** Large language model (LLM)-enabled edge networks (LLMENs) offer mobile users high-quality and low-latency AI-generated content services in the 6G era. However, unlike typical edge networks, LLMENs present unique security challenges due to the inherent…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Security--Fidelity Tradeoffs: The Hidden Cost of Prompt Injection Defense**  
- **Date:** 2026-06-29
- **Authors:** Mitchell Hermon, Rahul Gupta, Weitong Ruan et al.
- **Link:** https://arxiv.org/abs/2606.30783v1
- **Security insight:** We identify a security-fidelity tradeoff in defending LLMs against indirect prompt injection: defenses resist injected instructions largely by suppressing untrusted text, which corrupts tasks that must preserve it, such as translation and document editing.…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**IHDec: Divergence-Steered Contrastive Decoding for Securing Multi-Turn Instruction Hierarchies**  
- **Date:** 2026-06-29
- **Authors:** Nicole Geumheon Liu, Haeun Jang, Yonghyun Jun et al.
- **Link:** https://arxiv.org/abs/2606.29960v1
- **Security insight:** Large Language Models (LLMs) often fail to maintain instruction hierarchies (IH) when processing multi-source inputs with varying role-level priorities, paradoxically adhering to lower-priority directives during conflicts. While existing defenses mitigate…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### Poisoning & Backdoors

**Builder, Defender, Breaker: The Case Against Removing the Human from the AI-Driven Security Lifecycle**  
- **Date:** 2026-07-03
- **Authors:** Mohamed Chahine Ghanem
- **Link:** https://arxiv.org/abs/2607.03215v1
- **Security insight:** Artificial intelligence has spread across the whole of the security lifecycle. The same family of models now writes application code, hardens it, and probes it for weaknesses, so that a single generative substrate increasingly performs all three roles at…
- **Build idea:** Build a minimal poisoning simulator plus simple detectors (trigger search, label flip tests, anomaly baselines).

### Adversarial ML

**Generative AI and Federated Learning for Intrusion Detection Systems: A Survey**  
- **Date:** 2026-07-01
- **Authors:** Jiefei Liu, Abu Saleh Md Tayeen, Pratyay Kumar et al.
- **Link:** https://arxiv.org/abs/2607.01305v1
- **Security insight:** Intrusion Detection Systems (IDSs) are essential for monitoring network traffic and identifying malicious activities in modern cyber-physical, Internet of Things (IoT), enterprise, and distributed network environments. However, developing reliable IDS models…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.
