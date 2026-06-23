# AI Security Radar

_Last updated (UTC): **2026-06-23**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Detecting Malicious Agent Skills in the Wild using Attention**  
- **Date:** 2026-06-22
- **Authors:** Bacem Etteib, Daniele Lunghi, Tégawendé F. Bissyandé
- **Link:** https://arxiv.org/abs/2606.23416v1
- **Security insight:** LLM agents increasingly load skills, file-based packages of natural-language instructions written by third parties and distributed through marketplaces, that execute with the user's privileges. A single malicious skill can exfiltrate data, hijack the agent,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**GIF: Locally Sound Geometric Information Flow Control for LLMs**  
- **Date:** 2026-06-22
- **Authors:** Adam Storek, Nikolaus Holzer, Zhuo Zhang et al.
- **Link:** https://arxiv.org/abs/2606.23277v1
- **Security insight:** Large language models increasingly mediate interactions between sensitive data, untrusted inputs, and privileged actions in agentic systems, creating security and privacy risks. These range from prompt injections that manipulate downstream tool use to leakage…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**When AUC 0.998 Is Not Enough: A Candidate Evaluation Protocol for Hidden-State Probes of Indirect Prompt Injection in Multimodal Computer-Use Agents**  
- **Date:** 2026-06-22
- **Authors:** Yanhang Li, Zhichao Fan, Zexin Zhuang
- **Link:** https://arxiv.org/abs/2606.22864v1
- **Security insight:** Hidden-state probing -- a linear classifier on a frozen vision-language model's internal activations -- has emerged as an attractive evaluation tool for flagging indirect prompt injection (IPI) in multimodal computer-use agents before the agent emits a…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Safe to Check, Unsafe to Use: Relinking at the Compression Boundary of LLM Agents**  
- **Date:** 2026-06-19
- **Authors:** Zesen Liu, Zihan Zhang, Dongdong She
- **Link:** https://arxiv.org/abs/2606.21732v1
- **Security insight:** Summarization-based prompt compression is increasingly used by LLM agents to shorten long, distributed contexts, but it shifts the security boundary: filters inspect the pre-compression prompt while the backend acts on a newly generated compressed context. We…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**AgenticOS: An Intent-Oriented Secure Operating System Architecture for Autonomous AI Agents**  
- **Date:** 2026-06-19
- **Authors:** Zhen Zhao, Yu Zhang, Yanpeng Zhu et al.
- **Link:** https://arxiv.org/abs/2606.21129v1
- **Security insight:** Traditional OS security models based on "resource exposure plus permission checks" face structural challenges as LLM-driven autonomous agents acquire capabilities for planning, tool use, network access, and code execution. Once an agent runtime is compromised…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Local LLM Agents as Vulnerable Runtimes:A Source-Code Audit of the Agent Runtime Layer**  
- **Date:** 2026-06-19
- **Authors:** Zhengsong Zhang, Zongze Li, Jiawei Guo et al.
- **Link:** https://arxiv.org/abs/2606.21071v1
- **Security insight:** Local LLM agents such as OpenClaw and Nanobot run on end-user machines and act on host resources - the shell, filesystem, browser, stored credentials, and messaging applications - through natural-language goals. These agents have become privileged software…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Think Twice Before You Act: Protecting LLM Agents Against Tool Description Poisoning via Isolated Planning**  
- **Date:** 2026-06-18
- **Authors:** Shanghao Shi, Xiao Wang, Chaoyu Zhang et al.
- **Link:** https://arxiv.org/abs/2606.20922v1
- **Security insight:** The integration of external tools has substantially expanded the capabilities of large language model (LLM) agents, but it also introduces new attack surfaces beyond prompt injection. In particular, cross-tool description poisoning can manipulate planner-…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Analyzing Defensive Misdirection Against Model-Guided Automated Attacks on Agentic AI Systems**  
- **Date:** 2026-06-18
- **Authors:** Reza Soosahabi, Vivek Namsani
- **Link:** https://arxiv.org/abs/2606.20470v1
- **Security insight:** Agentic AI systems increasingly rely on language-model components to interpret instructions, process external data, invoke tools, and coordinate with other agents. These capabilities make prompt-injection and jailbreak attacks more consequential, especially…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**DE-FIVE: Detecting Malicious Image Prompts via Fourier Features and Image Vector Embeddings**  
- **Date:** 2026-06-22
- **Authors:** Xingwei Zhong, Varun Sharma, Kar Wai Fok et al.
- **Link:** https://arxiv.org/abs/2606.22779v1
- **Security insight:** Vision language models (VLMs) employ both visual and textual modalities to enable advanced vision-language inference. However, incorporating visual modalities expands the attack surface of VLMs, making them more susceptible to security threats such as…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**A Layered Security Framework Against Prompt Injection in RAG-Based Chatbots**  
- **Date:** 2026-06-17
- **Authors:** Gulshan Saleem, Nisar Ahmed, Muhammad Imran Zaman et al.
- **Link:** https://arxiv.org/abs/2606.19660v1
- **Security insight:** Prompt injection is ranked as the most critical vulnerability in large language model (LLM) deployments by the OWASP Top 10 for LLM Applications, yet existing defenses operate at isolated pipeline stages and remain incomplete. Input filters cannot inspect…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**TROPT: An Open Framework for Unifying and Advancing Discrete Text Optimization**  
- **Date:** 2026-06-22
- **Authors:** Matan Ben-Tov, Mahmood Sharif
- **Link:** https://arxiv.org/abs/2606.23496v1
- **Security insight:** Discrete text-trigger optimization -- searching for text sequences that, when ingested by a model, steer it toward a specified objective -- underpins model red-teaming (e.g., LLM jailbreaks), as well as auditing and interpretability. However, the current…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Poisoning & Backdoors

**Calibration Without Comprehension: Diagnosing the Limits of Fine-Tuning LLMs for Vulnerability Detection in Systems Software**  
- **Date:** 2026-06-18
- **Authors:** Arastoo Zibaeirad, Marco Vieira
- **Link:** https://arxiv.org/abs/2606.20502v1
- **Security insight:** Whether LLMs scoring well on vulnerability benchmarks genuinely reason about security or merely pattern-match on contaminated data remains unresolved. We present CWE-Trace, a framework for LLM vulnerability detection built from 834 manually curated Linux…
- **Build idea:** Build a minimal poisoning simulator plus simple detectors (trigger search, label flip tests, anomaly baselines).

### Other (Review)

**Confidently Wrong: Severity-Aware Calibration of Prompt-Injection Detectors under Attack Shift**  
- **Date:** 2026-06-21
- **Authors:** Md Anas Biswas
- **Link:** https://arxiv.org/abs/2606.22659v1
- **Security insight:** Prompt-injection detectors are deployed as guards: a model scores an input and a downstream system trusts or blocks it on that score. I study the confidence of these scores, not only their accuracy, when the attack distribution shifts away from the clean…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.

**What Do Safety-Aligned LLMs Learn From Mixed Compliance Demonstrations?**  
- **Date:** 2026-06-18
- **Authors:** Sihui Dai, Mann Patel
- **Link:** https://arxiv.org/abs/2606.20508v1
- **Security insight:** Prior work has shown that in-context demonstrations can jailbreak language models, but it remains unclear how models interpret different types of compliance demonstrations. We study this by mixing benign compliance demonstrations (non-harmful request, helpful…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
