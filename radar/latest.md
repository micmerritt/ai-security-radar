# AI Security Radar

_Last updated (UTC): **2026-11-26**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

**MINE: A Training-Free Defense against Indirect Prompt Injection via Mutual Information and Embedding Variance**  
- **Date:** 2026-11-25
- **Authors:** Truong Phan, Ngoc-Quan Pham, Dat Quoc Nguyen
- **Link:** https://arxiv.org/abs/2611.34188v1
- **Security insight:** Existing defenses against indirect prompt injection in retrieval-augmented generation (RAG) are inherently reactive: prompt-engineering methods are often overridden by the injected instructions, while supervised detectors must be retrained for each new attack…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**The Detour Is the Danger: Preserving Security During LLM Agent Recovery**  
- **Date:** 2026-11-25
- **Authors:** Boyang Ma, Jinku Li, Hao Wu et al.
- **Link:** https://arxiv.org/abs/2611.33605v1
- **Security insight:** LLM agents increasingly rely on external tools and reusable Skills to execute complex workflows, autonomously replanning when operations fail. However, such recovery may preserve task functionality while silently discarding the security protections required…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**AVERT: Anomalous Value Erasure with Response Testing against Visual Prompt Injection**  
- **Date:** 2026-11-24
- **Authors:** Newt Hue-Nam K. Nguyen, Jui-Yu Ho, Wei-Han Chen et al.
- **Link:** https://arxiv.org/abs/2611.33532v1
- **Security insight:** Vision Language Models (VLMs) are vulnerable to visual prompt injection, in which an adversarially perturbed image forces the model to respond with the attacker's chosen content, such as malicious tool calls, website links, or advertisements, sometimes…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Poisoning Self-Evolving Security Policies in LLM Agents**  
- **Date:** 2026-11-24
- **Authors:** Aymen Noor, Honglu Jiang
- **Link:** https://arxiv.org/abs/2611.33385v1
- **Security insight:** Self-evolving defenses improve LLM-agent security by learning reusable policies from observed attacks. However, we demonstrate that this learning process itself can become an attack surface. Using SED (Self-Evolving Defense) in the AgentDojo benchmark, we…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Attestation is All You Need: Toward a Zero-Trust Architecture for HPC AI Agents**  
- **Date:** 2026-11-24
- **Authors:** Jie Li, Chenxu Niu, Tongyang Wang et al.
- **Link:** https://arxiv.org/abs/2611.32958v1
- **Security insight:** AI agents are beginning to automate data analysis, orchestration, and simulation steering in HPC environments, but they introduce a security problem that existing cluster defenses do not address: the hijacked authorized agent. An adversary can subvert an…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**CAPTA: Identifying LLMs Behind AI Agents**  
- **Date:** 2026-11-24
- **Authors:** Kailun Yan, Yue Huang, Sisi Duan
- **Link:** https://arxiv.org/abs/2611.32686v1
- **Security insight:** Large language model (LLM)-based agents access remote services through tools to complete user tasks, often via API calls. In this setting, a remote service may want to identify the backend LLM of an agent to launch model-specific attacks, including prompt…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**LLM Agent Authorization Across Context Compaction**  
- **Date:** 2026-11-24
- **Authors:** Zeming Fei, Hongming Fei, Yi Xu et al.
- **Link:** https://arxiv.org/abs/2611.32194v1
- **Security insight:** Request-derived authorizers such as Progent protect LLM agents from prompt injection by deriving what an agent may do from the user's request. Their guarantee rests on attribution: the request is taken to be what the user said. Compaction breaks it. At every…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**ContextLure: Exploiting Benign Conversation History for Indirect Prompt Injection**  
- **Date:** 2026-11-23
- **Authors:** Yi Han, Zhen Sun, Zhijie Deng et al.
- **Link:** https://arxiv.org/abs/2611.31424v1
- **Security insight:** As LLMs become more capable, agents can perform more complex tasks with tools and maintain longer interactions with users. These benign conversations contain evidence on task results, user concerns, and operational constraints. The risk is that attackers who…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Carried-Over and Agent-Native Threats in the Supply Chain of LLM Agent Skills**  
- **Date:** 2026-11-23
- **Authors:** Kaixuan Li, Wenbo Guo, Sen Chen et al.
- **Link:** https://arxiv.org/abs/2611.30932v1
- **Security insight:** Agent skills are reusable packages that extend a large language model (LLM) agent with scripts, third-party dependencies, and natural-language instructions. An agent builds a skill's arguments from user requests and untrusted external content, so a flaw left…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**AgentBouncer: Defending Software Engineering Agents via Dynamic System-Call Mediation**  
- **Date:** 2026-11-23
- **Authors:** Pascal Joos, Michael Pradel
- **Link:** https://arxiv.org/abs/2611.30621v1
- **Security insight:** Software engineering (SE) agents can complete diverse engineering tasks by interacting with the development environment via tools that access files, run commands, and download resources. Unfortunately, the same ability that makes SE agents useful also makes…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Adversarial ML

**SALSA: Sampling Adversarial Suffixes from Learned Distributions for LLM Safety Assessment**  
- **Date:** 2026-11-24
- **Authors:** Shivank Rajput, Himanshu Singh, A. V. Subramanyam
- **Link:** https://arxiv.org/abs/2611.33030v1
- **Security insight:** Large language models (LLMs) remain vulnerable to jailbreak attacks, where adversaries append optimized suffixes to otherwise benign looking prompts to bypass safety alignment. Existing optimization-based GCG-style attacks can be effective, but they are…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

### Agent & Tool Security

**Latent-in-the-Middle: On the Security of Cross-Model Latent Communication in Multi-Agent Systems**  
- **Date:** 2026-11-25
- **Authors:** Manit Baser, Vyoman Jain, Rachel Yeo Hui Min et al.
- **Link:** https://arxiv.org/abs/2611.34278v1
- **Security insight:** As large language models increasingly collaborate in heterogeneous multi-agent systems, latent communication has emerged as an efficient alternative to exchanging natural-language messages. By sharing internal representations, agents can avoid repeatedly…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Evaluating LLM Security Review Agents with Operationally Sourced Ground Truth**  
- **Date:** 2026-11-23
- **Authors:** Mudita Khurana, Karim Liman-Tinguiri
- **Link:** https://arxiv.org/abs/2611.31606v1
- **Security insight:** LLM-based security review agents can reason about vulnerabilities that deterministic tools miss, but deploying them responsibly requires knowing whether they actually work. Existing benchmarks construct ground truth synthetically or from public CVE databases…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Other (Review)

**Not Just Any Example: Security Requirements and Fix Patterns for Guiding LLM Vulnerability Repair**  
- **Date:** 2026-11-24
- **Authors:** Zichen Liu, Liangyi Huang, Stanley Nguyen et al.
- **Link:** https://arxiv.org/abs/2611.31993v1
- **Security insight:** Software vulnerabilities leave systems open to attack, and their remediation is often delayed. Large language models (LLMs) have advanced automated patch generation, yet passing functionality tests does not ensure that a patch enforces the security…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
