# AI Security Radar

_Last updated (UTC): **2026-05-13**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**IPI-proxy: An Intercepting Proxy for Red-Teaming Web-Browsing AI Agents Against Indirect Prompt Injection**  
- **Date:** 2026-05-12
- **Authors:** Chia-Pei, Chen, Kentaroh Toyoda et al.
- **Link:** https://arxiv.org/abs/2605.11868v1
- **Security insight:** Web-browsing AI agents are increasingly deployed in enterprise settings under strict whitelists of approved domains, yet adversaries can still influence them by embedding hidden instructions in the HTML pages those domains serve. Existing red-teaming…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Agents Should Replace Narrow Predictive AI as the Orchestrator in 6G AI-RAN**  
- **Date:** 2026-05-12
- **Authors:** Pranshav Gajjar, Vijay K Shah
- **Link:** https://arxiv.org/abs/2605.11516v1
- **Security insight:** This position paper argues that to achieve Level 5 autonomous 6G networks, the next generation of Artificial Intelligence in Radio Access Networks (AI-RAN) should transition away from fragmented, narrow predictive models and instead adopt multimodal Large…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**LLMs for Secure Hardware Design and Related Problems: Opportunities and Challenges**  
- **Date:** 2026-05-11
- **Authors:** Johann Knechtel, Ozgur Sinanoglu, Ramesh Karri
- **Link:** https://arxiv.org/abs/2605.10807v1
- **Security insight:** The integration of Large Language Models (LLMs) into Electronic Design Automation (EDA) and hardware security is rapidly reshaping the semiconductor industry. While LLMs offer unprecedented capabilities in generating Register Transfer Level (RTL) code,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**The Granularity Mismatch in Agent Security: Argument-Level Provenance Solves Enforcement and Isolates the LLM Reasoning Bottleneck**  
- **Date:** 2026-05-11
- **Authors:** Linfeng Fan, Ziwei Li, Yuan Tian et al.
- **Link:** https://arxiv.org/abs/2605.11039v1
- **Security insight:** Tool-using LLM agents must act on untrusted webpages, emails, files, and API outputs while issuing privileged tool calls. Existing defenses often mediate trust at the granularity of an entire tool invocation, forcing a brittle choice in mixed-trust workflows:…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Oracle Poisoning: Corrupting Knowledge Graphs to Weaponise AI Agent Reasoning**  
- **Date:** 2026-05-10
- **Authors:** Ben Kereopa-Yorke, Guillermo Diaz, Holly Wright et al.
- **Link:** https://arxiv.org/abs/2605.09822v1
- **Security insight:** We define Oracle Poisoning, an attack class in which an adversary corrupts a structured knowledge graph that AI agents query at runtime via tool-use protocols, causing incorrect conclusions through correct reasoning. Unlike prompt injection, Oracle Poisoning…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Portable Agent Memory: A Protocol for Cryptographically-Verified Memory Transfer Across Heterogeneous AI Agents**  
- **Date:** 2026-05-10
- **Authors:** Santhosh Kumar Ravindran
- **Link:** https://arxiv.org/abs/2605.11032v1
- **Security insight:** We present Portable Agent Memory, an open protocol and reference implementation for transferring persistent memory state across heterogeneous AI agents. Modern AI agents accumulate rich context -- episodic events,semantic knowledge, procedural skills, working…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**AgentShield: Deception-based Compromise Detection for Tool-using LLM Agents**  
- **Date:** 2026-05-10
- **Authors:** Yassin H. Rassul, Tarik A. Rashid
- **Link:** https://arxiv.org/abs/2605.11026v1
- **Security insight:** Defenses against indirect prompt injection (IPI) in tool-using LLM agents share two structural weaknesses. First, they all attempt to prevent attacks rather than detect the compromises that slip through. Second, they have only been evaluated in English,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**When Agents Overtrust Environmental Evidence: An Extensible Agentic Framework for Benchmarking Evidence-Grounding Defects in LLM Agents**  
- **Date:** 2026-05-09
- **Authors:** Strick Sheng, Ziyue Wang, Liyi Zhou
- **Link:** https://arxiv.org/abs/2605.08828v2
- **Security insight:** Large language model agents increasingly operate through environment-facing scaffolds that expose files, web pages, APIs, and logs. These observations influence tool use, state tracking, and action sequencing, yet their reliability and authority are often…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**When Child Inherits: Modeling and Exploiting Subagent Spawn in Multi-Agent Networks**  
- **Date:** 2026-05-08
- **Authors:** Ziwen Cai, Yihe Zhang, Xiali Hei
- **Link:** https://arxiv.org/abs/2605.08460v1
- **Security insight:** Since the official release of ChatGPT in 2022, large language models (LLMs) have rapidly evolved from chatbot-style interfaces into agentic systems that can delegate work through tools and newly spawned subagents. While these capabilities improve automation…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**RUBEN: Rule-Based Explanations for Retrieval-Augmented LLM Systems**  
- **Date:** 2026-05-11
- **Authors:** Joel Rorseth, Parke Godfrey, Lukasz Golab et al.
- **Link:** https://arxiv.org/abs/2605.10862v1
- **Security insight:** This paper demonstrates RUBEN, an interactive tool for discovering minimal rules to explain the outputs of retrieval-augmented large language models (LLMs) in data-driven applications. We leverage novel pruning strategies to efficiently identify a minimal set…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**When Prompts Become Payloads: A Framework for Mitigating SQL Injection Attacks in Large Language Model-Driven Applications**  
- **Date:** 2026-05-11
- **Authors:** Farzad Nourmohammadzadeh Motlagh, Mehrdad Hajizadeh, Mehryar Majd et al.
- **Link:** https://arxiv.org/abs/2605.10176v1
- **Security insight:** Natural language interfaces to structured databases are becoming increasingly common, largely due to advances in large language models (LLMs) that enable users to query data using conversational input rather than formal query languages such as SQL. While this…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**CALYREX: Cross-Attention LaYeR EXtended Transformers for System Prompt Anchoring**  
- **Date:** 2026-05-10
- **Authors:** Li Lixing
- **Link:** https://arxiv.org/abs/2605.09737v1
- **Security insight:** Modern large language models (LLMs) rely on system prompts to establish behavioral constraints and safety rules. Standard causal self-attention treats privileged instructions and untrusted user content with equal structural priority -- a mismatch that leaves…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### Model Extraction & Privacy

**Identified-Set Geometry of Distributional Model Extraction under Top-$K$ Censored API Access**  
- **Date:** 2026-05-11
- **Authors:** Wenhua Nie, ZiCheng Zhu, Jianan Wu et al.
- **Link:** https://arxiv.org/abs/2605.10407v1
- **Security insight:** Modern LLM APIs often reveal only top-$K$ logit scores and censor the remaining vocabulary. We study the per-position distribution-recovery limits of this access model. For censoring threshold $τ$, the compatible teacher distributions form an identified set…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

### Adversarial ML

**The Art of the Jailbreak: Formulating Jailbreak Attacks for LLM Security Beyond Binary Scoring**  
- **Date:** 2026-05-09
- **Authors:** Ismail Hossain, Tanzim Ahad, Md Jahangir Alam et al.
- **Link:** https://arxiv.org/abs/2605.09225v1
- **Security insight:** Jailbreak attacks -- adversarial prompts that bypass LLM alignment through purely linguistic manipulation -- pose a growing operational security threat, yet the field lacks large-scale, reproducible infrastructure for generating, categorizing, and evaluating…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.
