# AI Security Radar

_Last updated (UTC): **2026-09-28**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

**MetaPermit: Scalable and Auditable Access Control for AI Agents via LLM-Inferred Meta-Attributes**  
- **Date:** 2026-09-25
- **Authors:** Hanzhang Ma, Ali Hariri, Tianxiang Shen et al.
- **Link:** https://arxiv.org/abs/2609.31039v1
- **Security insight:** The rise of autonomous AI agents equipped with tools has introduced significant security risks, ranging from unintended tool misuse to adversarial manipulation through Indirect Prompt Injection (IPI) attacks. In practice, deployed agent systems such as OpenAI…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Crypto-bound identity-verified capability tokens for coordinating distributed AI agents: A proposal**  
- **Date:** 2026-09-25
- **Authors:** Srikumar Subramanian, Shubhashis Sengupta
- **Link:** https://arxiv.org/abs/2609.30824v1
- **Security insight:** The prospect of fully autonomous transactional agents did not appear on the horizon until the advent of high capability language models. With such models, the operational benefits of adaptive task orchestration and independent (but constrained) decision…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Prompt Injection Detection for Email Agents Through Attack Chain Modeling**  
- **Date:** 2026-09-25
- **Authors:** Ahmad Hashmi, Dhyey Patel, Yunting Yin
- **Link:** https://arxiv.org/abs/2609.30657v1
- **Security insight:** Large language model email assistants are particularly vulnerable to indirect prompt injection because untrusted email content can be retrieved into the model context and influence subsequent tool use. Existing prompt injection detectors mainly formulate this…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Instrumental Monitor Evasion Emerges Under Ordinary Task Pressure**  
- **Date:** 2026-09-24
- **Authors:** David Schmotz, Derck Prinzhorn, Luca Beurer-Kellner et al.
- **Link:** https://arxiv.org/abs/2609.30217v1
- **Security insight:** A central concern in AI safety is that agents may treat oversight as an obstacle when it conflicts with completing their goals. We study instrumental evasion, the propensity of LLM agents to circumvent runtime monitoring as a means of completing ordinary…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**ENDOPROMPT: Victim-Side Pseudo-References for Utility Degradation**  
- **Date:** 2026-09-24
- **Authors:** Qingyu Wu, Zeyu Feng, Yongda Yu et al.
- **Link:** https://arxiv.org/abs/2609.29948v1
- **Security insight:** Prompt injection can degrade benign task performance without eliciting harmful content. Yet many attack objectives depend on task labels or predefined target responses. We present ENDOPROMPT, a white-box method that learns utility-degrading prefixes from…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Prefilling the Reasoning Channel: Output-Prefix Attacks on Reasoning LLMs**  
- **Date:** 2026-09-24
- **Authors:** Lukáš Brůna, Robert Bridges, Adam Ek
- **Link:** https://arxiv.org/abs/2609.29775v1
- **Security insight:** Large Language Models (LLMs) consume and produce a single sequence of text; hence, if text can be added to the beginning of the LLM's response, i.e., an output prefix, then all subsequent tokens will be conditioned on it. This output-prefix attack technique…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**OllamaDrama: Designing and Deploying a Honeypot to Measure Attacks on Exposed LLM Infrastructure**  
- **Date:** 2026-09-24
- **Authors:** Karina Elzer, Niklas Netterstrøm Johansen, Emmanouil Vasilomanolakis
- **Link:** https://arxiv.org/abs/2609.29757v1
- **Security insight:** Publicly exposed large language model (LLM) infrastructure creates a growing attack surface, yet real-world targeting remains poorly understood. We present Ollure, a low- and medium-interaction honeypot that emulates the Ollama API without a backend LLM.…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Just Ask Jev: Reinforcement Learning for Calibrated Decisions as a Zero-Shot Detector of AI Alignment Failures**  
- **Date:** 2026-09-24
- **Authors:** Ruoqi Guo, Yi Liu, Gelei Deng et al.
- **Link:** https://arxiv.org/abs/2609.29429v1
- **Security insight:** Detectors of alignment failures screen deployed language models and score alignment benchmarks. Most are generative judges that spend a decoding pass on every criterion, and classifiers that read token probabilities, such as Llama Guard, still score one fixed…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Through Human Eyes and Machine Eyes: Understanding View Mismatch in Video See-Through Extended Reality**  
- **Date:** 2026-09-24
- **Authors:** Yanming Xiu
- **Link:** https://arxiv.org/abs/2609.29173v1
- **Security insight:** Video see-through extended reality (VST XR) systems commonly use headset screenshots or captured frames as proxies for the user's first-person visual context. However, the system-captured view and the user's effective visible field do not necessarily…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**On the Effectiveness of Kernel-Level Evidence for Agent Security**  
- **Date:** 2026-09-24
- **Authors:** Spencer King, Zhilu Zhang, Mikhail Kuznetsov et al.
- **Link:** https://arxiv.org/abs/2609.28915v1
- **Security insight:** LLM agents are deployed into infrastructure that grants them broad host authority, yet existing agent-security benchmarks and defenses operate almost exclusively at the application telemetry layer: the served tool manifest, the user prompt, and the model's…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Decision Hijacking: Prompt Injection Attacks on Jev's Typed Probabilistic Decisions**  
- **Date:** 2026-09-23
- **Authors:** Tiantong Wu, Wei Yang Bryan Lim
- **Link:** https://arxiv.org/abs/2609.28613v1
- **Security insight:** Most studies of prompt injection focus on generative agents, leaving their effects on models with schema-defined outputs unclear. We examine these effects in Jev, a non-generative decision model, using 510 reconstructed InjecAgent cases. Malicious content…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### Poisoning & Backdoors

**Blockchain-Enabled Artificial Intelligence and AI Agents for Secure Data Sharing and Cybersecurity Applications**  
- **Date:** 2026-09-23
- **Authors:** Harsh Verma
- **Link:** https://arxiv.org/abs/2609.28843v1
- **Security insight:** Blockchain and artificial intelligence (AI) are converging into a single infrastructural layer for securing data sharing, model integrity, and autonomous decision-making across distributed systems. This paper presents a meta-synthesis that draws together four…
- **Build idea:** Build a minimal poisoning simulator plus simple detectors (trigger search, label flip tests, anomaly baselines).

### Model Extraction & Privacy

**User Model Extraction via Belief Self-Distillation**  
- **Date:** 2026-09-25
- **Authors:** Ali Holmov, Yiran Huang, Kirill Bykov et al.
- **Link:** https://arxiv.org/abs/2609.31603v1
- **Security insight:** Large language models (LLMs) implicitly infer attributes of their users and adapt their behavior accordingly, yet these beliefs remain difficult to inspect and causally manipulate. We introduce Belief Self-Distillation (BSD), a unified read-write framework…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

### Adversarial ML

**AgentXploit: Autonomous Repository-to-Runtime Red-Teaming for AI Agents**  
- **Date:** 2026-09-25
- **Authors:** Weida Liang, Shi Qiu, Zhun Wang et al.
- **Link:** https://arxiv.org/abs/2609.31318v1
- **Security insight:** AI agents combine language models with external data and tools that can modify files, call APIs, or execute code. Security failures can arise when adversarial content changes an agent's tool use or when the surrounding software contains vulnerabilities such…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.
