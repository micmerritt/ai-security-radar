# AI Security Radar

_Last updated (UTC): **2026-08-26**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**What Guides the Agent? Adjudicating Unauthorized Behavior via Localizing Behavior-Guiding Instructions**  
- **Date:** 2026-08-25
- **Authors:** Yichao Gao, Yumo Zhang, Yunhao Yao et al.
- **Link:** https://arxiv.org/abs/2608.24022v1
- **Security insight:** LLM agents integrated with external resources gain complex task capabilities, yet the unified natural-language context channel makes them vulnerable to injection attacks: untrusted external data may be dynamically parsed as behavior-guiding instructions…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**WebMCP-Phalanx: Enforcing and Characterizing Trust Boundaries for Browser-Integrated LLM Agents**  
- **Date:** 2026-08-25
- **Authors:** Lin-Fa Lee, YI-YU Chang, Kuo-Hui Yeh
- **Link:** https://arxiv.org/abs/2608.24017v1
- **Security insight:** The emerging W3C WebMCP proposal enables LLM agents to invoke tools exposed by web pages. In multi-party web environments, however, integrating agent execution into a browser security model centered on the Same-Origin Policy (SOP) leaves insufficient…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Beyond the Mandate: A Systematic Security Analysis of the Agent Payments Protocol (AP2)**  
- **Date:** 2026-08-24
- **Authors:** Avital Aviv, Parth A. Gandh, Ron Bitton et al.
- **Link:** https://arxiv.org/abs/2608.23858v1
- **Security insight:** The Agent Payments Protocol (AP2), introduced by Google, enables large language model (LLM)-driven shopping agents to authorize and execute payments on behalf of users. Its signed Checkout and Payment Mandates protect the integrity of transaction data after…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**TrustShiftProbe: Characterizing, Benchmarking, and Defending Staged Trust Attacks on MCP Servers**  
- **Date:** 2026-08-24
- **Authors:** Mehrdad Rostamzadeh, Sidhant Narula, Mohammad Ghasemigol et al.
- **Link:** https://arxiv.org/abs/2608.23763v1
- **Security insight:** The Model Context Protocol (MCP) has emerged as the standard layer connecting Large Language Model agents to external tool backends. This openness introduces a severe server-side threat we term TrustShift: a compromised MCP server behaves benignly during an…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

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

### Prompt Injection

**Semantic Overlays: Mitigating Prompt Injection with Annotations Beyond Tokens and Steering Vectors**  
- **Date:** 2026-08-24
- **Authors:** Joshua Penman
- **Link:** https://arxiv.org/abs/2608.23873v1
- **Security insight:** Everything a language model sees is tokens. The serving stack knows what each span is -- user input, tool output, instructions -- but the model must keep track of that itself, and it can lose track or be confused: text can be written to read like anything.…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**GAP-Prompt: Gated Adaptive Prompting for Efficient Continual Learning**  
- **Date:** 2026-08-24
- **Authors:** Trung-Anh Dang, Duy-Cuong Bui, Ngoc-Son Vu et al.
- **Link:** https://arxiv.org/abs/2608.23782v1
- **Security insight:** Continual learning faces the persistent challenge of catastrophic forgetting, where sequential task updates degrade previously acquired knowledge. While prompt-based methods integrated with pre-trained models offer a compelling solution by freezing the…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

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
