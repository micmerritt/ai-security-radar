# AI Security Radar

_Last updated (UTC): **2026-03-12**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**AttriGuard: Defeating Indirect Prompt Injection in LLM Agents via Causal Attribution of Tool Invocations**  
- **Date:** 2026-03-11
- **Authors:** Yu He, Haozhe Zhu, Yiming Li et al.
- **Link:** https://arxiv.org/abs/2603.10749v1
- **Security insight:** LLM agents are highly vulnerable to Indirect Prompt Injection (IPI), where adversaries embed malicious directives in untrusted tool outputs to hijack execution. Most existing defenses treat IPI as an input-level semantic discrimination problem, which often…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**IH-Challenge: A Training Dataset to Improve Instruction Hierarchy on Frontier LLMs**  
- **Date:** 2026-03-11
- **Authors:** Chuan Guo, Juan Felipe Ceron Uribe, Sicheng Zhu et al.
- **Link:** https://arxiv.org/abs/2603.10521v1
- **Security insight:** Instruction hierarchy (IH) defines how LLMs prioritize system, developer, user, and tool instructions under conflict, providing a concrete, trust-ordered policy for resolving instruction conflicts. IH is key to defending against jailbreaks, system prompt…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Compatibility at a Cost: Systematic Discovery and Exploitation of MCP Clause-Compliance Vulnerabilities**  
- **Date:** 2026-03-10
- **Authors:** Nanzi Yang, Weiheng Bai, Kangjie Lu
- **Link:** https://arxiv.org/abs/2603.10163v1
- **Security insight:** The Model Context Protocol (MCP) is a recently proposed interoperability standard that unifies how AI agents connect with external tools and data sources. By defining a set of common client-server message exchange clauses, MCP replaces fragmented integrations…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Security Considerations for Multi-agent Systems**  
- **Date:** 2026-03-09
- **Authors:** Tam Nguyen, Moses Ndebugre, Dheeraj Arremsetty
- **Link:** https://arxiv.org/abs/2603.09002v1
- **Security insight:** Multi-agent artificial intelligence systems or MAS are systems of autonomous agents that exercise delegated tool authority, share persistent memory, and coordinate via inter-agent communication. MAS introduces qualitatively distinct security vulnerabilities…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**SlowBA: An efficiency backdoor attack towards VLM-based GUI agents**  
- **Date:** 2026-03-09
- **Authors:** Junxian Li, Tu Lan, Haozhen Tan et al.
- **Link:** https://arxiv.org/abs/2603.08316v2
- **Security insight:** Modern vision-language-model (VLM) based graphical user interface (GUI) agents are expected not only to execute actions accurately but also to respond to user instructions with low latency. While existing research on GUI-agent security mainly focuses on…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Governance Architecture for Autonomous Agent Systems: Threats, Framework, and Engineering Practice**  
- **Date:** 2026-03-07
- **Authors:** Yuxu Ge
- **Link:** https://arxiv.org/abs/2603.07191v2
- **Security insight:** Autonomous agents powered by large language models introduce a class of execution-layer vulnerabilities -- prompt injection, retrieval poisoning, and uncontrolled tool invocation -- that existing guardrails fail to address systematically. In this work, we…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Beyond Input Guardrails: Reconstructing Cross-Agent Semantic Flows for Execution-Aware Attack Detection**  
- **Date:** 2026-03-04
- **Authors:** Yangyang Wei, Yijie Xu, Zhenyuan Li et al.
- **Link:** https://arxiv.org/abs/2603.04469v1
- **Security insight:** Multi-Agent System is emerging as the \textit{de facto} standard for complex task orchestration. However, its reliance on autonomous execution and unstructured inter-agent communication introduces severe risks, such as indirect prompt injection, that easily…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Goal-Driven Risk Assessment for LLM-Powered Systems: A Healthcare Case Study**  
- **Date:** 2026-03-04
- **Authors:** Neha Nagaraja, Hayretdin Bahsi
- **Link:** https://arxiv.org/abs/2603.03633v1
- **Security insight:** While incorporating LLMs into systems offers significant benefits in critical application areas such as healthcare, new security challenges emerge due to the potential cyber kill chain cycles that combine adversarial model, prompt injection and conventional…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Learning When to Act or Refuse: Guarding Agentic Reasoning Models for Safe Multi-Step Tool Use**  
- **Date:** 2026-03-03
- **Authors:** Aradhye Agarwal, Gurdit Siyan, Yash Pandya et al.
- **Link:** https://arxiv.org/abs/2603.03205v1
- **Security insight:** Agentic language models operate in a fundamentally different safety regime than chat models: they must plan, call tools, and execute long-horizon actions where a single misstep, such as accessing files or entering credentials, can cause irreversible harm.…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**VoiceSHIELD-Small: Real-Time Malicious Speech Detection and Transcription**  
- **Date:** 2026-03-08
- **Authors:** Sumit Ranjan, Sugandha Sharma, Ubaid Abbas et al.
- **Link:** https://arxiv.org/abs/2603.07708v1
- **Security insight:** Voice interfaces are quickly becoming a common way for people to interact with AI systems. This also brings new security risks, such as prompt injection, social engineering, and harmful voice commands. Traditional security methods rely on converting speech to…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Image-based Prompt Injection: Hijacking Multimodal LLMs through Visually Embedded Adversarial Instructions**  
- **Date:** 2026-03-04
- **Authors:** Neha Nagaraja, Lan Zhang, Zhilong Wang et al.
- **Link:** https://arxiv.org/abs/2603.03637v1
- **Security insight:** Multimodal Large Language Models (MLLMs) integrate vision and text to power applications, but this integration introduces new vulnerabilities. We study Image-based Prompt Injection (IPI), a black-box attack in which adversarial instructions are embedded into…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**Risk-Adjusted Harm Scoring for Automated Red Teaming for LLMs in Financial Services**  
- **Date:** 2026-03-11
- **Authors:** Fabrizio Dimino, Bhaskarjit Sarmah, Stefano Pasquali
- **Link:** https://arxiv.org/abs/2603.10807v1
- **Security insight:** The rapid adoption of large language models (LLMs) in financial services introduces new operational, regulatory, and security risks. Yet most red-teaming benchmarks remain domain-agnostic and fail to capture failure modes specific to regulated BFSI settings,…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Poisoning & Backdoors

**Client-Cooperative Split Learning**  
- **Date:** 2026-03-09
- **Authors:** Haiyu Deng, Yanna Jiang, Guangsheng Yu et al.
- **Link:** https://arxiv.org/abs/2603.08421v1
- **Security insight:** Model training is increasingly offered as a service for resource-constrained data owners to build customized models. Split Learning (SL) enables such services by offloading training computation under privacy constraints, and evolves toward serverless and…
- **Build idea:** Build a minimal poisoning simulator plus simple detectors (trigger search, label flip tests, anomaly baselines).

### Other (Review)

**Why LLMs Fail: A Failure Analysis and Partial Success Measurement for Automated Security Patch Generation**  
- **Date:** 2026-03-10
- **Authors:** Amir Al-Maamari
- **Link:** https://arxiv.org/abs/2603.10072v1
- **Security insight:** Large Language Models (LLMs) show promise for Automated Program Repair (APR), yet their effectiveness on security vulnerabilities remains poorly characterized. This study analyzes 319 LLM-generated security patchesacross 64 Java vulnerabilities from the Vul4J…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
