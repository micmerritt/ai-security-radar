# AI Security Radar

_Last updated (UTC): **2026-09-07**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**CONTINUITY: Security-Context Contracts for Composable LLM Agent Controls**  
- **Date:** 2026-09-04
- **Authors:** Chris Zheng, Geng Yang
- **Link:** https://arxiv.org/abs/2609.05269v1
- **Security insight:** LLM agent systems increasingly combine provenance tracking, authorization, policy enforcement, protocol adapters, and execution controls. However, individually correct security mechanisms do not necessarily compose into an end-to-end secure system: security-…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Repeat-After-Me: Black-Box Adaptive Visual Prompt Injection**  
- **Date:** 2026-09-03
- **Authors:** Sizhe Chen, Yu-Lin Tsai, Ivan Evtimov et al.
- **Link:** https://arxiv.org/abs/2609.04533v1
- **Security insight:** Prompt injection is widely recognized as a major security threat to AI agents that interact with untrusted external data, such as websites, documents, and emails. Prior work has shown that, in the text domain, black-box prompt injection can achieve near-…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Rethinking Indirect Prompt Injection as a Test-Time Search Problem**  
- **Date:** 2026-09-03
- **Authors:** Duong M. Nguyen, Joon Sik Kim, Blazej Manczak et al.
- **Link:** https://arxiv.org/abs/2609.04495v1
- **Security insight:** We formulate indirect prompt injection as a test-time search over a task-dependent attack surface induced by the environment, user task, and injection task. To operationalize this formulation, we introduce an agentic attacker with a dedicated search harness…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Shifting from Injection to Interaction: Rethinking Web Security in the Age of LLMs and Beyond**  
- **Date:** 2026-09-03
- **Authors:** Nivedita Singh, Alsharif Abuadbba, Yansong Gao et al.
- **Link:** https://arxiv.org/abs/2609.03999v1
- **Security insight:** Large language models (LLMs) are becoming integral to web applications and browser agents, transforming online interactions while introducing new attack vectors and reshaping longstanding web vulnerabilities. Classical threats such as cross-site scripting…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Stored Is Not Supported: Typed Provenance and Assertion Guardrails for Persistent AI Agents**  
- **Date:** 2026-09-02
- **Authors:** Jun He, Deying Yu
- **Link:** https://arxiv.org/abs/2609.02127v1
- **Security insight:** Persistent AI agents construct autobiographical state through reflection, retrieval, and consolidation. Persistence changes availability, not epistemic standing: stored or retrieved material is not thereby supported. Untrusted inputs, prompt injections, and…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Implicit Manipulation for Skill Selection in LLM Agents with Semantic Matching**  
- **Date:** 2026-09-02
- **Authors:** Qikai Wang, Yongzhao Zhang, Zhiwei Chen et al.
- **Link:** https://arxiv.org/abs/2609.02035v1
- **Security insight:** Skill selection is a key stage in LLM-agent workflows, determining which installed skill should handle a user request. Existing attacks on this stage primarily rely on explicit prompt injection or instruction-level steering, which can expose recognizable…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Agent Flight Recorder: Tamper-Evident Audit Trails with On-Chain Anchoring for Long-Horizon Tool-Using Agents**  
- **Date:** 2026-09-01
- **Authors:** Laurent Bindschaedler, Quentin Botha, Christoph Siebenbrunner
- **Link:** https://arxiv.org/abs/2609.01931v1
- **Security insight:** Long-horizon agents execute thousands of actions, resulting in sequential failures rather than isolated errors. When a coding agent deletes a production database or a prompt injection spreads across agents, the incident raises questions of causality,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Skill-as-API: Confidential Multi-Agent Coordination for Agentic Software Engineering**  
- **Date:** 2026-09-01
- **Authors:** Ziwei Zhao, Yu Gu, Haojun Liang et al.
- **Link:** https://arxiv.org/abs/2609.01677v1
- **Security insight:** AI coding agents are evolving from solitary tools into collaborative teammates that discover and invoke one another's specialized skills. But the coordination channel itself can leak a skill's intellectual property. Protocols such as MCP and A2A run…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**SoK: When Safe Agents Fail Together: The Security of Multi Agent LLM Systems**  
- **Date:** 2026-09-01
- **Authors:** Rui Yang, Junjie Xu, Zhengyu Liu et al.
- **Link:** https://arxiv.org/abs/2609.00595v1
- **Security insight:** Safe agents can fail together. Multi-agent LLM systems (MAS) move information, state, decisions, and authority across principal boundaries, creating failures that local checks may miss. Without an execution-level view, a multi-agent setting can easily be…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Influence Score and Transformers interpretability: Measure of the Effective Impact of Attention Heads at inference time**  
- **Date:** 2026-09-04
- **Authors:** Lisa Bouger, Yannick Teglia, Philippe Loubet Moundi
- **Link:** https://arxiv.org/abs/2609.05074v1
- **Security insight:** We propose an influence score to quantify the contribution of attention heads to classification decisions in Transformer-based models designed for prompt injection detection. The score combines directional influence on the logits with structural contribution…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**HiveTraceGuard-Pro: A Compact Generative Guardrail for Prompt Injection, Jailbreaks, and Adversarial Obfuscation**  
- **Date:** 2026-09-01
- **Authors:** Nikita Oblakov, Sabrina Sadiekh, Evgeniy Kokuykin
- **Link:** https://arxiv.org/abs/2609.01046v1
- **Security insight:** Production LLMs must handle inputs that attempt to override system instructions, bypass safety policies or elicit harmful responses. A common mitigation is a separate guardrail model. Existing reports, however, provide little evidence on Russian prompt…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**The Implications of Linguistic Illegibility for LLM Security**  
- **Date:** 2026-09-02
- **Authors:** James Mickens
- **Link:** https://arxiv.org/abs/2609.02852v1
- **Security insight:** LLMs are trained to generate natural language. However, various strands of evidence indicate that an LLM's externalized linguistic outputs and mechanistically-extracted linguistic features can be an unreliable lens for understanding internal model…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**EvoFlint: An Evolutionary Atlas of Multi-Turn LLM Vulnerabilities**  
- **Date:** 2026-08-31
- **Authors:** Feitong Qiao, Liren Peng, Shiming Ren et al.
- **Link:** https://arxiv.org/abs/2609.00487v1
- **Security insight:** Frontier language models that refuse harmful single-turn prompts often comply when the same intent is reached gradually over many turns, making multi-turn attacks one of the least understood failure modes of large language models. Most automated red-teaming…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Other (Review)

**Trust Me, I'm Your Developer: Self-Issued Authentication in Large Language Models**  
- **Date:** 2026-09-03
- **Authors:** Syed Ghazanfar Abbas, Dongyan Xu
- **Link:** https://arxiv.org/abs/2609.03247v1
- **Security insight:** Large language model (LLM) security has largely focused on role-playing jailbreaks, with less attention to what happens when a user asks an LLM to verify an identity claim through a test designed by the model itself. We study this behavior through a staged…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
