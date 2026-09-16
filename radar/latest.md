# AI Security Radar

_Last updated (UTC): **2026-09-16**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Emergence World: Adversarial Stress-Testing of Long-Horizon Multi-Agent Systems**  
- **Date:** 2026-09-15
- **Authors:** Deepak Akkil, Tamer Abuelsaad, Karthik Vikram et al.
- **Link:** https://arxiv.org/abs/2609.17320v1
- **Security insight:** As AI agents move from bounded tasks to persistent deployments, failures can propagate through memory, tools, other agents, and environmental state long after their interactions. This creates a safety regime that cannot be characterized by evaluating model…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Toward Secure AI-Powered Penetration Testing Agents: Security Threats, Guardrails, and Architectural Perspectives**  
- **Date:** 2026-09-15
- **Authors:** Rahul Dev T Y, Hiran V Nath
- **Link:** https://arxiv.org/abs/2609.16694v1
- **Security insight:** LLM-powered autonomous agents are transforming the penetration testing space with dynamic, multi-step offensive security workflows that require minimal supervision by humans. These agents leverage sophisticated reasoning abilities and external security tools…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Vulnerability Localization Benchmark: Measuring Agentic Security Analysis at Repository Scale**  
- **Date:** 2026-09-14
- **Authors:** Aman Priyanshu, Supriti Vijay, Kimia Majd et al.
- **Link:** https://arxiv.org/abs/2609.15939v1
- **Security insight:** Language-model agents increasingly operate over complete software repositories, yet cybersecurity evaluations primarily measure whether they can detect, reproduce, or repair vulnerabilities rather than whether they can locate the relevant code. We study…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Authorization Architectures for Tool-Using AI Agents**  
- **Date:** 2026-09-14
- **Authors:** Rakesh Kumar Surapani, Pradeep Kumar Dolabehera Kakitapelli, Arun Morampudi et al.
- **Link:** https://arxiv.org/abs/2609.15906v1
- **Security insight:** Tool-using artificial intelligence (AI) agents, systems that autonomously invoke application programming interfaces (APIs), databases, browsers, and inter-agent protocols such as the Model Context Protocol (MCP), are becoming production infrastructure. Yet…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Universal Defenses for Tool-Integrated LLM Agents Against Adversarial Attacks**  
- **Date:** 2026-09-14
- **Authors:** Xiaoyan Li, Yunli Wang
- **Link:** https://arxiv.org/abs/2609.16098v1
- **Security insight:** Large Language Model (LLM) agents have demonstrated impressive capabilities across a variety of domains, particularly when integrated with external tools for multi-step task completion. However, they are increasingly vulnerable to adversarial attacks,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**ActGuard: Pre-execution Action Auditing against Indirect Prompt Injection in LLM Agents**  
- **Date:** 2026-09-14
- **Authors:** Bingzheng Wang, Xiaoyan Gu, Wentao Wang et al.
- **Link:** https://arxiv.org/abs/2609.14987v1
- **Security insight:** Large language model (LLM) agents interact with external environments through tool invocation, but tool outputs can also expose them to indirect prompt injection (IPI) attacks. Existing defenses mainly rely on prompt hardening, content filtering, pre-…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**SkillSecurer: Detecting and Patching Prompt-Injection Vulnerabilities in AI Agent Skills**  
- **Date:** 2026-09-12
- **Authors:** Donato Mecca, Alberto Verna, Youness Bouchari et al.
- **Link:** https://arxiv.org/abs/2609.14079v1
- **Security insight:** Agent skills extend AI agents with reusable instructions, scripts, and configuration, but are also open to new attacks to influence an agent's decisions and actions. To address these risks, we present SkillSecurer, a fully agentic framework for generating,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Confuse the Model, Control the Flow: Understanding and Mitigating Privacy Leakage from LLM Agents with Information Flow Control**  
- **Date:** 2026-09-12
- **Authors:** Minsun Shim, Ramisha Raida Karim, Ruthwik Jakkula et al.
- **Link:** https://arxiv.org/abs/2609.14003v1
- **Security insight:** Personal AI agents built on large language models (LLMs) are increasingly given access to a user's private data and communications in order to provide personalized assistance. This access creates a persistent privacy risk: the agent must decide whether a…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Semantically Aligned Gradient-Driven Context-Preserving Image Editing**  
- **Date:** 2026-09-11
- **Authors:** Chiranjeev Chiranjeev, Muskan Dosi, Mayank Vatsa et al.
- **Link:** https://arxiv.org/abs/2609.12691v1
- **Security insight:** Instruction-guided image editing has a training-time blind spot. Generative editors are never required to semantically verify whether their outputs actually satisfy the instruction. Supervision stops at reconstruction and input textual-level conditioning.…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**The Agentic Company OS: Substrate Inversion for Sustained Enterprise Agent Deployment**  
- **Date:** 2026-09-11
- **Authors:** Oliver Aleksander Larsen, Mahyar T. Moghaddam
- **Link:** https://arxiv.org/abs/2609.13334v1
- **Security insight:** Enterprise AI agents often succeed in a demonstration and then stall once they must operate day after day. An industry report estimates that most pilots never reach production and that deployed systems rarely retain feedback or improve over time, while agent…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**The Agent Incident Registry: Toward Preventing Repeated AI Agent Failures**  
- **Date:** 2026-09-10
- **Authors:** Divyanshu Kumar, Rohith HN, Nitin Aravind Birur et al.
- **Link:** https://arxiv.org/abs/2609.11030v2
- **Security insight:** AI agents increasingly act through tools and delegated authority, but general incident repositories rarely capture the mechanisms needed to compare public failures with agent-security evaluations. We present the Agent Incident Registry (AIR) (Project page:…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### RAG & Retrieval Attacks

**Illusion of Depth: Revealing Hidden Stereo Vision Vulnerabilities in Depth Estimation**  
- **Date:** 2026-09-14
- **Authors:** Sri Hrushikesh Varma Bhupathiraju, Tetsu Ishizue, Nicholas U. Costagliola et al.
- **Link:** https://arxiv.org/abs/2609.16336v1
- **Security insight:** Stereo cameras are integrated into autonomous systems such as self-driving cars, drones, and robots to offer precise depth estimation in a cost-effective manner compared to LiDAR technology. In this work, we reveal an intrinsic vulnerability in stereo cameras…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**Approval Integrity and Recovery in LLM Answer Publication**  
- **Date:** 2026-09-14
- **Authors:** Faruk Alpay, Taylan Alpay
- **Link:** https://arxiv.org/abs/2609.15576v1
- **Security insight:** Publication integrity in LLM systems requires binding approved content to its current authorization context. We examine exact-content binding, authorization freshness and checkpoint recovery in Lightcap's publication enforcement mechanism. On 900…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Other (Review)

**PIDS-Bench: Evaluating Prompt-Injection Detectors Under Over-Defense, Obfuscation, and Distribution Shift**  
- **Date:** 2026-09-14
- **Authors:** Yusuf Khalid Shire, Sang-Chul Kim
- **Link:** https://arxiv.org/abs/2609.15017v1
- **Security insight:** Prompt-injection detectors are typically evaluated using aggregate F1 on in-distribution test data, which offers limited insight into behavior under distribution shift, particularly on the benign side of the decision boundary, where false positives impose…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
