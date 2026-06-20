# AI Security Radar

_Last updated (UTC): **2026-06-20**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Analyzing Defensive Misdirection Against Model-Guided Automated Attacks on Agentic AI Systems**  
- **Date:** 2026-06-18
- **Authors:** Reza Soosahabi, Vivek Namsani
- **Link:** https://arxiv.org/abs/2606.20470v1
- **Security insight:** Agentic AI systems increasingly rely on language-model components to interpret instructions, process external data, invoke tools, and coordinate with other agents. These capabilities make prompt-injection and jailbreak attacks more consequential, especially…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**CodeSentinel: A Three-Layer Defense Against Indirect Prompt Injection in Code Contexts**  
- **Date:** 2026-06-17
- **Authors:** Po-Han Cheng, Chia-Mu Yu, Ying-Dar Lin et al.
- **Link:** https://arxiv.org/abs/2606.19235v1
- **Security insight:** Code large language models increasingly retrieve external code context from repositories, documentation, issue threads, and coding-agent environments, creating an indirect prompt-injection surface where attackers hide instructions in comments, strings,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**The Gate Is Only as Honest as Its Contracts: ContractGuard for the Contract Layer of Risk-Aware Causal Gating**  
- **Date:** 2026-06-17
- **Authors:** Laxmipriya Ganesh Iyer, Rahul Suresh Babu
- **Link:** https://arxiv.org/abs/2606.18550v1
- **Security insight:** Risk-Aware Causal Gating (RACG) defends tool-augmented LLM agents against indirect prompt injection by removing dangerous tools from the agent's visible action space, so that even a fully injection-compliant agent cannot call a tool it cannot see. We make…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**SafeClawBench: Separating Semantic, Audit-Evidence, and Sandbox Harm in Tool-Using LLM Agents**  
- **Date:** 2026-06-16
- **Authors:** Yuchuan Tian, Mengyu Zheng, Haocheng Mei et al.
- **Link:** https://arxiv.org/abs/2606.18356v1
- **Security insight:** Tool-using language-model agents introduce security failures that go beyond unsafe text: they can disclose protected objects, write persistent memory, send messages, modify databases, or trigger harmful code and tool effects. Existing evaluations often…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**PARSE: Provenance-Aware Retrieval Sanitization for Professional Domain LLM Agents**  
- **Date:** 2026-06-16
- **Authors:** Aaditya Pai
- **Link:** https://arxiv.org/abs/2606.17467v1
- **Security insight:** Prompt injection defenses evaluated on synthetic benchmarks do not generalize to real enterprise documents, which are longer, denser, and interleave legitimate authority language with factual content. We demonstrate this gap with a real-document benchmark of…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**An Evaluation of Data Leakage Risks in Tool-Using LLM Agents in Realistic Scenarios**  
- **Date:** 2026-06-15
- **Authors:** Hankyul Baek, Jaewon Noh, Sang Seo et al.
- **Link:** https://arxiv.org/abs/2606.17114v1
- **Security insight:** AI agents are increasingly being adopted in enterprise and personal settings with access to emails, databases, documents, and other tools where they can read, update, and disseminate sensitive information. Much of prior research on data leakage risks in…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Transferable Self-Evolving Playbooks for Agentic Security Auditing**  
- **Date:** 2026-06-15
- **Authors:** Ziyue Wang, Cheuk Wang Maurice Ng, Chenchen Yu et al.
- **Link:** https://arxiv.org/abs/2606.16420v1
- **Security insight:** An LLM agent for vulnerability discovery and validation is more than a model. It combines three components: an LLM for code analysis, an agent harness such as Codex or OpenCode for navigation, tool use, and execution, and an audit playbook, domain-specific…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**A Layered Security Framework Against Prompt Injection in RAG-Based Chatbots**  
- **Date:** 2026-06-17
- **Authors:** Gulshan Saleem, Nisar Ahmed, Muhammad Imran Zaman et al.
- **Link:** https://arxiv.org/abs/2606.19660v1
- **Security insight:** Prompt injection is ranked as the most critical vulnerability in large language model (LLM) deployments by the OWASP Top 10 for LLM Applications, yet existing defenses operate at isolated pipeline stages and remain incomplete. Input filters cannot inspect…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Analyzing the Narration Gap in LLM-Solver Loops**  
- **Date:** 2026-06-17
- **Authors:** Zunchen Huang, Songgaojun Deng
- **Link:** https://arxiv.org/abs/2606.19588v1
- **Security insight:** Formal tools such as SAT and SMT solvers are increasingly embedded in language model reasoning pipelines when a safety or security critical question can be formulated in logic. Unlike chain of thought whose steps are sampled from the model distribution…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**KVEraser: Learning to Steer KV Cache for Efficient Localized Context Erasing**  
- **Date:** 2026-06-15
- **Authors:** Mufei Li, Shikun Liu, Dongqi Fu et al.
- **Link:** https://arxiv.org/abs/2606.17034v1
- **Security insight:** Post-hoc context erasing over the KV cache is challenging because a local edit has a global consequence: once a span has been processed, its influence propagates into the cached states of all subsequent tokens. This issue arises naturally in long-context LLM…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Rapid Poison: Practical Poisoning Attacks Against the Rapid Response Framework**  
- **Date:** 2026-06-15
- **Authors:** David Huang, Jaewon Chang, Avidan Shah et al.
- **Link:** https://arxiv.org/abs/2606.16242v1
- **Security insight:** The Rapid Response (RR) framework, deployed in production systems, including Anthropic's ASL-3 safeguards, continuously improves jailbreak-detection classifiers. When new jailbreaks emerge that bypass these classifiers, Rapid Response generates synthetic…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**MASCOT-Android: A Curated Dataset and Automated Collection Pipeline for Android Malware Source Code Specimens**  
- **Date:** 2026-06-15
- **Authors:** Bojing Li, Duo Zhong, Prajna Bhandary et al.
- **Link:** https://arxiv.org/abs/2606.16072v2
- **Security insight:** Compared with binaries and decompiled code, malware source code more directly reflects the attackers' original intent. However, the scarcity of source code and the high cost of manual review make such datasets difficult to build and maintain. We propose…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Poisoning & Backdoors

**Calibration Without Comprehension: Diagnosing the Limits of Fine-Tuning LLMs for Vulnerability Detection in Systems Software**  
- **Date:** 2026-06-18
- **Authors:** Arastoo Zibaeirad, Marco Vieira
- **Link:** https://arxiv.org/abs/2606.20502v1
- **Security insight:** Whether LLMs scoring well on vulnerability benchmarks genuinely reason about security or merely pattern-match on contaminated data remains unresolved. We present CWE-Trace, a framework for LLM vulnerability detection built from 834 manually curated Linux…
- **Build idea:** Build a minimal poisoning simulator plus simple detectors (trigger search, label flip tests, anomaly baselines).

### Other (Review)

**What Do Safety-Aligned LLMs Learn From Mixed Compliance Demonstrations?**  
- **Date:** 2026-06-18
- **Authors:** Sihui Dai, Mann Patel
- **Link:** https://arxiv.org/abs/2606.20508v1
- **Security insight:** Prior work has shown that in-context demonstrations can jailbreak language models, but it remains unclear how models interpret different types of compliance demonstrations. We study this by mixing benign compliance demonstrations (non-harmful request, helpful…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
