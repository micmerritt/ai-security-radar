# AI Security Radar

_Last updated (UTC): **2026-05-02**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**FlashRT: Towards Computationally and Memory Efficient Red-Teaming for Prompt Injection and Knowledge Corruption**  
- **Date:** 2026-04-30
- **Authors:** Yanting Wang, Chenlong Yin, Ying Chen et al.
- **Link:** https://arxiv.org/abs/2604.28157v1
- **Security insight:** Long-context large language models (LLMs)-for example, Gemini-3.1-Pro and Qwen-3.5-are widely used to empower many real-world applications, such as retrieval-augmented generation, autonomous agents, and AI assistants. However, security remains a major concern…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Security Attack and Defense Strategies for Autonomous Agent Frameworks: A Layered Review with OpenClaw as a Case Study**  
- **Date:** 2026-04-30
- **Authors:** Luyao Xu, Xiang Chen
- **Link:** https://arxiv.org/abs/2604.27464v1
- **Security insight:** Autonomous agent frameworks built upon large language models (LLMs) are evolving into complex, tool-integrated, and continuously operating systems, introducing security risks beyond traditional prompt-level vulnerabilities. As this paradigm is still at an…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Indirect Prompt Injection in the Wild: An Empirical Study of Prevalence, Techniques, and Objectives**  
- **Date:** 2026-04-29
- **Authors:** Soheil Khodayari, Xuenan Zhang, Bhupendra Acharya et al.
- **Link:** https://arxiv.org/abs/2604.27202v1
- **Security insight:** As LLMs are increasingly integrated into systems that browse, retrieve, summarize, and act on web content, webpages have become an untrusted input vector for downstream model behavior. This enables site owners, contributors, and adversaries to embed…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Enforcing Benign Trajectories: A Behavioral Firewall for Structured-Workflow AI Agents**  
- **Date:** 2026-04-29
- **Authors:** Hung Dang
- **Link:** https://arxiv.org/abs/2604.26274v1
- **Security insight:** Structured-workflow agents driven by large language models execute tool calls against sensitive external environments. We propose \codename, a telemetry-driven behavioral anomaly detection firewall. Drawing on sequence-based intrusion detection, \codename\…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**SnapGuard: Lightweight Prompt Injection Detection for Screenshot-Based Web Agents**  
- **Date:** 2026-04-28
- **Authors:** Mengyao Du, Han Fang, Haokai Ma et al.
- **Link:** https://arxiv.org/abs/2604.25562v1
- **Security insight:** Web agents have emerged as an effective paradigm for automating interactions with complex web environments, yet remain vulnerable to prompt injection attacks that embed malicious instructions into webpage content to induce unintended actions. This threat is…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**FCMBench-Video: Benchmarking Document Video Intelligence**  
- **Date:** 2026-04-28
- **Authors:** Runze Cui, Fangxin Shang, Yehui Yang et al.
- **Link:** https://arxiv.org/abs/2604.25186v2
- **Security insight:** Document understanding is a critical capability in financial credit review, onboarding, and remote verification, where both decision accuracy and evidence traceability matter. Compared with static document images, document videos present a temporally…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**One Perturbation, Two Failure Modes: Probing VLM Safety via Embedding-Guided Typographic Perturbations**  
- **Date:** 2026-04-28
- **Authors:** Ravikumar Balakrishnan, Sanket Mendapara
- **Link:** https://arxiv.org/abs/2604.25102v1
- **Security insight:** Typographic prompt injection exploits vision language models' (VLMs) ability to read text rendered in images, posing a growing threat as VLMs power autonomous agents. Prior work typically focus on maximizing attack success rate (ASR) but does not explain…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**SUDP: Secret-Use Delegation Protocol for Agentic Systems**  
- **Date:** 2026-04-27
- **Authors:** Xiaohang Yu, Hejia Geng, William Knottenbelt
- **Link:** https://arxiv.org/abs/2604.24920v1
- **Security insight:** Agentic systems increasingly act with user secrets for APIs, messaging platforms, and cloud services. Today's bearer-secret interfaces implement authorization by exposure: enabling action often means placing a reusable secret, or a reusable artifact derived…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**A Comparative Evaluation of AI Agent Security Guardrails**  
- **Date:** 2026-04-27
- **Authors:** Qi Li, Jiu Li, Pingtao Wei et al.
- **Link:** https://arxiv.org/abs/2604.24826v1
- **Security insight:** This report presents a comparative evaluation of DKnownAI Guard in AI agent security scenarios, benchmarked against three competing products: AWS Bedrock Guardrails, Azure Content Safety, and Lakera Guard. Using human annotation as the ground truth, we assess…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection**  
- **Date:** 2026-04-30
- **Authors:** Prashant Kulkarni
- **Link:** https://arxiv.org/abs/2604.28129v1
- **Security insight:** Multi-turn prompt injection follows a known attack path -- trust-building, pivoting, escalation but text-level defenses miss covert attacks where individual turns appear benign. We show this attack path leaves an activation-level signature in the model's…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Making AI-Assisted Grant Evaluation Auditable without Exposing the Model**  
- **Date:** 2026-04-28
- **Authors:** Kemal Bicakci
- **Link:** https://arxiv.org/abs/2604.25200v1
- **Security insight:** Public agencies are beginning to consider large language models (LLMs) as decision-support tools for grant evaluation. This creates a practical governance problem: the model and scoring rubric should not be exposed in a way that allows applicants to optimize…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**BatteryPass-12K: The First Dataset for the Novel Digital Battery Passport Conformance Task**  
- **Date:** 2026-04-28
- **Authors:** Tosin Adewumi, Martin Karlsson, Lama Alkhaled et al.
- **Link:** https://arxiv.org/abs/2604.26986v1
- **Security insight:** We introduce a novel task of digital battery passport (DBP) conformance classification and introduce the first public benchmark for the task: BatteryPass-12K, created synthetically from real pilot samples. This is as the EU's battery regulation on DBPs comes…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**Adaptive Prompt Embedding Optimization for LLM Jailbreaking**  
- **Date:** 2026-04-27
- **Authors:** Miles Q. Li, Benjamin C. M. Fung, Boyang Li et al.
- **Link:** https://arxiv.org/abs/2604.24983v1
- **Security insight:** Existing white-box jailbreak attacks against aligned LLMs typically append discrete adversarial suffixes to the user prompt, which visibly alters the prompt and operates in a combinatorial token space. Prior work has avoided directly optimizing the embeddings…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Other (Review)

**How Code Representation Shapes False-Positive Dynamics in Cross-Language LLM Vulnerability Detection**  
- **Date:** 2026-04-30
- **Authors:** Maofei Chen, Laifu Wang, Yue Qin et al.
- **Link:** https://arxiv.org/abs/2604.27714v1
- **Security insight:** How code representation format shapes false positive behaviour in cross-language LLM vulnerability detection remains poorly understood. We systematically vary training intensity and code representation format, comparing raw source text with pruned Abstract…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
