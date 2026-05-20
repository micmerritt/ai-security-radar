# AI Security Radar

_Last updated (UTC): **2026-05-20**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Agent Security is a Systems Problem**  
- **Date:** 2026-05-18
- **Authors:** Mihai Christodorescu, Earlence Fernandes, Ashish Hooda et al.
- **Link:** https://arxiv.org/abs/2605.18991v1
- **Security insight:** We take the position that agent security must be approached as a systems problem: the AI model powering the agent must be treated as an untrusted component, and security invariants must be enforced at the system level. Through this lens, efforts to increase…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Overeager Coding Agents: Measuring Out-of-Scope Actions on Benign Tasks**  
- **Date:** 2026-05-18
- **Authors:** Yubin Qu, Ying Zhang, Yanjun Zhang et al.
- **Link:** https://arxiv.org/abs/2605.18583v1
- **Security insight:** Coding agents now run autonomously with shell, file, and network privileges. When a user issues a benign request, the agent sometimes does more than asked: it deletes unrelated files, wipes a stale credentials backup, or rewrites configuration the user never…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**An Empirical Study of Privacy Leakage Chains via Prompt Injection in Black-Box Chatbot Environments**  
- **Date:** 2026-05-18
- **Authors:** Hongjang Yang, Hyunsik Na, Daeseon Choi
- **Link:** https://arxiv.org/abs/2605.18133v1
- **Security insight:** LLM-based chatbot agents increasingly process user requests by combining natural-language reasoning with external tools such as web browsing. These capabilities improve usability, but they also create attack surfaces when untrusted external content is…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**LivePI: More Realistic Benchmarking of Agents Against Indirect Prompt Injectio**  
- **Date:** 2026-05-18
- **Authors:** Lei Zhao, Abhay Bhaskar, Edgar Dobriban
- **Link:** https://arxiv.org/abs/2605.17986v1
- **Security insight:** AI agents such as OpenClaw are increasingly deployed in local workflows with access to external tools. This creates indirect prompt-injection (IPI) risk: an agent may execute harmful instructions embedded in untrusted inputs such as email, downloaded files,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**ESLD (External Surrogate Latent Defense): A Latent-Space Architecture for Faster, Stronger Prompt-Injection Defense**  
- **Date:** 2026-05-18
- **Authors:** Yash Narendra
- **Link:** https://arxiv.org/abs/2605.18918v1
- **Security insight:** Modern AI assistants are agentic. To answer a single user request, the underlying language model pulls in information from many sources, such as web searches, retrieved documents, tool outputs, and user follow-ups, and reasons over them across several steps.…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Remembering More, Risking More: Longitudinal Safety Risks in Memory-Equipped LLM Agents**  
- **Date:** 2026-05-18
- **Authors:** Ahmad Al-Tawaha, Shangding Gu, Peizhi Niu et al.
- **Link:** https://arxiv.org/abs/2605.17830v1
- **Security insight:** Safety evaluations of memory-equipped LLM agents typically measure within-task safety: whether an agent completes a single scenario safely, often under adversarial conditions such as prompt injection or memory poisoning. In deployment, however, a single agent…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**AI Agents May Always Fall for Prompt Injections**  
- **Date:** 2026-05-17
- **Authors:** Sahar Abdelnabi, Eugene Bagdasarian
- **Link:** https://arxiv.org/abs/2605.17634v1
- **Security insight:** Prompt injection is the most critical vulnerability in deployed AI agents. Despite recent progress, we show that the prevailing defense paradigm (data-instruction separation) both fails to detect attacks that operate through contextual manipulation and…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Trust No Tool: Evaluating and Defending LLM Agents under Untrusted Tool Feedback**  
- **Date:** 2026-05-17
- **Authors:** Lecheng Yan, Ruizhe Li, Xicheng Han et al.
- **Link:** https://arxiv.org/abs/2605.17453v1
- **Security insight:** Tool-using LLM agents increasingly rely on external tools to make consequential decisions, yet most existing agent-security benchmarks and defenses implicitly assume that tool feedback is trustworthy once a tool has been selected. We study a different failure…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**ADR: An Agentic Detection System for Enterprise Agentic AI Security**  
- **Date:** 2026-05-17
- **Authors:** Chenning Li, Pan Hu, Justin Xu et al.
- **Link:** https://arxiv.org/abs/2605.17380v1
- **Security insight:** We present the Agentic AI Detection and Response (ADR) system, the first large-scale, production-proven enterprise framework for securing AI agents operating through the Model Context Protocol (MCP). We identify three persistent challenges in this domain: (1)…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**ASPI: Seeking Ambiguity Clarification Amplifies Prompt Injection Vulnerability in LLM Agents**  
- **Date:** 2026-05-17
- **Authors:** Udari Madhushani Sehwag, Zhengyang Shan, Heming Liu et al.
- **Link:** https://arxiv.org/abs/2605.17324v1
- **Security insight:** Clarification-seeking behavior is widely regarded as a desirable property of LLM agents, enabling them to resolve ambiguity before acting on underspecified tasks. However, the security implications of this interaction pattern remain unexplored. We investigate…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**MADP: A Multi-Agent Pipeline for Sustainable Document Processing with Human-in-the-Loop**  
- **Date:** 2026-05-16
- **Authors:** Diego Gosmar, Giovanni Zenezini
- **Link:** https://arxiv.org/abs/2605.17159v1
- **Security insight:** Document processing automation remains a critical challenge in enterprise environments, where traditional manual approaches are labor-intensive and error-prone. We present MADP, a multi-agent architecture that addresses the challenge of automating document…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**FORGE: Self-Evolving Agent Memory With No Weight Updates via Population Broadcast**  
- **Date:** 2026-05-15
- **Authors:** Igor Bogdanov, Chung-Horng Lung, Thomas Kunz et al.
- **Link:** https://arxiv.org/abs/2605.16233v1
- **Security insight:** Can LLM agents improve decision-making through self-generated memory without gradient updates? We propose FORGE (Failure-Optimized Reflective Graduation and Evolution), a staged, population-based protocol that evolves prompt-injected natural-language memory…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**On the Geometric Limits of Transformer Defenses against Obfuscation Attacks: Latent Embedding Collapse & Performance Robustness Gap**  
- **Date:** 2026-05-18
- **Authors:** Becky Mashaido, Tapadhir Das
- **Link:** https://arxiv.org/abs/2605.19159v1
- **Security insight:** Prompt injection attacks pose significant risks to language model safety, yet existing defenses are typically evaluated using classification performance. We show that high detection performance does not imply representational robustness. Specifically, multi-…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**STRIDE-AI: A Threat Modeling Framework for Generative AI Security Assessment**  
- **Date:** 2026-05-16
- **Authors:** Tsafac Nkombong Regine Cyrille, Franziska Schwarz
- **Link:** https://arxiv.org/abs/2605.17163v1
- **Security insight:** Traditional cybersecurity methodologies target deterministic systems and fail to address the probabilistic nature of AI, leaving systems vulnerable to attack vectors such as model inversion, data poisoning, and prompt injection. Recent industry reports…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.
