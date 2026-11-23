# AI Security Radar

_Last updated (UTC): **2026-11-23**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

**Actions Speak Louder than Words: Stateful Privacy Sniffing of LLM Agents via Behavioral Covert Channels in Web Interactions**  
- **Date:** 2026-11-20
- **Authors:** Ruichao Liang, Wenzhong Deng, Jing Chen et al.
- **Link:** https://arxiv.org/abs/2611.27046v1
- **Security insight:** LLM agents increasingly rely on Web interaction, issuing searches, following links, and reading pages, to complete complex user tasks. Since each action is driven by the agent's private context, including the user's prompt, dialogue history, memory, and…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Subverting Tool Arguments: Defense-Evading Metadata Poisoning in LLM Agents**  
- **Date:** 2026-11-20
- **Authors:** Shih-Chieh Dai, Xinyu Sun, Haichuan Zhang et al.
- **Link:** https://arxiv.org/abs/2611.27041v1
- **Security insight:** Conventional indirect prompt injection (IPI) attacks hijack an LLM agent's workflow through malicious instructions embedded in retrieved external content. The growing adoption of the Model Context Protocol (MCP) exposes another attack surface: tool…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI)**  
- **Date:** 2026-11-19
- **Authors:** Mengxiao Wang, Mahbub Alam, Kalyan Nakka et al.
- **Link:** https://arxiv.org/abs/2611.26553v1
- **Security insight:** Agents based on large language models (LLMs) can now delete files and send payments on behalf of their users. News media reports routinely describe failures of these agents (e.g., Replit's coding agent deleting a production database), but a report often only…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**SEOYUN: Refusal-Inducing Exam Documents for AI-Glasses Pipelines**  
- **Date:** 2026-11-19
- **Authors:** Dohyeon Kwon
- **Link:** https://arxiv.org/abs/2611.26033v1
- **Security insight:** Camera-equipped glasses can convert an examination page into a query to a vision-language model (VLM). Device detection addresses possession; a complementary question is whether an examination document can reduce the usefulness of an unauthorized capture. We…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**PIPETTE: Prompt Injection Purple-Teaming for Robust LLM Agents**  
- **Date:** 2026-11-18
- **Authors:** Lipeng He, Yihan Wang, Jiawen Zhang et al.
- **Link:** https://arxiv.org/abs/2611.24362v1
- **Security insight:** Large language model (LLM) agents routinely interact with untrusted external data, exposing them to indirect prompt injection (IPI) attacks that hijack agents into executing attacker-chosen tasks. To uncover these vulnerabilities at scale, automated red-…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**AutoPI: Taxonomy-Guided Adaptive Red Teaming for Prompt Injection in LLM Agents**  
- **Date:** 2026-11-18
- **Authors:** Stavros Damianakis, Konstantinos Psounis
- **Link:** https://arxiv.org/abs/2611.24313v1
- **Security insight:** Prompt injection is the dominant unsolved security risk for LLM agents, and the community now agrees that robustness must be measured against adaptive attackers rather than fixed benchmark injections. Many adaptive red teamers exist, and most are built to…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**What Survives the Shift from Text to Pixels? Conditional Protection against Prompt Injection in Image-Rendered Documents**  
- **Date:** 2026-11-18
- **Authors:** Haoyang Liu, Yinong Xu, Zhe Lang et al.
- **Link:** https://arxiv.org/abs/2611.24231v1
- **Security insight:** Multimodal language models increasingly answer questions over external documents, exposing them to indirect prompt injection: commands planted in untrusted content to hijack the response. Rendering untrusted content as page images lowers attack success on…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Securing and Auditing Long-Horizon LLM Agents: State-Transfer Auditing and Controls in the Agent Harness**  
- **Date:** 2026-11-17
- **Authors:** Deep Shah, Nehal Kathrotia
- **Link:** https://arxiv.org/abs/2611.23346v1
- **Security insight:** Long-horizon LLM agents across codebases, web browsers, and enterprise infrastructure rely on an execution harness to move state between the working context, session history, persistent memory, and external environment. While conventional execution traces log…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**Auditable Financial Knowledge Graphs: Schema-Driven Construction and Intrinsic Quality Evaluation**  
- **Date:** 2026-11-20
- **Authors:** Samarth Sarin, Lovepreet Singh, Dhagash Mehta
- **Link:** https://arxiv.org/abs/2611.27835v1
- **Security insight:** Financial documents combine narrative disclosures, accounting metrics, corporate structures, management commentary, and time-dependent facts, making them difficult to represent using conventional chunk-based retrieval-augmented generation systems. This paper…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**On the Impact of Feature Reduction Techniques on Adversarial Attacks**  
- **Date:** 2026-11-18
- **Authors:** Mohammad Meymani, Roozbeh Razavi-Far
- **Link:** https://arxiv.org/abs/2611.25004v1
- **Security insight:** Adversarial attacks have posed significant threats to machine learning models by exploiting their inherent vulnerabilities. Researchers have established an interdisciplinary field called adversarial machine learning to explore these vulnerabilities and…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Adversarial ML

**Gradient-Based Defensive Poisoning Against System Identification Attacks on Cyber-Physical Systems**  
- **Date:** 2026-11-18
- **Authors:** Gonçalo Fernandes, José Cecílio, Victor Mattos et al.
- **Link:** https://arxiv.org/abs/2611.24662v1
- **Security insight:** AI-driven attacks learn the models of cyber-physical systems (CPS) by passively observing controller and plant signals, then use this knowledge to act covertly. Because covertness depends on the accuracy of the identified model, degrading that accuracy is a…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

**Network-Exposed Configuration Attacks on LLM-Controlled Social Robots**  
- **Date:** 2026-11-17
- **Authors:** Stanley Akingbola, Ugbede Ibrahim, Yan Lin Aung et al.
- **Link:** https://arxiv.org/abs/2611.22761v1
- **Security insight:** Large language models (LLMs) in embodied robots create security dependencies beyond inference. We investigate a network-exposed configuration attack on the Pollen Robotics Reachy Mini Lite, allowing an unauthenticated attacker to replace personality settings…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

### Agent & Tool Security

**SoK: Assessing the Evolution of LLM Capability in Software Vulnerability Research**  
- **Date:** 2026-11-19
- **Authors:** Amine Lbath, Manan Suri, Aurelien Delaitre et al.
- **Link:** https://arxiv.org/abs/2611.26601v1
- **Security insight:** LLM-based agents are becoming increasingly capable at discovering, validating and patching vulnerabilities in real software, and vendors and researchers report that this is already changing how vulnerabilities are found and fixed. These claims, however, are…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Guarding the Kingdom of Skill-Based Agents in the AI Dynasty of Computation: Control-Flow Integrity for Agent Skills**  
- **Date:** 2026-11-18
- **Authors:** Bonan Ruan, Yuhao Sun, Jiahao Liu et al.
- **Link:** https://arxiv.org/abs/2611.24185v1
- **Security insight:** Control-flow integrity (CFI) confines a program to a control-flow graph fixed ahead of time. Procedural agent skills move this control flow into prompt text, and a large language model (LLM) agent decides at runtime whether each step runs in its reasoning, a…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.
