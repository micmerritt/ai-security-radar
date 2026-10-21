# AI Security Radar

_Last updated (UTC): **2026-10-21**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

**After the Attacker Leaves: Benchmarking Carryover Attacks on LLM Agents**  
- **Date:** 2026-10-20
- **Authors:** Zhiyue Xu, Xukai Wang, Zhiyuan Huang et al.
- **Link:** https://arxiv.org/abs/2610.28425v1
- **Security insight:** Modern LLM agents persist state across sessions via two channels: long-lived memory files silently prepended to the system prompt, and scheduled tasks waking the agent without user input. A one-time indirect prompt injection committed to either channel can…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Context-Aware Prompt Injection Detection via Small Language Models in RAG Pipelines: nokast-secureRAG**  
- **Date:** 2026-10-20
- **Authors:** Abhishek Rai
- **Link:** https://arxiv.org/abs/2610.28364v1
- **Security insight:** Local Retrieval-Augmented Generation (RAG) systems are vulnerable to indirect prompt injection and retrieval poisoning, where malicious instructions in retrieved content are mistaken for trusted input. We present nokast-secureRAG, a roughly 0.5B-parameter…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**KNOX: Hardware-assisted Regulatory Sandbox for Generative Models**  
- **Date:** 2026-10-20
- **Authors:** Vasisht Duddu, Adam Caulfield, Xi He
- **Link:** https://arxiv.org/abs/2610.27543v1
- **Security insight:** Regulations require companies to run AI models in a regulatory sandbox, an isolated environment that enables monitoring model behavior by regulators, prior to deployment. But, they do not spell out the technical mechanisms to design such a sandbox. Ideally, a…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Fake News, Real Crashes: Information Injection Attacks on LLM Financial Trading Agents**  
- **Date:** 2026-10-19
- **Authors:** Mengxiao Wang, Nitesh Saxena
- **Link:** https://arxiv.org/abs/2610.26438v1
- **Security insight:** Large language model (LLM) agents now trade real capital using news as evidence, yet they cannot reliably tell fabricated headlines from real news. Because they read the same feeds under near-identical policies, a single fabricated post can push them into the…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**SpanGuard: Decoupling Instruction Localization from Authorization for Lightweight IPI Defense**  
- **Date:** 2026-10-19
- **Authors:** Yinxiang Wang, Zehua Ma, Kejiang Chen et al.
- **Link:** https://arxiv.org/abs/2610.26013v1
- **Security insight:** LLM-based guardrails are effective against indirect prompt injection (IPI), but their performance depends heavily on model capability: as the guardrail model becomes smaller or weaker, detection degrades substantially. This raises a natural question: can we…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**RAGLeak: Supply-Chain Privacy Backdoors in Retrieval-Augmented Generation**  
- **Date:** 2026-10-19
- **Authors:** Yuchen Chen, Wei Cheng, Yuan Xiao et al.
- **Link:** https://arxiv.org/abs/2610.25937v1
- **Security insight:** Retrieval-Augmented Generation (RAG) enables large language models to access external knowledge during inference, but its reliance on external knowledge bases also introduces new attack surfaces. Existing data extraction attacks against RAG systems rely on…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**SoK: PIAtlas: Decomposing the Unbounded Prompt Injection Attack Space**  
- **Date:** 2026-10-18
- **Authors:** Stavros Damianakis, Konstantinos Psounis
- **Link:** https://arxiv.org/abs/2610.24999v1
- **Security insight:** Prompt injection is the dominant security risk for large-language-model (LLM) applications and agents, yet the field still lacks a coherent map of how these attacks are constructed. More than twenty public datasets describe prompt injection using incompatible…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**RATION: Towards Quantitative Risk-Based Access Control for AI Agents**  
- **Date:** 2026-10-16
- **Authors:** Yuntao Du, Harsh Chaudhari, Yuetian Chen et al.
- **Link:** https://arxiv.org/abs/2610.24311v1
- **Security insight:** AI agents increasingly interact with external environments to complete complex user tasks. These interactions can lead to unexpected behavior and expose agents to security threats such as indirect prompt injection. Current agent security systems largely…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**SPIDES: Information-Flow Control for Browser Agents**  
- **Date:** 2026-10-16
- **Authors:** Egor Zverev, Juhee Kim, Leon Trampert et al.
- **Link:** https://arxiv.org/abs/2610.24277v1
- **Security insight:** Browser agents automate complex workflows by reading and acting on arbitrary page content, but this flexibility exposes them to prompt injection attacks and unintended data exfiltration. Recent work argues that LLM-driven browser agents erode traditional web…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**MobileInject: Evaluating Reasoning-to-Action Security of MLLM-Based Mobile Agents under Cross-Modal Consistency Injection**  
- **Date:** 2026-10-16
- **Authors:** Songping Wang, Peiyang Li, Yi Huang et al.
- **Link:** https://arxiv.org/abs/2610.23307v1
- **Security insight:** Multimodal large language model (MLLM)-based mobile agents are rapidly evolving from conversational assistants into autonomous systems that perceive, reason over, and act on smartphone environments. This capability also exposes a new security risk:…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**CAT-RAG: Improving Secure Code Generation with Category-Aware Agentic Retrieval**  
- **Date:** 2026-10-17
- **Authors:** Mahdieh Abazar, Lorenzo De Carli, Benjamin Tan
- **Link:** https://arxiv.org/abs/2610.24907v1
- **Security insight:** Despite rapid progress in LLM-based code generation, security vulnerabilities remain widespread, and retrieval-augmented code generation (RACG) can further amplify risk when retrieved knowledge is verbose or vulnerable to poisoning. Existing secure RACG…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Agent & Tool Security

**AgenticVulHunter: Bringing Local Agentic Vulnerability Hunting to Your Terminal**  
- **Date:** 2026-10-19
- **Authors:** Nishant Abhishek, Ping Charoenwet, Kla Tantithamthavorn
- **Link:** https://arxiv.org/abs/2610.27383v1
- **Security insight:** Finding vulnerabilities early, before they can affect the production system, is important for reducing the risk of any software attacks. However, detecting vulnerabilities during secure code review is still difficult because the vulnerable code logic may…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**The Window Is in the Reasoning: When LLM Agents Decide to Follow Prompt Injections**  
- **Date:** 2026-10-16
- **Authors:** Haoxuan Jia, Yang Liu, Bin Chong et al.
- **Link:** https://arxiv.org/abs/2610.24048v1
- **Security insight:** LLM agents that read untrusted content can be hijacked by prompt injections. Runtime monitors that try to catch a hijack before the agent acts, and benchmarks that score each task with a single run, share an assumption: whether an agent follows an injection…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Other (Review)

**Beyond Attack Success Rate: Cost-Aware Metric for Evaluating Iterative LLM Jailbreaks**  
- **Date:** 2026-10-19
- **Authors:** Rohan Menon, Chih-Hong Cheng
- **Link:** https://arxiv.org/abs/2610.26589v1
- **Security insight:** Attack success rate (ASR) evaluates jailbreaks against large language models without accounting for repeated calls to the victim model. Yet each additional call gives the deployed system another opportunity to detect the attack and intervene. We introduce…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
