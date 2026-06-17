# AI Security Radar

_Last updated (UTC): **2026-06-17**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

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

**SkillVetBench: LLM-as-Judge for Multi-Dimensional Security Risk Evaluation in Open-Source LLM Agent Skills**  
- **Date:** 2026-06-14
- **Authors:** Ismail Hossain, Sai Puppala, Md Jahangir Alam et al.
- **Link:** https://arxiv.org/abs/2606.15899v1
- **Security insight:** Open-source LLM agent ecosystems are growing rapidly, yet the security of community-contributed skills - modular tool definitions that extend agent capabilities - remains largely unvetted. The gap we fill: existing scanners operate at the code layer and are…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Snyk VulnBench JS 1.0: Can LLMs Find the Same Bugs Twice?**  
- **Date:** 2026-06-14
- **Authors:** Liran Tal, Johannes Kloos, Arsenii Rudich et al.
- **Link:** https://arxiv.org/abs/2606.15762v1
- **Security insight:** We ran 300 repeated vulnerability-finding scans to measure how repeatable agentic large language model (LLM) security review is on the same JavaScript code, prompt, and benchmark harness. The headline result is that LLM security findings were unevenly…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**FragFuse: Bypassing Access Control of Large Language Model Agents via Memory-Based Query Fragmentation and Fusion**  
- **Date:** 2026-06-14
- **Authors:** Zixin Rao, Wentian Zhu, Chan Aristella Lu et al.
- **Link:** https://arxiv.org/abs/2606.15609v1
- **Security insight:** Large language model (LLM) agents increasingly rely on long-term memory to support complex task execution, user personalization, and domain adaptation. Meanwhile, emerging access-control mechanisms for LLM agents are being explored to block policy-violating…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Defending against Adaptive Prompt Injection Attacks via Reasoning-enabled Task Alignment**  
- **Date:** 2026-06-13
- **Authors:** Lipeng He, Yihan Wang, Jiawen Zhang et al.
- **Link:** https://arxiv.org/abs/2606.15441v1
- **Security insight:** Indirect prompt injection attacks hijack LLM-based agents by embedding malicious instructions in third-party data that the agent retrieves during task execution. Existing defenses report near-zero attack success rate on static benchmarks, yet recent adaptive…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**AutoDojo: Adaptive Attacks Expose Superficial Defenses and User-Underspecification Limits in LLM Agents**  
- **Date:** 2026-06-13
- **Authors:** Xinhang Ma, Taoran Li, Chaowei Xiao et al.
- **Link:** https://arxiv.org/abs/2606.15057v1
- **Security insight:** Indirect prompt injection (IPI) is a major security threat to LLM-powered agents. Thus, a growing body of work have proposed a variety of defensive approaches against IPI. These can be grouped into three broad categories: 1) prompt-based (using prompting as a…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

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

**GAS-Leak-LLM: Genetic Algorithm-Based Suffix Optimization for Black-Box LLM Jailbreaking**  
- **Date:** 2026-06-14
- **Authors:** Aman Anifer, Vignesh Kumar Kembu, Vishnu M et al.
- **Link:** https://arxiv.org/abs/2606.15788v1
- **Security insight:** Large Language Models (LLMs) constitute pivotal components within the AI-dominated information technology ecosystem. To mitigate risks associated with harmful or policy-violating outputs, commercial systems employ advanced alignment strategies and multi-…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**MASCOT-Android: A Curated Dataset and Automated Collection Pipeline for Android Malware Source Code Specimens**  
- **Date:** 2026-06-15
- **Authors:** Bojing Li, Duo Zhong, Prajna Bhandary et al.
- **Link:** https://arxiv.org/abs/2606.16072v2
- **Security insight:** Compared with binaries and decompiled code, malware source code more directly reflects the attackers' original intent. However, the scarcity of source code and the high cost of manual review make such datasets difficult to build and maintain. We propose…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**Let Them Steal: Trapping Large Language Model Extraction Attacks with Knowledge Honeypot**  
- **Date:** 2026-06-14
- **Authors:** Yuyang Dai, Yushun Dong
- **Link:** https://arxiv.org/abs/2606.15810v1
- **Security insight:** Large language models deployed as commercial APIs are vulnerable to model extraction attacks, while existing defenses either act too late or degrade utility for legitimate users. We propose \textbf{Knowledge Trap}, a defense that redirects extraction attacks…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Adversarial ML

**Forced Deferral: Manipulating Routing Decisions in Multimodal LLM Cascades**  
- **Date:** 2026-06-13
- **Authors:** Zhongye Liu, Yaopei Zeng, Yurui Chang et al.
- **Link:** https://arxiv.org/abs/2606.15308v1
- **Security insight:** While multimodal large language models (MLLMs) have shown strong visual reasoning abilities, serving a large model for every query is computationally expensive. MLLM cascades mitigate this cost by first querying a weak but cheaper model and deferring to a…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.
