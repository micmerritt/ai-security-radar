# AI Security Radar

_Last updated (UTC): **2026-10-19**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

**MobileInject: Evaluating Reasoning-to-Action Security of MLLM-Based Mobile Agents under Cross-Modal Consistency Injection**  
- **Date:** 2026-10-16
- **Authors:** Songping Wang, Peiyang Li, Yi Huang et al.
- **Link:** https://arxiv.org/abs/2610.23307v1
- **Security insight:** Multimodal large language model (MLLM)-based mobile agents are rapidly evolving from conversational assistants into autonomous systems that perceive, reason over, and act on smartphone environments. This capability also exposes a new security risk:…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Ignored, Not Refused: What Low Prompt-Injection Success Rates Hide in Small Tool-Using Agents**  
- **Date:** 2026-10-16
- **Authors:** Farhan Zarif, Kazi Shahid Ahmed Galib, Synthia Akter Promi et al.
- **Link:** https://arxiv.org/abs/2610.23254v1
- **Security insight:** Tool-using agents read untrusted external content, which exposes them to indirect prompt injection (IPI), where hidden instructions hijack the agent's tool calls. Benchmarks measure IPI security by the attack success rate (ASR), which treats every failed…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**From Approval to Abuse: Privilege Escalation Attacks on Harness-Protected Coding Agents**  
- **Date:** 2026-10-16
- **Authors:** Xianglin Yang, Yechao Zhang, Jiahao Liu et al.
- **Link:** https://arxiv.org/abs/2610.22987v1
- **Security insight:** Coding agents use execution harnesses to constrain the consequences of prompt injection by enforcing permission boundaries. These systems deterministically intercept any out-of-sandbox action and prompt the user for approval. To reduce approval fatigue, users…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Stealthy Poisoning Attacks via Reused KV Cache of Reasoning**  
- **Date:** 2026-10-16
- **Authors:** L. Zhu, Y. Jung, S. Szyller
- **Link:** https://arxiv.org/abs/2610.22873v1
- **Security insight:** Modern large language model (LLM) systems reuse key-value (KV) caches to accelerate inference. Recent work has shown that reusing KV caches from reasoning traces can also improve task performance, similar to retrieval-augmented generation (RAG). We…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**The Model Knows Better: Defending Medical Multi-Agent Systems Against Prompt Injection**  
- **Date:** 2026-10-15
- **Authors:** Fardin Ahsan Sakib, Ziwei Zhu, Ozlem Uzuner
- **Link:** https://arxiv.org/abs/2610.22594v1
- **Security insight:** Medical multi-agent systems, in which LLM agents discuss a case, are increasingly studied for clinical decision support. Prompt injection, text that an attacker adds to a model's input, can manipulate LLMs into wrong decisions. How it affects these systems,…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**From Detection to Decision: Calibration and Deferral for Prompt-Injection Detection**  
- **Date:** 2026-10-14
- **Authors:** Qianlong Lan, Anuj Kaul, Vinothini Pandurangan et al.
- **Link:** https://arxiv.org/abs/2610.20907v1
- **Security insight:** Prompt-injection defenses are commonly evaluated as binary detectors, although deployed LLM applications must make operational decisions about whether to allow, block, or escalate potentially malicious inputs. Recent probabilistic decision models aim to…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**INFUSE: A Unified Surface Benchmark for Indirect Prompt Injection in Agentic Systems**  
- **Date:** 2026-10-14
- **Authors:** Thuy Dung Nguyen, Jingyi Guo, Rana Seda Dubauskas et al.
- **Link:** https://arxiv.org/abs/2610.20776v1
- **Security insight:** LLM-based agents increasingly execute long-horizon, end-to-end workflows involving shell commands, code modification, dependency installation, and interaction with remote services. This growing autonomy expands their exposure to indirect prompt injection…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Are You Reading the Right Thing? Rethinking Internal Signals for Prompt-Injection Detection**  
- **Date:** 2026-10-14
- **Authors:** Sarthak Gupta, Priyanka Tembey
- **Link:** https://arxiv.org/abs/2610.19452v1
- **Security insight:** Several recent studies propose detecting prompt injections from a language model's internal state. However, these methods do not measure a single security property. Residual-stream probes, attention scores, role projections, exposure probes, and concept…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**AgentSafeEvo: Adversarial Co-Evolution for LLM Agent Safety**  
- **Date:** 2026-10-14
- **Authors:** Chenxu Wang, Xiaoyu Wen, Han Qi et al.
- **Link:** https://arxiv.org/abs/2610.19422v1
- **Security insight:** Large language model (LLM) agents accomplish complex tasks through multi-turn interactions with external tools. However, malicious content embedded in user queries, tool descriptions, or environment observations can manipulate their decisions and induce…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Policy-Verified Self-Training: Learning Agent Compliance from Verifiable Policy Rewards**  
- **Date:** 2026-10-14
- **Authors:** Min-Young Yu
- **Link:** https://arxiv.org/abs/2610.19372v1
- **Security insight:** Runtime policy verifiers can prevent agents from executing disallowed actions, but their decisions are typically used only for enforcement and discarded afterward. We ask whether these decisions can instead become verifiable policy rewards for training the…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### Poisoning & Backdoors

**SAFETYEDIT: Sparse Internal Targets with Prompt-Wide Control for LLM Jailbreak Backdoors**  
- **Date:** 2026-10-15
- **Authors:** Yutong Ke, Yansu Wang, Zeyu Zhang et al.
- **Link:** https://arxiv.org/abs/2610.22640v1
- **Security insight:** Model-editing backdoors aim to induce harmful responses under a trigger while preserving ordinary behavior on untriggered input. Recent model-editing approaches target affirmative response prefixes through rank-one updates to a small subset of model weights.…
- **Build idea:** Build a minimal poisoning simulator plus simple detectors (trigger search, label flip tests, anomaly baselines).

### Adversarial ML

**Identify, Classify, Act: Per-Instruction Controlled Compliance for LLMs over External Data**  
- **Date:** 2026-10-16
- **Authors:** Zesheng Shi, Xue Li, Chenrui Dai et al.
- **Link:** https://arxiv.org/abs/2610.22874v1
- **Security insight:** LLMs over external data face a per-instruction tension: a single document or tool return often interleaves legitimate directives with adversarial prompt injections, and the model must follow the former while rejecting the latter. Existing defenses suppress or…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

**Can Autonomous Vehicles Keep Their Cool? A Survey of Thermal Side-Channel and Perception Attacks**  
- **Date:** 2026-10-15
- **Authors:** Harsh Aaryan, Ce Zhou
- **Link:** https://arxiv.org/abs/2610.21034v1
- **Security insight:** Autonomous vehicles (AVs) couple safety-critical perception to thermally constrained compute. Interfaces built for night perception and package thermal reliability were never engineered as confidentiality boundaries, and closing one such path leaves the other…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

### Agent & Tool Security

**When Approval Becomes Execution: Authorization-Grounded Workflow Attacks on Tool-Using Agents**  
- **Date:** 2026-10-16
- **Authors:** Chenggong Shi, Hongmei Mou
- **Link:** https://arxiv.org/abs/2610.23077v1
- **Security insight:** Tool-using language-model agents increasingly rely on local services for document access, approval management, and enterprise workflow execution. This paper studies an authorization-grounded workflow attack in the OpenClaw Agent Security Attack Competition, a…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.
