# AI Security Radar

_Last updated (UTC): **2026-11-24**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

**Carried-Over and Agent-Native Threats in the Supply Chain of LLM Agent Skills**  
- **Date:** 2026-11-23
- **Authors:** Kaixuan Li, Wenbo Guo, Sen Chen et al.
- **Link:** https://arxiv.org/abs/2611.30932v1
- **Security insight:** Agent skills are reusable packages that extend a large language model (LLM) agent with scripts, third-party dependencies, and natural-language instructions. An agent builds a skill's arguments from user requests and untrusted external content, so a flaw left…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Conartist: Adaptive Agentic Red-Teaming of Computer-Using Agents against Multi-Step Prompt Injection**  
- **Date:** 2026-11-23
- **Authors:** Jiaqi Rong, Yunchen Lu, Lihai Nie et al.
- **Link:** https://arxiv.org/abs/2611.29977v1
- **Security insight:** Harnesses secure Computer-Using Agents by enforcing security constraints and defending against prompt injection attacks. However, we find that two core security mechanisms of agent harnesses remain vulnerable. First, consistency checking prevents agents from…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Relativising Integrity and Robustness: Prompt Injection and Partitioned Enclaves**  
- **Date:** 2026-11-22
- **Authors:** Brijesh Dongol
- **Link:** https://arxiv.org/abs/2611.29802v1
- **Security insight:** Relative security (RS) judges a system against a reference system, but has only been applied to confidentiality. We introduce relative integrity (RI), which states that every behaviour a system exhibits under an attacker's influence must be one the reference…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Benchmarking Web Agent Defenses Against Adaptive Visual Prompt Injection**  
- **Date:** 2026-11-22
- **Authors:** Haichuan Zhang, Zhiyuan Zhong, Shih-Chieh Dai et al.
- **Link:** https://arxiv.org/abs/2611.29268v1
- **Security insight:** Multimodal web agents automate website interactions but remain vulnerable to visual prompt injection (VPI), where malicious webpage content manipulates their visual processing and induces unintended actions. Although several defenses focus on detecting…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Who Is Prompt-Injecting Coding Agents? An Empirical Study of Hidden AI-Directed Text on GitHub**  
- **Date:** 2026-11-21
- **Authors:** Gabi Nakibly, Zvika Babo
- **Link:** https://arxiv.org/abs/2611.28763v1
- **Security insight:** AI coding agents now triage issues, review pull requests and pick up tasks inside GitHub repositories, and to do so they read text that anyone with a GitHub account can write. This makes GitHub a prime surface for indirect prompt injection, in which…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

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

### RAG & Retrieval Attacks

**AgentBouncer: Defending Software Engineering Agents via Dynamic System-Call Mediation**  
- **Date:** 2026-11-23
- **Authors:** Pascal Joos, Michael Pradel
- **Link:** https://arxiv.org/abs/2611.30621v1
- **Security insight:** Software engineering (SE) agents can complete diverse engineering tasks by interacting with the development environment via tools that access files, run commands, and download resources. Unfortunately, the same ability that makes SE agents useful also makes…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**Auditable Financial Knowledge Graphs: Schema-Driven Construction and Intrinsic Quality Evaluation**  
- **Date:** 2026-11-20
- **Authors:** Samarth Sarin, Lovepreet Singh, Dhagash Mehta
- **Link:** https://arxiv.org/abs/2611.27835v1
- **Security insight:** Financial documents combine narrative disclosures, accounting metrics, corporate structures, management commentary, and time-dependent facts, making them difficult to represent using conventional chunk-based retrieval-augmented generation systems. This paper…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Agent & Tool Security

**Bounded Autonomy: A Trust-Anchored Defense Against Resource-Exhaustion Attacks on Tool-Augmented LLM Agents**  
- **Date:** 2026-11-23
- **Authors:** Ziyuan Chen, Yueming Lyu, Songze Li et al.
- **Link:** https://arxiv.org/abs/2611.30383v1
- **Security insight:** Tool-augmented Large Language Model (LLM) agents are vulnerable to resource-exhaustion attacks that amplify model-token consumption through persistent context amplification, large tool output amplification, and error-induced agentic loops. Despite growing…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Attributing Security Outcomes in LLM-Agent Evaluations: The Role of Content-Free State**  
- **Date:** 2026-11-23
- **Authors:** Abdelmonaim Bounite, Zangir Iklassov
- **Link:** https://arxiv.org/abs/2611.30259v1
- **Security insight:** Security benchmarks for LLM agents record whether each attack succeeded and compare agents, attacks, and defenses by attack success rate (ASR). Such comparisons are valid only if the agent, the attack, and the defense cause each verdict. We show that verdicts…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Sequential Selection against an Adaptive Opponent**  
- **Date:** 2026-11-23
- **Authors:** Zhongyuan Lyu, Xiaocong Xu
- **Link:** https://arxiv.org/abs/2611.30006v1
- **Security insight:** Selecting a strategy by testing it against an opponent is common in game-playing AI, red-teaming of language models, and safety evaluations of AI agents. In many of these settings, the opponent adapts to what it observes, so a strategy that keeps winning in…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**SoK: Assessing the Evolution of LLM Capability in Software Vulnerability Research**  
- **Date:** 2026-11-19
- **Authors:** Amine Lbath, Manan Suri, Aurelien Delaitre et al.
- **Link:** https://arxiv.org/abs/2611.26601v1
- **Security insight:** LLM-based agents are becoming increasingly capable at discovering, validating and patching vulnerabilities in real software, and vendors and researchers report that this is already changing how vulnerabilities are found and fixed. These claims, however, are…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Other (Review)

**Right Verdict, Right Reason? An Execution-Grounded Study of Whether LLM Vulnerability Detectors Understand Vulnerabilities**  
- **Date:** 2026-11-21
- **Authors:** Leizhen Zhang, Sheng Chen
- **Link:** https://arxiv.org/abs/2611.28584v1
- **Security insight:** Large language models (LLMs) are increasingly used to detect vulnerabilities, and their benchmark scores are often read as evidence that they understand the vulnerabilities they report. We test this reading against program execution. For 515 C and C++…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
