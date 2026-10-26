# AI Security Radar

_Last updated (UTC): **2026-10-26**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

**On Task, Off Track: Benchmarking LLM and Agent Robustness to Near-Target Prompt Injection**  
- **Date:** 2026-10-23
- **Authors:** Yuyang Gong, Zihao Wang, Jiawei Liu et al.
- **Link:** https://arxiv.org/abs/2610.32531v1
- **Security insight:** Prompt injection benchmarks assess whether large language models (LLMs) and agents resist malicious instructions embedded in external content. However, a system could perform well by rejecting attacks that obviously abandon the user's request, while still…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Agentic AI Defense: Decode-Time Provenance Binding for MCP**  
- **Date:** 2026-10-22
- **Authors:** Eric Yocam, Varghese Vaidyan, Paris Kalathas et al.
- **Link:** https://arxiv.org/abs/2610.31974v1
- **Security insight:** Agentic AI systems using the Model Context Protocol (MCP) are vulnerable to indirect prompt injection through untrusted tool outputs. We demonstrate cross-modal trust laundering, in which instructions concealed in an email-signature image using least-…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Certified Execution Harness for Agentic AI: Safe and Least-Intrusive Petri-Net Supervisory Control Between Reasoning and Action**  
- **Date:** 2026-10-22
- **Authors:** Chao Gu, Quanyan Zhu
- **Link:** https://arxiv.org/abs/2610.31376v1
- **Security insight:** This paper studies the problem of safe tool execution for large language model (LLM) agents under prompt injection. Using Petri nets, we formalize the execution harness between the LLM and its tools as a supervisory control problem, in which marks represent…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Prompt Injection Through Forensic Evidence: A Taxonomy and Proof of Concept of Anti-Forensic Attacks on LLM-Assisted Digital Investigations**  
- **Date:** 2026-10-21
- **Authors:** Frank Breitinger, Jan Gruber, Christopher Hargreaves et al.
- **Link:** https://arxiv.org/abs/2610.29747v1
- **Security insight:** Large language models (LLMs) are entering digital forensics as examination assistants and autonomous agents. Digital forensics inverts the usual setting for indirect prompt injection: the evidence under analysis is attacker-controlled by definition, and the…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**MPIDetector: Detecting Multi-modal Prompt Injection via LLM-based Reasoning**  
- **Date:** 2026-10-21
- **Authors:** Yiheng Li, Jingyue Li
- **Link:** https://arxiv.org/abs/2610.30202v1
- **Security insight:** With the rapid integration of Multi-modal Large Language Models (MLLMs) into real-world applications, Prompt Injection (PI) has emerged as a critical security threat. Attackers can conceal malicious instructions within textual narratives or visual inputs to…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Where AI Vulnerability Discovery Harnesses Go Quiet: Structural False Negatives and Hidden Vulnerabilities**  
- **Date:** 2026-10-21
- **Authors:** Gadi Evron
- **Link:** https://arxiv.org/abs/2610.29379v1
- **Security insight:** LLM-based vulnerability discovery harnesses can miss real, reachable vulnerabilities because of how the harness around the model is built. Steps that select code, filter it, and store and merge findings can drop a vulnerability before or after the model runs,…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Protection Is Not One Event: A Survey of RAG Protection Research by Measured Endpoint**  
- **Date:** 2026-10-21
- **Authors:** Peiyang Liu, Xi Wang, Di Liang et al.
- **Link:** https://arxiv.org/abs/2610.30193v1
- **Security insight:** Retrieval-augmented generation (RAG) systems face security, privacy, and copyright risks including content leakage, source reconstruction, unauthorized access, data poisoning, and prompt injection. Yet RAG protection studies use incompatible evaluation…
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

### RAG & Retrieval Attacks

**Preventing Model Extraction in Contextual Linear Optimization**  
- **Date:** 2026-10-21
- **Authors:** Adam N. Elmachtoub, Tianyi Lin, Wenxuan Liu
- **Link:** https://arxiv.org/abs/2610.29918v1
- **Security insight:** Consider a contextual linear optimization problem, where a predict-then-optimize (PTO) system returns optimal decisions without revealing the cost vectors used in its downstream linear program. Our focus is on how to prevent attackers, who can submit context…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Adversarial ML

**Data-Void Exploits in Web-Searching LLMs**  
- **Date:** 2026-10-21
- **Authors:** Michele Guerra, Wuyeh Jobe, Sanjana Nambiar et al.
- **Link:** https://arxiv.org/abs/2610.30365v1
- **Security insight:** Web-searching Large Language Models (LLMs) have changed how users seek online information: instead of sifting through ranked lists of links, users read synthesized answers. This shift creates a new LLM vulnerability: a data-void exploit. Disinformers publish…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

### Agent & Tool Security

**Ulysses: A Security Harness For Synthesizing Verifiable Web Exploits**  
- **Date:** 2026-10-22
- **Authors:** Aditya Oke, André Vicente Duarte, Rui Melo et al.
- **Link:** https://arxiv.org/abs/2610.31831v1
- **Security insight:** How can an AI agent automatically discover security vulnerabilities in any software repository? Existing approaches use LLMs to generate software vulnerability exploits. However, it is challenging for an LLM to reliably verify its own generated exploits. In…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Other (Review)

**Trusting the Tool: Asymmetric Deference of LLM Vulnerability Auditors to Static-Analysis Evidence**  
- **Date:** 2026-10-23
- **Authors:** ZhiHong Liu, Shuyao Gao
- **Link:** https://arxiv.org/abs/2610.32876v1
- **Security insight:** Pipelines that combine large language models (LLMs) with static analysis let the model consume the analyser's output as evidence, but whether the model distinguishes true from false evidence, and whether its scrutiny depends on what the evidence claims, has…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.

**Not Where You Think: Protecting Location Privacy Against Reasoning-Based Geolocation**  
- **Date:** 2026-10-21
- **Authors:** Shanghao Shi, Jian Xiao, Hao Li et al.
- **Link:** https://arxiv.org/abs/2610.30439v1
- **Security insight:** Recent large reasoning models can infer where ordinary photos were taken using only visual information, creating a serious location privacy risk even when metadata and obvious geographic identifiers are removed. To understand the mechanism behind such fine-…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
