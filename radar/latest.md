# AI Security Radar

_Last updated (UTC): **2026-11-03**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

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

**Beyond Prompt Injection: The Tool Update Gap in LLM Agent Security**  
- **Date:** 2026-11-01
- **Authors:** Shiyu Kan, Yue Qi, Yufei Han et al.
- **Link:** https://arxiv.org/abs/2611.01976v1
- **Security insight:** Large language model based agents increasingly rely on external tools to invoke services and interact with web resources. These tools can evolve through software updates, yet agentic frameworks may continue trusting them without re-verifying their safety…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**MemHarmBench: Evaluating Cross-Session Prompt Injection in Memory-Persistent AI Agents**  
- **Date:** 2026-11-01
- **Authors:** Zhihua Wang, Yunhao Feng, Yifeng Gao et al.
- **Link:** https://arxiv.org/abs/2611.01700v1
- **Security insight:** AI agents often rely on persistent memory to retain user preferences and operational rules across sessions. However, this capability introduces a new safety risk: malicious instructions from messages, documents, or Web content can be retained in memory and…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**AgentCap: Capability-Based Runtime Authorization for Secure LLM Agent Execution**  
- **Date:** 2026-10-31
- **Authors:** Aravinda Kashyap Kabbinamakki Suresh, Peng Gao
- **Link:** https://arxiv.org/abs/2611.00729v1
- **Security insight:** Language-model agents commonly collapse two decisions that security systems separate: selecting an action and determining whether that action is authorized. When a model exercises standing authority, indirect prompt injection can convert influence over its…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**The Long Con on the Web: Earn-then-Exploit Fraud Attacks against Coding Agents**  
- **Date:** 2026-10-31
- **Authors:** Xingling Xu, Zhengwei Jiang, Zheng Zhi et al.
- **Link:** https://arxiv.org/abs/2611.00725v1
- **Security insight:** Coding agents increasingly operate with web access and high privileges, creating a new attack surface where web fraud can directly target autonomous agents. Existing studies mainly focus on malicious links, prompt injection, and interface deception, while…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**SecPO: Principled Adversarial Training for Prompt Injection Security**  
- **Date:** 2026-10-30
- **Authors:** Sizhe Chen, Yibo Peng, Jaewon Chang et al.
- **Link:** https://arxiv.org/abs/2610.41998v1
- **Security insight:** Recognized as a top threat to AI agents, prompt injection allows instructions from untrusted data (email, documents, websites) to manipulate the agent's operation. The existing best-defended LLM, Meta-SecAlign, is trained with the DPO loss but still suffers…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**IAMRAGBENCH: Benchmarking Authorization Expansions in LLM-Generated AWS IAM Policies under RAG Poisoning**  
- **Date:** 2026-11-02
- **Authors:** Hasan Kaplan, Indika Kumara, Willem-Jan van den Heuvel et al.
- **Link:** https://arxiv.org/abs/2611.03431v1
- **Security insight:** Large language models (LLMs) using retrieval-augmented generation (RAG) can synthesize Amazon Web Services (AWS) Identity and Access Management (IAM) policies from tasks and operational documents. Attacker-controlled context may induce provider-valid policies…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Agent & Tool Security

**Cumulative and Audited Guardrail Tool Evolution for LLM Agent Safety**  
- **Date:** 2026-11-02
- **Authors:** Xiao Yang, Aishan Liu, Siyuan Liang et al.
- **Link:** https://arxiv.org/abs/2611.02516v1
- **Security insight:** Large language model (LLM) agents increasingly operate in open-world environments where safety risks cannot be fully predefined. However, most existing guardrail mechanisms remain static, relying on fixed rules, prompts, or classifiers that generalize poorly…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**LEANGUARD: Lean-Verified Guardrails for Tool-Using Agents**  
- **Date:** 2026-11-02
- **Authors:** Sreehari Sankar, Debargha Ganguly, Vikash Singh et al.
- **Link:** https://arxiv.org/abs/2611.02332v1
- **Security insight:** Tool-using language-model agents often execute actions that their domain policies forbid. We present LeanGuard, a runtime that checks every proposed tool call against a policy written in Lean4 before the call reaches the environment. Policies combine state…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Other (Review)

**On the Framing Effect of AI Red-Teaming Instructions: Evidence from Prior Exercises and Controlled Simulations**  
- **Date:** 2026-10-30
- **Authors:** Michael Feffer, Alice Qian, Anusha Sinha et al.
- **Link:** https://arxiv.org/abs/2611.00412v1
- **Security insight:** AI red-teaming, adversarially probing generative AI systems to surface harms, has become a central evaluation method. However, prior work has highlighted that red-teaming is a fairly open-ended task, laden with myriad design choices that can shape its…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
