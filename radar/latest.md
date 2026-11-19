# AI Security Radar

_Last updated (UTC): **2026-11-19**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

**PIPETTE: Prompt Injection Purple-Teaming for Robust LLM Agents**  
- **Date:** 2026-11-18
- **Authors:** Lipeng He, Yihan Wang, Jiawen Zhang et al.
- **Link:** https://arxiv.org/abs/2611.24362v1
- **Security insight:** Large language model (LLM) agents routinely interact with untrusted external data, exposing them to indirect prompt injection (IPI) attacks that hijack agents into executing attacker-chosen tasks. To uncover these vulnerabilities at scale, automated red-…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**AutoPI: Taxonomy-Guided Adaptive Red Teaming for Prompt Injection in LLM Agents**  
- **Date:** 2026-11-18
- **Authors:** Stavros Damianakis, Konstantinos Psounis
- **Link:** https://arxiv.org/abs/2611.24313v1
- **Security insight:** Prompt injection is the dominant unsolved security risk for LLM agents, and the community now agrees that robustness must be measured against adaptive attackers rather than fixed benchmark injections. Many adaptive red teamers exist, and most are built to…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**What Survives the Shift from Text to Pixels? Conditional Protection against Prompt Injection in Image-Rendered Documents**  
- **Date:** 2026-11-18
- **Authors:** Haoyang Liu, Yinong Xu, Zhe Lang et al.
- **Link:** https://arxiv.org/abs/2611.24231v1
- **Security insight:** Multimodal language models increasingly answer questions over external documents, exposing them to indirect prompt injection: commands planted in untrusted content to hijack the response. Rendering untrusted content as page images lowers attack success on…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Securing and Auditing Long-Horizon LLM Agents: State-Transfer Auditing and Controls in the Agent Harness**  
- **Date:** 2026-11-17
- **Authors:** Deep Shah, Nehal Kathrotia
- **Link:** https://arxiv.org/abs/2611.23346v1
- **Security insight:** Long-horizon LLM agents across codebases, web browsers, and enterprise infrastructure rely on an execution harness to move state between the working context, session history, persistent memory, and external environment. While conventional execution traces log…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**GapLeak: When Privacy-Preserving LLM-based Web Agents Become a Privacy Risk**  
- **Date:** 2026-11-17
- **Authors:** Chaklam Cheong, Tiancong Cao, Qi Li et al.
- **Link:** https://arxiv.org/abs/2611.22223v1
- **Security insight:** Large Language Model (LLM)-based web agents rely on data minimization and least privilege to protect user privacy. We show that these principles are necessary but insufficient: they constrain authorized sources, but not higher-sensitivity sources that remain…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Threat Landscape of Vibe Coding and the Road to Secure Autonomy**  
- **Date:** 2026-11-16
- **Authors:** Devki Nandan Jha, Shubh Anand, Karthick Keeranagere Krishnaiah et al.
- **Link:** https://arxiv.org/abs/2611.21822v1
- **Security insight:** Vibe coding is reshaping software development, enabling faster implementation and allowing individuals with limited programming experience to describe requirements in natural language while AI agents write, test, and deploy the code. As these agents evolve…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Evaluating Authorization and Trust Boundaries in Agentic Orchestration Frameworks**  
- **Date:** 2026-11-16
- **Authors:** Sahaya Jestus Lazer, Kshitiz Aryal, Maanak Gupta et al.
- **Link:** https://arxiv.org/abs/2611.21259v1
- **Security insight:** Agentic AI systems extend large language models with tools, memory, and multi-agent collaboration, introducing security risks at orchestration boundaries. These risks depend on how identities are represented, operations are authorized, and instructions or…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Risk-certified prompt optimization for LLM-as-a-judge guardrails**  
- **Date:** 2026-11-15
- **Authors:** Hussein Jawad, Alexandre Landeau, Guy Fleury Iradukunda et al.
- **Link:** https://arxiv.org/abs/2611.20156v1
- **Security insight:** LLM-as-a-judge guardrails are often controlled primarily through system prompts, yet standard prompt optimization methods target average performance rather than explicit safety constraints. This paper studies system-prompt selection as a constrained…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Security of Deep Research Agents: Attack Surface, Defenses, Benchmarks, and Agenda Seeding against Research Planning**  
- **Date:** 2026-11-15
- **Authors:** Yang Luo, Guangpu Chen, Yichen Liu et al.
- **Link:** https://arxiv.org/abs/2611.20045v1
- **Security insight:** Deep research and agentic search agents autonomously retrieve content from the open web and generate reports with citations, and their outputs are often taken directly as research conclusions. This paper systematizes security research in this area along four…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**Wildfire-SSR: Geolocation-Aware Multimodal Fusion for Structure-Level Wildfire Risk Assessment**  
- **Date:** 2026-11-16
- **Authors:** Yu-Hsuan Ho, Yiming Xiao, Hao-En Lai et al.
- **Link:** https://arxiv.org/abs/2611.21563v1
- **Security insight:** Structure-level wildfire vulnerability assessment is critical for reducing losses in wildland-urban interface communities, yet existing methods often fail to combine parcel-scale ignition pathways with community-scale geographic coverage. This study…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Model Extraction & Privacy

**Surrogate-Assisted Compact-Model Extraction for SKY130 CMOS at 77 K**  
- **Date:** 2026-11-16
- **Authors:** Aaron Wang, Olivia Gzamouranis, Vaibhav Lohia et al.
- **Link:** https://arxiv.org/abs/2611.21594v1
- **Security insight:** Cryogenic circuit design requires compact transistor models that reproduce measured low-temperature behavior and run in standard circuit simulators. We fit BSIM4 parameters to measured I-V curves of SkyWater 130 nm (SKY130) transistors at 77 K using a neural…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

### Adversarial ML

**Gradient-Based Defensive Poisoning Against System Identification Attacks on Cyber-Physical Systems**  
- **Date:** 2026-11-18
- **Authors:** Gonçalo Fernandes, José Cecílio, Victor Mattos et al.
- **Link:** https://arxiv.org/abs/2611.24662v1
- **Security insight:** AI-driven attacks learn the models of cyber-physical systems (CPS) by passively observing controller and plant signals, then use this knowledge to act covertly. Because covertness depends on the accuracy of the identified model, degrading that accuracy is a…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

**Network-Exposed Configuration Attacks on LLM-Controlled Social Robots**  
- **Date:** 2026-11-17
- **Authors:** Stanley Akingbola, Ugbede Ibrahim, Yan Lin Aung et al.
- **Link:** https://arxiv.org/abs/2611.22761v1
- **Security insight:** Large language models (LLMs) in embodied robots create security dependencies beyond inference. We investigate a network-exposed configuration attack on the Pollen Robotics Reachy Mini Lite, allowing an unauthenticated attacker to replace personality settings…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

### Agent & Tool Security

**Guarding the Kingdom of Skill-Based Agents in the AI Dynasty of Computation: Control-Flow Integrity for Agent Skills**  
- **Date:** 2026-11-18
- **Authors:** Bonan Ruan, Yuhao Sun, Jiahao Liu et al.
- **Link:** https://arxiv.org/abs/2611.24185v1
- **Security insight:** Control-flow integrity (CFI) confines a program to a control-flow graph fixed ahead of time. Procedural agent skills move this control flow into prompt text, and a large language model (LLM) agent decides at runtime whether each step runs in its reasoning, a…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.
