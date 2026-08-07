# AI Security Radar

_Last updated (UTC): **2026-08-07**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**PromptShield Home: Ambient Multimodal Prompt Injection Defense for Smart-Home Agents**  
- **Date:** 2026-08-06
- **Authors:** He Zhang, Feilong Li, Dingning Long et al.
- **Link:** https://arxiv.org/abs/2608.05495v1
- **Security insight:** Smart-home assistants increasingly use multimodal large language models (MLLMs) that perceive video and audio directly. This raises a safety question specific to the home: can the agent tell a genuine user command from ambient or externally-sourced content,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Robust Context-Aware Detection of Malicious Instructions in Text**  
- **Date:** 2026-08-05
- **Authors:** Buzhao Liu, Xinhang Ma, Yevgeniy Vorobeychik
- **Link:** https://arxiv.org/abs/2608.05430v1
- **Security insight:** The remarkable instruction-following ability of modern LLMs has enabled their practical use as the minds of agents that can autonomously complete increasingly complex tasks. Therein, however, also lies their vulnerability to attacks which embed malicious…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Agent Against Agent: An Agentic System for Automatic Prompt Injection Red Teaming**  
- **Date:** 2026-08-05
- **Authors:** Yanting Wang, Chenlong Yin, Runpeng Geng et al.
- **Link:** https://arxiv.org/abs/2608.05108v1
- **Security insight:** Prompt injection poses significant security risks to LLM agents. Efficient and effective red-teaming is therefore critical, both for evaluating these risks and for collecting training data to improve defenses. Existing state-of-the-art prompt injection red-…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**LoginTrap: Uncovering Task-Agnostic Phishing-Style Indirect Prompt Injection Attacks against LLM-based Web Agents**  
- **Date:** 2026-08-05
- **Authors:** Longtao Guo, Zelin Zhang, Kaifeng Huang et al.
- **Link:** https://arxiv.org/abs/2608.04741v1
- **Security insight:** LLM-based web agents automate user tasks by observing webpages and executing browser actions on behalf of users. As these agents operate on real web services, login becomes a sensitive authentication boundary because it involves credentials and sensitive…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Breadcrumbing Search Agents**  
- **Date:** 2026-08-05
- **Authors:** Xuebin Li, Hanqing Zhao, Siyuan Liang et al.
- **Link:** https://arxiv.org/abs/2608.04565v1
- **Security insight:** LLM-based search agents are widely used for information-seeking tasks, but their reliance on external tool returns introduces a critical security risk: web content retrieved during execution is untrusted, exposing agents to prompt injection and goal…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Behavioral Skill Reconstruction: Reconstructing Hidden Functionality from LLM Agent Skills**  
- **Date:** 2026-08-04
- **Authors:** Peichun Hua, Haoxuan Xu, Mengyuan Li
- **Link:** https://arxiv.org/abs/2608.04192v1
- **Security insight:** Closed source agent skills may encode proprietary instructions, scripts, constants, and data. Providers may offer their capabilities as services while keeping the underlying packages hidden. Prior work focuses on prompt injection attacks that directly…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**AgentAntibody: An Adaptive Immune System for Defending LLM Agents against Prompt Injection**  
- **Date:** 2026-08-04
- **Authors:** Shihao Weng, Yang Feng, Xiaofei Xie et al.
- **Link:** https://arxiv.org/abs/2608.04053v1
- **Security insight:** Prompt injection remains a critical threat to LLM agents, yet existing defenses treat each task as a self-contained problem, independent of previous encounters. In practice, user requests are often underspecified: they describe the desired outcome without…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Invisible Ink Threats: Adversarial Goals Behind Legitimate Tasks in Computer-Use Agents**  
- **Date:** 2026-08-03
- **Authors:** Jia-Chen Zhang, Ze-Yu Zhang, Kai-Wei Zhang
- **Link:** https://arxiv.org/abs/2608.02018v2
- **Security insight:** Computer-use agents (CUAs), which empower large language models to autonomously operate operating systems and the web, are increasingly vulnerable to indirect prompt injection attacks. A widely adopted defense is the human-in-the-loop paradigm, in which the…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Hijacking Robots with a Piece of Paper: A Systematic Study of Physical Prompt Injection in VLM-Controlled Robots**  
- **Date:** 2026-08-06
- **Authors:** S. M . Bhagya P. Samarakoon, M. A. Viraj J. Muthugala, W. K. R. Sachinthana et al.
- **Link:** https://arxiv.org/abs/2608.05715v1
- **Security insight:** Vision-Language Models (VLMs) are increasingly deployed as planners in robotic systems, where they translate natural-language commands into executable actions grounded in visual scene understanding. This tight coupling between perception and instruction-…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Mitigating Visual Degradation in MLLMs via Spatial-Spectral Visual Anchor Learning**  
- **Date:** 2026-08-03
- **Authors:** Qianlong Yang, Bowen Ye, Xianda Guo et al.
- **Link:** https://arxiv.org/abs/2608.01635v1
- **Security insight:** Despite the progress of multimodal large language models (MLLMs), they continue to exhibit deficiencies in visual perception. Following visual instruction tuning, internal MLLM representations rapidly deviate from their original semantic states during…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**Algebraic Cryptanalytic Extraction on Hard-Label Neural Networks**  
- **Date:** 2026-08-06
- **Authors:** Zirui Chen, Shi Tang, Zhengchao Gao et al.
- **Link:** https://arxiv.org/abs/2608.05736v1
- **Security insight:** Although the state-of-the-art neural network model extraction attack in the hard-label setting by Carlini et al. at EUROCRYPT 2025 has polynomial-time complexity in theory, its dual-point clustering relies on singular value decomposition (SVD) with a time…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**Gecko: Fast Private Inference via Secure Public Encoder Offloading**  
- **Date:** 2026-08-03
- **Authors:** Cheng'an Wei, Kai Chen, Yue Zhao et al.
- **Link:** https://arxiv.org/abs/2608.02378v1
- **Security insight:** Private inference protects both user inputs and server models during neural network inference, but existing solutions remain too slow for practical deployment. This motivates recent efforts to run a public encoder, such as a pretrained backbone, outside the…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**DenialRAG: Single-Document RAG Poisoning via Embedded Parametric Denial**  
- **Date:** 2026-08-02
- **Authors:** Abay Zhurekbay, Tao Liu, Fan Li
- **Link:** https://arxiv.org/abs/2608.02678v1
- **Security insight:** Retrieval-augmented generation (RAG) systems are vulnerable to corpus poisoning: an attacker who inserts a crafted document into the retrieval corpus can steer the underlying large language model (LLM) toward an attacker-chosen wrong answer. Prior single-…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Adversarial ML

**SoK: Intent-Oriented Systematization of Multi-Turn LLM Jailbreaks**  
- **Date:** 2026-08-02
- **Authors:** Siyuan Li, Aodu Wulianghai, Zehao Liu et al.
- **Link:** https://arxiv.org/abs/2608.01117v1
- **Security insight:** Large Language Models (LLMs) are increasingly deployed in interactive settings, where user intent commonly unfolds through multi-turn dialogue. Multi-turn jailbreaks exploit this pattern by advancing a harmful intent across turns, so that no single message…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.
