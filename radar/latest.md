# AI Security Radar

_Last updated (UTC): **2026-10-08**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

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

**Towards a Unified Misuse Monitoring Benchmark**  
- **Date:** 2026-10-05
- **Authors:** Aniruddh Pramod, James Oldfield, Adel Bibi
- **Link:** https://arxiv.org/abs/2610.07089v1
- **Security insight:** LLM agents increasingly act in multi-actor environments, exposing them to misuse from multiple sources: decomposition attacks, where a harmful request is split into innocuous sub-requests, and prompt injection attacks, where a compromised tool delivers a…
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

**Agentic schema-guided extraction of materials process knowledge from scientific literature**  
- **Date:** 2026-10-05
- **Authors:** Sameer Sadruddin, Jennifer D'Souza
- **Link:** https://arxiv.org/abs/2610.06322v1
- **Security insight:** Materials literature contains detailed experimental knowledge, but procedures, chemical entities and measurements remain difficult to aggregate because they are reported in heterogeneous forms and depend on process-specific context. We present SciKGExtract, a…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

### Agent & Tool Security

**TrustMI: Causally controlling how assistants trust their users**  
- **Date:** 2026-10-05
- **Authors:** Théo Lasnier, Romain Froger, Maxence Lasbordes et al.
- **Link:** https://arxiv.org/abs/2610.06064v1
- **Security insight:** Large Language Model (LLM) assistants routinely decide whether they can trust users and third parties whose competence, intentions, and integrity they cannot verify. This uncertainty matters for safety, as trusting the wrong party can lead an agent to comply…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Other (Review)

**Correct Verdicts, Flawed Reasoning: Structured Auditing of LLM-based Vulnerability Reasoning**  
- **Date:** 2026-10-05
- **Authors:** Boyue Caroline Hu, Kaivalya Ahir, Ronghao Ni et al.
- **Link:** https://arxiv.org/abs/2610.06366v1
- **Security insight:** Large Language Models (LLMs) are increasingly deployed for automated software vulnerability analysis. Binary classification alone is insufficient; practitioners need explanations to triage bugs and engineer patches. Standard practice relies on Chain-of-…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
