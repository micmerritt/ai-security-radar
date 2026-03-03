# AI Security Radar

_Last updated (UTC): **2026-03-03**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

`prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability`

## New / recent research (arXiv)

### DualSentinel: A Lightweight Framework for Detecting Targeted Attacks in Black-box LLM via Dual Entropy Lull Pattern

- **Date:** 2026-03-02

- **Authors:** Xiaoyi Pang, Xuanyi Hao, Pengyu Liu et al.

- **Link:** https://arxiv.org/abs/2603.01574v1

- **Why it matters:** Recent intelligent systems integrate powerful Large Language Models (LLMs) through APIs, but their trustworthiness may be critically undermined by targeted attacks like backdoor and prompt injection attacks, which secretly force LLMs to generate specific…

- **Build hook:** What would a minimal test harness / dataset / detection rule look like for this?


### Tracking Capabilities for Safer Agents

- **Date:** 2026-03-01

- **Authors:** Martin Odersky, Yaoyu Zhao, Yichen Xu et al.

- **Link:** https://arxiv.org/abs/2603.00991v1

- **Why it matters:** AI agents that interact with the real world through tool calls pose fundamental safety challenges: agents might leak private information, cause unintended side effects, or be manipulated through prompt injection. To address these challenges, we propose to put…

- **Build hook:** What would a minimal test harness / dataset / detection rule look like for this?


### From Goals to Aspects, Revisited: An NFR Pattern Language for Agentic AI Systems

- **Date:** 2026-02-28

- **Authors:** Yijun Yu

- **Link:** https://arxiv.org/abs/2603.00472v1

- **Why it matters:** Agentic AI systems exhibit numerous crosscutting concerns -- security, observability, cost management, fault tolerance -- that are poorly modularized in current implementations, contributing to the high failure rate of AI projects in reaching production. The…

- **Build hook:** What would a minimal test harness / dataset / detection rule look like for this?


### From Signals to Causes: A Causal Signal Processing Framework for Robust and Interpretable Clinical Risk Prediction

- **Date:** 2026-02-27

- **Authors:** Surajit Das, Maxine Tan

- **Link:** https://arxiv.org/abs/2602.23977v1

- **Why it matters:** Learning-based signal processing systems increasingly support high-stakes medical decisions using heterogeneous biomedical signals, including medical images, physiological time series, and clinical records. Despite strong predictive performance, many models…

- **Build hook:** What would a minimal test harness / dataset / detection rule look like for this?


### SwitchCraft: Training-Free Multi-Event Video Generation with Attention Controls

- **Date:** 2026-02-27

- **Authors:** Qianxun Xu, Chenxi Song, Yujun Cai et al.

- **Link:** https://arxiv.org/abs/2602.23956v1

- **Why it matters:** Recent advances in text-to-video diffusion models have enabled high-fidelity and temporally coherent videos synthesis. However, current models are predominantly optimized for single-event generation. When handling multi-event prompts, without explicit…

- **Build hook:** What would a minimal test harness / dataset / detection rule look like for this?


### LiaisonAgent: An Multi-Agent Framework for Autonomous Risk Investigation and Governance

- **Date:** 2026-02-27

- **Authors:** Chuanming Tang, Ling Qing, Shifeng Chen

- **Link:** https://arxiv.org/abs/2603.00200v1

- **Why it matters:** The rapid evolution of sophisticated cyberattacks has strained modern Security Operations Centers (SOC), which traditionally rely on rule-based or signature-driven detection systems. These legacy frameworks often generate high volumes of technical alerts that…

- **Build hook:** What would a minimal test harness / dataset / detection rule look like for this?


### AgentSentry: Mitigating Indirect Prompt Injection in LLM Agents via Temporal Causal Diagnostics and Context Purification

- **Date:** 2026-02-26

- **Authors:** Tian Zhang, Yiwei Xu, Juan Wang et al.

- **Link:** https://arxiv.org/abs/2602.22724v1

- **Why it matters:** Large language model (LLM) agents increasingly rely on external tools and retrieval systems to autonomously complete complex tasks. However, this design exposes agents to indirect prompt injection (IPI), where attacker-controlled context embedded in tool…

- **Build hook:** What would a minimal test harness / dataset / detection rule look like for this?


### Reverse CAPTCHA: Evaluating LLM Susceptibility to Invisible Unicode Instruction Injection

- **Date:** 2026-02-26

- **Authors:** Marcus Graves

- **Link:** https://arxiv.org/abs/2603.00164v1

- **Why it matters:** We introduce Reverse CAPTCHA, an evaluation framework that tests whether large language models follow invisible Unicode-encoded instructions embedded in otherwise normal-looking text. Unlike traditional CAPTCHAs that distinguish humans from machines, our…

- **Build hook:** What would a minimal test harness / dataset / detection rule look like for this?


### Silent Egress: When Implicit Prompt Injection Makes LLM Agents Leak Without a Trace

- **Date:** 2026-02-25

- **Authors:** Qianlong Lan, Anuj Kaul, Shaun Jones et al.

- **Link:** https://arxiv.org/abs/2602.22450v1

- **Why it matters:** Agentic large language model systems increasingly automate tasks by retrieving URLs and calling external tools. We show that this workflow gives rise to implicit prompt injection: adversarial instructions embedded in automatically generated URL previews,…

- **Build hook:** What would a minimal test harness / dataset / detection rule look like for this?


### Poisoned Acoustics

- **Date:** 2026-02-25

- **Authors:** Harrison Dahme

- **Link:** https://arxiv.org/abs/2602.22258v1

- **Why it matters:** Training-data poisoning attacks can induce targeted, undetectable failure in deep neural networks by corrupting a vanishingly small fraction of training labels. We demonstrate this on acoustic vehicle classification using the MELAUDIS urban intersection…

- **Build hook:** What would a minimal test harness / dataset / detection rule look like for this?
