# AI Security Radar

_Last updated (UTC): **2026-08-21**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**MobileWorldSafety: Benchmarking GUI Agent Safety Against Environmental Injection Attacks in Android Apps**  
- **Date:** 2026-08-18
- **Authors:** Sujin Chen, Lijun Li, Tianyi Du et al.
- **Link:** https://arxiv.org/abs/2608.17659v1
- **Security insight:** LLM-powered GUI agents that autonomously operate smartphones are rapidly transitioning from research prototypes to early real-world deployment. However, because these agents routinely process untrusted environmental content, they are highly vulnerable to…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**When Agents Act on Web3: An Attack-Surface Survey of MCP, Skills, and Tool Calling**  
- **Date:** 2026-08-18
- **Authors:** Rabimba Karanjai, Yang Lu, Nour Diallo et al.
- **Link:** https://arxiv.org/abs/2608.17275v1
- **Security insight:** AI agents increasingly act rather than merely read: across the Model Context Protocol (MCP) ecosystem, the share of deployed tools that modify external state has risen from 27% to 65% of tool use. When agents exercise this authority on public blockchains…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**PACE: Policy-Attested Contract Execution for Safe AI Agents in Decentralized Finance**  
- **Date:** 2026-08-18
- **Authors:** Rabimba Karanjai, Yang Lu, Richard Williamson et al.
- **Link:** https://arxiv.org/abs/2608.17220v1
- **Security insight:** Autonomous AI agents are emerging as interfaces for decentralized finance (DeFi) actions such as swaps, lending operations, and yield management. Because these agents rely on large language models (LLMs) to plan transactions, they inherit the LLM's…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Security of Foundation-Model-Powered Embodied Agents: Attack Surfaces, Attacks, Defenses, and Evaluation**  
- **Date:** 2026-08-17
- **Authors:** Jiawei Liu, Jiacheng Guo, Tian Zhang et al.
- **Link:** https://arxiv.org/abs/2608.16843v1
- **Security insight:** Foundation models are increasingly used for perception, reasoning, planning, and action generation in embodied agents, creating security risks that can propagate from digital inputs to physical behavior. Existing surveys often organize threats by mechanisms…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Security Assessment of DeepSeek Harness with A.I.G: Evaluating Resistance to Indirect Prompt Injection**  
- **Date:** 2026-08-17
- **Authors:** Zonghao Ying, Xiangfan Wu, Huiyu Wu et al.
- **Link:** https://arxiv.org/abs/2608.16393v2
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

### Prompt Injection

**COPA: Continual Preference Optimization for Adaptive Prompt Injection Defense**  
- **Date:** 2026-08-20
- **Authors:** Roshan Sood, Onat Gungor, Tajana Rosing
- **Link:** https://arxiv.org/abs/2608.19982v1
- **Security insight:** LLMs remain vulnerable to prompt injection attacks, where adversarial instructions embedded in user inputs or external content manipulate model behavior and bypass safeguards. Existing defenses are predominantly static, relying on fixed alignment objectives…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Visible Reasoning and Indirect Prompt-Injection Monitorability Across English, Tamil, and Tanglish**  
- **Date:** 2026-08-15
- **Authors:** Madhusudhanan G
- **Link:** https://arxiv.org/abs/2608.15392v1
- **Security insight:** Chain-of-thought monitoring is a potentially useful safety signal, but its reliability across languages and behavioral settings remains uncertain. In a small case study of eight manually verified synthetic scenarios, one model, one annotator, and one…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.
