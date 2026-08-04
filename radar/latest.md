# AI Security Radar

_Last updated (UTC): **2026-08-04**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

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
- **Link:** https://arxiv.org/abs/2608.00747v1
- **Security insight:** Large language models are increasingly integrated into autonomous robotic systems for task planning and control, but this integration exposes them to prompt injection attacks that can lead to unsafe decisions and physical harm. Multi-agent settings increase…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**From Monoliths to Swarms: A Study of Attack Surface Evolution in the Transition to Multi-Agent Web Systems**  
- **Date:** 2026-07-31
- **Authors:** Yashaswi Malla, Sandra Siby
- **Link:** https://arxiv.org/abs/2608.00202v1
- **Security insight:** Large Language Model (LLM)-based web agents are increasingly evolving from single-agent systems (SAS) to multi-agent systems (MAS). While MAS can lead to improved task performance by decomposing complex tasks across specialized sub-agents, such role…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Tool Specifications Matter: Uncovering and Mitigating Safety Risks in AI Agents**  
- **Date:** 2026-07-31
- **Authors:** Minghui Pan, Jiayuxuan Yang, Yuanyuan Yuan et al.
- **Link:** https://arxiv.org/abs/2607.29254v1
- **Security insight:** AI agents extend large language models (LLMs) with external tools, enabling them to perform complex tasks and translate model outputs into consequential real-world actions. Yet LLMs often become substantially less safe when deployed as agents, and the source…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Piggybacking on Perception: Stealthy Concurrent Audio Prompt Injections against Multimodal LLM Agents**  
- **Date:** 2026-07-30
- **Authors:** Mingxiao Liu, Yitong Li, Haoren Zhao et al.
- **Link:** https://arxiv.org/abs/2607.28165v2
- **Security insight:** Large Language Model (LLM)-driven multimodal agents are increasingly deployed to execute autonomous tasks via continuous audio interaction. While this paradigm enhances interaction naturalness, it introduces a critical yet under-explored attack surface, as…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**GPT-Red: Automated Red Teaming via Self-Play at Scale**  
- **Date:** 2026-07-28
- **Authors:** Eric Wallace, Christopher A. Choquette-Choo, Nikhil Kandpal et al.
- **Link:** https://arxiv.org/abs/2607.26115v1
- **Security insight:** We introduce \textbf{GPT-Red}, an automated red-teaming agent that is trained to discover novel prompt injection attacks against frontier LLMs. The goal of this model is to evaluate and improve the robustness of our production systems. To this end, we use it…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Mitigating Visual Degradation in MLLMs via Spatial-Spectral Visual Anchor Learning**  
- **Date:** 2026-08-03
- **Authors:** Qianlong Yang, Bowen Ye, Xianda Guo et al.
- **Link:** https://arxiv.org/abs/2608.01635v1
- **Security insight:** Despite the progress of multimodal large language models (MLLMs), they continue to exhibit deficiencies in visual perception. Following visual instruction tuning, internal MLLM representations rapidly deviate from their original semantic states during…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Security of World-Model-Based Embodied AI: A Lifecycle of Threats, Defenses, and Evaluation**  
- **Date:** 2026-07-30
- **Authors:** Fazhong Liu, Zhuoyan Chen, Haozhen Tan et al.
- **Link:** https://arxiv.org/abs/2607.28226v1
- **Security insight:** World models give embodied AI a predictive core: they compress observations into states, simulate action-conditioned futures, and enable planning beyond reactive control. This predictive layer, however, opens a new security boundary-compromise can propagate…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**Gecko: Fast Private Inference via Secure Public Encoder Offloading**  
- **Date:** 2026-08-03
- **Authors:** Cheng'an Wei, Kai Chen, Yue Zhao et al.
- **Link:** https://arxiv.org/abs/2608.02378v1
- **Security insight:** Private inference protects both user inputs and server models during neural network inference, but existing solutions remain too slow for practical deployment. This motivates recent efforts to run a public encoder, such as a pretrained backbone, outside the…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**Caliber: Cross-Architecture Extraction-Cost Control for Score-Returning APIs**  
- **Date:** 2026-08-02
- **Authors:** Chi Wang, Hanwen Wang, Yu Xia et al.
- **Link:** https://arxiv.org/abs/2608.01023v1
- **Security insight:** We present Caliber, an output-perturbation defense against model extraction that formulates noise selection as a calibration problem: how much the defense degrades the supervision signal used to train a surrogate, and the provable per-input query cost of…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**RadPRISM: Schema-stratified radiology-report supervision for concept-disentangled image representations and visual grounding**  
- **Date:** 2026-07-31
- **Authors:** Fabian Drexel, Marlene Fritzsche, Era Stambollxhiu et al.
- **Link:** https://arxiv.org/abs/2608.00147v1
- **Security insight:** Vision-language pretraining learns rich medical image representations from radiology reports, but previous model variants commonly operate within a single shared embedding space, so concept-level structure and interpretability must be recovered post hoc,…
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
