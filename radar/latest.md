# AI Security Radar

_Last updated (UTC): **2026-06-25**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**AI Snitches Get Glitches: Towards Evading Agentic Surveillance**  
- **Date:** 2026-06-24
- **Authors:** Hyejun Jeong, Dzung Pham, Amir Houmansadr et al.
- **Link:** https://arxiv.org/abs/2606.25836v1
- **Security insight:** To better assist users with completing challenging tasks, AI agents mediate communications, access data, and interact with different APIs. Many employers (and even nation-states) already provide their users with this technology. However, widespread adoption…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Poisoned Playbooks: Demystifying Knowledge Poisoning Effects on AI Security Agents**  
- **Date:** 2026-06-23
- **Authors:** Juho Park, Hyunmin Choi, Kevin Nam
- **Link:** https://arxiv.org/abs/2606.24402v1
- **Security insight:** AI security agents increasingly rely on Retrieval-Augmented Generation (RAG) to use external security knowledge for vulnerability analysis and exploit reasoning. This creates a new risk: poisoned write-ups can be operationalized into incorrect exploit…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**RIFT-Bench: Dynamic Red-teaming For Agentic AI Systems**  
- **Date:** 2026-06-22
- **Authors:** Yarin Yerushalmi Levi, Roy Betser, Amit Giloni et al.
- **Link:** https://arxiv.org/abs/2606.23927v1
- **Security insight:** Agentic AI systems powered by large language models (LLMs) are rapidly evolving into autonomous decision-making systems, exposing attack vectors beyond those of traditional LLM vulnerabilities. Existing security evaluations are often tied to specific…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

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

### Prompt Injection

**How Reliable Is Your Jailbreak Judge? Calibration and Adversarial Robustness of Automated ASR Scoring**  
- **Date:** 2026-06-24
- **Authors:** Yang Gao
- **Link:** https://arxiv.org/abs/2606.25487v1
- **Security insight:** Almost every paper on LLM jailbreaks and prompt injection reports an attack-success rate (ASR), and that number is assigned not by people but by an automated judge: either a safety classifier trained for the task, or a general chat model prompted to grade.…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**LLM-Based Scientific Peer Review: Methods, Benchmarks, and Reliability Challenges**  
- **Date:** 2026-06-23
- **Authors:** Thi Huyen Nguyen, Zahra Ahmadi
- **Link:** https://arxiv.org/abs/2606.25057v1
- **Security insight:** The rapid growth of scientific submissions has pushed traditional peer review toward its scalability limits, motivating the exploration of large language models (LLMs) as intelligent automated evaluation assistants. Although recent studies show that LLMs can…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**DE-FIVE: Detecting Malicious Image Prompts via Fourier Features and Image Vector Embeddings**  
- **Date:** 2026-06-22
- **Authors:** Xingwei Zhong, Varun Sharma, Kar Wai Fok et al.
- **Link:** https://arxiv.org/abs/2606.22779v1
- **Security insight:** Vision language models (VLMs) employ both visual and textual modalities to enable advanced vision-language inference. However, incorporating visual modalities expands the attack surface of VLMs, making them more susceptible to security threats such as…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**TROPT: An Open Framework for Unifying and Advancing Discrete Text Optimization**  
- **Date:** 2026-06-22
- **Authors:** Matan Ben-Tov, Mahmood Sharif
- **Link:** https://arxiv.org/abs/2606.23496v1
- **Security insight:** Discrete text-trigger optimization -- searching for text sequences that, when ingested by a model, steer it toward a specified objective -- underpins model red-teaming (e.g., LLM jailbreaks), as well as auditing and interpretability. However, the current…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Adversarial ML

**A Red Teaming Framework for Large Language Models: A Case Study on Faithfulness Evaluation**  
- **Date:** 2026-06-24
- **Authors:** Abrar Alotaibi, Raed Mughus, Moataz Ahmed
- **Link:** https://arxiv.org/abs/2606.25476v1
- **Security insight:** Large language models (LLMs) have demonstrated remarkable performance across natural language processing tasks, yet their deployment in high-stakes applications raises critical concerns regarding reliability, safety, and trustworthiness. In this paper, we…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

### Other (Review)

**Representation Matters: An Empirical Study of Program Representations for LLM Vulnerability Reasoning**  
- **Date:** 2026-06-24
- **Authors:** Andrew Stoltman, Johnathan Tang, Haipeng Cai
- **Link:** https://arxiv.org/abs/2606.25356v1
- **Security insight:** Large Language Models (LLMs) are increasingly used for automated vulnerability detection, but it remains unclear how program structure and semantics should be represented for LLM-based reasoning. Most prompting-based approaches provide raw source code,…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.

**Confidently Wrong: Severity-Aware Calibration of Prompt-Injection Detectors under Attack Shift**  
- **Date:** 2026-06-21
- **Authors:** Md Anas Biswas
- **Link:** https://arxiv.org/abs/2606.22659v1
- **Security insight:** Prompt-injection detectors are deployed as guards: a model scores an input and a downstream system trusts or blocks it on that score. I study the confidence of these scores, not only their accuracy, when the attack distribution shifts away from the clean…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
