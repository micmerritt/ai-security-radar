# AI Security Radar

_Last updated (UTC): **2026-03-13**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Security Considerations for Artificial Intelligence Agents**  
- **Date:** 2026-03-12
- **Authors:** Ninghui Li, Kaiyuan Zhang, Kyle Polley et al.
- **Link:** https://arxiv.org/abs/2603.12230v1
- **Security insight:** This article, a lightly adapted version of Perplexity's response to NIST/CAISI Request for Information 2025-0035, details our observations and recommendations concerning the security of frontier AI agents. These insights are informed by Perplexity's…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Cascade: Composing Software-Hardware Attack Gadgets for Adversarial Threat Amplification in Compound AI Systems**  
- **Date:** 2026-03-12
- **Authors:** Sarbartha Banerjee, Prateek Sahu, Anjo Vahldiek-Oberwagner et al.
- **Link:** https://arxiv.org/abs/2603.12023v1
- **Security insight:** Rapid progress in generative AI has given rise to Compound AI systems - pipelines comprised of multiple large language models (LLM), software tools and database systems. Compound AI systems are constructed on a layered traditional software stack running on a…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**OpenClaw PRISM: A Zero-Fork, Defense-in-Depth Runtime Security Layer for Tool-Augmented LLM Agents**  
- **Date:** 2026-03-12
- **Authors:** Frank Li
- **Link:** https://arxiv.org/abs/2603.11853v1
- **Security insight:** Tool-augmented LLM agents introduce security risks that extend beyond user-input filtering, including indirect prompt injection through fetched content, unsafe tool execution, credential leakage, and tampering with local control files. We present OpenClaw…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Taming OpenClaw: Security Analysis and Mitigation of Autonomous LLM Agent Threats**  
- **Date:** 2026-03-12
- **Authors:** Xinhao Deng, Yixiang Zhang, Jiaqing Wu et al.
- **Link:** https://arxiv.org/abs/2603.11619v1
- **Security insight:** Autonomous Large Language Model (LLM) agents, exemplified by OpenClaw, demonstrate remarkable capabilities in executing complex, long-horizon tasks. However, their tightly coupled instant-messaging interaction paradigm and high-privilege execution…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

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

**The Attack and Defense Landscape of Agentic AI: A Comprehensive Survey**  
- **Date:** 2026-03-11
- **Authors:** Juhee Kim, Xiaoyuan Liu, Zhun Wang et al.
- **Link:** https://arxiv.org/abs/2603.11088v1
- **Security insight:** AI agents that combine large language models with non-AI system components are rapidly emerging in real-world applications, offering unprecedented automation and flexibility. However, this unprecedented flexibility introduces complex security challenges…
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

### Prompt Injection

**The Mirror Design Pattern: Strict Data Geometry over Model Scale for Prompt Injection Detection**  
- **Date:** 2026-03-12
- **Authors:** J Alex Corll
- **Link:** https://arxiv.org/abs/2603.11875v1
- **Security insight:** Prompt injection defenses are often framed as semantic understanding problems and delegated to increasingly large neural detectors. For the first screening layer, however, the requirements are different: the detector runs on every request and therefore must…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Jailbreak Scaling Laws for Large Language Models: Polynomial-Exponential Crossover**  
- **Date:** 2026-03-11
- **Authors:** Indranil Halder, Annesya Banerjee, Cengiz Pehlevan
- **Link:** https://arxiv.org/abs/2603.11331v1
- **Security insight:** Adversarial attacks can reliably steer safety-aligned large language models toward unsafe behavior. Empirically, we find that adversarial prompt-injection attacks can amplify attack success rate from the slow polynomial growth observed without injection to…
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
