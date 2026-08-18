# AI Security Radar

_Last updated (UTC): **2026-08-18**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Security of Foundation-Model-Powered Embodied Agents: Attack Surfaces, Attacks, Defenses, and Evaluation**  
- **Date:** 2026-08-17
- **Authors:** Jiawei Liu, Jiacheng Guo, Tian Zhang et al.
- **Link:** https://arxiv.org/abs/2608.16843v1
- **Security insight:** Foundation models are increasingly used for perception, reasoning, planning, and action generation in embodied agents, creating security risks that can propagate from digital inputs to physical behavior. Existing surveys often organize threats by mechanisms…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Security Assessment of DeepSeek Harness with A.I.G: Evaluating Resistance to Indirect Prompt Injection**  
- **Date:** 2026-08-17
- **Authors:** Zonghao Ying, Xiangfan Wu, Huiyu Wu et al.
- **Link:** https://arxiv.org/abs/2608.16393v1
- **Security insight:** We assess indirect prompt injection in DeepSeek Harness (DSH), using AI-Infra-Guard (A.I.G) to construct tests, deliver controlled taint, execute DSH, collect traces, and judge outcomes. The study covers 14,560 controlled executions over 16 indirect-content…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Agent-Native Telemetry: Verifiable State-Delta Evidence for Autonomous Operations**  
- **Date:** 2026-08-17
- **Authors:** Jun He, Deying Yu
- **Link:** https://arxiv.org/abs/2608.16178v1
- **Security insight:** Operational telemetry is predominantly engineered for human reading: systems repeatedly serialize verbose prose, static keys, and redundant context across billions of log lines. As autonomous AI agents become primary operational consumers, feeding them…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Bounded Agents: Delegation Security for Multi-Agent AI Systems**  
- **Date:** 2026-08-16
- **Authors:** Xabier Muruaga
- **Link:** https://arxiv.org/abs/2608.15888v1
- **Security insight:** LLM-based agents can act on behalf of a user to access cloud services, call tools, or invoke agents. At session start, the agent's permissions are set but remain static, and each request is evaluated independently, without considering prior actions. Within…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**TwinGridShield: Consequence-Aware Runtime Authorization for LLM Grid-Agent Actions**  
- **Date:** 2026-08-15
- **Authors:** Md Fazley Rafy
- **Link:** https://arxiv.org/abs/2608.15391v1
- **Security insight:** Large language model (LLM)-assisted energy-management tools can translate natural-language context into structured grid commands, but syntactic validity does not imply physical admissibility. This paper presents TwinGridShield, a model-independent runtime…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Beyond Direct Access: Resource Hijacking in LLM Agents**  
- **Date:** 2026-08-15
- **Authors:** Puyu Zeng, Qibing Ren
- **Link:** https://arxiv.org/abs/2608.15108v1
- **Security insight:** Large language model agents are increasingly connected to high-value resources such as computing infrastructure, credentials, usage budgets, identities, private knowledge, communication channels, and organizational workflows. Existing agent security research…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Command-Space Counterfactual Explanations for Pareto-Conditioned Reinforcement Learning**  
- **Date:** 2026-08-15
- **Authors:** Joanikij Chulev, Hendrik Baier
- **Link:** https://arxiv.org/abs/2608.14963v1
- **Security insight:** Pareto Conditioned Networks learn multiple multi-objective reinforcement learning behaviours by conditioning a single policy on a desired return command. However, the local mapping from command and state to action remains opaque. We propose command-space…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Workspace Topology as an Attack Vector in Agentic Coding Assistants**  
- **Date:** 2026-08-14
- **Authors:** Alexandre G. R. Day, Pradeep Yadlapalli, Sriram Venkatapathy et al.
- **Link:** https://arxiv.org/abs/2608.14876v1
- **Security insight:** Agentic coding assistants are finding widespread use, not just in new code development but in quickly ingesting and leveraging third-party code. This opens up a risk of malicious code being ingested as these coding tools operate with broad filesystem access…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

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

### Prompt Injection

**Visible Reasoning and Indirect Prompt-Injection Monitorability Across English, Tamil, and Tanglish**  
- **Date:** 2026-08-15
- **Authors:** Madhusudhanan G
- **Link:** https://arxiv.org/abs/2608.15392v1
- **Security insight:** Chain-of-thought monitoring is a potentially useful safety signal, but its reliability across languages and behavioral settings remains uncertain. In a small case study of eight manually verified synthetic scenarios, one model, one annotator, and one…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

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
