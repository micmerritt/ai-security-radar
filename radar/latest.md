# AI Security Radar

_Last updated (UTC): **2026-08-11**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Stealing Reasoning Traces from Proprietary LLM APIs**  
- **Date:** 2026-08-10
- **Authors:** Alexander Panfilov, David Schmotz, Ilia Shumailov et al.
- **Link:** https://arxiv.org/abs/2608.09867v1
- **Security insight:** Leading large language model providers now conceal their models' step-by-step reasoning, or chain-of-thought, to protect intellectual property and limit information leakage. Rather than storing these traces server-side, providers return them to the client as…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Same Question, Different Answer? Measuring and Mitigating Prompt Privilege for Equitable AI Access**  
- **Date:** 2026-08-09
- **Authors:** Lier Jin, Lan Hu, Binqi Shen et al.
- **Link:** https://arxiv.org/abs/2608.08942v1
- **Security insight:** Large language models (LLMs) are increasingly integrated into healthcare, education, public services, and everyday decision making. They should provide comparable assistance regardless of a user's literacy, communication style, or prompt-engineering…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Not an A11y: How Android Accessibility Exposes Mobile AI Agents to Indirect Prompt Injection**  
- **Date:** 2026-08-09
- **Authors:** Rahul Deivasigamani, Sayeda Faatin Alvi, Derqui Andrea et al.
- **Link:** https://arxiv.org/abs/2608.08939v1
- **Security insight:** The rise of autonomous AI agents represents a major paradigm shift in how users interact with mobile devices. Frameworks such as MobileRun and Mobile-Use can autonomously navigate Android applications and execute complex multi-step tasks. To interpret user…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Toward Metacognitive One-Shot Indirect Prompt Injection: Strategy Abstraction Via Outcome-Conditioned Reflection**  
- **Date:** 2026-08-09
- **Authors:** Sihan Hou, Xinmeng Hou, Zhijun Zhang et al.
- **Link:** https://arxiv.org/abs/2608.08795v1
- **Security insight:** Tool-using large language model (LLM) agents are vulnerable to indirect prompt injection (IPI), in which malicious instructions embedded in external observations manipulate subsequent agent decisions and actions. Most existing adaptive attacks rely on…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**SkillsMetric: Mapping the Detection Boundary of Static Analysis for Malicious Agent Skills**  
- **Date:** 2026-08-09
- **Authors:** Xinze Chen, Chi Zhang, Ping Ji et al.
- **Link:** https://arxiv.org/abs/2608.08468v1
- **Security insight:** Agent Skills---structured packages of instructions and scripts that augment LLM-based agents---are rapidly proliferating, yet their security properties remain under-explored. We present \textsc{SkillsMetric}, a five-stage static analysis framework that scores…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Defending Retrieval-Augmented Intrusion Detection Against Knowledge Poisoning and Prompt Injection**  
- **Date:** 2026-08-08
- **Authors:** Kaysarul Anas Apurba, Md. Hasibul Hasan, Mahedee Zaman Moon et al.
- **Link:** https://arxiv.org/abs/2608.08100v1
- **Security insight:** Retrieval-Augmented Generation (RAG) enables large language models to classify network flows and generate human-readable incident reports by retrieving semantically similar historical traffic from a vector knowledge base. However, the retrieval layer…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**The Anatomy of a Prompt Injection: A Component Model for Structured Analysis**  
- **Date:** 2026-08-07
- **Authors:** Jeremy McHugh
- **Link:** https://arxiv.org/abs/2608.07808v1
- **Security insight:** Four years after prompt injection was first identified in 2022, attacks are still predominantly documented as verbatim strings rather than structured exploits, despite advancing agent capabilities and threat actors embedding injections to subvert AI-assisted…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**NiyamAI - An Intent-Bound AI Agent with Cryptographically Verifiable Guardrails using Zero-Knowledge Proofs**  
- **Date:** 2026-08-07
- **Authors:** Aditya Katkar, Om Karkele, Kartik Mandhane et al.
- **Link:** https://arxiv.org/abs/2608.07167v1
- **Security insight:** Giving an AI agent the ability to send emails, query databases, or execute commands is useful--until the agent is tricked into doing something it shouldn't. Prompt injection, hallucinated reasoning, and unsafe tool calls form the primary attack surface for…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**StepJack: Benchmarking Computer-Use Agent Safety Against Multi-Step Indirect Prompt Injection**  
- **Date:** 2026-08-06
- **Authors:** Zhuoxin Zhan, Akbar Rafiey, Avery Ma et al.
- **Link:** https://arxiv.org/abs/2608.06477v1
- **Security insight:** Computer-use agents (CUAs) face a growing threat from indirect prompt injection, where adversarial instructions are planted in the environment such as web pages. In this paper, we introduce multi-step indirect prompt injection, a new attack class against CUAs…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**PromptShield Home: Ambient Multimodal Prompt Injection Defense for Smart-Home Agents**  
- **Date:** 2026-08-06
- **Authors:** He Zhang, Feilong Li, Dingning Long et al.
- **Link:** https://arxiv.org/abs/2608.05495v1
- **Security insight:** Smart-home assistants increasingly use multimodal large language models (MLLMs) that perceive video and audio directly. This raises a safety question specific to the home: can the agent tell a genuine user command from ambient or externally-sourced content,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**BASIS: Breach-Aware Selective Prompt Injection Shielding with Prefill Attention Probes**  
- **Date:** 2026-08-08
- **Authors:** Laiqiao Qin, Tianqing Zhu, Longxiang Gao et al.
- **Link:** https://arxiv.org/abs/2608.08027v1
- **Security insight:** Prompt injection is a critical security threat in large language model (LLM) applications, where attackers hijack model behavior by embedding malicious instructions in user or external data. Existing detection methods only detect the presence of injection and…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Hijacking Robots with a Piece of Paper: A Systematic Study of Physical Prompt Injection in VLM-Controlled Robots**  
- **Date:** 2026-08-06
- **Authors:** S. M . Bhagya P. Samarakoon, M. A. Viraj J. Muthugala, W. K. R. Sachinthana et al.
- **Link:** https://arxiv.org/abs/2608.05715v1
- **Security insight:** Vision-Language Models (VLMs) are increasingly deployed as planners in robotic systems, where they translate natural-language commands into executable actions grounded in visual scene understanding. This tight coupling between perception and instruction-…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**When Context Bites: Detecting RAG Poisoning via Document-Level Attention Collapse**  
- **Date:** 2026-08-07
- **Authors:** Yingtao Ren, Ziyi Zhao, Yiwei Fu et al.
- **Link:** https://arxiv.org/abs/2608.06947v1
- **Security insight:** Retrieval-augmented generation (RAG) is indispensable for enhancing large language models. However, RAGs are increasingly susceptible to poisoning attacks, in which adversarial documents are injected to manipulate generator outputs. Previous methods rely on…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**Algebraic Cryptanalytic Extraction on Hard-Label Neural Networks**  
- **Date:** 2026-08-06
- **Authors:** Zirui Chen, Shi Tang, Zhengchao Gao et al.
- **Link:** https://arxiv.org/abs/2608.05736v1
- **Security insight:** Although the state-of-the-art neural network model extraction attack in the hard-label setting by Carlini et al. at EUROCRYPT 2025 has polynomial-time complexity in theory, its dual-point clustering relies on singular value decomposition (SVD) with a time…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.
