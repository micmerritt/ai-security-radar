# AI Security Radar

_Last updated (UTC): **2026-11-05**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

**SecureGARD: Dynamic Ontology-Guided Governance for Secure Tool-Using LLM Agents**  
- **Date:** 2026-11-04
- **Authors:** Guoqin Xiong, Shengtao Wen, Xiang Chen et al.
- **Link:** https://arxiv.org/abs/2611.06682v1
- **Security insight:** Tool-using large language model (LLM) agents translate model outputs into consequential actions, turning indirect prompt injection into an execution-security problem. Existing defenses constrain tool calls, trajectories, or information flows, but often leave…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Right Tool, Wrong Parameters: Defending LLM Agents Against Parameter Poisoning**  
- **Date:** 2026-11-03
- **Authors:** Yao Wang, Zehua Ma, Weiming Zhang et al.
- **Link:** https://arxiv.org/abs/2611.04673v1
- **Security insight:** Indirect Prompt Injection (IPI) poses a critical threat to LLM agents. Existing defenses largely focus on whether an injection induces a new tool invocation or unintended action. In this paper, we study a different attack surface, parameter poisoning, where…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**The Devil is in the Context: Nine Dimensions of Prompt Injection Attacks**  
- **Date:** 2026-11-03
- **Authors:** Jiamin Chang, Kristina Nikolić, Rishi Sharma et al.
- **Link:** https://arxiv.org/abs/2611.04672v1
- **Security insight:** Prompt injection is usually discussed and evaluated as a single, homogeneous type of attack. However, vulnerabilities reported in real-world systems show that prompt injections vary widely. Moreover, the same instruction can be a prompt injection in one…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**From Guidelines to Practice: Defining Requirements for AI Red-Teaming Tools**  
- **Date:** 2026-11-03
- **Authors:** Gia Phong Tran, Thai Duong Huynh, Randolph Loh et al.
- **Link:** https://arxiv.org/abs/2611.04271v1
- **Security insight:** Artificial Intelligence (AI) has seen significant developments and increased usage in recent years. AI benefits various tasks, automates decision-making, and enhances efficiency. However, AI also introduces additional attack surfaces for threat actors to…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**ATrust: Adaptive Trust Boundary Expansion for Securing LLM Agents**  
- **Date:** 2026-11-02
- **Authors:** Xu Zhang, Zhichao Lu
- **Link:** https://arxiv.org/abs/2611.02741v1
- **Security insight:** As large language model (LLM) agents take on more complex tasks with greater autonomy, security has become a major obstacle to their broader deployment. Unlike in attacks that require complex exploitation of operating system vulnerabilities, attackers can…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**SearchInject: Retrieval Exposure Control for Indirect Prompt Injection in Language-Model Search**  
- **Date:** 2026-11-02
- **Authors:** Kainan Zhou, Gangzhen Qian, Janet Sung et al.
- **Link:** https://arxiv.org/abs/2611.02643v1
- **Security insight:** An indirect prompt injection can affect a search-augmented large language model only after its carrier page reaches model context. SearchInject controls this admission decision with a joint score combining retrieval relevance, search-abuse cues, instruction…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Where Does MCP Security End? A Three-Tier Mitigation Mapping Framework for the OWASP MCP Top 10**  
- **Date:** 2026-11-02
- **Authors:** Christopher Krakauer, Andreas Schaad
- **Link:** https://arxiv.org/abs/2611.02611v1
- **Security insight:** The Model Context Protocol (MCP) has become a leading standard for connecting Large Language Models (LLMs) to external tools, software, and data sources. MCP architecture favors ease of integration over security, blending the data and control planes into a…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**StateFence: Task-State Protection Against Evidence-Chain Contamination in Blue-Team LLM Agents**  
- **Date:** 2026-11-02
- **Authors:** Haowen Dai, Alejandro Guerra-Manzanares
- **Link:** https://arxiv.org/abs/2611.02605v1
- **Security insight:** Indirect prompt injection creates a distinctive risk for blue-team Large Language Model (LLM) agents in Security Operations Centers (SOCs). Malicious instructions can be embedded in telemetry, tickets, retrieval results, or memory and then propagate through…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Benchmark of THReD: Evaluating an LLM Agent and Its Preprocessing Tools for Turning Electronic Health Records into AI-Ready Datasets**  
- **Date:** 2026-11-02
- **Authors:** Javad Mohammad Alizadeh, Huanmei Wu
- **Link:** https://arxiv.org/abs/2611.02484v1
- **Security insight:** LLM agents are increasingly built into data-analysis software, yet little evidence shows how reliably they preprocess clinical data or whether the tools they invoke give correct, reproducible output. We report a benchmark of THReD, a web-based system that…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**IAMRAGBENCH: Benchmarking Authorization Expansions in LLM-Generated AWS IAM Policies under RAG Poisoning**  
- **Date:** 2026-11-02
- **Authors:** Hasan Kaplan, Indika Kumara, Willem-Jan van den Heuvel et al.
- **Link:** https://arxiv.org/abs/2611.03431v1
- **Security insight:** Large language models (LLMs) using retrieval-augmented generation (RAG) can synthesize Amazon Web Services (AWS) Identity and Access Management (IAM) policies from tasks and operational documents. Attacker-controlled context may induce provider-valid policies…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Model Extraction & Privacy

**Fingerprinting the Dispatchers behind Distributed Model Extraction**  
- **Date:** 2026-11-04
- **Authors:** Snigdha Chandan Khilar
- **Link:** https://arxiv.org/abs/2611.06661v1
- **Security insight:** API distillation campaigns try to hide model-stealing traffic by splitting requests across thousands of load-balanced accounts, which standard content classifiers often miss. However, request timestamps, specifically arrival time and stream completion time,…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

### Adversarial ML

**ScamWorld: An Interactive Environment for Evaluating Web Agents Against Online Fraud**  
- **Date:** 2026-11-03
- **Authors:** Yutao Wu, Xiao Liu, Ming Wen et al.
- **Link:** https://arxiv.org/abs/2611.04879v2
- **Security insight:** Web agents increasingly browse, shop, and manage accounts on behalf of their users. Prior work has shown that they can be misled by adversarial content, including prompt injections and deceptive interfaces. Beyond such attacks, agents operating on the open…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

### Agent & Tool Security

**Securing Web Agents with the Compile-Then-Execute Paradigm**  
- **Date:** 2026-11-04
- **Authors:** Annabella Chow, Jinhao Zhu, Sylvie Venuto et al.
- **Link:** https://arxiv.org/abs/2611.06039v1
- **Security insight:** Web agents commonly follow the ReAct paradigm, selecting each action from runtime observations that inherently mix trusted and untrusted content. This design makes their control flow vulnerable to prompt injections embedded in webpages. We introduce Baya, a…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Cumulative and Audited Guardrail Tool Evolution for LLM Agent Safety**  
- **Date:** 2026-11-02
- **Authors:** Xiao Yang, Aishan Liu, Siyuan Liang et al.
- **Link:** https://arxiv.org/abs/2611.02516v1
- **Security insight:** Large language model (LLM) agents increasingly operate in open-world environments where safety risks cannot be fully predefined. However, most existing guardrail mechanisms remain static, relying on fixed rules, prompts, or classifiers that generalize poorly…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.
