# AI Security Radar

_Last updated (UTC): **2026-10-22**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

**Prompt Injection Through Forensic Evidence: A Taxonomy and Proof of Concept of Anti-Forensic Attacks on LLM-Assisted Digital Investigations**  
- **Date:** 2026-10-21
- **Authors:** Frank Breitinger, Jan Gruber, Christopher Hargreaves et al.
- **Link:** https://arxiv.org/abs/2610.29747v1
- **Security insight:** Large language models (LLMs) are entering digital forensics as examination assistants and autonomous agents. Digital forensics inverts the usual setting for indirect prompt injection: the evidence under analysis is attacker-controlled by definition, and the…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Where AI Vulnerability Discovery Harnesses Go Quiet: Structural False Negatives and Hidden Vulnerabilities**  
- **Date:** 2026-10-21
- **Authors:** Gadi Evron
- **Link:** https://arxiv.org/abs/2610.29379v1
- **Security insight:** LLM-based vulnerability discovery harnesses can miss real, reachable vulnerabilities because of how the harness around the model is built. Steps that select code, filter it, and store and merge findings can drop a vulnerability before or after the model runs,…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Attention-based Classification for Indirect Prompt Injection**  
- **Date:** 2026-10-20
- **Authors:** Amelia Kawasaki, Stefan Lee
- **Link:** https://arxiv.org/abs/2610.28988v1
- **Security insight:** Indirect prompt injection (IPI) attacks, in which adversarial instructions are embedded in external data processed by a language model, pose a significant threat to the integrity of deployed LLM agents. Attention Tracker (Hung et al., 2025) is a recently…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Combining Long-Term Memory and LLMs Comes at a High Cost: From Prompt Injection to Persistent Compromise**  
- **Date:** 2026-10-20
- **Authors:** Pedro H. Barcha Correia, Matheus Azevedo de Sá, Paulo H. Gomes de Senna et al.
- **Link:** https://arxiv.org/abs/2610.28810v1
- **Security insight:** The widespread adoption of generative artificial intelligence in recent years has brought a parallel rise in prompt injection and jailbreak attacks. By embedding malicious instructions, these exploits manipulate language models to bypass intended behavior and…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

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

### RAG & Retrieval Attacks

**Preventing Model Extraction in Contextual Linear Optimization**  
- **Date:** 2026-10-21
- **Authors:** Adam N. Elmachtoub, Tianyi Lin, Wenxuan Liu
- **Link:** https://arxiv.org/abs/2610.29918v1
- **Security insight:** Consider a contextual linear optimization problem, where a predict-then-optimize (PTO) system returns optimal decisions without revealing the cost vectors used in its downstream linear program. Our focus is on how to prevent attackers, who can submit context…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Agent & Tool Security

**AgenticVulHunter: Bringing Local Agentic Vulnerability Hunting to Your Terminal**  
- **Date:** 2026-10-19
- **Authors:** Nishant Abhishek, Ping Charoenwet, Kla Tantithamthavorn
- **Link:** https://arxiv.org/abs/2610.27383v1
- **Security insight:** Finding vulnerabilities early, before they can affect the production system, is important for reducing the risk of any software attacks. However, detecting vulnerabilities during secure code review is still difficult because the vulnerable code logic may…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Other (Review)

**Beyond Attack Success Rate: Cost-Aware Metric for Evaluating Iterative LLM Jailbreaks**  
- **Date:** 2026-10-19
- **Authors:** Rohan Menon, Chih-Hong Cheng
- **Link:** https://arxiv.org/abs/2610.26589v1
- **Security insight:** Attack success rate (ASR) evaluates jailbreaks against large language models without accounting for repeated calls to the victim model. Yet each additional call gives the deployed system another opportunity to detect the attack and intervene. We introduce…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
