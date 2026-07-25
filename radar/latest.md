# AI Security Radar

_Last updated (UTC): **2026-07-25**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**The Ethics of Autonomous AI Agents for Offensive Security**  
- **Date:** 2026-07-22
- **Authors:** Andreas Happe, Jürgen Cito, Jasmin Wachter
- **Link:** https://arxiv.org/abs/2607.20255v1
- **Security insight:** LLM-driven autonomous agents are reshaping offensive security. Unlike traditional penetration-testing tooling -- deterministic, narrowly scoped, and operated by trained practitioners -- agentic security tools exhibit \textit{indeterminacy} along three…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Know Your Agent: Reconnaissance-Driven Pentesting of AI Agents**  
- **Date:** 2026-07-22
- **Authors:** Or Zion Eliav, Eyal Lenga, Shir Bernstien et al.
- **Link:** https://arxiv.org/abs/2607.19837v1
- **Security insight:** Traditional pentesting uses reconnaissance at each step to uncover unseen weaknesses, build stronger attacks, and advance the objective; we argue that AI agents require the same treatment. We formalize agent reconnaissance by modeling the process and…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Twin Agent: Context Residual Compression for Privilege Separated Agents**  
- **Date:** 2026-07-21
- **Authors:** Zhanhao Hu, Dennis Jacob, Xiao Huang et al.
- **Link:** https://arxiv.org/abs/2607.19595v1
- **Security insight:** Large language model (LLM) agents are vulnerable to security risks, such as prompt injection attacks from untrusted context that manipulate downstream reasoning and tool use. Existing secure-by-design approaches mitigate this risk by separating untrusted…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**The safety failures we are not instrumenting: a perspective on hidden safety-critical challenges in modern AI systems**  
- **Date:** 2026-07-21
- **Authors:** Gjergji Kasneci, Enkelejda Kasneci
- **Link:** https://arxiv.org/abs/2607.19292v1
- **Security insight:** Current AI safety discourse still focuses disproportionately on visible failures, including obvious harms, dramatic misuse, and hypothetical catastrophic scenarios. That focus is incomplete. In deployed systems, many of the most consequential failures are…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Data Leakage Prevention in Agentic Applications via Preemptive Hardening**  
- **Date:** 2026-07-21
- **Authors:** Akansha Shukla, Emily Bellov, Parth Atulbhai Gandhi et al.
- **Link:** https://arxiv.org/abs/2607.18847v1
- **Security insight:** Agentic systems integrate LLM driven planning with interfaces to external tools, making data leakage and tool misuse feasible via instruction/data boundary failures and prompt injection attacks. Enforcing required controls consistently is particularly…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**ChainWatch: A Kill Chain-Aligned Sequential Detection Framework for Multi-Step Attacks in MCP-Based AI Agent Systems**  
- **Date:** 2026-07-20
- **Authors:** Om Narayan, Rashmi Jyoti, Ramkinker Singh
- **Link:** https://arxiv.org/abs/2607.19432v1
- **Security insight:** The Model Context Protocol (MCP) is an open-source standard that allows AI agents to connect to external tools, databases, and services. While this connectivity enables powerful agent capabilities, it also introduces multi-step attacks that existing per-call…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Trusted Credentials, Untrusted Behavior: Benchmarking LLM-Agent Security in High-Performance Computing**  
- **Date:** 2026-07-20
- **Authors:** Jie Li
- **Link:** https://arxiv.org/abs/2607.18485v1
- **Security insight:** Large language model (LLM) agents are starting to take on routine work in high-performance computing (HPC), including monitoring Slurm jobs, diagnosing failed builds, inspecting simulation output, and coordinating scientific workflows. To do this work, an…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**ChannelGuard: Safe Models Do Not Compose into Safe Multi-Agent Systems**  
- **Date:** 2026-07-20
- **Authors:** Elias Hossain, Md Mehedi Hasan Nipu, Fatema Tuj Johora Faria et al.
- **Link:** https://arxiv.org/abs/2607.19430v1
- **Security insight:** Multi-agent LLM applications chain a planner, worker agents, a verifier, and a synthesizer, and every hop between agents is an unmonitored channel through which an adversary can smuggle instructions. Existing defenses guard only the input boundary…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Adaptive Adversaries: A Multi-Turn, Multi-LLM Benchmark for LLM Agent Security**  
- **Date:** 2026-07-20
- **Authors:** Devina Jain, David Hartmann, Chuan Li
- **Link:** https://arxiv.org/abs/2607.18063v1
- **Security insight:** LLM-based agents process external content, exposing them to prompt injection and multi-turn manipulation. Most safety benchmarks evaluate defenders against fixed attack pools collected before evaluation, single-turn or multi-turn. We present a 21-scenario…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Stress Testing Concept Erasure with Large Language Model Agents**  
- **Date:** 2026-07-20
- **Authors:** Yuyang Xue, Feng Chen, Zhihua Liu et al.
- **Link:** https://arxiv.org/abs/2607.17890v2
- **Security insight:** Concept erasure aims to remove semantic concepts from a trained generative model and is increasingly important for responsible AI deployment. However, verifying whether a model has robustly removed targeted concepts remains a critical challenge. Existing…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Salience Induction against Multi-Hop RAG Agents: Threat and Defense**  
- **Date:** 2026-07-20
- **Authors:** Xingfu Zhou, Pengfei Wang, Yuan Zhou et al.
- **Link:** https://arxiv.org/abs/2607.17535v1
- **Security insight:** Agentic retrieval-augmented generation (RAG) systems increasingly retrieve external evidence and orchestrate tools for knowledge-intensive applications. In Multi-Hop question answering, agents chain facts across documents. Existing defenses focus on content…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**V-DEAL: Diagnosing Video Safety De-Calibration as an Understanding-Refusal Coupling Failure**  
- **Date:** 2026-07-23
- **Authors:** Zhetong Zhang, Honghao Fu, Miao Xu et al.
- **Link:** https://arxiv.org/abs/2607.21151v1
- **Security insight:** As Video Large Language Models are increasingly deployed in real-world applications, ensuring their safety alignment has become critical. Counterintuitively, we find that harmful videos paired with benign queries achieve higher attack success rates than the…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**CPInj: Uncovering Prompt Injection Risks in Textual Collaborative Prompt Optimization**  
- **Date:** 2026-07-21
- **Authors:** Xinting Liao, Behnoosh Zamanlooy, Masoumeh Shafieinejad et al.
- **Link:** https://arxiv.org/abs/2607.18622v1
- **Security insight:** Textual Collaborative Prompt Optimization (TCPO) extends Textgrad (Yuksekgonul et al., 2025) to a decentralized setting by allowing multiple clients to jointly improve prompts for large language models (LLMs) while keeping their data locally. Its reliance on…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**A Multi-Model Hybrid Defense Approach Against White-box Adversarial Attacks in Computer Network Traffic**  
- **Date:** 2026-07-19
- **Authors:** Khushnaseeb Roshan
- **Link:** https://arxiv.org/abs/2607.17105v1
- **Security insight:** It is crucial to safeguard computer networks from evolving network security threats and unknown cyberattacks. An essential tool for protecting computer networks against unknown cyber threats is Network Intrusion Detection System (NIDS). However, NIDS faces a…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.
