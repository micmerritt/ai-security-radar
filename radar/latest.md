# AI Security Radar

_Last updated (UTC): **2026-11-12**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

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

**ErosionBench: Probing Alignment Decay in Enterprise Multi-Agent Systems**  
- **Date:** 2026-11-08
- **Authors:** Riya Bharathwaj, Akshara Prabhakar, Roshan Ram et al.
- **Link:** https://arxiv.org/abs/2611.11266v1
- **Security insight:** As enterprises delegate consequential work to multi-agent LLM systems, benign-looking requests can escalate into unsafe actions as they propagate across sessions through poisoned shared state, long-context documents, and trusted peer messages: no single…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**CompositionEvidence: Controlling Geometric Evidence for Cinematic Composition Reasoning with Frozen Vision-Language Models**  
- **Date:** 2026-11-07
- **Authors:** Yichen He, Xin Huang, Yuxi Liu
- **Link:** https://arxiv.org/abs/2611.10559v1
- **Security insight:** Cinematic composition questions depend on in-frame geometry that vision-language models (VLMs) use inconsistently. External perception tools can expose this geometry, but naive prompt injection can overwrite useful visual predictions. On ShotBench…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**Agents of Chaos: A Systematization of Knowledge (SoK) on Malicious Attacks on Agentic AI Systems**  
- **Date:** 2026-11-07
- **Authors:** Thanh M. Truong-Le, Amber Bennoui, Hoang-Ly Nguyen et al.
- **Link:** https://arxiv.org/abs/2611.10843v1
- **Security insight:** Agentic AI systems extend large language models with tools, memory, retrieval, browser or computer-use interfaces, code execution, external services, and multi-agent coordination. Although these capabilities enable agents to act beyond text generation and…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Model Extraction & Privacy

**Cutpurse: Decomposing Explanation-Guided Model Extraction on Tabular Data**  
- **Date:** 2026-11-06
- **Authors:** Seyma Selcan Magara, Hanru Zhang, Fatme El Zahraa Hamad et al.
- **Link:** https://arxiv.org/abs/2611.09375v1
- **Security insight:** Explanation APIs are often treated as increasing model-extraction risk, but an end-to-end attack comparison cannot show whether an explanation reveals model-specific information or merely supplies a convenient next-query coordinate. We study this distinction…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

### Adversarial ML

**Do Benign-Trained Hidden-State Probes Detect Tool Errors Under Adversarial Conditions?**  
- **Date:** 2026-11-08
- **Authors:** Bibek Bhandari, Kshitij Lingthep
- **Link:** https://arxiv.org/abs/2611.11172v1
- **Security insight:** Although hidden-state probes efficiently monitor model operation, it remains unclear whether probes trained on benign tool use remain useful for detecting incorrect actions under adversarial conditions. In this research, we assess this problem from the…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

### Other (Review)

**Enmo Safety: External, Non-invasive, Model-agnostic Oversight for Off-the-Shelf Language Models**  
- **Date:** 2026-11-06
- **Authors:** Mohammed Nayeem Khan, Sarun Kumar K. S., Allan Kevin T. et al.
- **Link:** https://arxiv.org/abs/2611.10099v1
- **Security insight:** We study a safety harness that improves itself without touching model weights. Enmo Safety wraps a chat model with a deterministic input assessment, trigger-matched safety guidance, spotlighting of untrusted content, and an output guard. A reflector model…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
