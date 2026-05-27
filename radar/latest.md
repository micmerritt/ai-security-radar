# AI Security Radar

_Last updated (UTC): **2026-05-27**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Cordon-MAS: Defending RAG against Knowledge Poisoning via Information-Flow Control**  
- **Date:** 2026-05-26
- **Authors:** Zhe Yu, Wenpeng Xing, Gaolei Li et al.
- **Link:** https://arxiv.org/abs/2605.26754v1
- **Security insight:** Retrieval-augmented generation (RAG) increasingly underpins high-stakes applications, yet remains vulnerable to Confundo-style poisoning where adversarially optimized documents manipulate generated outputs. Existing defenses assume that detecting poisoned…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Aligning Provenance with Authorization: A Dual-Graph Defense for LLM Agents**  
- **Date:** 2026-05-26
- **Authors:** Peiran Wang, Ying Li, Yuan Tian
- **Link:** https://arxiv.org/abs/2605.26497v1
- **Security insight:** LLM-based agents are increasingly deployed in high-stakes scenarios such as email management, financial transactions, and code execution, where they interact with the external world through tool calling. During execution, these agents must read external data…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**AgentSecBench: Measuring Prompt Injection, Privacy Leakage, and Tool-Use Integrity in LLM Agents**  
- **Date:** 2026-05-25
- **Authors:** Faruk Alpay, Taylan Alpay
- **Link:** https://arxiv.org/abs/2605.26269v1
- **Security insight:** LLM agents process trusted instructions, retrieved records, and tool observations through a common generative channel. This conflates data flow with authority: an untrusted string can affect a secret-bearing response or an action proposal even when no…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**How Agentic AI Coding Assistants Become the Attacker's Shell**  
- **Date:** 2026-05-25
- **Authors:** Yue Liu, Yanjie Zhao, Yunbo Lyu et al.
- **Link:** https://arxiv.org/abs/2605.25871v1
- **Security insight:** Agentic AI coding assistants can edit files, run commands, and access the internet on behalf of developers. However, their reliance on unvetted external artifacts introduces a new attack vector. Hidden instructions in external artifacts can hijack these…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Device Context Protocol: A Compact, Safety-First Architecture for LLM-Driven Control of Constrained Devices**  
- **Date:** 2026-05-24
- **Authors:** Dongxu Yang
- **Link:** https://arxiv.org/abs/2605.26159v1
- **Security insight:** Large language models are increasingly used as orchestrators of external tools via the Model Context Protocol (MCP), but MCP is built for software services with megabytes of memory and does not descend to the microcontrollers that dominate the long tail of…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**IterInject: Indirect Prompt Injection Against LLM Agents via Feedback-Guided Iterative Optimization**  
- **Date:** 2026-05-23
- **Authors:** Zixuan Chen, Jiaxiang Chen, Li Luo et al.
- **Link:** https://arxiv.org/abs/2605.24659v1
- **Security insight:** LLM-based agents are increasingly deployed for complex tasks requiring planning, tool use, and interaction with external services. Their reliance on untrusted external content exposes them to indirect prompt injection (IPI), in which adversarial instructions…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Poisoning the Watchtower: Prompt Injection Attacks Against LLM-Augmented Security Operations Through Adversarial Log Content**  
- **Date:** 2026-05-23
- **Authors:** Rohan Pandey, Archit Bhujang
- **Link:** https://arxiv.org/abs/2605.24421v1
- **Security insight:** Large language models (LLMs) are increasingly used as analyst assistants in security operations centers (SOCs), where they ingest log and alert data to produce triage labels, incident summaries, or remediation advice. We study a structural failure mode of…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Prompt Injection Detection is Regime-Dependent: A Deployment-Aware Evaluation with Interpretable Structural Signals**  
- **Date:** 2026-05-26
- **Authors:** Akindoyin Akinrele, Shreyank N Gowda
- **Link:** https://arxiv.org/abs/2605.26999v1
- **Security insight:** Prompt injection poses a critical threat to the safe deployment of large language models, yet existing detection approaches are typically evaluated under limited settings that do not reflect real-world operating constraints. In this work, we present a…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Cordyceps: Covert Control Attacks on LLMs via Data Poisoning**  
- **Date:** 2026-05-26
- **Authors:** Zedian Shao, Charles Fleming, Teodora Baluta
- **Link:** https://arxiv.org/abs/2605.26595v1
- **Security insight:** Large language models (LLMs) are often fine-tuned on uncurated text datasets that adversaries can poison. Existing poisoning attacks primarily rely on fixed trigger phrases that defenses such as outlier detection, clean-data regularization, or online…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**LLM-as-a-Reviewer: Benchmarking Their Ability, Divergence, and Prompt Injection Resistance as Paper Reviewers**  
- **Date:** 2026-05-25
- **Authors:** Lingyao Li, Junjie Xiong, Changjia Zhu et al.
- **Link:** https://arxiv.org/abs/2605.25415v1
- **Security insight:** Large language models (LLMs) are increasingly used in academic peer review, yet their reliability, alignment with human judgment, and robustness to adversarial attacks remain poorly understood. We present a systematic benchmark of LLM-as-a-Reviewer on 898…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Localization then Neutralization: Gradient-guided Token Suppression against Visual Prompt Injection Attack**  
- **Date:** 2026-05-24
- **Authors:** Dongpeng Zhang, Ke Ma, Yangbangyan Jiang et al.
- **Link:** https://arxiv.org/abs/2605.25194v1
- **Security insight:** Adversarial images pose a severe security threat to multimodal large language models through prompt injection. Existing defenses largely lack a principled understanding of the underlying mechanisms and struggle to balance efficiency and defense utility. In…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**MixFake: Benchmarking and Enhancing Audio Deepfake Detection in Diverse Real-world Mixed Audio**  
- **Date:** 2026-05-22
- **Authors:** Qingcao Li, Yipeng Lin, Weichen Lian et al.
- **Link:** https://arxiv.org/abs/2605.23201v1
- **Security insight:** Speech deepfake detection has achieved remarkable success in clean environments but faces significant challenges in complex, real-world scenarios where speech is often mixed with background music or noise. Current state-of-the-art methods rely on semantic…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Prompt Overflow: What the Guardrail Inspects Is Not What the Model Infers**  
- **Date:** 2026-05-22
- **Authors:** Yuanbo Zhou, Changjia Zhu, Junyu Wang et al.
- **Link:** https://arxiv.org/abs/2605.23196v1
- **Security insight:** Guardrail models (a.k.a. safety checkers) are widely deployed to screen user inputs before they reach large language models (LLMs), serving as a primary defense against prompt injection attacks. Due to strict context constraints, these models handle…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**Ellipsoid Control: A White-list Jailbreak Defense via Benign Latent Modeling**  
- **Date:** 2026-05-23
- **Authors:** Luoyu Chen, Weiqi Wang, Zhiyi Tian et al.
- **Link:** https://arxiv.org/abs/2605.24552v1
- **Security insight:** Representation engineering (RepE) defenses have shown strong robustness against jailbreak attacks on large language models (LLMs). However, these methods fundamentally rely on black-list supervision: they learn jailbreak-to-refusal activation transformations…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.
