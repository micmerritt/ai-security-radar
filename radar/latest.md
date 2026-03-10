# AI Security Radar

_Last updated (UTC): **2026-03-10**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**SlowBA: An efficiency backdoor attack towards VLM-based GUI agents**  
- **Date:** 2026-03-09
- **Authors:** Junxian Li, Tu Lan, Haozhen Tan et al.
- **Link:** https://arxiv.org/abs/2603.08316v1
- **Security insight:** Modern vision-language-model (VLM) based graphical user interface (GUI) agents are expected not only to execute actions accurately but also to respond to user instructions with low latency. While existing research on GUI-agent security mainly focuses on…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Governance Architecture for Autonomous Agent Systems: Threats, Framework, and Engineering Practice**  
- **Date:** 2026-03-07
- **Authors:** Yuxu Ge
- **Link:** https://arxiv.org/abs/2603.07191v1
- **Security insight:** Autonomous agents powered by large language models introduce a class of execution-layer vulnerabilities -- prompt injection, retrieval poisoning, and uncontrolled tool invocation -- that existing guardrails fail to address systematically. In this work, we…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

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

### Prompt Injection

**VoiceSHIELD-Small: Real-Time Malicious Speech Detection and Transcription**  
- **Date:** 2026-03-08
- **Authors:** Sumit Ranjan, Sugandha Sharma, Ubaid Abbas et al.
- **Link:** https://arxiv.org/abs/2603.07708v1
- **Security insight:** Voice interfaces are quickly becoming a common way for people to interact with AI systems. This also brings new security risks, such as prompt injection, social engineering, and harmful voice commands. Traditional security methods rely on converting speech to…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

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

### RAG & Retrieval Attacks

**ExpGuard: LLM Content Moderation in Specialized Domains**  
- **Date:** 2026-03-03
- **Authors:** Minseok Choi, Dongjin Kim, Seungbin Yang et al.
- **Link:** https://arxiv.org/abs/2603.02588v1
- **Security insight:** With the growing deployment of large language models (LLMs) in real-world applications, establishing robust safety guardrails to moderate their inputs and outputs has become essential to ensure adherence to safety policies. Current guardrail models…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Poisoning & Backdoors

**Client-Cooperative Split Learning**  
- **Date:** 2026-03-09
- **Authors:** Haiyu Deng, Yanna Jiang, Guangsheng Yu et al.
- **Link:** https://arxiv.org/abs/2603.08421v1
- **Security insight:** Model training is increasingly offered as a service for resource-constrained data owners to build customized models. Split Learning (SL) enables such services by offloading training computation under privacy constraints, and evolves toward serverless and…
- **Build idea:** Build a minimal poisoning simulator plus simple detectors (trigger search, label flip tests, anomaly baselines).

### Model Extraction & Privacy

**Kraken: Higher-order EM Side-Channel Attacks on DNNs in Near and Far Field**  
- **Date:** 2026-03-03
- **Authors:** Peter Horvath, Ilia Shumailov, Lukasz Chmielewski et al.
- **Link:** https://arxiv.org/abs/2603.02891v1
- **Security insight:** The multi-million dollar investment required for modern machine learning (ML) has made large ML models a prime target for theft. In response, the field of model stealing has emerged. Attacks based on physical side-channel information have shown that DNN model…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?
