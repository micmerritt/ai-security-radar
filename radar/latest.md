# AI Security Radar

_Last updated (UTC): **2026-10-01**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

**Aletheia: Permission-Minimality Testing for Coding-Agent Rules**  
- **Date:** 2026-09-30
- **Authors:** Jieke Shi, Yuchen Chen, Junda He et al.
- **Link:** https://arxiv.org/abs/2609.39678v1
- **Security insight:** Repository instruction files guide coding agents, but also expose them to prompt injection. Malicious rules can request credential access or data transfer while the agent produces a correct patch. We present Aletheia, a framework for permission-minimality…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Where Do LLMs Decide to Break the Rules? Mechanistic Localization of Prompt Injection Compliance**  
- **Date:** 2026-09-29
- **Authors:** Rui Wen, Jiayang Liu, Zeyu Yang et al.
- **Link:** https://arxiv.org/abs/2609.37737v1
- **Security insight:** When a prompt injection attack succeeds, a Large Language Model (LLM) abandons its assigned system role to comply with an adversarial instruction. While prior work has extensively quantified how often this occurs, we ask a more fundamental question: where…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**ToolFence: Fine-Grained Authorization for Secure Tool-Using LLM Agents**  
- **Date:** 2026-09-29
- **Authors:** Yanjie Li, Xiangyu He, Xuelong Dai et al.
- **Link:** https://arxiv.org/abs/2609.37196v1
- **Security insight:** Tool-using LLM agents remain vulnerable to indirect prompt injection because trusted instructions and untrusted observations share one context, allowing malicious content to steer consequential input-filtering defenses. Multi-path consensus defenses still…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Selecting The Most Informative Tokens in Natural Language Autoencoders**  
- **Date:** 2026-09-29
- **Authors:** Federico Torrielli, Gianluca Barmina, Andrea Blasi Núñez et al.
- **Link:** https://arxiv.org/abs/2609.37040v1
- **Security insight:** Natural language autoencoders translate a language model's internal activations into readable explanations. Explaining every token position is costly. Which positions should an auditor inspect to understand a potential threat? We study this question across…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**ContractWarden: Kernel-Enforced Damage Boundaries for AI Agents via Human-Authorized Contracts**  
- **Date:** 2026-09-29
- **Authors:** Dongxu Cui, Zhichao Gu, Ping Zheng et al.
- **Link:** https://arxiv.org/abs/2609.38248v1
- **Security insight:** Large language model agents can execute commands, create subprocesses, and directly access files and networks, allowing prompt injection or planning errors to become operating-system side effects. We present ContractWarden, a Linux reference monitor that…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**pikit: A Composable Toolkit for Indirect Prompt Injection Research and Evaluation**  
- **Date:** 2026-09-29
- **Authors:** Zonghao Ying, Xiangfan Wu, Bo Yang et al.
- **Link:** https://arxiv.org/abs/2609.36817v1
- **Security insight:** Indirect prompt injection embeds malicious instructions within external content retrieved by LLM-based agents, altering target behavior without user authorization. We introduce pikit, a research toolkit designed to systematically evaluate these threats across…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Self-Evolving Defense: Continual Security Policy Learning for LLM Agents**  
- **Date:** 2026-09-29
- **Authors:** Minh Nhat Le, Nisarga Gondi, Yibo Peng et al.
- **Link:** https://arxiv.org/abs/2609.36603v1
- **Security insight:** Large language models (LLMs) increasingly power agents that access sensitive information, use external tools, and modify software repositories. Although these capabilities offer substantial benefits, they also create security risks such as jailbreaks, prompt…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Divide and Inject: Can Agents Reconstruct an Indirect Prompt Injection from Fragments?**  
- **Date:** 2026-09-29
- **Authors:** Michael Lee, Zhipeng Wei, Yue Dong et al.
- **Link:** https://arxiv.org/abs/2609.36576v1
- **Security insight:** Agentic systems are now being widely used to orchestrate tools and reason over long contexts. However, the improving capabilities of the large language models powering these agents also create new attack surfaces for indirect prompt injection. In particular,…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**CounterSteer: Suppressing Indirect Prompt Injection with Activation Steering**  
- **Date:** 2026-09-29
- **Authors:** Mark Russinovich
- **Link:** https://arxiv.org/abs/2609.36570v1
- **Security insight:** Indirect prompt injection makes an LLM agent treat untrusted retrieved text as instructions. We present CounterSteer, an inference-time defense that suppresses this behavior inside the model. Per model, a five-step recipe fits a residual-stream direction from…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Render Before Reading: Visual Rendering as a Prompt Injection Defense**  
- **Date:** 2026-09-28
- **Authors:** Jie Zhang, Andrei Baroian, Jan N. van Rijn et al.
- **Link:** https://arxiv.org/abs/2609.36121v1
- **Security insight:** Large language models are vulnerable to prompt injection attacks, where third-party adversarial content can hijack the model's behavior. In this paper, we study the role played by the adversarial data's input modality, and identify a systematic asymmetry:…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Tracekit: Tamper-Evident Intent-Reasoning-Action Auditing for Autonomous Coding Agents**  
- **Date:** 2026-09-28
- **Authors:** Bravish Ghosh
- **Link:** https://arxiv.org/abs/2609.35659v1
- **Security insight:** Autonomous coding agents read untrusted files, run shell commands and spawn sub-agents with little supervision, yet their record is usually an editable log. We present Tracekit, an open-source, dependency-free system that captures three channels for every…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Same Bytes, Different Authority: Reserved-Token Representations in Chat-Template Prompt Injection**  
- **Date:** 2026-09-28
- **Authors:** Yan Zhan, Yunze Song, Mengkai Hou et al.
- **Link:** https://arxiv.org/abs/2609.35932v1
- **Security insight:** Prompt injection against LLM agents becomes much stronger when the injected instruction is wrapped in the model's own chat template. A forged template marker such as <|im_start|> can reach the model either as a single reserved control token or as a sequence…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### Adversarial ML

**Deep Learning Latency Attacks and Defenses: A Cross-Domain Survey of Availability Threats**  
- **Date:** 2026-09-29
- **Authors:** Zonghua Gu, Zeyu Gao, Amin Saremi et al.
- **Link:** https://arxiv.org/abs/2609.36732v1
- **Security insight:** Adversarial machine learning has focused mainly on integrity, but availability is an increasingly consequential complement. Latency attacks (also energy-latency attacks) increase inference-time work, energy, or response time, causing deadline misses,…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

### Agent & Tool Security

**CoSec: Benchmarking Agent Security in Communities**  
- **Date:** 2026-09-28
- **Authors:** Hao Chen, Wenhui Dong, Ye Chen et al.
- **Link:** https://arxiv.org/abs/2609.34790v2
- **Security insight:** LLM agents operate in persistent collaborative environments involving multiple users, communities, memories, files, and tools. Community boundaries may remain fixed or evolve with changes in membership, roles, composition, and relationships. Agents must…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.
