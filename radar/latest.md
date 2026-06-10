# AI Security Radar

_Last updated (UTC): **2026-06-10**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

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

**Game-Theoretic Multi-Agent Control for Robust Contextual Reasoning in LLMs**  
- **Date:** 2026-06-09
- **Authors:** Saeid Jamshidi, Amin Nikanjam, Arghavan Moradi Dakhel et al.
- **Link:** https://arxiv.org/abs/2606.10322v1
- **Security insight:** Large Language Models (LLMs) in multi-turn interactions maintain evolving context rather than generating isolated responses, making them vulnerable to prompt-injection and context-poisoning attacks in which locally plausible adversarial fragments gradually…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**PRISM: Recovering Instruction Sets from Language Model Activations**  
- **Date:** 2026-06-08
- **Authors:** Gilad Gressel, Rahul Pankajakshan, Julia Diament et al.
- **Link:** https://arxiv.org/abs/2606.09563v1
- **Security insight:** As LLMs are deployed as agents, reliable monitoring requires knowing not only what they output, but which instructions are steering their behavior. This is difficult when models infer unintended subgoals, follow contextual cues, or are influenced by prompt…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**SecureClaw: Clawing Back Control of LLM Agents**  
- **Date:** 2026-06-08
- **Authors:** Yuhan Ma, Stefan Schmid
- **Link:** https://arxiv.org/abs/2606.09549v1
- **Security insight:** Tool-using large language model (LLM) agents face two distinct security failures: unauthorized external actions and exposure of sensitive plaintext inside the runtime before any final output check can intervene. Existing defenses usually protect one boundary,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Brain-Prompt Injection: A Route-Safety Audit for BCI-LLM Agents**  
- **Date:** 2026-06-08
- **Authors:** Jianwei Tai
- **Link:** https://arxiv.org/abs/2606.09315v1
- **Security insight:** BCI-to-agent pipelines turn decoded neural activity into an authorization channel for tool-use agents, exposing a new attack surface we call \emph{brain-prompt injection}: signal-side perturbations, context-only injections, and adaptive dual-decoder attacks…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**GitInject: Real-World Prompt Injection Attacks in AI-Powered CI/CD Pipelines**  
- **Date:** 2026-06-07
- **Authors:** Jafar Isbarov, Umid Suleymanov, Ilia Shumailov et al.
- **Link:** https://arxiv.org/abs/2606.09935v1
- **Security insight:** AI-powered agents are increasingly embedded in continuous integration and continuous delivery/deployment (CI/CD) pipelines to autonomously review pull requests (PRs), triage issues, and maintain codebases. These agents ingest untrusted content while operating…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Data Agents Under Attack: Vulnerabilities in LLM-Driven Analytical Systems**  
- **Date:** 2026-06-07
- **Authors:** Kuncan Wang, Ziting Wang, Peizhuo Lv et al.
- **Link:** https://arxiv.org/abs/2606.08661v1
- **Security insight:** Data agents integrate LLM-driven reasoning with relational data access, executable analytical tools, and multi-step workflow orchestration, making them increasingly central to enterprise analytics. This integration introduces new security vulnerabilities…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**VATS: Exploiting Implicit Authority in Error-Path Injection via Systematic Mutation**  
- **Date:** 2026-06-06
- **Authors:** Harshil Patel, Kunal Pai
- **Link:** https://arxiv.org/abs/2606.07992v1
- **Security insight:** As the Model Context Protocol (MCP) standardizes tool-calling for autonomous agents, it introduces a critical, unexamined attack surface: the error-handling loop. We hypothesize that tool error messages possess implicit authority, triggering corrective…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Training LLMs to Enforce Multi-Level Instruction Hierarchies via Gravity-Weighted Direct Preference Optimization**  
- **Date:** 2026-06-09
- **Authors:** Lena S. Bolliger, Lena A. Jäger
- **Link:** https://arxiv.org/abs/2606.10860v1
- **Security insight:** Production LLMs receive instructions from sources with very different levels of trust, yet attend to every token with uniform architectural privilege. This is the structural vulnerability that enables malicious prompt injections and, more broadly, leaves…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**The Injection Paradox: Brand-Level Suppression in Safety-Trained LLM Recommendations via RAG Context Injection**  
- **Date:** 2026-06-08
- **Authors:** Hyunseok Paeng
- **Link:** https://arxiv.org/abs/2606.09204v1
- **Security insight:** We present a reproducible failure mode of safety training in RAG-based LLM recommendation -- the Injection Paradox -- in which prompt injections embedded in retrieved documents backfire against the attacker, suppressing the target brand below the injection-…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Document-Authored Control-Signal Impersonation: A Low-Cost Indirect Prompt Attack on RAG Safety Boundaries**  
- **Date:** 2026-06-08
- **Authors:** Jianguo Zhu
- **Link:** https://arxiv.org/abs/2606.09005v1
- **Security insight:** Retrieval-augmented generation (RAG) systems often serialize user queries, retrieved documents, metadata, system labels, and task instructions into one natural-language prompt. We study a source-authority boundary failure in this design: attacker-authored…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Hiding in Plain Floats: Steganographic Carriers for Indirect Prompt and Content Injection**  
- **Date:** 2026-06-07
- **Authors:** Mudit Sinha, Sanika Chavan
- **Link:** https://arxiv.org/abs/2606.08403v1
- **Security insight:** Text-centered prompt-injection defenses assume that the malicious signal is visible in one of the inspected text views. We study a reproducible LLM01-style indirect prompt/content-injection failure mode where that assumption breaks: a payload caught in plain…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### Adversarial ML

**Learning to Attack and Defend: Adaptive Red Teaming of Language Models via GRPO**  
- **Date:** 2026-06-08
- **Authors:** Blake Bullwinkel, Eugenia Kim, Amanda Minnich et al.
- **Link:** https://arxiv.org/abs/2606.09701v1
- **Security insight:** AI red teaming must continually adapt to evolving attackers and defenders. Reinforcement learning offers a promising approach to discovering novel attacks, and co-training methods can produce more robust defenders in tandem. Recent works have demonstrated the…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.
