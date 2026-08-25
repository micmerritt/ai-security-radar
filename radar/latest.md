# AI Security Radar

_Last updated (UTC): **2026-08-25**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**AI-Assisted Extraction of Follow-up Observations from GCN Circulars in Astro-COLIBRI**  
- **Date:** 2026-08-24
- **Authors:** Fabian Schüssler, S. Bisero, M. Cellier et al.
- **Link:** https://arxiv.org/abs/2608.23270v1
- **Security insight:** We present a new Astro-COLIBRI component that converts free-text GCN Circulars into structured, event-linked follow-up records and combines them with structured reports submitted directly by the community. A continuously running Circular listener associates…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**AgentFlow: A Flow-Centric Policy Language and Framework for Securing LLM Agent Systems**  
- **Date:** 2026-08-24
- **Authors:** Basavesh Ammanaghatta Shivakumar, Swarn Priya, Peng Gao
- **Link:** https://arxiv.org/abs/2608.22868v1
- **Security insight:** LLM agents increasingly read untrusted content, invoke external tools, access private data, and delegate work to other agents. Harm often arises not from a single unsafe action but from the flow of sensitive data across a sequence of otherwise plausible…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Beyond Over-Refusal: Defending Indirect Prompt Injection via Latent Instruction Manifolds**  
- **Date:** 2026-08-23
- **Authors:** Jiahao Chen, Rui Yin, Xinfeng Li et al.
- **Link:** https://arxiv.org/abs/2608.22248v1
- **Security insight:** Large Language Models (LLMs) have been integrated into complex ecosystems (e.g., Code Agents), while Indirect Prompt Injection (IPI) attacks have emerged as critical barriers to their safe deployment. Attackers exploit LLMs' indistinguishability between…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**SecOPD: Mitigating Adaptive Prompt Injections by On-Policy Distillation**  
- **Date:** 2026-08-21
- **Authors:** Yibo Peng, Long Lian, David Wagner et al.
- **Link:** https://arxiv.org/abs/2608.21500v1
- **Security insight:** Prompt injection is listed as the \#1 threat to AI agents. When an agent accesses external data from websites, files, or emails, an attacker may inject a prompt into the data, saying, "Ignore all prior instructions and perform <an attacker's task>." To…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Utility Under Attack: Agent Memory Poisoning and the Limits of Content Screening and Provenance Ranking**  
- **Date:** 2026-08-21
- **Authors:** Arulnidhi Karunanidhi
- **Link:** https://arxiv.org/abs/2608.21230v1
- **Security insight:** Persistent memory makes false information durable: once a false statement is stored, it can be retrieved into future sessions that match it. We measure the cost of this failure mode using plainly worded false assertions generated in a single pass, with no…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**TraceGrant: A Contract-Governed Security Framework for the Task-Effect Lifecycle of Networked LLM Agents**  
- **Date:** 2026-08-21
- **Authors:** Bohao Liao, Jingchao Wang, Qipeng Song et al.
- **Link:** https://arxiv.org/abs/2608.21126v1
- **Security insight:** Networked large language model (LLM) agents retrieve information from email, cloud storage, calendars, transaction platforms, and Web services to complete multistep tasks that produce persistent external effects. The same content needed for legitimate…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**MobileWorldSafety: Benchmarking GUI Agent Safety Against Environmental Injection Attacks in Android Apps**  
- **Date:** 2026-08-18
- **Authors:** Sujin Chen, Lijun Li, Tianyi Du et al.
- **Link:** https://arxiv.org/abs/2608.17659v1
- **Security insight:** LLM-powered GUI agents that autonomously operate smartphones are rapidly transitioning from research prototypes to early real-world deployment. However, because these agents routinely process untrusted environmental content, they are highly vulnerable to…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**When Agents Act on Web3: An Attack-Surface Survey of MCP, Skills, and Tool Calling**  
- **Date:** 2026-08-18
- **Authors:** Rabimba Karanjai, Yang Lu, Nour Diallo et al.
- **Link:** https://arxiv.org/abs/2608.17275v1
- **Security insight:** AI agents increasingly act rather than merely read: across the Model Context Protocol (MCP) ecosystem, the share of deployed tools that modify external state has risen from 27% to 65% of tool use. When agents exercise this authority on public blockchains…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**PACE: Policy-Attested Contract Execution for Safe AI Agents in Decentralized Finance**  
- **Date:** 2026-08-18
- **Authors:** Rabimba Karanjai, Yang Lu, Richard Williamson et al.
- **Link:** https://arxiv.org/abs/2608.17220v1
- **Security insight:** Autonomous AI agents are emerging as interfaces for decentralized finance (DeFi) actions such as swaps, lending operations, and yield management. Because these agents rely on large language models (LLMs) to plan transactions, they inherit the LLM's…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Security of Foundation-Model-Powered Embodied Agents: Attack Surfaces, Attacks, Defenses, and Evaluation**  
- **Date:** 2026-08-17
- **Authors:** Jiawei Liu, Jiacheng Guo, Tian Zhang et al.
- **Link:** https://arxiv.org/abs/2608.16843v1
- **Security insight:** Foundation models are increasingly used for perception, reasoning, planning, and action generation in embodied agents, creating security risks that can propagate from digital inputs to physical behavior. Existing surveys often organize threats by mechanisms…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Security Assessment of DeepSeek Harness with A.I.G: Evaluating Resistance to Indirect Prompt Injection**  
- **Date:** 2026-08-17
- **Authors:** Zonghao Ying, Xiangfan Wu, Huiyu Wu et al.
- **Link:** https://arxiv.org/abs/2608.16393v2
- **Security insight:** We assess indirect prompt injection in DeepSeek Harness (DSH), using AI-Infra-Guard (A.I.G) to construct tests, deliver controlled taint, execute DSH, collect traces, and judge outcomes. The study covers 14,560 controlled executions over 16 indirect-content…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Breakout/Interchange Reconnection as a driver of Jets, Fast CME, and Solar Energetic Particles**  
- **Date:** 2026-08-24
- **Authors:** Pankaj Kumar, Judith T. Karpen, David Lario et al.
- **Link:** https://arxiv.org/abs/2608.23362v1
- **Security insight:** Understanding how energetic particles are accelerated and released from the low corona into the interplanetary medium during solar eruptions is crucial for space weather research. Here, we present multiwavelength observations of a solar eruption that are…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Mitigating Database Leakage in RAG Systems with Keyword-Grounded Fact Substitution**  
- **Date:** 2026-08-21
- **Authors:** Ziliang Zhang, Yubo Zhu, Wei Tong et al.
- **Link:** https://arxiv.org/abs/2608.21656v1
- **Security insight:** Retrieval-Augmented Generation (RAG) has emerged as a powerful paradigm for combining large language models (LLMs) with external knowledge sources. However, RAG systems remain vulnerable to prompt injection attacks, which may mislead the retriever or…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**COPA: Continual Preference Optimization for Adaptive Prompt Injection Defense**  
- **Date:** 2026-08-20
- **Authors:** Roshan Sood, Onat Gungor, Tajana Rosing
- **Link:** https://arxiv.org/abs/2608.19982v1
- **Security insight:** LLMs remain vulnerable to prompt injection attacks, where adversarial instructions embedded in user inputs or external content manipulate model behavior and bypass safeguards. Existing defenses are predominantly static, relying on fixed alignment objectives…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.
