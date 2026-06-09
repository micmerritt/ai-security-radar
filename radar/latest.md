# AI Security Radar

_Last updated (UTC): **2026-06-09**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**PRISM: Recovering Instruction Sets from Language Model Activations**  
- **Date:** 2026-06-08
- **Authors:** Gilad Gressel, Rahul Pankajakshan, Julia Diament et al.
- **Link:** https://arxiv.org/abs/2606.09563v1
- **Security insight:** As LLMs are deployed as agents, reliable monitoring requires knowing not only what they output, but which instructions are steering their behavior. This is difficult when models infer unintended subgoals, follow contextual cues, or are influenced by prompt…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**SecureClaw: Clawing Back Control of LLM Agents**  
- **Date:** 2026-06-08
- **Authors:** Yuhan Ma, Stefan Schmid
- **Link:** https://arxiv.org/abs/2606.09549v1
- **Security insight:** Tool-using large language model (LLM) agents face two distinct security failures: unauthorized external actions and exposure of sensitive plaintext inside the runtime before any final output check can intervene. Existing defenses usually protect one boundary,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Brain-Prompt Injection: A Route-Safety Audit for BCI-LLM Agents**  
- **Date:** 2026-06-08
- **Authors:** Jianwei Tai
- **Link:** https://arxiv.org/abs/2606.09315v1
- **Security insight:** BCI-to-agent pipelines turn decoded neural activity into an authorization channel for tool-use agents, exposing a new attack surface we call \emph{brain-prompt injection}: signal-side perturbations, context-only injections, and adaptive dual-decoder attacks…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Data Agents Under Attack: Vulnerabilities in LLM-Driven Analytical Systems**  
- **Date:** 2026-06-07
- **Authors:** Kuncan Wang, Ziting Wang, Peizhuo Lv et al.
- **Link:** https://arxiv.org/abs/2606.08661v1
- **Security insight:** Data agents integrate LLM-driven reasoning with relational data access, executable analytical tools, and multi-step workflow orchestration, making them increasingly central to enterprise analytics. This integration introduces new security vulnerabilities…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**VATS: Exploiting Implicit Authority in Error-Path Injection via Systematic Mutation**  
- **Date:** 2026-06-06
- **Authors:** Harshil Patel, Kunal Pai
- **Link:** https://arxiv.org/abs/2606.07992v1
- **Security insight:** As the Model Context Protocol (MCP) standardizes tool-calling for autonomous agents, it introduces a critical, unexamined attack surface: the error-handling loop. We hypothesize that tool error messages possess implicit authority, triggering corrective…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**MalSkillBench: A Runtime-Verified Benchmark of Malicious Agent Skills**  
- **Date:** 2026-06-05
- **Authors:** Wenbo Guo, Wei Zeng, Chengwei Liu et al.
- **Link:** https://arxiv.org/abs/2606.07131v1
- **Security insight:** AI coding agents such as Claude Code and Gemini CLI increasingly extend themselves with third-party skills: markdown packages bundling natural-language instructions, executable scripts, and tool permissions. Because a skill is at once code and agent-facing…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Review the Code, Not the Story: A Vision and Protocol for Code-First Peer Review**  
- **Date:** 2026-06-05
- **Authors:** Jienan Chen
- **Link:** https://arxiv.org/abs/2606.07683v1
- **Security insight:** Peer review in computational fields remains centered on author-written manuscripts, even though the decisive evidence for many claims resides in executable code, data, configurations, and experiment pipelines. This manuscript-first workflow gives authors…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**The Injection Paradox: Brand-Level Suppression in Safety-Trained LLM Recommendations via RAG Context Injection**  
- **Date:** 2026-06-08
- **Authors:** Hyunseok Paeng
- **Link:** https://arxiv.org/abs/2606.09204v1
- **Security insight:** We present a reproducible failure mode of safety training in RAG-based LLM recommendation -- the Injection Paradox -- in which prompt injections embedded in retrieved documents backfire against the attacker, suppressing the target brand below the injection-…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Document-Authored Control-Signal Impersonation: A Low-Cost Indirect Prompt Attack on RAG Safety Boundaries**  
- **Date:** 2026-06-08
- **Authors:** Jianguo Zhu
- **Link:** https://arxiv.org/abs/2606.09005v1
- **Security insight:** Retrieval-augmented generation (RAG) systems often serialize user queries, retrieved documents, metadata, system labels, and task instructions into one natural-language prompt. We study a source-authority boundary failure in this design: attacker-authored…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Hiding in Plain Floats: Steganographic Carriers for Indirect Prompt and Content Injection**  
- **Date:** 2026-06-07
- **Authors:** Mudit Sinha, Sanika Chavan
- **Link:** https://arxiv.org/abs/2606.08403v1
- **Security insight:** Text-centered prompt-injection defenses assume that the malicious signal is visible in one of the inspected text views. We study a reproducible LLM01-style indirect prompt/content-injection failure mode where that assumption breaks: a payload caught in plain…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Beyond Pass/Fail: Using Process Mining to Understand How LLMs Resist (and Fail) Red Team Attacks**  
- **Date:** 2026-06-05
- **Authors:** Zvi Topol
- **Link:** https://arxiv.org/abs/2606.07833v1
- **Security insight:** Standard AI red teaming evaluations reduce adversarial campaigns to a single binary outcome, attack success rate (ASR), not taking into account the sequential structure of how models resist or yield to attacks. We propose applying process mining, a discipline…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**An Embarrassingly Simple Detector for Model Extraction Attacks in Large Language Model API Traffic**  
- **Date:** 2026-06-04
- **Authors:** Shuze Liu, Qianwen Guo, Yushun Dong
- **Link:** https://arxiv.org/abs/2606.05725v1
- **Security insight:** Large language models (LLMs) are increasingly deployed through hosted APIs, making model extraction a practical threat to model ownership and service security. However, individual extraction queries often resemble benign requests, and existing evaluations…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Adversarial ML

**Learning to Attack and Defend: Adaptive Red Teaming of Language Models via GRPO**  
- **Date:** 2026-06-08
- **Authors:** Blake Bullwinkel, Eugenia Kim, Amanda Minnich et al.
- **Link:** https://arxiv.org/abs/2606.09701v1
- **Security insight:** AI red teaming must continually adapt to evolving attackers and defenders. Reinforcement learning offers a promising approach to discovering novel attacks, and co-training methods can produce more robust defenders in tandem. Recent works have demonstrated the…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

### Other (Review)

**Safety Paradox: How Enhanced Safety Awareness Leaves LLMs Vulnerable to Posterior Attack**  
- **Date:** 2026-06-04
- **Authors:** Long P. Hoang, Hai V. Le, Shaoyang Xu et al.
- **Link:** https://arxiv.org/abs/2606.05614v1
- **Security insight:** Large language models (LLMs) are rigorously aligned to refuse harmful requests, a process that inherently cultivates a latent capacity to evaluate and recognize unsafe content. In this work, we reveal that this advanced safety awareness inadvertently…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
