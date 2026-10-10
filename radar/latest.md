# AI Security Radar

_Last updated (UTC): **2026-10-10**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

**LTBD: Learnable Trust-Boundary Delimiters for Prompt Injection Defense**  
- **Date:** 2026-10-08
- **Authors:** Luman Zhao, Minghui Xu, Yue Zhang et al.
- **Link:** https://arxiv.org/abs/2610.11634v1
- **Security insight:** Large language models (LLMs) perform remarkably well on complex tasks, yet remain highly vulnerable to prompt injection attacks, where malicious instructions embedded in external data can override user intent. Existing defenses remain limited by model fine-…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**BRANCH: Bypassing Multi-Scanner AI Guardrails**  
- **Date:** 2026-10-07
- **Authors:** William Hackett, Peter Garraghan
- **Link:** https://arxiv.org/abs/2610.10742v1
- **Security insight:** AI systems increasingly rely on Large Language Models (LLMs) as core reasoning engines, making them targets for prompt injection and jailbreaks. Guardrails monitor and validate model inputs and outputs, yet their isolated, task-focused detection leaves gaps…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**AgentTracer: Tracing Indirect Prompt Injection Attack through Fine-Grained Intention-Execution Alignment**  
- **Date:** 2026-10-07
- **Authors:** Zitong Yao, Jiangrong Wu, Yixi Lin et al.
- **Link:** https://arxiv.org/abs/2610.09935v1
- **Security insight:** Large language model (LLM) agents interact with external resources to complete complex user tasks, exposing them to indirect prompt injection (IPI), where malicious instructions redirect agents toward attacker-intended tasks. Since IPI is difficult to defend…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Package Hallucination Attacks on Coding Agents through Prompt Injection in Rule Files**  
- **Date:** 2026-10-07
- **Authors:** Yupu Wang, Zhengyuan Jiang, Reachal Wang et al.
- **Link:** https://arxiv.org/abs/2610.09264v1
- **Security insight:** Modern agentic coding frameworks increasingly rely on community-shared rule files (e.g., AGENTS.md or .cursorrules) to guide autonomous code generation, yet the security risks of this pipeline remain underexplored. To bridge this gap, we introduce the package…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**ASPIRE: Agentic Safety & Prompt Injection Red-teaming Engine**  
- **Date:** 2026-10-06
- **Authors:** Pengfei He, Deep Mitra, Vishesh Sharma et al.
- **Link:** https://arxiv.org/abs/2610.08951v1
- **Security insight:** LLM agents retrieve untrusted content and act through tools, creating indirect prompt-injection risks that can cause unauthorized actions or persistent state changes. Existing automated red-teaming largely optimizes payloads for pre-specified scenarios,…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**AdvSim2Real : Training Web Agents Against Adaptive Prompt Injection in a Web World Model**  
- **Date:** 2026-10-06
- **Authors:** Sarim Hashmi, Mukul Ranjan, Kshitij Mishra et al.
- **Link:** https://arxiv.org/abs/2610.08773v1
- **Security insight:** Web agents complete user requests by reading and acting on pages that third parties write, so an instruction planted on a page can redirect the agent away from the user's goal. The agent cannot simply ignore the page, because the page also holds the values…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Secure Speculative Decoding for Large Language Models**  
- **Date:** 2026-10-06
- **Authors:** Yichi Zhang, Zhiqi Wang, Neil Gong et al.
- **Link:** https://arxiv.org/abs/2610.08678v1
- **Security insight:** Speculative decoding accelerates inference for a large language model (LLM), referred to as the \emph{target model}, by first using a smaller model, referred to as the \emph{draft model}, to generate candidate tokens and then verifying them with the target…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**RAISED: Self-Distillation for Robustness to Prompt Injection in LLM Agents**  
- **Date:** 2026-10-05
- **Authors:** Mohamed Dhouib, Clement Elliker, Alexi Canesse et al.
- **Link:** https://arxiv.org/abs/2610.06401v2
- **Security insight:** Tool-using language-model agents are vulnerable to indirect prompt injection because they must act on untrusted external content. Existing training-time defenses can reduce attack success rates, but often at the cost of general capabilities. We show that…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**RAG-PIBench: A Leakage-Aware Benchmark for Prompt-Injection Detection in Trustworthy RAG Systems**  
- **Date:** 2026-10-06
- **Authors:** Niveen O. Jaffal, Ahmet Yuksel, David Mohaisen
- **Link:** https://arxiv.org/abs/2610.08571v1
- **Security insight:** Retrieval-Augmented Generation (RAG) systems are vulnerable to prompt-injection attacks embedded in retrieved content. We introduce RAG-PIBench, a benchmark for RAG-style prompt-injection detection containing 4,876 contextual examples across frozen train,…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**Surviving the Router: Optimizing Skill Injections for Retrieval and Execution**  
- **Date:** 2026-10-06
- **Authors:** Haneen Najjar, Luca Scionis, Haritz Puerto et al.
- **Link:** https://arxiv.org/abs/2610.08098v1
- **Security insight:** AI agents increasingly rely on modular third-party "skills" that are dynamically selected by skill routers to execute complex tasks. While recent studies highlight the threat of prompt injections embedded in these skills, existing evaluations often assume…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**Dynamic Budget Allocation for LLM Evaluation under Hard Resource Constraints**  
- **Date:** 2026-10-05
- **Authors:** Shai Feldman, Yaniv Romano
- **Link:** https://arxiv.org/abs/2610.07362v1
- **Security insight:** We evaluate large language models (LLMs) in multi-turn interactions through their time-to-event: the number of interaction steps required to produce an event of interest, such as a successful jailbreak or agentic task completion. Under limited compute,…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Model Extraction & Privacy

**MARCO: The Radioactive Watermark for Protein Generative Models**  
- **Date:** 2026-10-06
- **Authors:** Huajie Chen, Xin Guo, Yuchen Shi et al.
- **Link:** https://arxiv.org/abs/2610.08316v1
- **Security insight:** Protein Generative Models (PGMs) have revolutionized structural biology by enabling the design of complex 3D protein structures from sequence data. However, this breakthrough introduces a dual-use challenge, exposing high-value PGMs to economic risks like…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

### Agent & Tool Security

**From Reactive Containment to Proactive Assurance: Lessons from OpenAI, Anthropic, and Google Agent Security Incidents**  
- **Date:** 2026-10-08
- **Authors:** Abbas Raftari
- **Link:** https://arxiv.org/abs/2610.12463v1
- **Security insight:** In 2026, cybersecurity evaluations involving OpenAI, Anthropic, and Google agents reached real systems outside their authorized test scope. The paths were different. OpenAI agents exploited research infrastructure, coordinated across runs, and compromised…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**One Word Opens the Gate: The Option-Channel Attack on Typed Decision Models as Agent Guardrails**  
- **Date:** 2026-10-08
- **Authors:** Seyedarmin Azizi, Erfan Baghaei Potraghloo, Massoud Pedram
- **Link:** https://arxiv.org/abs/2610.12292v1
- **Security insight:** A typed decision model reads a piece of text and returns a probability over caller-defined options, each with a short written definition, generating no text. Recent work places these models in agent systems as guardrails: the component that reads a proposed…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.
