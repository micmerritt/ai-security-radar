# AI Security Radar

_Last updated (UTC): **2026-08-14**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Labels Are Not Endpoints: Treatment Leakage and Construct Validity in MCP Agent Security Evaluation**  
- **Date:** 2026-08-13
- **Authors:** Rana Muhammad Ahmed, Sabahat Abbas
- **Link:** https://arxiv.org/abs/2608.12880v1
- **Security insight:** Security evaluations of tool-using agents often equate stored labels with behavioral facts. We audit a preserved campaign by tracing 10,200 execution rows to 180 model-bound requests, 45 semantic requests, and 15 observable stimuli. Two schema treatments were…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Rethinking Agent Security as a Networking Problem**  
- **Date:** 2026-08-12
- **Authors:** Van Tran, Taveesh Sharma, Tajveer Singh Dhesi et al.
- **Link:** https://arxiv.org/abs/2608.12172v1
- **Security insight:** AI agents are rapidly becoming more capable and widely deployed, promising substantial gains in productivity and enabling new classes of applications. However, their growing autonomy also introduces significant privacy and security risks. Existing defenses…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**ToolHazard: Scaling Adversarial Environments for Security Evaluation and Alignment of LLM-based Agents**  
- **Date:** 2026-08-12
- **Authors:** Yutao Mou, Pengfei Yang, Zhe Yin et al.
- **Link:** https://arxiv.org/abs/2608.11878v1
- **Security insight:** Large language model (LLM) agents integrated with external tools are vulnerable to indirect prompt injections embedded in environmental states. However, existing studies largely rely on manually implemented or reused environments, stochastic LLM-based tool…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**On Understanding, Identifying, and Mitigating Vulnerabilities in Agentic Large Language Models**  
- **Date:** 2026-08-11
- **Authors:** Md Jafrin Hossain, Mohammad Arif Hossain, Nirwan Ansari
- **Link:** https://arxiv.org/abs/2608.10530v1
- **Security insight:** Large Language Models (LLMs) have undergone a shift from stateless conversational interfaces to autonomous agents capable of multi-step planning, tool invocation, code execution, and maintaining persistent memory. When these agents operate with real-world…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**From Prompt Injection to Web Exploitation: Revisiting Classic Vulnerabilities in LLM-Integrated Applications**  
- **Date:** 2026-08-10
- **Authors:** Spiros Tsigkopoulos, Christoforos Ntantogian
- **Link:** https://arxiv.org/abs/2608.10281v1
- **Security insight:** Large Language Models are increasingly integrated into web applications through chatbots, tool-calling pipelines, and agentic workflows. In these systems, user input may influence not only generated text, but also backend actions such as database queries,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Stealing Reasoning Traces from Proprietary LLM APIs**  
- **Date:** 2026-08-10
- **Authors:** Alexander Panfilov, David Schmotz, Ilia Shumailov et al.
- **Link:** https://arxiv.org/abs/2608.09867v1
- **Security insight:** Leading large language model providers now conceal their models' step-by-step reasoning, or chain-of-thought, to protect intellectual property and limit information leakage. Rather than storing these traces server-side, providers return them to the client as…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Same Question, Different Answer? Measuring and Mitigating Prompt Privilege for Equitable AI Access**  
- **Date:** 2026-08-09
- **Authors:** Lier Jin, Lan Hu, Binqi Shen et al.
- **Link:** https://arxiv.org/abs/2608.08942v1
- **Security insight:** Large language models (LLMs) are increasingly integrated into healthcare, education, public services, and everyday decision making. They should provide comparable assistance regardless of a user's literacy, communication style, or prompt-engineering…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Not an A11y: How Android Accessibility Exposes Mobile AI Agents to Indirect Prompt Injection**  
- **Date:** 2026-08-09
- **Authors:** Rahul Deivasigamani, Sayeda Faatin Alvi, Derqui Andrea et al.
- **Link:** https://arxiv.org/abs/2608.08939v1
- **Security insight:** The rise of autonomous AI agents represents a major paradigm shift in how users interact with mobile devices. Frameworks such as MobileRun and Mobile-Use can autonomously navigate Android applications and execute complex multi-step tasks. To interpret user…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Toward Metacognitive One-Shot Indirect Prompt Injection: Strategy Abstraction Via Outcome-Conditioned Reflection**  
- **Date:** 2026-08-09
- **Authors:** Sihan Hou, Xinmeng Hou, Zhijun Zhang et al.
- **Link:** https://arxiv.org/abs/2608.08795v1
- **Security insight:** Tool-using large language model (LLM) agents are vulnerable to indirect prompt injection (IPI), in which malicious instructions embedded in external observations manipulate subsequent agent decisions and actions. Most existing adaptive attacks rely on…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**SkillsMetric: Mapping the Detection Boundary of Static Analysis for Malicious Agent Skills**  
- **Date:** 2026-08-09
- **Authors:** Xinze Chen, Chi Zhang, Ping Ji et al.
- **Link:** https://arxiv.org/abs/2608.08468v1
- **Security insight:** Agent Skills---structured packages of instructions and scripts that augment LLM-based agents---are rapidly proliferating, yet their security properties remain under-explored. We present \textsc{SkillsMetric}, a five-stage static analysis framework that scores…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Defending Retrieval-Augmented Intrusion Detection Against Knowledge Poisoning and Prompt Injection**  
- **Date:** 2026-08-08
- **Authors:** Kaysarul Anas Apurba, Md. Hasibul Hasan, Mahedee Zaman Moon et al.
- **Link:** https://arxiv.org/abs/2608.08100v1
- **Security insight:** Retrieval-Augmented Generation (RAG) enables large language models to classify network flows and generate human-readable incident reports by retrieving semantically similar historical traffic from a vector knowledge base. However, the retrieval layer…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### RAG & Retrieval Attacks

**Generating Attacks for LLMs with GFlowNets**  
- **Date:** 2026-08-10
- **Authors:** Berkay Ozcam, Irem Onen, Mehmet Fatih Amasyali et al.
- **Link:** https://arxiv.org/abs/2608.10171v1
- **Security insight:** The rapid advancement of Large Language Models (LLMs) has facilitated their ubiquitous integration into various domains, leading to widespread adoption. However, this escalating trend has introduced significant security vulnerabilities, necessitating the…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Model Extraction & Privacy

**Towards Automated Domain Model Extraction from Source Code using Heuristics and Open-Source LLMs**  
- **Date:** 2026-08-12
- **Authors:** Alessandra Mancas, Mounir Ammam, Hyacinth Ali et al.
- **Link:** https://arxiv.org/abs/2608.12228v1
- **Security insight:** Large language models (LLMs) have recently shown strong capabilities for code understanding, making them promising for reverse engineering domain models from source code. However, state-ofthe- art proprietary LLMs cannot be used in many industrial contexts…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

**Defending against Model Extraction for GNNs with Model Reprogramming**  
- **Date:** 2026-08-11
- **Authors:** Yan Wen, Zhenyi Wang, Heng Huang
- **Link:** https://arxiv.org/abs/2608.11495v1
- **Security insight:** Graph Neural Networks (GNNs) serve as the backbone for high-stakes applications in Machine-Learning-as-a-Service (MLaaS). Still, their black-box deployment exposes them to Model Extraction (ME) attacks, in which adversaries steal intellectual property by…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?
