# AI Security Radar

_Last updated (UTC): **2026-03-08**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Beyond Input Guardrails: Reconstructing Cross-Agent Semantic Flows for Execution-Aware Attack Detection**  
- **Date:** 2026-03-04
- **Authors:** Yangyang Wei, Yijie Xu, Zhenyuan Li et al.
- **Link:** https://arxiv.org/abs/2603.04469v1
- **Security insight:** Multi-Agent System is emerging as the \textit{de facto} standard for complex task orchestration. However, its reliance on autonomous execution and unstructured inter-agent communication introduces severe risks, such as indirect prompt injection, that easily…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Goal-Driven Risk Assessment for LLM-Powered Systems: A Healthcare Case Study**  
- **Date:** 2026-03-04
- **Authors:** Neha Nagaraja, Hayretdin Bahsi
- **Link:** https://arxiv.org/abs/2603.03633v1
- **Security insight:** While incorporating LLMs into systems offers significant benefits in critical application areas such as healthcare, new security challenges emerge due to the potential cyber kill chain cycles that combine adversarial model, prompt injection and conventional…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Learning When to Act or Refuse: Guarding Agentic Reasoning Models for Safe Multi-Step Tool Use**  
- **Date:** 2026-03-03
- **Authors:** Aradhye Agarwal, Gurdit Siyan, Yash Pandya et al.
- **Link:** https://arxiv.org/abs/2603.03205v1
- **Security insight:** Agentic language models operate in a fundamentally different safety regime than chat models: they must plan, call tools, and execute long-horizon actions where a single misstep, such as accessing files or entering credentials, can cause irreversible harm.…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Tracking Capabilities for Safer Agents**  
- **Date:** 2026-03-01
- **Authors:** Martin Odersky, Yaoyu Zhao, Yichen Xu et al.
- **Link:** https://arxiv.org/abs/2603.00991v1
- **Security insight:** AI agents that interact with the real world through tool calls pose fundamental safety challenges: agents might leak private information, cause unintended side effects, or be manipulated through prompt injection. To address these challenges, we propose to put…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**From Goals to Aspects, Revisited: An NFR Pattern Language for Agentic AI Systems**  
- **Date:** 2026-02-28
- **Authors:** Yijun Yu
- **Link:** https://arxiv.org/abs/2603.00472v1
- **Security insight:** Agentic AI systems exhibit numerous crosscutting concerns -- security, observability, cost management, fault tolerance -- that are poorly modularized in current implementations, contributing to the high failure rate of AI projects in reaching production. The…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**LiaisonAgent: An Multi-Agent Framework for Autonomous Risk Investigation and Governance**  
- **Date:** 2026-02-27
- **Authors:** Chuanming Tang, Ling Qing, Shifeng Chen
- **Link:** https://arxiv.org/abs/2603.00200v1
- **Security insight:** The rapid evolution of sophisticated cyberattacks has strained modern Security Operations Centers (SOC), which traditionally rely on rule-based or signature-driven detection systems. These legacy frameworks often generate high volumes of technical alerts that…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Image-based Prompt Injection: Hijacking Multimodal LLMs through Visually Embedded Adversarial Instructions**  
- **Date:** 2026-03-04
- **Authors:** Neha Nagaraja, Lan Zhang, Zhilong Wang et al.
- **Link:** https://arxiv.org/abs/2603.03637v1
- **Security insight:** Multimodal Large Language Models (MLLMs) integrate vision and text to power applications, but this integration introduces new vulnerabilities. We study Image-based Prompt Injection (IPI), a black-box attack in which adversarial instructions are embedded into…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Benchmark of Benchmarks: Unpacking Influence and Code Repository Quality in LLM Safety Benchmarks**  
- **Date:** 2026-03-03
- **Authors:** Junjie Chu, Xinyue Shen, Ye Leng et al.
- **Link:** https://arxiv.org/abs/2603.04459v1
- **Security insight:** The rapid growth of research in LLM safety makes it hard to track all advances. Benchmarks are therefore crucial for capturing key trends and enabling systematic comparisons. Yet, it remains unclear why certain benchmarks gain prominence, and no systematic…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**DualSentinel: A Lightweight Framework for Detecting Targeted Attacks in Black-box LLM via Dual Entropy Lull Pattern**  
- **Date:** 2026-03-02
- **Authors:** Xiaoyi Pang, Xuanyi Hao, Pengyu Liu et al.
- **Link:** https://arxiv.org/abs/2603.01574v1
- **Security insight:** Recent intelligent systems integrate powerful Large Language Models (LLMs) through APIs, but their trustworthiness may be critically undermined by targeted attacks like backdoor and prompt injection attacks, which secretly force LLMs to generate specific…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**SwitchCraft: Training-Free Multi-Event Video Generation with Attention Controls**  
- **Date:** 2026-02-27
- **Authors:** Qianxun Xu, Chenxi Song, Yujun Cai et al.
- **Link:** https://arxiv.org/abs/2602.23956v1
- **Security insight:** Recent advances in text-to-video diffusion models have enabled high-fidelity and temporally coherent videos synthesis. However, current models are predominantly optimized for single-event generation. When handling multi-event prompts, without explicit…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**ExpGuard: LLM Content Moderation in Specialized Domains**  
- **Date:** 2026-03-03
- **Authors:** Minseok Choi, Dongjin Kim, Seungbin Yang et al.
- **Link:** https://arxiv.org/abs/2603.02588v1
- **Security insight:** With the growing deployment of large language models (LLMs) in real-world applications, establishing robust safety guardrails to moderate their inputs and outputs has become essential to ensure adherence to safety policies. Current guardrail models…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Model Extraction & Privacy

**Kraken: Higher-order EM Side-Channel Attacks on DNNs in Near and Far Field**  
- **Date:** 2026-03-03
- **Authors:** Peter Horvath, Ilia Shumailov, Lukasz Chmielewski et al.
- **Link:** https://arxiv.org/abs/2603.02891v1
- **Security insight:** The multi-million dollar investment required for modern machine learning (ML) has made large ML models a prime target for theft. In response, the field of model stealing has emerged. Attacks based on physical side-channel information have shown that DNN model…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?
