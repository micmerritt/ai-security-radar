# AI Security Radar

_Last updated (UTC): **2026-08-06**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

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
- **Link:** https://arxiv.org/abs/2608.02018v1
- **Security insight:** Computer-use agents (CUAs), which empower large language models to autonomously operate operating systems and the web, are increasingly vulnerable to indirect prompt injection attacks. A widely adopted defense is the human-in-the-loop paradigm, in which the…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Copyright Is the Headline; Capability Is the Blind Spot: AI Technology in the Book-Publishing Trade Press, November 2025--August 2026**  
- **Date:** 2026-08-02
- **Authors:** Fred Zimmerman
- **Link:** https://arxiv.org/abs/2608.00964v1
- **Security insight:** This rapid evidence review examines 89 articles about artificial intelligence (AI) and book publishing published from November 1, 2025 through August 1, 2026. The purposive corpus spans English-, Chinese-, German-, French-, Spanish-, Portuguese-, Italian-,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**When Prompts Control Robots: Prompt Injection Attacks in Multi-Agent Robotic Systems**  
- **Date:** 2026-08-01
- **Authors:** Neha Nagaraja, Amisha Bagari, Hayretdin Bahsi
- **Link:** https://arxiv.org/abs/2608.00747v2
- **Security insight:** Large language models are increasingly integrated into autonomous robotic systems for task planning and control, but this integration exposes them to prompt injection attacks that can lead to unsafe decisions and physical harm. Multi-agent settings increase…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Mitigating Visual Degradation in MLLMs via Spatial-Spectral Visual Anchor Learning**  
- **Date:** 2026-08-03
- **Authors:** Qianlong Yang, Bowen Ye, Xianda Guo et al.
- **Link:** https://arxiv.org/abs/2608.01635v1
- **Security insight:** Despite the progress of multimodal large language models (MLLMs), they continue to exhibit deficiencies in visual perception. Following visual instruction tuning, internal MLLM representations rapidly deviate from their original semantic states during…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

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

**Caliber: Cross-Architecture Extraction-Cost Control for Score-Returning APIs**  
- **Date:** 2026-08-02
- **Authors:** Chi Wang, Hanwen Wang, Yu Xia et al.
- **Link:** https://arxiv.org/abs/2608.01023v1
- **Security insight:** We present Caliber, an output-perturbation defense against model extraction that formulates noise selection as a calibration problem: how much the defense degrades the supervision signal used to train a surrogate, and the provable per-input query cost of…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Adversarial ML

**SoK: Intent-Oriented Systematization of Multi-Turn LLM Jailbreaks**  
- **Date:** 2026-08-02
- **Authors:** Siyuan Li, Aodu Wulianghai, Zehao Liu et al.
- **Link:** https://arxiv.org/abs/2608.01117v1
- **Security insight:** Large Language Models (LLMs) are increasingly deployed in interactive settings, where user intent commonly unfolds through multi-turn dialogue. Multi-turn jailbreaks exploit this pattern by advancing a harmful intent across turns, so that no single message…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

**Fighting Fire with Fire: On the Feasibility of Protecting Exercises Against AI Cheating**  
- **Date:** 2026-08-02
- **Authors:** Tobias Braun, Jonas Grebe, Louis Rethfeld et al.
- **Link:** https://arxiv.org/abs/2608.01112v1
- **Security insight:** The widespread adoption of generative AI enables students to outsource cognitive effort to increasingly capable assistants, creating an illusion of competence while undermining the independent reasoning that education aims to cultivate. We investigate whether…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.
