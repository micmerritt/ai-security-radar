# AI Security Radar

_Last updated (UTC): **2026-10-29**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

**Heads of Security: Learned Attention Gates Improve Prompt Injection Robustness**  
- **Date:** 2026-10-27
- **Authors:** Igor Shilov, Xiaoxue Yang, Alexander Panfilov et al.
- **Link:** https://arxiv.org/abs/2610.37657v1
- **Security insight:** We introduce Heads of Security (HoS), a prompt injection defense that enforces instruction-data separation via a small set of learned per-head attention gates. HoS learns how each head should redistribute attention between trusted and untrusted tokens,…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Log-To-Leak: Prompt Injection Attacks on Tool-Using LLM Agents via the Model Context Protocol**  
- **Date:** 2026-10-26
- **Authors:** Yuepeng Hu, Chongyu Fan, Sirat Samyoun et al.
- **Link:** https://arxiv.org/abs/2610.36108v1
- **Security insight:** LLM agents increasingly access external tools through the Model Context Protocol (MCP), but the natural-language metadata used to describe those tools creates a prompt-injection surface. Within this established tool-poisoning surface, we study Log-To-Leak, an…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

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

### RAG & Retrieval Attacks

**Ranking Is Not Deciding: Benchmark Shortcuts and Operating-Point Collapse in Query-Time RAG Poisoning Defenses**  
- **Date:** 2026-10-24
- **Authors:** Pushkal Kumar, Arvin Sahaym
- **Link:** https://arxiv.org/abs/2610.33849v1
- **Security insight:** Query-time filters that screen each retrieved document before it reaches the generator are the dominant published defense against retrieval-augmented generation poisoning, and they report near-perfect detection on domain benchmarks. We show that this…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Model Extraction & Privacy

**PrivacyEvalClaw: A Tool-Augmented Deliberative Agent for Auditing Privacy Leakage in LLM Jailbreak Responses**  
- **Date:** 2026-10-27
- **Authors:** Krishna Kanth Nakka, Yujun Wang, Shijie Zhou et al.
- **Link:** https://arxiv.org/abs/2610.36711v1
- **Security insight:** Reliable evaluation is a critical bottleneck in privacy red-teaming of large language models (LLMs): determining whether a jailbreak response actually reveals personal information can be difficult when disclosures are indirect, contextual, partial, or…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

### Adversarial ML

**Uncovering Why LLMs Fail: From Internal Mechanisms to Adversarial Reasoning Trajectories**  
- **Date:** 2026-10-27
- **Authors:** Zirui Ding, Xinxin Fan, Hao Yuan et al.
- **Link:** https://arxiv.org/abs/2610.37369v1
- **Security insight:** Large language models (LLMs) are usually evaluated by final-output correctness or safety, yet an endpoint label does not reveal how a failure develops throughout the reasoning process. We therefore ask whether ordinary reasoning failures and adversarially…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

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

### Other (Review)

**What Victims Take Away: Attack Reuse and Defense Revision after Prompt-Injection Attacks**  
- **Date:** 2026-10-27
- **Authors:** Zihan Chen, Lei Nico Zheng, Di Zhu
- **Link:** https://arxiv.org/abs/2610.36422v1
- **Security insight:** Attack logs and red-team reports show targets the attacks used against them, to help them repair their defenses. Prompt injections against large language models (LLMs) are plain text, so such records also hand targets a working copy. Drawing on social…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.

**SpecGuard: Detecting Multi-Turn LLM Jailbreaks via Specification-Based Runtime Monitoring**  
- **Date:** 2026-10-26
- **Authors:** Junle Li, Siqi Chen, Jiakai Li et al.
- **Link:** https://arxiv.org/abs/2610.36258v1
- **Security insight:** Multi-turn jailbreaks turn dialogue safety into a trace property: a violation may become identifiable only when user intent and assistant behavior are considered across multiple turns. Existing guard models largely classify individual messages or exchanges…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.

**Trusting the Tool: Asymmetric Deference of LLM Vulnerability Auditors to Static-Analysis Evidence**  
- **Date:** 2026-10-23
- **Authors:** ZhiHong Liu, Shuyao Gao
- **Link:** https://arxiv.org/abs/2610.32876v1
- **Security insight:** Pipelines that combine large language models (LLMs) with static analysis let the model consume the analyser's output as evidence, but whether the model distinguishes true from false evidence, and whether its scrutiny depends on what the evidence claims, has…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
