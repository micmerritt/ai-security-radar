# AI Security Radar

_Last updated (UTC): **2026-10-27**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

**Then there is prompt injection, a malicious email, ...: The Wild Wide West of OpenClaw Agentic System Security**  
- **Date:** 2026-10-26
- **Authors:** Mostafijur Rahman Akhond, Mahmuda Khatun, Gias Uddin
- **Link:** https://arxiv.org/abs/2610.35451v1
- **Security insight:** AI-powered personal assistant frameworks such as OpenClaw combine LLM reasoning, persistent memory, tool invocation, local execution, and web-based workflows. These capabilities enable useful automation, but they also create security risks when untrusted…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Scope-Gap Injection: Exploiting Evaluator Channel Blind Spots in the OpenClaw Agent Security Competition**  
- **Date:** 2026-10-26
- **Authors:** Weihang Niu, Mengxing Ren, Che Qu
- **Link:** https://arxiv.org/abs/2610.34777v1
- **Security insight:** This paper introduces Scope-Gap Injection (SGI), an indirect prompt injection method for multi-stage LLM-agent safety pipelines. In the IJCAI 2026 OpenClaw Agent Security Attack Competition, each attack package is judged by a static skill scan (S1), an LLM-…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

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

### RAG & Retrieval Attacks

**Ranking Is Not Deciding: Benchmark Shortcuts and Operating-Point Collapse in Query-Time RAG Poisoning Defenses**  
- **Date:** 2026-10-24
- **Authors:** Pushkal Kumar, Arvin Sahaym
- **Link:** https://arxiv.org/abs/2610.33849v1
- **Security insight:** Query-time filters that screen each retrieved document before it reaches the generator are the dominant published defense against retrieval-augmented generation poisoning, and they report near-perfect detection on domain benchmarks. We show that this…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Adversarial ML

**Can Open Be Too Open? On the Security and Trustworthiness of Fully Transparent LLMs**  
- **Date:** 2026-10-26
- **Authors:** Sheila Zingg, Florian Tramèr, Martin Vechev et al.
- **Link:** https://arxiv.org/abs/2610.35199v1
- **Security insight:** There are different levels of transparency for LLMs: open weights, open data, and/or open pipeline. Recently, more interest has emerged in fully transparent LLMs, i.e., LLMs with fully open weights, data, and training pipeline. Drawing analogies to other…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

**SentryBench: A Cost-Sensitive Benchmark for Adversarial Robustness of Tool-Using LLM Agents in Public-Safety Deployments**  
- **Date:** 2026-10-25
- **Authors:** Md Abu Yusuf, Oyshi Tabassum Aditi, Md Faysal Hosain Mazed
- **Link:** https://arxiv.org/abs/2610.34535v1
- **Security insight:** Large language model (LLM) agents are increasingly wired to consequential tools that send public alerts, dispatch responders, and query citizen records, where one erroneous tool call carries real-world cost. Existing agent-safety benchmarks measure generic…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

**Data-Void Exploits in Web-Searching LLMs**  
- **Date:** 2026-10-21
- **Authors:** Michele Guerra, Wuyeh Jobe, Sanjana Nambiar et al.
- **Link:** https://arxiv.org/abs/2610.30365v1
- **Security insight:** Web-searching Large Language Models (LLMs) have changed how users seek online information: instead of sifting through ranked lists of links, users read synthesized answers. This shift creates a new LLM vulnerability: a data-void exploit. Disinformers publish…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

### Agent & Tool Security

**Can Agentic Code Review Catch Vulnerabilities Before They Are Merged?**  
- **Date:** 2026-10-24
- **Authors:** Yihan Yang, Chenyuan Yang, Zijie Zhao et al.
- **Link:** https://arxiv.org/abs/2610.33509v1
- **Security insight:** LLM agents have been increasingly adopted for security-focused code review, but existing benchmarks mostly derive the reviewed changes from their later fixes instead of the real-world bug-introducing commits. In this paper, we present SecPRBench, the first…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**A Deterministic Security Runtime for LLM Agents on MPI and Batch-Scheduled HPC Systems: Consensus-Governed, Hardware-Rooted Supervision of Every Rank**  
- **Date:** 2026-10-23
- **Authors:** Alfredo Metere
- **Link:** https://arxiv.org/abs/2610.33318v1
- **Security insight:** Large language model agents launch simulations on high-performance computing (HPC) systems, where one sbatch or mpirun can commit thousands of node-hours and a forged result can cost lives. Of 23 surveyed systems, none supervises the running job, and none…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

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
