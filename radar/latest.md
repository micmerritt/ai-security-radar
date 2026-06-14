# AI Security Radar

_Last updated (UTC): **2026-06-14**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking for Real-world Web Agents**  
- **Date:** 2026-06-11
- **Authors:** Zihao Wang, Yiming Li, Yutong Wu et al.
- **Link:** https://arxiv.org/abs/2606.13385v1
- **Security insight:** Web agents driven by large language models (LLMs) are increasingly deployed in real-world environments, where they operate over untrusted web content and execute actions with direct consequences. This makes them vulnerable to prompt-injection attacks, in…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Nous: An Attempt to Extract and Inject the Cognition Behind Prediction-Market Behavior**  
- **Date:** 2026-06-11
- **Authors:** Haowei Qian
- **Link:** https://arxiv.org/abs/2606.13038v1
- **Security insight:** As LLM agents proliferate in prediction markets and collective decision-making, they risk a cognitive monoculture: agents built on shared foundation models produce correlated forecasts, and recent measurement finds frontier-model errors correlated at r ~…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**PI-Hunter: Automated Red-Teaming for Exposing and Localizing Prompt Injections**  
- **Date:** 2026-06-10
- **Authors:** Pengfei He, Lesly Miculicich, Vishesh Sharma et al.
- **Link:** https://arxiv.org/abs/2606.12737v1
- **Security insight:** Large Language Models (LLMs) are rapidly evolving into agentic systems that interact with external tools and environments, introducing new security risks such as indirect prompt injection attacks through untrusted external sources. Existing defenses mainly…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Does AI Reviewer See the Full Picture? Attacking and Defending Multimodal Peer Review**  
- **Date:** 2026-06-10
- **Authors:** Xinyu Zhao, Rana Muhammad Shahroz Khan, Zhen Xu et al.
- **Link:** https://arxiv.org/abs/2606.12716v1
- **Security insight:** The integration of Large Language Models (LLMs) and Multimodal LLMs (MLLMs) into scientific peer-review workflows introduces novel and significant risks for adversarial manipulation, especially given the multimodal nature of scientific papers where figures,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Smarter Saboteurs, Better Fixers: Scaling & Security in Linear Multi-Agent Workflows**  
- **Date:** 2026-06-10
- **Authors:** Timothy McAllister, Sina Abdidizaji, Ivan Garibay et al.
- **Link:** https://arxiv.org/abs/2606.12709v1
- **Security insight:** As LLM-based multi-agent systems (MAS) are deployed in the wild, the resilience of their collaboration structures against adversarial compromise becomes a critical safety concern. Attackers may leverage prompt-injection or jailbreaking to sabotage individual…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation**  
- **Date:** 2026-06-09
- **Authors:** Yuchen Ling, Shengcheng Yu, Zhenyu Chen et al.
- **Link:** https://arxiv.org/abs/2606.10749v1
- **Security insight:** Large language model (LLM) agents are rapidly moving from conversational interfaces to software components that plan, invoke tools, maintain memory, and act on external environments. This transition changes the nature of security risk. In agentic settings,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Assessing Automated Prompt Injection Attacks in Agentic Environments**  
- **Date:** 2026-06-09
- **Authors:** David Hofer, Edoardo Debenedetti, Florian Tramèr
- **Link:** https://arxiv.org/abs/2606.10525v1
- **Security insight:** Indirect prompt injection poses a critical threat to LLM agents that interact with untrusted external data, yet automated attack methods--proven effective for jailbreaking--remain underexplored in realistic agentic settings. We present a comprehensive…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**No Hidden Prompts Needed! You Can Game AI Peer Review with Presentation-Only Revisions**  
- **Date:** 2026-06-11
- **Authors:** Xu Yang, Zhizhou Sha, Junbo Li et al.
- **Link:** https://arxiv.org/abs/2606.13044v1
- **Security insight:** As AI-generated reviews move from experimental tools into peer-review infrastructure, most robustness concerns have focused on explicit attacks such as hidden instructions and prompt injection. We study a harder and more policy-relevant failure mode: no…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**External Experience Serving in Production LLM Systems: A Deployment-Oriented Study of Quality-Cost Trade-offs**  
- **Date:** 2026-06-10
- **Authors:** Lin Sun, Heming Zhang, Xiangzheng Zhang
- **Link:** https://arxiv.org/abs/2606.11806v1
- **Security insight:** Production LLM systems accumulate reusable operational experience, but the practical deployment issue is not merely whether such experience can help. It is how different serving strategies trade off quality against online cost under realistic constraints.…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Training LLMs to Enforce Multi-Level Instruction Hierarchies via Gravity-Weighted Direct Preference Optimization**  
- **Date:** 2026-06-09
- **Authors:** Lena S. Bolliger, Lena A. Jäger
- **Link:** https://arxiv.org/abs/2606.10860v1
- **Security insight:** Production LLMs receive instructions from sources with very different levels of trust, yet attend to every token with uniform architectural privilege. This is the structural vulnerability that enables malicious prompt injections and, more broadly, leaves…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**Acoda: Adversarial Code Obfuscation for Defending against LLM-based Analysis**  
- **Date:** 2026-06-10
- **Authors:** Hongzhou Rao, Zikan Dong, Yanjie Zhao et al.
- **Link:** https://arxiv.org/abs/2606.11755v1
- **Security insight:** With the widespread adoption of Large Language Models (LLMs) in software engineering (SE) tasks such as code understanding, debugging, and vulnerability detection, their powerful semantic reasoning ability has also introduced new security and privacy risks.…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**T2S: A Rehearsal-Based Approach for Extraction-Resistant Model Watermarking**  
- **Date:** 2026-06-10
- **Authors:** Jian-Ping Mei, Weibin Zhang, Ao Yao et al.
- **Link:** https://arxiv.org/abs/2606.11698v1
- **Security insight:** Model watermarking safeguards AI model intellectual property by embedding distinctive knowledge that induces unique behavioral signatures. The primary technical challenge lies in ensuring watermark robustness against various post-processing attacks on the…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**Influence Factors on RAG Poisoning**  
- **Date:** 2026-06-09
- **Authors:** Pedro Pereira, Eva Maia, Isabel Praça et al.
- **Link:** https://arxiv.org/abs/2606.12469v1
- **Security insight:** Retrieval-Augmented Generation (RAG) systems enhance large language models by grounding responses in retrieved documents from external knowledge sources at inference time. However, this reliance on retrieved content introduces vulnerabilities to poisoning…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Model Extraction & Privacy

**SciR: A Controllable Benchmark for Scientific Reasoning in LLMs**  
- **Date:** 2026-06-11
- **Authors:** Pierre Beckmann, Marco Valentino, Andre Freitas
- **Link:** https://arxiv.org/abs/2606.13020v1
- **Security insight:** Three paradigmatic forms of inference recur across scientific reasoning: deduction, induction, and causal abduction. Reliably evaluating LLMs on these in scientific settings is currently out of reach: scientific benchmarks built on human annotations are…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?
