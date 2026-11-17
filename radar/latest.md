# AI Security Radar

_Last updated (UTC): **2026-11-17**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

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

**Agent Authenticator: Passkey-Grade, Hardware-Bound Authentication for AI Agents**  
- **Date:** 2026-11-14
- **Authors:** Harish Santhanalakshmi Ganesan
- **Link:** https://arxiv.org/abs/2611.19536v1
- **Security insight:** AI coding agents now push code, publish packages, call model APIs and operate cloud resources on behalf of developers. They authenticate to these services with the same bearer secrets humans use, personal access tokens, API keys and package-registry tokens,…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Do Rule-Based Tools Help LLMs Translate Endangered Uralic Languages in the Prompt or over MCP?**  
- **Date:** 2026-11-14
- **Authors:** Iaroslav Chelombitko, Mika Hämäläinen
- **Link:** https://arxiv.org/abs/2611.19439v1
- **Security insight:** Komi-Zyrian, Moksha, Erzya and Udmurt have mature rule-based resources, among them finite-state analysers, constraint grammars and bilingual dictionaries, which language models do not use. We ask whether giving a model access to these resources improves…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**When the Spec Sheet Lies: Injection Attacks on LLM-Generated Compliance Artifacts**  
- **Date:** 2026-11-14
- **Authors:** Adriana Watson, Marco Bücheler, Grant Richards
- **Link:** https://arxiv.org/abs/2611.19090v1
- **Security insight:** As Large Language Models (LLMs) become used more commonly across a variety of fields, a growing body of research has highlighted particular concerns surrounding model security. Notably, prompt injection attacks, where malicious instructions are inserted into…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**CapLite: Prompt-Injection Defense for Small Language Model Agents without Model-Written Security Artifacts**  
- **Date:** 2026-11-12
- **Authors:** Zimo Xu, Wenzhuo Liu, Hideki Nakayama
- **Link:** https://arxiv.org/abs/2611.17115v1
- **Security insight:** Enforcement defenses against prompt injection, such as CaMeL, Progent, IPIGuard and DRIFT, ask the agent's own model to write a security artifact (a program, a privilege policy, a dependency graph or a constraint list) that code then enforces. We ask whether…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Scale-Induced Semantic Shift in Visual Prompt Injection Against VLMs and Web Agents**  
- **Date:** 2026-11-12
- **Authors:** Yiheng Zhao, Runze Ji, Chenyu Yi et al.
- **Link:** https://arxiv.org/abs/2611.16744v1
- **Security insight:** Visual content in multimedia systems may be resized, compressed, or re-rendered before it is interpreted by a vision-language model. We study a security failure mode in which these transformations change the machine-readable semantics of an image: a textual…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Intent-Aware Protection for AI Agents**  
- **Date:** 2026-11-12
- **Authors:** Fady Copty, Neta Haiby, Max Braitmaiere et al.
- **Link:** https://arxiv.org/abs/2611.16122v1
- **Security insight:** AI agents increasingly access enterprise data, invoke powerful tools, and act with limited human oversight. Existing security defenses primarily detect prompt injection, harmful outputs, or suspicious behavior, but do not determine whether an agent remains…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Smart Model Routing for Order-of-Magnitude LLM Cost Reduction**  
- **Date:** 2026-11-11
- **Authors:** Hesham Elbakoury, Deep Shah, Ankur Sharma
- **Link:** https://arxiv.org/abs/2611.15911v1
- **Security insight:** Frontier large language models (LLMs) deliver the strongest response quality but carry per-token prices often more than an order of magnitude above those of smaller, task-adequate models. Smart model routing addresses this mismatch by assigning each query to…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**Wildfire-SSR: Geolocation-Aware Multimodal Fusion for Structure-Level Wildfire Risk Assessment**  
- **Date:** 2026-11-16
- **Authors:** Yu-Hsuan Ho, Yiming Xiao, Hao-En Lai et al.
- **Link:** https://arxiv.org/abs/2611.21563v1
- **Security insight:** Structure-level wildfire vulnerability assessment is critical for reducing losses in wildland-urban interface communities, yet existing methods often fail to combine parcel-scale ignition pathways with community-scale geographic coverage. This study…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Poisoning & Backdoors

**Steering Bayesian Inference and Decisions through Data Poisoning**  
- **Date:** 2026-11-14
- **Authors:** Roi Naveiro, William N. Caballero, Juan Maroñas
- **Link:** https://arxiv.org/abs/2611.19557v1
- **Security insight:** Adversarial machine learning has revealed that statistical models can be manipulated through poisoned data, and Bayesian inference is no exception. Earlier work has shown that subtle poisoning attacks can drive the posterior toward a distribution of the…
- **Build idea:** Build a minimal poisoning simulator plus simple detectors (trigger search, label flip tests, anomaly baselines).

### Model Extraction & Privacy

**Surrogate-Assisted Compact-Model Extraction for SKY130 CMOS at 77 K**  
- **Date:** 2026-11-16
- **Authors:** Aaron Wang, Olivia Gzamouranis, Vaibhav Lohia et al.
- **Link:** https://arxiv.org/abs/2611.21594v1
- **Security insight:** Cryogenic circuit design requires compact transistor models that reproduce measured low-temperature behavior and run in standard circuit simulators. We fit BSIM4 parameters to measured I-V curves of SkyWater 130 nm (SKY130) transistors at 77 K using a neural…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

### Adversarial ML

**VAST: Compiling Grounded Vulnerability Scenarios into Verifiable, Multi-Step Environments for Evaluating LLM Red-Team Agents**  
- **Date:** 2026-11-14
- **Authors:** Zhen Wan
- **Link:** https://arxiv.org/abs/2611.19465v1
- **Security insight:** Evaluating Large Language Model (LLM) security agents requires reproducible environments whose workflow difficulty can be varied and whose failures can be diagnosed. We present VAST (Verifiable Adversarial Scenario Training & Evaluation), a declarative range…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.
