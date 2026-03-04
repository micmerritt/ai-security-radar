# AI Security Radar

_Last updated (UTC): **2026-03-04**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

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

**AgentSentry: Mitigating Indirect Prompt Injection in LLM Agents via Temporal Causal Diagnostics and Context Purification**  
- **Date:** 2026-02-26
- **Authors:** Tian Zhang, Yiwei Xu, Juan Wang et al.
- **Link:** https://arxiv.org/abs/2602.22724v1
- **Security insight:** Large language model (LLM) agents increasingly rely on external tools and retrieval systems to autonomously complete complex tasks. However, this design exposes agents to indirect prompt injection (IPI), where attacker-controlled context embedded in tool…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Silent Egress: When Implicit Prompt Injection Makes LLM Agents Leak Without a Trace**  
- **Date:** 2026-02-25
- **Authors:** Qianlong Lan, Anuj Kaul, Shaun Jones et al.
- **Link:** https://arxiv.org/abs/2602.22450v1
- **Security insight:** Agentic large language model systems increasingly automate tasks by retrieving URLs and calling external tools. We show that this workflow gives rise to implicit prompt injection: adversarial instructions embedded in automatically generated URL previews,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**"Are You Sure?": An Empirical Study of Human Perception Vulnerability in LLM-Driven Agentic Systems**  
- **Date:** 2026-02-24
- **Authors:** Xinfeng Li, Shenyu Dai, Kelong Zheng et al.
- **Link:** https://arxiv.org/abs/2602.21127v1
- **Security insight:** Large language model (LLM) agents are rapidly becoming trusted copilots in high-stakes domains like software development and healthcare. However, this deepening trust introduces a novel attack surface: Agent-Mediated Deception (AMD), where compromised agents…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**SoK: Agentic Skills -- Beyond Tool Use in LLM Agents**  
- **Date:** 2026-02-24
- **Authors:** Yanna Jiang, Delong Li, Haiyu Deng et al.
- **Link:** https://arxiv.org/abs/2602.20867v1
- **Security insight:** Agentic systems increasingly rely on reusable procedural capabilities, \textit{a.k.a., agentic skills}, to execute long-horizon workflows reliably. These capabilities are callable modules that package procedural knowledge with explicit applicability…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

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

**Reverse CAPTCHA: Evaluating LLM Susceptibility to Invisible Unicode Instruction Injection**  
- **Date:** 2026-02-26
- **Authors:** Marcus Graves
- **Link:** https://arxiv.org/abs/2603.00164v1
- **Security insight:** We introduce Reverse CAPTCHA, an evaluation framework that tests whether large language models follow invisible Unicode-encoded instructions embedded in otherwise normal-looking text. Unlike traditional CAPTCHAs that distinguish humans from machines, our…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**ExpGuard: LLM Content Moderation in Specialized Domains**  
- **Date:** 2026-03-03
- **Authors:** Minseok Choi, Dongjin Kim, Seungbin Yang et al.
- **Link:** https://arxiv.org/abs/2603.02588v1
- **Security insight:** With the growing deployment of large language models (LLMs) in real-world applications, establishing robust safety guardrails to moderate their inputs and outputs has become essential to ensure adherence to safety policies. Current guardrail models…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Poisoning & Backdoors

**Poisoned Acoustics**  
- **Date:** 2026-02-25
- **Authors:** Harrison Dahme
- **Link:** https://arxiv.org/abs/2602.22258v1
- **Security insight:** Training-data poisoning attacks can induce targeted, undetectable failure in deep neural networks by corrupting a vanishingly small fraction of training labels. We demonstrate this on acoustic vehicle classification using the MELAUDIS urban intersection…
- **Build idea:** Build a minimal poisoning simulator plus simple detectors (trigger search, label flip tests, anomaly baselines).

### Model Extraction & Privacy

**Kraken: Higher-order EM Side-Channel Attacks on DNNs in Near and Far Field**  
- **Date:** 2026-03-03
- **Authors:** Peter Horvath, Ilia Shumailov, Lukasz Chmielewski et al.
- **Link:** https://arxiv.org/abs/2603.02891v1
- **Security insight:** The multi-million dollar investment required for modern machine learning (ML) has made large ML models a prime target for theft. In response, the field of model stealing has emerged. Attacks based on physical side-channel information have shown that DNN model…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?
