# AI Security Radar

_Last updated (UTC): **2026-09-29**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

**Tracekit: Tamper-Evident Intent-Reasoning-Action Auditing for Autonomous Coding Agents**  
- **Date:** 2026-09-28
- **Authors:** Bravish Ghosh
- **Link:** https://arxiv.org/abs/2609.35659v1
- **Security insight:** Autonomous coding agents read untrusted files, run shell commands and spawn sub-agents with little supervision, yet their record is usually an editable log. We present Tracekit, an open-source, dependency-free system that captures three channels for every…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Nudgeability: Reasoning Models Follow Confidence Signals Without Tracking Their Own Competence**  
- **Date:** 2026-09-28
- **Authors:** Rohit Saxena, Utkarsh Upadhyay
- **Link:** https://arxiv.org/abs/2609.34572v1
- **Security insight:** Reasoning language models that can call tools must decide during inference whether to answer unaided or delegate. Any self-reflection mechanism for this must answer three questions: where the reflective signal comes from (verbal reports, output distributions,…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**CoDeL: Co-Evolutionary Defense against Indirect Prompt Injection in LLM-based Agents**  
- **Date:** 2026-09-28
- **Authors:** Xiao Yang, Yangchen Ou, Yuhan Gao et al.
- **Link:** https://arxiv.org/abs/2609.34463v1
- **Security insight:** Large language model (LLM)-based agents increasingly rely on external tools and content, exposing them to indirect prompt injection (IPI). This threat has motivated a wide range of defenses, among which training-based defenses are often regarded as most…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Certified Multi-Source Integrity for Structured Agent Actions**  
- **Date:** 2026-09-28
- **Authors:** Anmol Pandey, Aditya Jain, Liang Chen et al.
- **Link:** https://arxiv.org/abs/2609.34245v1
- **Security insight:** LLM agents increasingly take privileged, often irreversible structured actions, such as paying an invoice. They assemble each action from action-critical fields in documents and tool outputs that an adversary can corrupt, and indirect prompt injection can…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Climbing the Hill: Prompt Injection Red-Teaming Against Frontier Models with Curriculum Reinforcement Learning**  
- **Date:** 2026-09-27
- **Authors:** Chenlong Yin, Xiaolong Jin, Wei Zou et al.
- **Link:** https://arxiv.org/abs/2609.33628v1
- **Security insight:** Prompt injection is a leading security risk for LLMs and LLM-based applications such as agents. State-of-the-art red-teaming methods for prompt injection leverage reinforcement learning (RL) to train an attacker LLM to generate effective injected prompts.…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**API Secrets Should Never Become Tokens in the LLM's Vocabulary: A Threat Analysis of API Credential Handling in LLM Agent Systems and an Empirical Evaluation of a Vault-Mediated Execution Boundary**  
- **Date:** 2026-09-27
- **Authors:** Patrick Kenney, Hadi Ahmadi, Denis Lusson et al.
- **Link:** https://arxiv.org/abs/2609.33371v1
- **Security insight:** Tool-using large language model (LLM) agents turn credential hygiene from a storage problem into an execution-security problem. A key pasted into a prompt, or embedded in a system prompt or tool configuration, crosses from an authentication boundary into a…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**ORBIT: A Framework for Multi-Agent Safety and Security Evaluations**  
- **Date:** 2026-09-27
- **Authors:** Ben Hagag, William L. Anderson, Srija Chakraborty et al.
- **Link:** https://arxiv.org/abs/2609.33102v1
- **Security insight:** Multi-agent LLM systems are increasingly deployed for complex, long-horizon tasks or emerge as a natural consequence of agents interacting in the wild. Yet they give rise to significant safety and security risks: the flexible protocols that enable task…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Silent Failures in Agentic Security Evaluation: A Validated Harness for Tool-Call Mediation Under Indirect Prompt Injection**  
- **Date:** 2026-09-26
- **Authors:** Animesh Shaw
- **Link:** https://arxiv.org/abs/2609.32691v1
- **Security insight:** LLM agents that invoke privileged tools are vulnerable to indirect prompt injection (IPI), in which adversarial instructions embedded in retrieved data hijack the agent's actions. A growing body of work evaluates defenses against IPI, but the validity of that…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### Poisoning & Backdoors

**A Solvable Theory of Pre-training Data Poisoning: Regime-Dependent Scaling Exponents**  
- **Date:** 2026-09-26
- **Authors:** Indranil Halder, Rastri Dey, Cengiz Pehlevan
- **Link:** https://arxiv.org/abs/2609.32288v1
- **Security insight:** Pre-training data poisoning of large language models is usually studied using targeted backdoors and their survival through safety post-training, which leaves open a more basic question: how does a model's clean data performance degrade as the poison rate…
- **Build idea:** Build a minimal poisoning simulator plus simple detectors (trigger search, label flip tests, anomaly baselines).

### Model Extraction & Privacy

**Unknown is not normal: separating language-model extraction from rule-based decision logic for clinical risk scores**  
- **Date:** 2026-09-28
- **Authors:** Nicolás Vera Zúñiga
- **Link:** https://arxiv.org/abs/2609.34112v1
- **Security insight:** Large language models (LLMs) are increasingly used to compute clinical risk scores from free-text notes. Notes are often incomplete, and treating undocumented findings as normal can silently misclassify patients. We test whether separating three-state…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

**User Model Extraction via Belief Self-Distillation**  
- **Date:** 2026-09-25
- **Authors:** Ali Holmov, Yiran Huang, Kirill Bykov et al.
- **Link:** https://arxiv.org/abs/2609.31603v1
- **Security insight:** Large language models (LLMs) implicitly infer attributes of their users and adapt their behavior accordingly, yet these beliefs remain difficult to inspect and causally manipulate. We introduce Belief Self-Distillation (BSD), a unified read-write framework…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

### Adversarial ML

**When Consent Outlives Context: Residual Authority Replay in Long-Lived Agents**  
- **Date:** 2026-09-27
- **Authors:** Zhihao Zhang, Chao Wang, Rujia Li et al.
- **Link:** https://arxiv.org/abs/2609.33910v1
- **Security insight:** LLM agents increasingly rely on user approval to authorize security-sensitive actions at runtime. Such approvals are granted within a specific task and execution context. In long-lived agents, authorization decisions may need to persist across tasks or…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

### Agent & Tool Security

**CoSec: Benchmarking Agent Security in Communities**  
- **Date:** 2026-09-28
- **Authors:** Hao Chen, Wenhui Dong, Ye Chen et al.
- **Link:** https://arxiv.org/abs/2609.34790v1
- **Security insight:** LLM agents operate in persistent collaborative environments involving multiple users, communities, memories, files, and tools. Community boundaries may remain fixed or evolve with changes in membership, roles, composition, and relationships. Agents must…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Evaluating System One Models for Agent Security Decisions: Reliability, Calibration, and Selective Automation**  
- **Date:** 2026-09-27
- **Authors:** Yixuan Liu
- **Link:** https://arxiv.org/abs/2609.33401v1
- **Security insight:** Model-based judges support agent security by detecting prompt injections, assessing interaction risks, and screening harmful requests. System One models expose typed decisions with probabilities that software can use to allow, block, or escalate inputs, but…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.
