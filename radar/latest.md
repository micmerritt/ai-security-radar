# AI Security Radar

_Last updated (UTC): **2026-06-28**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**MIRROR: Novelty-Constrained Memory-Guided MCTS Red-Teaming for Agentic RAG**  
- **Date:** 2026-06-25
- **Authors:** Inderjeet Singh, Andrés Murillo, Motoyoshi Sekiya et al.
- **Link:** https://arxiv.org/abs/2606.26793v1
- **Security insight:** Multimodal agentic retrieval-augmented generation (RAG) systems expand the attack surface beyond prompt injection to include text poisoning, image injection, direct-query attacks, and orchestrator-level tool manipulation. Existing red-teaming approaches are…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Agents That Know Too Much: A Data-Centric Survey of Privacy in LLM Agents**  
- **Date:** 2026-06-25
- **Authors:** Nada Lahjouji, Ashwin Gerard Colaco
- **Link:** https://arxiv.org/abs/2606.26627v1
- **Security insight:** Large language model agents increasingly query databases, search document collections, call external APIs, remember past interactions, and act on a user's behalf. As they move from answering questions to operating over sensitive data, privacy becomes harder…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents**  
- **Date:** 2026-06-25
- **Authors:** Praneeth Narisetty, Shiva Nagendra Babu Kore, Uday Kumar Reddy Kattamanchi et al.
- **Link:** https://arxiv.org/abs/2606.26479v1
- **Security insight:** Recent work (2024 to 2026) has converged on a strategy for defending tool-using LLM agents against indirect prompt injection: rather than training the model to refuse malicious instructions, enforce security outside the model with a deterministic policy that…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Beyond Feedforward Networks: Reentry Neural Systems as the Fundamental Basis of Subjecthood and Intrinsic Safety of Next-Generation AGI**  
- **Date:** 2026-06-24
- **Authors:** A. S. Ushakov, Yu. N. Berdinsk
- **Link:** https://arxiv.org/abs/2606.26406v1
- **Security insight:** We propose a complete architectural blueprint for safe artificial general intelligence based on a closed reentry loop (D <-> I cycle). In contrast to feedforward networks, which are directed acyclic graphs (C=0, S=0) incapable of self-reference, the proposed…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Verifying Intent and Harm: A Unified Defense Against LLM-Generated Threats**  
- **Date:** 2026-06-24
- **Authors:** Poojitha Thota, Yun Lei, Santhosh Thangaraj et al.
- **Link:** https://arxiv.org/abs/2606.26377v1
- **Security insight:** Large language models (LLMs) are increasingly deployed in interactive applications, yet they remain vulnerable to adversarial interactions that induce harmful, deceptive, or policy-violating outputs. Existing defenses typically analyze either user prompts or…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**CyberChainBench: Can AI Agents Secure Smart Contracts Against Real-World On-Chain Vulnerabilities?**  
- **Date:** 2026-06-24
- **Authors:** Jintao Huang, Fengqing Jiang, Radha Poovendran et al.
- **Link:** https://arxiv.org/abs/2606.26216v1
- **Security insight:** We present CyberChainBench, a benchmark for evaluating LLM-based agents on smart contract security across three complementary tasks: vulnerability detection, exploit generation, and patch synthesis. Built from 541 real-world exploit incidents from…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

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

### Prompt Injection

**Prompt Injection in Automated Résumé Screening with Large Language Models: Single and Multi-Injection Settings**  
- **Date:** 2026-06-25
- **Authors:** Preet Baxi, Jiannan Xu, Jane Yi Jiang et al.
- **Link:** https://arxiv.org/abs/2606.27287v1
- **Security insight:** Large language models (LLMs) are increasingly used to screen and rank job applicants, creating incentives for candidates to strategically manipulate algorithmic hiring systems. We study prompt injection in automated résumé screening, defined as subtle self-…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**How Reliable Is Your Jailbreak Judge? Calibration and Adversarial Robustness of Automated ASR Scoring**  
- **Date:** 2026-06-24
- **Authors:** Yang Gao
- **Link:** https://arxiv.org/abs/2606.25487v2
- **Security insight:** Almost every paper on LLM jailbreaks and prompt injection reports an attack-success rate (ASR), and that number is assigned not by people but by an automated judge: either a safety classifier trained for the task, or a general chat model prompted to grade.…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**LLM-Based Scientific Peer Review: Methods, Benchmarks, and Reliability Challenges**  
- **Date:** 2026-06-23
- **Authors:** Thi Huyen Nguyen, Zahra Ahmadi
- **Link:** https://arxiv.org/abs/2606.25057v1
- **Security insight:** The rapid growth of scientific submissions has pushed traditional peer review toward its scalability limits, motivating the exploration of large language models (LLMs) as intelligent automated evaluation assistants. Although recent studies show that LLMs can…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

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
