# AI Security Radar

_Last updated (UTC): **2026-04-13**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**BadSkill: Backdoor Attacks on Agent Skills via Model-in-Skill Poisoning**  
- **Date:** 2026-04-10
- **Authors:** Guiyao Tie, Jiawen Shi, Pan Zhou et al.
- **Link:** https://arxiv.org/abs/2604.09378v1
- **Security insight:** Agent ecosystems increasingly rely on installable skills to extend functionality, and some skills bundle learned model artifacts as part of their execution logic. This creates a supply-chain risk that is not captured by prompt injection or ordinary plugin…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Are GUI Agents Focused Enough? Automated Distraction via Semantic-level UI Element Injection**  
- **Date:** 2026-04-09
- **Authors:** Wenkui Yang, Chao Jin, Haisu Zhu et al.
- **Link:** https://arxiv.org/abs/2604.07831v1
- **Security insight:** Existing red-teaming studies on GUI agents have important limitations. Adversarial perturbations typically require white-box access, which is unavailable for commercial systems, while prompt injection is increasingly mitigated by stronger safety alignment. To…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**TraceSafe: A Systematic Assessment of LLM Guardrails on Multi-Step Tool-Calling Trajectories**  
- **Date:** 2026-04-08
- **Authors:** Yen-Shan Chen, Sian-Yao Huang, Cheng-Lin Yang et al.
- **Link:** https://arxiv.org/abs/2604.07223v1
- **Security insight:** As large language models (LLMs) evolve from static chatbots into autonomous agents, the primary vulnerability surface shifts from final outputs to intermediate execution traces. While safety guardrails are well-benchmarked for natural language responses,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**ARuleCon: Agentic Security Rule Conversion**  
- **Date:** 2026-04-08
- **Authors:** Ming Xu, Hongtai Wang, Yanpei Guo et al.
- **Link:** https://arxiv.org/abs/2604.06762v1
- **Security insight:** Security Information and Event Management (SIEM) systems make it possible for detecting intrusion anomalies in real-time manner by their applied security rules. However, the heterogeneity of vendor-specific rules (e.g., Splunk SPL, Microsoft KQL, IBM AQL,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**SkillSieve: A Hierarchical Triage Framework for Detecting Malicious AI Agent Skills**  
- **Date:** 2026-04-08
- **Authors:** Yinghan Hou, Zongyou Yang
- **Link:** https://arxiv.org/abs/2604.06550v1
- **Security insight:** OpenClaw's ClawHub marketplace hosts over 13,000 community-contributed agent skills, and between 13% and 26% of them contain security vulnerabilities according to recent audits. Regex scanners miss obfuscated payloads; formal static analyzers cannot read the…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Compiled AI: Deterministic Code Generation for LLM-Based Workflow Automation**  
- **Date:** 2026-04-06
- **Authors:** Geert Trooskens, Aaron Karlsberg, Anmol Sharma et al.
- **Link:** https://arxiv.org/abs/2604.05150v1
- **Security insight:** We study compiled AI, a paradigm in which large language models generate executable code artifacts during a compilation phase, after which workflows execute deterministically without further model invocation. This paradigm has antecedents in prior work on…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**ShieldNet: Network-Level Guardrails against Emerging Supply-Chain Injections in Agentic Systems**  
- **Date:** 2026-04-06
- **Authors:** Zhuowen Yuan, Zhaorun Chen, Zhen Xiang et al.
- **Link:** https://arxiv.org/abs/2604.04426v1
- **Security insight:** Existing research on LLM agent security mainly focuses on prompt injection and unsafe input/output behaviors. However, as agents increasingly rely on third-party tools and MCP servers, a new class of supply-chain threats has emerged, where malicious behaviors…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Leave My Images Alone: Preventing Multi-Modal Large Language Models from Analyzing Images via Visual Prompt Injection**  
- **Date:** 2026-04-10
- **Authors:** Zedian Shao, Hongbin Liu, Yuepeng Hu et al.
- **Link:** https://arxiv.org/abs/2604.09024v1
- **Security insight:** Multi-modal large language models (MLLMs) have emerged as powerful tools for analyzing Internet-scale image data, offering significant benefits but also raising critical safety and societal concerns. In particular, open-weight MLLMs may be misused to extract…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**PIArena: A Platform for Prompt Injection Evaluation**  
- **Date:** 2026-04-09
- **Authors:** Runpeng Geng, Chenlong Yin, Yanting Wang et al.
- **Link:** https://arxiv.org/abs/2604.08499v1
- **Security insight:** Prompt injection attacks pose serious security risks across a wide range of real-world applications. While receiving increasing attention, the community faces a critical gap: the lack of a unified platform for prompt injection evaluation. This makes it…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Security Concerns in Generative AI Coding Assistants: Insights from Online Discussions on GitHub Copilot**  
- **Date:** 2026-04-09
- **Authors:** Nicolás E. Díaz Ferreyra, Monika Swetha Gurupathi, Zadia Codabux et al.
- **Link:** https://arxiv.org/abs/2604.08352v1
- **Security insight:** Generative Artificial Intelligence (GenAI) has become a central component of many development tools (e.g., GitHub Copilot) that support software practitioners across multiple programming tasks, including code completion, documentation, and bug detection.…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**The Defense Trilemma: Why Prompt Injection Defense Wrappers Fail?**  
- **Date:** 2026-04-07
- **Authors:** Manish Bhatt, Sarthak Munshi, Vineeth Sai Narajala et al.
- **Link:** https://arxiv.org/abs/2604.06436v2
- **Security insight:** We prove that no continuous, utility-preserving wrapper defense-a function $D: X\to X$ that preprocesses inputs before the model sees them-can make all outputs strictly safe for a language model with connected prompt space, and we characterize exactly where…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Gradient-Controlled Decoding: A Safety Guardrail for LLMs with Dual-Anchor Steering**  
- **Date:** 2026-04-06
- **Authors:** Purva Chiniya, Kevin Scaria, Sagar Chaturvedi
- **Link:** https://arxiv.org/abs/2604.05179v1
- **Security insight:** Large language models (LLMs) remain susceptible to jailbreak and direct prompt-injection attacks, yet the strongest defensive filters frequently over-refuse benign queries and degrade user experience. Previous work on jailbreak and prompt injection detection…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**SALLIE: Safeguarding Against Latent Language & Image Exploits**  
- **Date:** 2026-04-06
- **Authors:** Guy Azov, Ofer Rivlin, Guy Shtar
- **Link:** https://arxiv.org/abs/2604.06247v1
- **Security insight:** Large Language Models (LLMs) and Vision-Language Models (VLMs) remain highly vulnerable to textual and visual jailbreaks, as well as prompt injections (arXiv:2307.15043, Greshake et al., 2023, arXiv:2306.13213). Existing defenses often degrade performance…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**TRUSTDESC: Preventing Tool Poisoning in LLM Applications via Trusted Description Generation**  
- **Date:** 2026-04-08
- **Authors:** Hengkai Ye, Zhechang Zhang, Jinyuan Jia et al.
- **Link:** https://arxiv.org/abs/2604.07536v1
- **Security insight:** Large language models (LLMs) increasingly rely on external tools to perform time-sensitive tasks and real-world actions. While tool integration expands LLM capabilities, it also introduces a new prompt-injection attack surface: tool poisoning attacks (TPAs).…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.
