# AI Security Radar

_Last updated (UTC): **2026-09-04**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

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

**Delegation Without Trust: An Empirical Gap Analysis of Identity, Authorization, and Runtime Governance in Multi-Agent LLM Systems**  
- **Date:** 2026-08-31
- **Authors:** Panduranga Sai Varma Dantuluri, Jyotirmoy Sundi
- **Link:** https://arxiv.org/abs/2609.00267v1
- **Security insight:** Autonomous LLM agents increasingly act on a user's behalf: they hold credentials, call tools and services, and spawn sub-agents that act further on their behalf. This turns a long-standing distributed-systems question -- who is authorized to do what, on whose…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**ECLIPSE: Self-Evolving Stealthy Prompt Injection Attack against Long-Horizon Agentic Systems**  
- **Date:** 2026-08-31
- **Authors:** Shiqian Zhao, Yangfan Zhou, Xinfeng Li et al.
- **Link:** https://arxiv.org/abs/2608.30441v1
- **Security insight:** Recently, large language model (LLM) agents, such as Codex, Claude Code, and OpenClaw, have become capable of planning and executing long-horizon tasks through repeated tool calls. This capability also creates new opportunities for prompt injection. Existing…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Attesting Outputs and Delegation Ancestry in Multi-Agent AI Systems**  
- **Date:** 2026-08-31
- **Authors:** Lifei Liu, Haoran Yu
- **Link:** https://arxiv.org/abs/2608.30387v1
- **Security insight:** Multi-agent applications delegate work across independently operated deployers. After an incident, a verifier must answer two questions: which deployer released the reported bytes, and whether each cross-deployer edge was authorized. Credentials establish who…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Will the User Ever Know? Covert Indirect Prompt Injection Attacks on Tool-Using LLM Agents**  
- **Date:** 2026-08-31
- **Authors:** Yunseok Lee, Yunji Kim, Woojin Lee
- **Link:** https://arxiv.org/abs/2608.30362v2
- **Security insight:** As LLM agents take real-world actions through tools, indirect prompt injection (IPI) has emerged as a serious threat. The standard metric, Attack Success Rate (ASR), counts whether an injection succeeds but ignores what the user notices in the agent's final…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

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
