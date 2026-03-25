# AI Security Radar

_Last updated (UTC): **2026-03-25**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Mind Your HEARTBEAT! Claw Background Execution Inherently Enables Silent Memory Pollution**  
- **Date:** 2026-03-24
- **Authors:** Yechao Zhang, Shiqian Zhao, Jie Zhang et al.
- **Link:** https://arxiv.org/abs/2603.23064v1
- **Security insight:** We identify a critical security vulnerability in mainstream Claw personal AI agents: untrusted content encountered during heartbeat-driven background execution can silently pollute agent memory and subsequently influence user-facing behavior without the…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**SoK: The Attack Surface of Agentic AI -- Tools, and Autonomy**  
- **Date:** 2026-03-24
- **Authors:** Ali Dehghantanha, Sajad Homayoun
- **Link:** https://arxiv.org/abs/2603.22928v1
- **Security insight:** Recent AI systems combine large language models with tools, external knowledge via retrieval-augmented generation (RAG), and even autonomous multi-agent decision loops. This agentic AI paradigm greatly expands capabilities - but also vastly enlarges the…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Model Context Protocol Threat Modeling and Analyzing Vulnerabilities to Prompt Injection with Tool Poisoning**  
- **Date:** 2026-03-23
- **Authors:** Charoes Huang, Xin Huang, Ngoc Phu Tran et al.
- **Link:** https://arxiv.org/abs/2603.22489v1
- **Security insight:** The Model Context Protocol (MCP) has rapidly emerged as a universal standard for connecting AI assistants to external tools and data sources. While MCP simplifies integration between AI applications and various services, it introduces significant security…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Are AI-assisted Development Tools Immune to Prompt Injection?**  
- **Date:** 2026-03-23
- **Authors:** Charoes Huang, Xin Huang, Amin Milani Fard
- **Link:** https://arxiv.org/abs/2603.21642v1
- **Security insight:** Prompt injection is listed as the number-one vulnerability class in the OWASP Top 10 for LLM Applications that can subvert LLM guardrails, disclose sensitive data, and trigger unauthorized tool use. Developers are rapidly adopting AI-assisted development…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Detection of adversarial intent in Human-AI teams using LLMs**  
- **Date:** 2026-03-21
- **Authors:** Abed K. Musaffar, Ambuj Singh, Francesco Bullo
- **Link:** https://arxiv.org/abs/2603.20976v1
- **Security insight:** Large language models (LLMs) are increasingly deployed in human-AI teams as support agents for complex tasks such as information retrieval, programming, and decision-making assistance. While these agents' autonomy and contextual knowledge enables them to be…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**The production of meaning in the processing of natural language**  
- **Date:** 2026-03-20
- **Authors:** Christopher J. Agostino, Quan Le Thien, Nayan D'Souza et al.
- **Link:** https://arxiv.org/abs/2603.20381v1
- **Security insight:** Understanding the fundamental mechanisms governing the production of meaning in the processing of natural language is critical for designing safe, thoughtful, engaging, and empowering human-agent interactions. Experiments in cognitive science and social…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Trojan's Whisper: Stealthy Manipulation of OpenClaw through Injected Bootstrapped Guidance**  
- **Date:** 2026-03-20
- **Authors:** Fazhong Liu, Zhuoyan Chen, Tu Lan et al.
- **Link:** https://arxiv.org/abs/2603.19974v1
- **Security insight:** Autonomous coding agents are increasingly integrated into software development workflows, offering capabilities that extend beyond code suggestion to active system interaction and environment management. OpenClaw, a representative platform in this emerging…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**A Framework for Formalizing LLM Agent Security**  
- **Date:** 2026-03-19
- **Authors:** Vincent Siu, Jingxuan He, Kyle Montgomery et al.
- **Link:** https://arxiv.org/abs/2603.19469v1
- **Security insight:** Security in LLM agents is inherently contextual. For example, the same action taken by an agent may represent legitimate behavior or a security violation depending on whose instruction led to the action, what objective is being pursued, and whether the action…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**The Autonomy Tax: Defense Training Breaks LLM Agents**  
- **Date:** 2026-03-19
- **Authors:** Shawn Li, Yue Zhao
- **Link:** https://arxiv.org/abs/2603.19423v1
- **Security insight:** Large language model (LLM) agents increasingly rely on external tools (file operations, API calls, database transactions) to autonomously complete complex multi-step tasks. Practitioners deploy defense-trained models to protect against prompt injection…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**LLMON: An LLM-native Markup Language to Leverage Structure and Semantics at the LLM Interface**  
- **Date:** 2026-03-23
- **Authors:** Michael Hind, Basel Shbita, Bo Wu et al.
- **Link:** https://arxiv.org/abs/2603.22519v1
- **Security insight:** Textual Large Language Models (LLMs) provide a simple and familiar interface: a string of text is used for both input and output. However, the information conveyed to an LLM often has a richer structure and semantics, which is not conveyed in a string. For…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**SecureBreak -- A dataset towards safe and secure models**  
- **Date:** 2026-03-23
- **Authors:** Marco Arazzi, Vignesh Kumar Kembu, Antonino Nocera
- **Link:** https://arxiv.org/abs/2603.21975v1
- **Security insight:** Large language models are becoming pervasive core components in many real-world applications. As a consequence, security alignment represents a critical requirement for their safe deployment. Although previous related works focused primarily on model…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Prompt Control-Flow Integrity: A Priority-Aware Runtime Defense Against Prompt Injection in LLM Systems**  
- **Date:** 2026-03-19
- **Authors:** Md Takrim Ul Alam, Akif Islam, Mohd Ruhul Ameen et al.
- **Link:** https://arxiv.org/abs/2603.18433v1
- **Security insight:** Large language models (LLMs) deployed behind APIs and retrieval-augmented generation (RAG) stacks are vulnerable to prompt injection attacks that may override system policies, subvert intended behavior, and induce unsafe outputs. Existing defenses often treat…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**Parameter-Efficient Modality-Balanced Symmetric Fusion for Multimodal Remote Sensing Semantic Segmentation**  
- **Date:** 2026-03-18
- **Authors:** Haocheng Li, Juepeng Zheng, Shuangxi Miao et al.
- **Link:** https://arxiv.org/abs/2603.17705v1
- **Security insight:** Multimodal remote sensing semantic segmentation enhances scene interpretation by exploiting complementary physical cues from heterogeneous data. Although pretrained Vision Foundation Models (VFMs) provide strong general-purpose representations, adapting them…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Adversarial ML

**LJ-Bench: Ontology-Based Benchmark for U.S. Crime**  
- **Date:** 2026-03-21
- **Authors:** Hung Yun Tseng, Wuzhen Li, Blerina Gkotse et al.
- **Link:** https://arxiv.org/abs/2603.20572v1
- **Security insight:** The potential of Large Language Models (LLMs) to provide harmful information remains a significant concern due to the vast breadth of illegal queries they may encounter. Unfortunately, existing benchmarks only focus on a handful types of illegal activities,…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.
