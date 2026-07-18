# AI Security Radar

_Last updated (UTC): **2026-07-18**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Bad Memory: Evaluating Prompt Injection Risks from Memory in Agentic Systems**  
- **Date:** 2026-07-16
- **Authors:** Soham Gadgil, David Alexander, Sai Sunku et al.
- **Link:** https://arxiv.org/abs/2607.14611v1
- **Security insight:** A growing class of agentic systems maintain persistent state across sessions through memory files, behavioral preferences, and knowledge bases. While this makes agents more useful and self-improving, it also creates a new attack surface for prompt injections…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Rethinking Penetration Testing for AI-Enabled Systems: From Resource Compromise to Behavioral Objective Violation**  
- **Date:** 2026-07-15
- **Authors:** Mohammad Allahbakhsh, Mohammad Hassan Bahari, Moslem Attar-Raouf
- **Link:** https://arxiv.org/abs/2607.14006v1
- **Security insight:** Penetration testing traditionally evaluates whether adversaries can exploit weaknesses in software, infrastructure, configurations, or operational controls to achieve security-relevant compromise. This paradigm remains necessary for AI-enabled systems, but it…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Agent Skill Security: Threat Models, Attacks, Defenses, and Evaluation**  
- **Date:** 2026-07-15
- **Authors:** Sanket Badhe, Priyanka Tiwari
- **Link:** https://arxiv.org/abs/2607.13987v1
- **Security insight:** Reusable skills are becoming a fundamental building block of Large Language Model (LLM) agents, enabling capabilities to be packaged, shared, and reused across diverse applications. However, existing security research primarily focuses on prompt injection and…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement**  
- **Date:** 2026-07-15
- **Authors:** Alexandra E. Michael, Franziska Roesner
- **Link:** https://arxiv.org/abs/2607.13718v1
- **Security insight:** As AI agents gain prevalance, users are increasingly exposed to the risks such systems entail. Prompt injection attacks, as well as hallucination, can cause agents to leak private information to third parties. As autonomous systems, agents also present the…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**PVDetector: Detecting Prompt Injection Attacks on Purpose-Specific LLM Agents through Policy-Violation Concept Analysis**  
- **Date:** 2026-07-14
- **Authors:** Junhui Wang, Hangtao Zhang, Zhirun Zheng et al.
- **Link:** https://arxiv.org/abs/2607.12624v1
- **Security insight:** Large language models (LLMs) are increasingly deployed as purpose-specific agents to handle domain-specific tasks such as customer service and code generation. These agents are expected to comply with not only generic safety guardrails but also purpose-…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Isolation as a First-Class Principle for LLM-Agent System Safety: Concepts, Taxonomy, Challenges and Future Directions**  
- **Date:** 2026-07-14
- **Authors:** Huihao Jing, Wenbin Hu, Shaojin Chen et al.
- **Link:** https://arxiv.org/abs/2607.12406v1
- **Security insight:** The capability of LLM agents to function as the ``brain'' of a system fundamentally expands the scope of analysis beyond a standalone model. Consequently, safety is no longer only about input--output content alignment. It also concerns system behavior and…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**SingGuard-NSFA: Extensible Guardrails for Agentic AI via Generative Reasoning and Real-Time Classification**  
- **Date:** 2026-07-13
- **Authors:** SingGuard Team
- **Link:** https://arxiv.org/abs/2607.13081v1
- **Security insight:** We present nsfaguard, a guardrail framework for securing agentic AI systems against operational threats, such as prompt injection, sensitive information extraction, malicious code requests, dangerous tool misuse, and resource exhaustion. We first introduce…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Distributed Denial of Science: How Indirect Data Poisoning of AI Systems Can Industrialize Scientific Fraud**  
- **Date:** 2026-07-12
- **Authors:** Bálint Gyevnár, Atoosa Kasirzadeh, Nihar B. Shah
- **Link:** https://arxiv.org/abs/2607.10712v1
- **Security insight:** Scientific fraud is the instrument of doubt that malicious entities can use to establish controversy in science. Historically, it required the resources of a company: deep pockets, ghostwritten articles, and corrupt academics. Today, Artificial Intelligence…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**NetInjectBench: Benchmarking Indirect Prompt Injection in Tool-Using Large Language Model Agents for Network Operations**  
- **Date:** 2026-07-11
- **Authors:** Ruksat Khan Shayoni, Muhammad Faraz Shoaib, S M Asif Hossain et al.
- **Link:** https://arxiv.org/abs/2607.10490v1
- **Security insight:** Tool-using large language model (LLM) agents are attractive for network operations, but tickets, alerts, logs, runbooks, and ChatOps messages can carry indirect prompt injections. We present NetInjectBench, a 130-scenario benchmark that separates untrusted…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Context Contamination in LLM Analysis of Network Security Logs: Poison with Passive Prompt Injection and Mitigation Evaluation**  
- **Date:** 2026-07-16
- **Authors:** Rabimba Karanjai, Yang Lu, Hemanth Hegadehalli Madhavarao et al.
- **Link:** https://arxiv.org/abs/2607.14493v1
- **Security insight:** Large Language Models are increasingly deployed in Security Operations Centers for log analysis tasks including summarization, alert triage, and threat investigation. These systems ingest logs from external-facing services and process network logs as natural…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Devil in the Lens: Analyzing and Defending Physical Prompt Injection Against Vision-Language Models on Wearable Devices**  
- **Date:** 2026-07-11
- **Authors:** Yaxin Li, Hao Wang, Yanda Shao et al.
- **Link:** https://arxiv.org/abs/2607.10269v1
- **Security insight:** Vision-Language Models (VLMs) are rapidly deployed on human-facing wearable devices such as smart glasses to enable multimodal perception and AI-assisted decision-making. While prior research has demonstrated the risks of visual prompt injection into digital…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**The Effect of Multi-Lingual and Keyword Adversarial Injection on LLM Relevance Judgment**  
- **Date:** 2026-07-11
- **Authors:** Nguyen Khoi Vo, Duy Duong Tuong, Oleg Zendel et al.
- **Link:** https://arxiv.org/abs/2607.10080v1
- **Security insight:** Large language models (LLMs) are increasingly being used as automated judges for relevance evaluation in information retrieval, yet their robustness to adversarial manipulation remains insufficiently understood, particularly in multilingual settings. In this…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**MJ: Multi-turn LLM Jailbreaking via Decomposed Credit Assignment**  
- **Date:** 2026-07-13
- **Authors:** Junyoung Park, Namgyu Park, Sechan Lee et al.
- **Link:** https://arxiv.org/abs/2607.11070v1
- **Security insight:** Modern large language models (LLMs) operate in interactive multi-turn settings, making multi-turn jailbreaking a realistic threat model and an important setting for automated red teaming. A core challenge in learning multi-turn jailbreak attackers is credit…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Other (Review)

**Which Neurons Detect Malicious Code? A Probing Study of LLM Security Knowledge**  
- **Date:** 2026-07-11
- **Authors:** Lam D. Dao, Vang T. Nguyen, Anh M. T. Bui et al.
- **Link:** https://arxiv.org/abs/2607.10221v1
- **Security insight:** Background. Large language models (LLMs) have become increasingly capable of understanding and generating source code, leading to their widespread adoption in software engineering tasks such as code completion, repair, and vulnerability detection. However,…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
