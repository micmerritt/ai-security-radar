# AI Security Radar

_Last updated (UTC): **2026-06-01**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**From Prompt Injection to Persistent Control: Defending Agentic Harness Against Trojan Backdoors**  
- **Date:** 2026-05-29
- **Authors:** Jiejun Tan, Zhicheng Dou, Xinyu Yang et al.
- **Link:** https://arxiv.org/abs/2605.31042v1
- **Security insight:** LLM agents are evolving from conversational chatbots to operational tools in real-world workspaces. In local agentic harnesses, an LLM can read and write files, call tools, and reuse workspace state across sessions. While such capabilities enhance utility,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Send a SCOUT First: Pre-hoc Reasoning for Adaptive Detector Allocation in Prompt-Injection Defense**  
- **Date:** 2026-05-29
- **Authors:** Shuhao Zhang, Jiarui Li, Qi Cao et al.
- **Link:** https://arxiv.org/abs/2605.30837v1
- **Security insight:** Prompt-injection detectors are heterogeneous: each is strong on a different slice of attacks, and none is always reliable. Yet existing systems still treat detection as a fixed single-detector pipeline, committing every request to one detector's blind spots.…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Depth-Dependent Indirect Prompt Injection in Tool-Calling ReAct Agents: Injection Depth, Payload Framing, and Turn-Budget Sensitivity**  
- **Date:** 2026-05-29
- **Authors:** Mohammadreza Rashidi
- **Link:** https://arxiv.org/abs/2605.30686v1
- **Security insight:** ReAct agents that interleave chain-of-thought reasoning with tool calls are increasingly deployed for real tasks such as scheduling, file retrieval, and data access. Their tool observation loop creates a direct attack surface: an adversary who controls any…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Investigating Detection and Obfuscation of Prompt Injection Attacks Against Software Reverse Engineering AI Agents**  
- **Date:** 2026-05-29
- **Authors:** Brian Crawford, Patrick McClure
- **Link:** https://arxiv.org/abs/2605.30677v1
- **Security insight:** Agentic software reverse engineering systems are vulnerable to prompt injection attacks placed into the source code of executable binary files. This research demonstrates defensive tactics for detecting the presences of prompt injection strings in the…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Automatically Attacking Software Reverse Engineering AI Agents**  
- **Date:** 2026-05-28
- **Authors:** Brian Crawford, Justin Phillips, Patrick McClure
- **Link:** https://arxiv.org/abs/2605.30667v1
- **Security insight:** Software tools for reverse engineering executable binary files, such as Ghidra, enable malware analysts to safely conduct robust static analysis without having access to original source code. Coupled with the analytic power of large language models (LLM),…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**When AI Meets Wall Street: A Survey on Trustworthy AI in Fintech**  
- **Date:** 2026-05-28
- **Authors:** Qingwen Zeng, Zhenghao Zhao, Yitian Yang et al.
- **Link:** https://arxiv.org/abs/2605.30650v1
- **Security insight:** Artificial intelligence is now embedded as a primary decision engine in continuously operated financial AI pipelines spanning training and updating, deployment and inference, and operation with monitoring and feedback. The automation and scale that make these…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Strengthening Polymorphic Prompt Assembling: Dynamic Separator Generation Against Emerging Prompt Injection Attacks**  
- **Date:** 2026-05-28
- **Authors:** Nima Dorzhiev, Peng Liu
- **Link:** https://arxiv.org/abs/2605.30534v1
- **Security insight:** Polymorphic Prompt Assembling (PPA) defends LLM agents against prompt injections by randomly selecting separator pairs from a fixed pool to isolate user input from system instructions. Although effective, static pool reuse exposes a blast-radius…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**The Surface You Test Is Not the Surface That Breaks**  
- **Date:** 2026-05-28
- **Authors:** Shifat E Arman, Syed Nazmus Sakib, Nafiul Haque et al.
- **Link:** https://arxiv.org/abs/2605.30454v1
- **Security insight:** Tool-augmented LLM agents are vulnerable to prompt injection: a third party who controls part of the agent's context can plant instructions that the agent then executes as if they came from the user. Current evaluations report a single attack success rate per…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Minimal Prompt Perturbations Lead to Code Vulnerabilities: Prompt Fragility and Hidden-State Signals in Coding LLMs**  
- **Date:** 2026-05-28
- **Authors:** Alexander Sternfeld, Andrei Kucharavy, Ljiljana Dolamic
- **Link:** https://arxiv.org/abs/2605.29737v1
- **Security insight:** LLM-based coding assistants are seeing rapid adoption, offering substantial gains in developer productivity. As organizations increasingly ship code these agents produce, the security of that code becomes critical. Prior work has shown that minor prompt…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Measuring Real-World Prompt Injection Attacks in LLM-based Resume Screening**  
- **Date:** 2026-05-27
- **Authors:** Mohan Zhang, Yuqi Jia, Zhen Tan et al.
- **Link:** https://arxiv.org/abs/2605.28999v1
- **Security insight:** LLMs are vulnerable to prompt injection attacks. However, this vulnerability has been primarily demonstrated conceptually in academic studies or through a few anecdotal case studies. Its prevalence and impact in real-world LLM-based applications are largely…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**Evolving Skill-Structured Attack Memory Enhances LLM Jailbreaking**  
- **Date:** 2026-05-28
- **Authors:** Junke Zhang, Jianwei Wang, Sishuo Chen et al.
- **Link:** https://arxiv.org/abs/2605.29237v1
- **Security insight:** Jailbreak attacks on large language models (LLMs) aim to induce LLMs to produce content that they are expected to refuse. Automated black-box jailbreak generation is especially important for safety evaluation, where the attacker observes only model outputs…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Poisoning & Backdoors

**Token-Level Generalization in LoRA Adapter Backdoors: Attack Characterization and Behavioral Detection**  
- **Date:** 2026-05-28
- **Authors:** Travis Lelle
- **Link:** https://arxiv.org/abs/2605.30189v1
- **Security insight:** We show that LoRA adapters, the dominant distribution format for fine-tuned LLMs, can be reliably backdoored through training data poisoning while preserving baseline task performance. On a Qwen 2.5 1.5B prompt-injection classifier, a small fraction of…
- **Build idea:** Build a minimal poisoning simulator plus simple detectors (trigger search, label flip tests, anomaly baselines).

### Model Extraction & Privacy

**Can Subgraph Explanations Be Weaponized to Steal Graph Neural Networks?**  
- **Date:** 2026-05-28
- **Authors:** Ojas Nimase, Jiate Li, Yue Zhao et al.
- **Link:** https://arxiv.org/abs/2605.30470v1
- **Security insight:** Graph Machine Learning as a Service (GMLaaS) platforms increasingly implement explainability interfaces to meet regulatory transparency requirements. However, this transparency creates exploitable vulnerabilities for model extraction attacks. We present the…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

### Other (Review)

**Dissecting the Black Box: Circuit-Level Analysis of LLM Vulnerability Detection**  
- **Date:** 2026-05-28
- **Authors:** Syafiq Al Atiiq, Chun Zhou, Christian Gehrmann
- **Link:** https://arxiv.org/abs/2605.29901v1
- **Security insight:** Large language models (LLMs) can detect software vulnerabilities, but how do they actually identify vulnerable code? We address this question using mechanistic interpretability; analyzing the internal computations of a neural network to understand its…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
