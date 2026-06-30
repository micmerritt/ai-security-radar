# AI Security Radar

_Last updated (UTC): **2026-06-30**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Forensic Trajectory Signatures for Agent Memory Poisoning Detection**  
- **Date:** 2026-06-29
- **Authors:** Jun Wen Leong
- **Link:** https://arxiv.org/abs/2606.30566v1
- **Security insight:** We discover a behavioral invariant in LLM agents under persistent memory poisoning: in architectures where routing information is retrieved through observable memory-tool invocations, successful attacks require calling memory_recall_fact before…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Agent Security Meets Regulatory Reality -- A Practitioner Systematization of Autonomous-Agent Threats and Controls in Regulated Financial Systems**  
- **Date:** 2026-06-28
- **Authors:** Krishna Mohan, Guda Nagavenkata Srinivasa
- **Link:** https://arxiv.org/abs/2606.29142v1
- **Security insight:** Large language model agents are entering regulated financial systems, yet the security literature characterizing their attack surface is almost entirely laboratory-based, and the practitioner guidance on regulated deployment is neither peer-reviewed nor…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**From Determinism to Delegation: AI-Native Software Engineering and the Evolution of the Agentic Engineer**  
- **Date:** 2026-06-27
- **Authors:** Mamdouh Alenezi
- **Link:** https://arxiv.org/abs/2606.28791v1
- **Security insight:** Software engineering is experiencing its most significant transformation since the emergence of high-level programming languages. As large language models (LLMs) increasingly enable sustained, multi-step, tool-mediated execution, engineering value is shifting…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Why Trust Your Agent? Empirical Security Gains from TRiSM-Guided Agentic Workflows in Healthcare**  
- **Date:** 2026-06-27
- **Authors:** Liam Kearns
- **Link:** https://arxiv.org/abs/2606.28666v1
- **Security insight:** Agent-based AI has enabled the automation of tasks by exposing application tools and resources to large language models (LLMs). However, to improve scope and accuracy, agents are often given access rights that exceed those of ordinary users, introducing…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**LLM agents security duality: a comprehensive survey of self-security and empowered cybersecurity**  
- **Date:** 2026-06-26
- **Authors:** Yiwei Xu, Yong Zhuang, Xuanming Liu et al.
- **Link:** https://arxiv.org/abs/2606.28450v1
- **Security insight:** Large language model (LLM) agents are rapidly being integrated into real-world systems. Their autonomy and tool-use capabilities generate substantial value while simultaneously expanding the security attack surface. This survey provides a comprehensive…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

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

### Prompt Injection

**IHDec: Divergence-Steered Contrastive Decoding for Securing Multi-Turn Instruction Hierarchies**  
- **Date:** 2026-06-29
- **Authors:** Nicole Geumheon Liu, Haeun Jang, Yonghyun Jun et al.
- **Link:** https://arxiv.org/abs/2606.29960v1
- **Security insight:** Large Language Models (LLMs) often fail to maintain instruction hierarchies (IH) when processing multi-source inputs with varying role-level priorities, paradoxically adhering to lower-priority directives during conflicts. While existing defenses mitigate…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**An Empirical Evaluation of Prompt Injection Vulnerabilities in Large Language Models Across Multilingual and Obfuscated Attack Scenarios**  
- **Date:** 2026-06-28
- **Authors:** Caglar Uysal, Baturay Birinci, Süha Orhun Mutluergil et al.
- **Link:** https://arxiv.org/abs/2606.29602v1
- **Security insight:** Large Language Models (LLMs) have rapidly evolved, transforming industries by automating complex tasks and generating human-like content. However, as their adoption accelerates, prompt injection vulnerabilities have become increasingly apparent. Malicious…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**RIPA: Sensory-Vector Prompt Injection Attacks on LLM-Controlled ROS 2 Robots**  
- **Date:** 2026-06-26
- **Authors:** Nima Dorzhiev
- **Link:** https://arxiv.org/abs/2606.28649v1
- **Security insight:** We present RIPA, the first systematic multi-channel empirical study of prompt injection attacks delivered through the sensory pipeline of a ROS 2-based LLM-controlled robotic system. Across 100 independent runs per injection variant on five LLMs spanning four…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**On the Inseparability of Instructions and Data in Shared-Embedding Sequence Models**  
- **Date:** 2026-06-25
- **Authors:** Dewank Pant, Shruti Lohani, Avijit Kumar
- **Link:** https://arxiv.org/abs/2606.27567v1
- **Security insight:** Prompt injection is the top security risk for LLM-integrated applications, yet every defense proposed so far has been broken. We prove this is not a coincidence: in shared-embedding architectures that lack enforced control-data separation, perfect prompt-…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Prompt Injection in Automated Résumé Screening with Large Language Models: Single and Multi-Injection Settings**  
- **Date:** 2026-06-25
- **Authors:** Preet Baxi, Jiannan Xu, Jane Yi Jiang et al.
- **Link:** https://arxiv.org/abs/2606.27287v1
- **Security insight:** Large language models (LLMs) are increasingly used to screen and rank job applicants, creating incentives for candidates to strategically manipulate algorithmic hiring systems. We study prompt injection in automated résumé screening, defined as subtle self-…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**SCARCE: Scalable Cascade Analysis for Rare-event Characterisation via Embeddings**  
- **Date:** 2026-06-28
- **Authors:** Yingjie Wang, Yi Dong, Edmund Lau et al.
- **Link:** https://arxiv.org/abs/2606.29623v1
- **Security insight:** Rare events govern the safety profile of modern AI systems, yet their probabilities are extremely difficult to estimate: direct Monte Carlo requires prohibitive sample budgets. Subset Simulation (SS) addresses this by decomposing a rare-event probability into…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.
