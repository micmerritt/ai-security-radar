# AI Security Radar

_Last updated (UTC): **2026-05-12**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**LLMs for Secure Hardware Design and Related Problems: Opportunities and Challenges**  
- **Date:** 2026-05-11
- **Authors:** Johann Knechtel, Ozgur Sinanoglu, Ramesh Karri
- **Link:** https://arxiv.org/abs/2605.10807v1
- **Security insight:** The integration of Large Language Models (LLMs) into Electronic Design Automation (EDA) and hardware security is rapidly reshaping the semiconductor industry. While LLMs offer unprecedented capabilities in generating Register Transfer Level (RTL) code,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Oracle Poisoning: Corrupting Knowledge Graphs to Weaponise AI Agent Reasoning**  
- **Date:** 2026-05-10
- **Authors:** Ben Kereopa-Yorke, Guillermo Diaz, Holly Wright et al.
- **Link:** https://arxiv.org/abs/2605.09822v1
- **Security insight:** We define Oracle Poisoning, an attack class in which an adversary corrupts a structured knowledge graph that AI agents query at runtime via tool-use protocols, causing incorrect conclusions through correct reasoning. Unlike prompt injection, Oracle Poisoning…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**When Agents Overtrust Environmental Evidence: An Extensible Agentic Framework for Benchmarking Evidence-Grounding Defects in LLM Agents**  
- **Date:** 2026-05-09
- **Authors:** Strick Sheng, Ziyue Wang, Liyi Zhou
- **Link:** https://arxiv.org/abs/2605.08828v1
- **Security insight:** Large language model agents increasingly operate through environment-facing scaffolds that expose files, web pages, APIs, and logs. These observations influence tool use, state tracking, and action sequencing, yet their reliability and authority are often…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**When Child Inherits: Modeling and Exploiting Subagent Spawn in Multi-Agent Networks**  
- **Date:** 2026-05-08
- **Authors:** Ziwen Cai, Yihe Zhang, Xiali Hei
- **Link:** https://arxiv.org/abs/2605.08460v1
- **Security insight:** Since the official release of ChatGPT in 2022, large language models (LLMs) have rapidly evolved from chatbot-style interfaces into agentic systems that can delegate work through tools and newly spawned subagents. While these capabilities improve automation…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**LLM Advertisement based on Neuron Auctions**  
- **Date:** 2026-05-08
- **Authors:** Peiran Yun, Wenxin Xu, Jiayuan Liu et al.
- **Link:** https://arxiv.org/abs/2605.08326v1
- **Security insight:** As Large Language Models (LLMs) transition into conversational agents, generative advertising emerges as a crucial monetization strategy. However, embedding advertisements within unstructured LLM outputs introduces a critical trilemma: balancing advertiser…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**WebTrap: Stealthy Mid-Task Hijacking of Browser Agents During Navigation**  
- **Date:** 2026-05-08
- **Authors:** Zhichao Liu, Wenbo Pan, Haining Yu et al.
- **Link:** https://arxiv.org/abs/2605.08310v1
- **Security insight:** Browser agents are increasingly deployed in long-horizon tasks, which require executing extended action chains to accomplish user goals. However, this prolonged execution process provides attackers with more opportunities to inject malicious instructions.…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Research on Security Enhancement Methods for Adversarial Robust Large Language Model Intelligent Agents for Medical Decision-Making Tasks**  
- **Date:** 2026-05-07
- **Authors:** Saisai Hu
- **Link:** https://arxiv.org/abs/2605.08257v1
- **Security insight:** Motivated by the challenge to improve the adversarial robustness, security, and trust of medical decision making intelligent agents, this study develops a full-link security enhancement framework, which describes "input risk perception - medical evidence…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**RUBEN: Rule-Based Explanations for Retrieval-Augmented LLM Systems**  
- **Date:** 2026-05-11
- **Authors:** Joel Rorseth, Parke Godfrey, Lukasz Golab et al.
- **Link:** https://arxiv.org/abs/2605.10862v1
- **Security insight:** This paper demonstrates RUBEN, an interactive tool for discovering minimal rules to explain the outputs of retrieval-augmented large language models (LLMs) in data-driven applications. We leverage novel pruning strategies to efficiently identify a minimal set…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**When Prompts Become Payloads: A Framework for Mitigating SQL Injection Attacks in Large Language Model-Driven Applications**  
- **Date:** 2026-05-11
- **Authors:** Farzad Nourmohammadzadeh Motlagh, Mehrdad Hajizadeh, Mehryar Majd et al.
- **Link:** https://arxiv.org/abs/2605.10176v1
- **Security insight:** Natural language interfaces to structured databases are becoming increasingly common, largely due to advances in large language models (LLMs) that enable users to query data using conversational input rather than formal query languages such as SQL. While this…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**CALYREX: Cross-Attention LaYeR EXtended Transformers for System Prompt Anchoring**  
- **Date:** 2026-05-10
- **Authors:** Li Lixing
- **Link:** https://arxiv.org/abs/2605.09737v1
- **Security insight:** Modern large language models (LLMs) rely on system prompts to establish behavioral constraints and safety rules. Standard causal self-attention treats privileged instructions and untrusted user content with equal structural priority -- a mismatch that leaves…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**MIPIAD: Multilingual Indirect Prompt Injection Attack Defense with Qwen -- TF-IDF Hybrid and Meta-Ensemble Learning**  
- **Date:** 2026-05-08
- **Authors:** Al Muhit Muhtadi, Mostafa Rifat Tazwar
- **Link:** https://arxiv.org/abs/2605.07269v1
- **Security insight:** Indirect prompt injection remains a persistent weakness in retrieval-augmented and tool-using LLM systems, and the problem becomes harder to characterise in multilingual settings. We present MIPIAD, a defense framework evaluated on English and Bangla that…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### Model Extraction & Privacy

**Identified-Set Geometry of Distributional Model Extraction under Top-$K$ Censored API Access**  
- **Date:** 2026-05-11
- **Authors:** Wenhua Nie, ZiCheng Zhu, Jianan Wu et al.
- **Link:** https://arxiv.org/abs/2605.10407v1
- **Security insight:** Modern LLM APIs often reveal only top-$K$ logit scores and censor the remaining vocabulary. We study the per-position distribution-recovery limits of this access model. For censoring threshold $τ$, the compatible teacher distributions form an identified set…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

### Adversarial ML

**The Art of the Jailbreak: Formulating Jailbreak Attacks for LLM Security Beyond Binary Scoring**  
- **Date:** 2026-05-09
- **Authors:** Ismail Hossain, Tanzim Ahad, Md Jahangir Alam et al.
- **Link:** https://arxiv.org/abs/2605.09225v1
- **Security insight:** Jailbreak attacks -- adversarial prompts that bypass LLM alignment through purely linguistic manipulation -- pose a growing operational security threat, yet the field lacks large-scale, reproducible infrastructure for generating, categorizing, and evaluating…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

### Other (Review)

**Dependence on Early and Late Reverberation of Single-Channel Speaker Distance Estimation**  
- **Date:** 2026-05-08
- **Authors:** Michael Neri, Archontis Politis, Tuomas Virtanen
- **Link:** https://arxiv.org/abs/2605.07694v1
- **Security insight:** Single-channel speaker distance estimation has recently achieved centimeter-level accuracy in simulated environments, yet it remains unclear which components of the room impulse response (RIR) the model exploits and how performance depends on the recording…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
