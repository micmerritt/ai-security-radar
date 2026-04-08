# AI Security Radar

_Last updated (UTC): **2026-04-08**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Compiled AI: Deterministic Code Generation for LLM-Based Workflow Automation**  
- **Date:** 2026-04-06
- **Authors:** Geert Trooskens, Aaron Karlsberg, Anmol Sharma et al.
- **Link:** https://arxiv.org/abs/2604.05150v1
- **Security insight:** We study compiled AI, a paradigm in which large language models generate executable code artifacts during a compilation phase, after which workflows execute deterministically without further model invocation. This paradigm has antecedents in prior work on…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**ShieldNet: Network-Level Guardrails against Emerging Supply-Chain Injections in Agentic Systems**  
- **Date:** 2026-04-06
- **Authors:** Zhuowen Yuan, Zhaorun Chen, Zhen Xiang et al.
- **Link:** https://arxiv.org/abs/2604.04426v1
- **Security insight:** Existing research on LLM agent security mainly focuses on prompt injection and unsafe input/output behaviors. However, as agents increasingly rely on third-party tools and MCP servers, a new class of supply-chain threats has emerged, where malicious behaviors…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Your Agent is More Brittle Than You Think: Uncovering Indirect Injection Vulnerabilities in Agentic LLMs**  
- **Date:** 2026-04-04
- **Authors:** Wenhui Zhu, Xuanzhao Dong, Xiwen Chen et al.
- **Link:** https://arxiv.org/abs/2604.03870v1
- **Security insight:** The rapid deployment of open-source frameworks has significantly advanced the development of modern multi-agent systems. However, expanded action spaces, including uncontrolled privilege exposure and hidden inter-system interactions, pose severe security…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Credential Leakage in LLM Agent Skills: A Large-Scale Empirical Study**  
- **Date:** 2026-04-03
- **Authors:** Zhihao Chen, Ying Zhang, Yi Liu et al.
- **Link:** https://arxiv.org/abs/2604.03070v1
- **Security insight:** Third-party skills extend LLM agents with powerful capabilities but often handle sensitive credentials in privileged environments, making leakage risks poorly understood. We present the first large-scale empirical study of this problem, analyzing 17,022…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**ClawSafety: "Safe" LLMs, Unsafe Agents**  
- **Date:** 2026-04-01
- **Authors:** Bowen Wei, Yunbei Zhang, Jinhao Pan et al.
- **Link:** https://arxiv.org/abs/2604.01438v2
- **Security insight:** Personal AI agents like OpenClaw run with elevated privileges on users' local machines, where a single successful prompt injection can leak credentials, redirect financial transactions, or destroy files. This threat goes well beyond conventional text-level…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Safety, Security, and Cognitive Risks in World Models**  
- **Date:** 2026-04-01
- **Authors:** Manoj Parmar
- **Link:** https://arxiv.org/abs/2604.01346v2
- **Security insight:** World models - learned internal simulators of environment dynamics - are rapidly becoming foundational to autonomous decision-making in robotics, autonomous vehicles, and agentic AI. By predicting future states in compressed latent spaces, they enable sample-…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**AgentWatcher: A Rule-based Prompt Injection Monitor**  
- **Date:** 2026-04-01
- **Authors:** Yanting Wang, Wei Zou, Runpeng Geng et al.
- **Link:** https://arxiv.org/abs/2604.01194v1
- **Security insight:** Large language models (LLMs) and their applications, such as agents, are highly vulnerable to prompt injection attacks. State-of-the-art prompt injection detection methods have the following limitations: (1) their effectiveness degrades significantly as…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**KAIJU: An Executive Kernel for Intent-Gated Execution of LLM Agents**  
- **Date:** 2026-03-31
- **Authors:** Cormac Guerin, Frank Guerin
- **Link:** https://arxiv.org/abs/2604.02375v1
- **Security insight:** Tool-calling autonomous agents based on large language models using ReAct exhibit three limitations: serial latency, quadratic context growth, and vulnerability to prompt injection and hallucination. Recent work moves towards separating planning from…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Architecting Secure AI Agents: Perspectives on System-Level Defenses Against Indirect Prompt Injection Attacks**  
- **Date:** 2026-03-31
- **Authors:** Chong Xiang, Drew Zagieboylo, Shaona Ghosh et al.
- **Link:** https://arxiv.org/abs/2603.30016v1
- **Security insight:** AI agents, predominantly powered by large language models (LLMs), are vulnerable to indirect prompt injection, in which malicious instructions embedded in untrusted data can trigger dangerous agent actions. This position paper discusses our vision for system-…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Gradient-Controlled Decoding: A Safety Guardrail for LLMs with Dual-Anchor Steering**  
- **Date:** 2026-04-06
- **Authors:** Purva Chiniya, Kevin Scaria, Sagar Chaturvedi
- **Link:** https://arxiv.org/abs/2604.05179v1
- **Security insight:** Large language models (LLMs) remain susceptible to jailbreak and direct prompt-injection attacks, yet the strongest defensive filters frequently over-refuse benign queries and degrade user experience. Previous work on jailbreak and prompt injection detection…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**LLM-Enabled Open-Source Systems in the Wild: An Empirical Study of Vulnerabilities in GitHub Security Advisories**  
- **Date:** 2026-04-05
- **Authors:** Fariha Tanjim Shifat, Hariswar Baburaj, Ce Zhou et al.
- **Link:** https://arxiv.org/abs/2604.04288v1
- **Security insight:** Large language models (LLMs) are increasingly embedded in open-source software (OSS) ecosystems, creating complex interactions among natural language prompts, probabilistic model outputs, and execution-capable components. However, it remains unclear whether…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Automating Cloud Security and Forensics Through a Secure-by-Design Generative AI Framework**  
- **Date:** 2026-04-05
- **Authors:** Dalal Alharthi, Ivan Roberto Kawaminami Garcia
- **Link:** https://arxiv.org/abs/2604.03912v1
- **Security insight:** As cloud environments become increasingly complex, cybersecurity and forensic investigations must evolve to meet emerging threats. Large Language Models (LLMs) have shown promise in automating log analysis and reasoning tasks, yet they remain vulnerable to…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**AttackEval: A Systematic Empirical Study of Prompt Injection Attack Effectiveness Against Large Language Models**  
- **Date:** 2026-04-04
- **Authors:** Jackson Wang
- **Link:** https://arxiv.org/abs/2604.03598v1
- **Security insight:** Prompt injection has emerged as a critical vulnerability in large language model (LLM) deployments, yet existing research is heavily weighted toward defenses. The attack side -- specifically, which injection strategies are most effective and why -- remains…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**LogicPoison: Logical Attacks on Graph Retrieval-Augmented Generation**  
- **Date:** 2026-04-03
- **Authors:** Yilin Xiao, Jin Chen, Qinggang Zhang et al.
- **Link:** https://arxiv.org/abs/2604.02954v1
- **Security insight:** Graph-based Retrieval-Augmented Generation (GraphRAG) enhances the reasoning capabilities of Large Language Models (LLMs) by grounding their responses in structured knowledge graphs. Leveraging community detection and relation filtering techniques, GraphRAG…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.
