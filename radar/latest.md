# AI Security Radar

_Last updated (UTC): **2026-04-30**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

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
- **Link:** https://arxiv.org/abs/2604.25186v1
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

**AgentVisor: Defending LLM Agents Against Prompt Injection via Semantic Virtualization**  
- **Date:** 2026-04-27
- **Authors:** Zonghao Ying, Haozheng Wang, Jiangfan Liu et al.
- **Link:** https://arxiv.org/abs/2604.24118v1
- **Security insight:** Large Language Model (LLM) agents are increasingly used to automate complex workflows, but integrating untrusted external data with privileged execution exposes them to severe security risks, particularly direct and indirect prompt injection. Existing…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Poster: ClawdGo: Endogenous Security Awareness Training for Autonomous AI Agents**  
- **Date:** 2026-04-27
- **Authors:** Jiaqi Li, Yang Zhao, Bin Sun et al.
- **Link:** https://arxiv.org/abs/2604.24020v1
- **Security insight:** Autonomous AI agents deployed on platforms such as OpenClaw face prompt injection, memory poisoning, supply-chain attacks, and social engineering, yet existing defences address only the platform perimeter, leaving the agent's own threat judgement entirely…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Making AI-Assisted Grant Evaluation Auditable without Exposing the Model**  
- **Date:** 2026-04-28
- **Authors:** Kemal Bicakci
- **Link:** https://arxiv.org/abs/2604.25200v1
- **Security insight:** Public agencies are beginning to consider large language models (LLMs) as decision-support tools for grant evaluation. This creates a practical governance problem: the model and scoring rubric should not be exposed in a way that allows applicants to optimize…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Layerwise Convergence Fingerprints for Runtime Misbehavior Detection in Large Language Models**  
- **Date:** 2026-04-27
- **Authors:** Nay Myat Min, Long H. Pham, Jun Sun
- **Link:** https://arxiv.org/abs/2604.24542v1
- **Security insight:** Large language models deployed at runtime can misbehave in ways that clean-data validation cannot anticipate: training-time backdoors lie dormant until triggered, jailbreaks subvert safety alignment, and prompt injections override the deployer's instructions.…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Evaluation of Prompt Injection Defenses in Large Language Models**  
- **Date:** 2026-04-26
- **Authors:** Priyal Deep, Shane Emmons, Amy Fox et al.
- **Link:** https://arxiv.org/abs/2604.23887v1
- **Security insight:** LLM-powered applications routinely embed secrets in system prompts, yet models can be tricked into revealing them. We built an adaptive attacker that evolves its strategies over hundreds of rounds and tested it against nine defense configurations across more…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**Adaptive Prompt Embedding Optimization for LLM Jailbreaking**  
- **Date:** 2026-04-27
- **Authors:** Miles Q. Li, Benjamin C. M. Fung, Boyang Li et al.
- **Link:** https://arxiv.org/abs/2604.24983v1
- **Security insight:** Existing white-box jailbreak attacks against aligned LLMs typically append discrete adversarial suffixes to the user prompt, which visibly alters the prompt and operates in a combinatorial token space. Prior work has avoided directly optimizing the embeddings…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms**  
- **Date:** 2026-04-26
- **Authors:** Qi Li, Bo Yin, Weiqi Huang et al.
- **Link:** https://arxiv.org/abs/2604.23775v1
- **Security insight:** Vision-Language-Action (VLA) models are emerging as a unified substrate for embodied intelligence. This shift raises a new class of safety challenges, stemming from the embodied nature of VLA systems, including irreversible physical consequences, a multimodal…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Adversarial ML

**High-Probability Guarantees for Random Zeroth-Order (Stochastic) Gradient Descent**  
- **Date:** 2026-04-26
- **Authors:** Haishan Ye
- **Link:** https://arxiv.org/abs/2604.23613v1
- **Security insight:** Zeroth-order optimization aims to minimize an objective function using only function evaluations, and is therefore fundamental in black-box optimization, hyperparameter tuning, bandit learning, and adversarial machine learning. While classical zeroth-order…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.
