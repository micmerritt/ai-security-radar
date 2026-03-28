# AI Security Radar

_Last updated (UTC): **2026-03-28**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs**  
- **Date:** 2026-03-25
- **Authors:** Alexander Panfilov, Peter Romov, Igor Shilov et al.
- **Link:** https://arxiv.org/abs/2603.24511v1
- **Security insight:** LLM agents like Claude Code can not only write code but also be used for autonomous AI research and engineering \citep{rank2026posttrainbench, novikov2025alphaevolve}. We show that an \emph{autoresearch}-style pipeline \citep{karpathy2026autoresearch} powered…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Invisible Threats from Model Context Protocol: Generating Stealthy Injection Payload via Tree-based Adaptive Search**  
- **Date:** 2026-03-25
- **Authors:** Yulin Shen, Xudong Pan, Geng Hong et al.
- **Link:** https://arxiv.org/abs/2603.24203v1
- **Security insight:** Recent advances in the Model Context Protocol (MCP) have enabled large language models (LLMs) to invoke external tools with unprecedented ease. This creates a new class of powerful and tool augmented agents. Unfortunately, this capability also introduces an…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**The Cognitive Firewall:Securing Browser Based AI Agents Against Indirect Prompt Injection Via Hybrid Edge Cloud Defense**  
- **Date:** 2026-03-24
- **Authors:** Qianlong Lan, Anuj Kaul
- **Link:** https://arxiv.org/abs/2603.23791v1
- **Security insight:** Deploying large language models (LLMs) as autonomous browser agents exposes a significant attack surface in the form of Indirect Prompt Injection (IPI). Cloud-based defenses can provide strong semantic analysis, but they introduce latency and raise privacy…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Mind Your HEARTBEAT! Claw Background Execution Inherently Enables Silent Memory Pollution**  
- **Date:** 2026-03-24
- **Authors:** Yechao Zhang, Shiqian Zhao, Jie Zhang et al.
- **Link:** https://arxiv.org/abs/2603.23064v2
- **Security insight:** We identify a critical security vulnerability in mainstream Claw personal AI agents: untrusted content encountered during heartbeat-driven background execution can silently pollute agent memory and subsequently influence user-facing behavior without the…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**SoK: The Attack Surface of Agentic AI -- Tools, and Autonomy**  
- **Date:** 2026-03-24
- **Authors:** Ali Dehghantanha, Sajad Homayoun
- **Link:** https://arxiv.org/abs/2603.22928v1
- **Security insight:** Recent AI systems combine large language models with tools, external knowledge via retrieval-augmented generation (RAG), and even autonomous multi-agent decision loops. This agentic AI paradigm greatly expands capabilities - but also vastly enlarges the…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Model Context Protocol Threat Modeling and Analyzing Vulnerabilities to Prompt Injection with Tool Poisoning**  
- **Date:** 2026-03-23
- **Authors:** Charoes Huang, Xin Huang, Ngoc Phu Tran et al.
- **Link:** https://arxiv.org/abs/2603.22489v1
- **Security insight:** The Model Context Protocol (MCP) has rapidly emerged as a universal standard for connecting AI assistants to external tools and data sources. While MCP simplifies integration between AI applications and various services, it introduces significant security…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Prompt Attack Detection with LLM-as-a-Judge and Mixture-of-Models**  
- **Date:** 2026-03-26
- **Authors:** Hieu Xuan Le, Benjamin Goh, Quy Anh Tang
- **Link:** https://arxiv.org/abs/2603.25176v1
- **Security insight:** Prompt attacks, including jailbreaks and prompt injections, pose a critical security risk to Large Language Model (LLM) systems. In production, guardrails must mitigate these attacks under strict low-latency constraints, resulting in a deployment gap in which…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**PIDP-Attack: Combining Prompt Injection with Database Poisoning Attacks on Retrieval-Augmented Generation Systems**  
- **Date:** 2026-03-26
- **Authors:** Haozhen Wang, Haoyue Liu, Jionghao Zhu et al.
- **Link:** https://arxiv.org/abs/2603.25164v1
- **Security insight:** Large Language Models (LLMs) have demonstrated remarkable performance across a wide range of applications. However, their practical deployment is often hindered by issues such as outdated knowledge and the tendency to generate hallucinations. To address these…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**LLMON: An LLM-native Markup Language to Leverage Structure and Semantics at the LLM Interface**  
- **Date:** 2026-03-23
- **Authors:** Michael Hind, Basel Shbita, Bo Wu et al.
- **Link:** https://arxiv.org/abs/2603.22519v1
- **Security insight:** Textual Large Language Models (LLMs) provide a simple and familiar interface: a string of text is used for both input and output. However, the information conveyed to an LLM often has a richer structure and semantics, which is not conveyed in a string. For…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**SecureBreak -- A dataset towards safe and secure models**  
- **Date:** 2026-03-23
- **Authors:** Marco Arazzi, Vignesh Kumar Kembu, Antonino Nocera
- **Link:** https://arxiv.org/abs/2603.21975v1
- **Security insight:** Large language models are becoming pervasive core components in many real-world applications. As a consequence, security alignment represents a critical requirement for their safe deployment. Although previous related works focused primarily on model…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**AI Security in the Foundation Model Era: A Comprehensive Survey from a Unified Perspective**  
- **Date:** 2026-03-25
- **Authors:** Zhenyi Wang, Siyu Luan
- **Link:** https://arxiv.org/abs/2603.24857v1
- **Security insight:** As machine learning (ML) systems expand in both scale and functionality, the security landscape has become increasingly complex, with a proliferation of attacks and defenses. However, existing studies largely treat these threats in isolation, lacking a…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Poisoning & Backdoors

**On the Vulnerability of Deep Automatic Modulation Classifiers to Explainable Backdoor Threats**  
- **Date:** 2026-03-26
- **Authors:** Younes Salmi, Hanna Bogucka
- **Link:** https://arxiv.org/abs/2603.25310v1
- **Security insight:** Deep learning (DL) has been widely studied for assisting applications of modern wireless communications. One of the applications is automatic modulation classification (AMC). However, DL models are found to be vulnerable to adversarial machine learning (AML)…
- **Build idea:** Build a minimal poisoning simulator plus simple detectors (trigger search, label flip tests, anomaly baselines).

**Physical Backdoor Attack Against Deep Learning-Based Modulation Classification**  
- **Date:** 2026-03-26
- **Authors:** Younes Salmi, Hanna Bogucka
- **Link:** https://arxiv.org/abs/2603.25304v1
- **Security insight:** Deep Learning (DL) has become a key technology that assists radio frequency (RF) signal classification applications, such as modulation classification. However, the DL models are vulnerable to adversarial machine learning threats, such as data manipulation…
- **Build idea:** Build a minimal poisoning simulator plus simple detectors (trigger search, label flip tests, anomaly baselines).

### Model Extraction & Privacy

**A Public Theory of Distillation Resistance via Constraint-Coupled Reasoning Architectures**  
- **Date:** 2026-03-26
- **Authors:** Peng Wei, Wesley Shu
- **Link:** https://arxiv.org/abs/2603.25022v1
- **Security insight:** Knowledge distillation, model extraction, and behavior transfer have become central concerns in frontier AI. The main risk is not merely copying, but the possibility that useful capability can be transferred more cheaply than the governance structure that…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?
