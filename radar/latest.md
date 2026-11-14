# AI Security Radar

_Last updated (UTC): **2026-11-14**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

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

**Can the Confidence and Decisions of System 1 Models Be Trusted? An Explainability and Perturbation Audit of Jev-Style Decision Models**  
- **Date:** 2026-11-09
- **Authors:** Julien Delaunay
- **Link:** https://arxiv.org/abs/2611.12521v1
- **Security insight:** "System 1" decision models (pioneered by TypeSafe AI's Jev) replace autoregressive text generation with a single forward pass returning typed probability distributions over declared schemas (Choice, Score, Noul). While deployed for low-latency routing and…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Say Shibboleth: Fingerprinting the LLMs and Harnesses Behind Agentic Attacks**  
- **Date:** 2026-11-09
- **Authors:** Dario Pasquini, Reworr, Giuseppe Ateniese et al.
- **Link:** https://arxiv.org/abs/2611.12386v1
- **Security insight:** We study the fingerprinting of agentic cyberattacks. Our objective is to reliably infer information about the attacker's configuration, such as LLM version and harness, from telemetry. To achieve this, we introduce a technique we call shibboleth traps:…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Harness Matters: Measuring and Dissecting Security Resilience in Web Agents**  
- **Date:** 2026-11-09
- **Authors:** Xinyi Wu, Jiagui Chen, JiaYi Dong et al.
- **Link:** https://arxiv.org/abs/2611.11971v1
- **Security insight:** Web agents extend LLMs from text generation to real-world web interaction by relying on execution harnesses that interpret user goals, perceive webpages, plan actions, and ground model decisions into browser operations. While prior work has recognized that…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Scaling Adaptive Prompt Injection Attacks with Agent Swarms**  
- **Date:** 2026-11-09
- **Authors:** Alexey Kurakin, Vishal Karande, Alex Bie et al.
- **Link:** https://arxiv.org/abs/2611.11861v1
- **Security insight:** Prompt injections have emerged as one of the top security risks faced by AI agents today. Early work in prompt injection attacks looked at simple tool-call agents and static attack payloads, and were saturated since mid-2025. As of Fall 2026, human red-…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Treating the Model as an Untrusted Component: Deterministic Policy Enforcement, Human Approval and Taint Tracking Against Prompt Injection in Tool-Using Agents, with Validation on Open-Weights Models**  
- **Date:** 2026-11-08
- **Authors:** Mustafa S. Aljumaily, Nawar S. Alseelawi, Raghad Alshabandar
- **Link:** https://arxiv.org/abs/2611.11571v1
- **Security insight:** Tool-using LLM agents act on instructions embedded in the data they read, so prompt injection is a structural rather than a prompt-wording problem. We compare in-prompt defences (hardened prompts, spotlighting, LLM detectors) with deterministic enforcement…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**On the Relative Security of Prompt Injection: Mechanised Definitions, Defences and Verdicts for LLM Agents**  
- **Date:** 2026-11-08
- **Authors:** Brijesh Dongol
- **Link:** https://arxiv.org/abs/2611.11506v1
- **Security insight:** An LLM agent that reads untrusted content, such as an email or a web page, may follow instructions hidden in it. Noninterference is too strong for such agents, since a useful agent lets untrusted content influence what it does and may disclose the user's data…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**When Coding Agents Get Arms: Safety Risks Across the Digital-Physical Boundary**  
- **Date:** 2026-11-08
- **Authors:** Yiming Sun, Mi Zhang
- **Link:** https://arxiv.org/abs/2611.11438v1
- **Security insight:** Advances in spatial understanding have enabled frontier models to power coding agents that control a real robot arm zero-shot and end-to-end, without task-specific demonstrations or retraining. This brings two new safety challenges. First, the extensive…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Least-Privilege Auditing of Agent Tool Calls with Intent Graphs and Reasoning-Guided Escalation**  
- **Date:** 2026-11-08
- **Authors:** Doron Shavit
- **Link:** https://arxiv.org/abs/2611.11305v1
- **Security insight:** LLM agents that call tools are exposed to indirect prompt injection: instructions hidden in tool outputs can steer an agent into calls the user never asked for. We present a runtime audit that derives an executable intent graph from the user's objective and…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**Your Secrets Are Showing: Deep Image Hiding Models Are Surprisingly Easy to Attack**  
- **Date:** 2026-11-11
- **Authors:** Hao Liu, Jing Yu, Weizhi Liu et al.
- **Link:** https://arxiv.org/abs/2611.15583v1
- **Security insight:** In this work, we ask whether an attacker can go beyond detecting a hidden image and tell what it depicts, even without knowing which model hid it. We show that, for deep image hiding, this is surprisingly easy. To test this, we build an evaluation dataset of…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Adversarial ML

**Adversarial Risk in the Generative AI Era Necessitates Dropping the Small Epsilon Ball**  
- **Date:** 2026-11-10
- **Authors:** Andrew C. Cullen, Neil G. Marchant, Paul Montague et al.
- **Link:** https://arxiv.org/abs/2611.14594v1
- **Security insight:** Adversarial Machine Learning research is currently centered on the search for the epsilon-ball: minimal perturbations designed to fool models while remaining imperceptible to humans. We argue that this fixation on $\ell_p$ norms is a metrological trap that…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.
