# AI Security Radar

_Last updated (UTC): **2026-11-02**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

**SecPO: Principled Adversarial Training for Prompt Injection Security**  
- **Date:** 2026-10-30
- **Authors:** Sizhe Chen, Yibo Peng, Jaewon Chang et al.
- **Link:** https://arxiv.org/abs/2610.41998v1
- **Security insight:** Recognized as a top threat to AI agents, prompt injection allows instructions from untrusted data (email, documents, websites) to manipulate the agent's operation. The existing best-defended LLM, Meta-SecAlign, is trained with the DPO loss but still suffers…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Erase the Injected Region: Multimodal Prompt-Injection Defense with On-Policy Self-Distillation**  
- **Date:** 2026-10-30
- **Authors:** Shuo Hong, Jiaxin Ma, Xidi Cai et al.
- **Link:** https://arxiv.org/abs/2610.41307v1
- **Security insight:** Multimodal indirect prompt injection embeds malicious instructions in external media that also contains information needed for the user's task. Existing defenses can block the attack yet impair the model's use of that information, leaving a gap between attack…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**AgentShield: Fortifying Web Applications Against AI Agents and Agentic Browsers**  
- **Date:** 2026-10-30
- **Authors:** Moiz Ali, Nafis Karim, Rownak Islam et al.
- **Link:** https://arxiv.org/abs/2610.41181v1
- **Security insight:** LLM-powered browser agents are transforming web automation by autonomously interacting with websites and executing complex workflows. However, the effectiveness of existing anti-bot defenses against these systems remains unclear. We present a systematic…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**LanG 2.0: Energy-Efficient Agentic AI for Semi-Automated Security Operations at Scale**  
- **Date:** 2026-10-29
- **Authors:** Anes Abdennebi, Nadjia Kara, Laaziz Lahlou et al.
- **Link:** https://arxiv.org/abs/2610.41072v1
- **Security insight:** Security operations centers (SOCs) need to turn terabytes of alerts, logs and flows into trusted, affordable decisions to unveil hidden threats. We present LanG 2.0, an agentic system that detects threats, correlates evidence and writes rules, investigating…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**CLIC: Closed-Loop Intent Consistency for Securing LLM-Driven Control in Open RAN**  
- **Date:** 2026-10-29
- **Authors:** Sunder Ali Khowaja, Kapal Dev, Joongheon Kim et al.
- **Link:** https://arxiv.org/abs/2610.40744v1
- **Security insight:** With the progressive capabilities of large language models (LLMs), researchers are finding ways to integrate them into the control loops of Open Radio Access Network (O-RAN) to enable slicing and resource management through user intents. However, integration…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**SEAL: Sealed Queries for Local Sanitization against Indirect Prompt Injection**  
- **Date:** 2026-10-29
- **Authors:** Doohyun Kim, Donghwa Kang, Mingyu Jun et al.
- **Link:** https://arxiv.org/abs/2610.39758v1
- **Security insight:** Indirect prompt injection threatens local LLM agents through untrusted tool outputs, motivating defenses that suppress attacks while preserving task evidence under limited inference budgets. We introduce SEAL, which learns a soft prompt and scoring readout…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**REALM: Identifying Minimal Task Assets for LLM Agents**  
- **Date:** 2026-10-29
- **Authors:** Zihou Ren, Byungchul Tak, Long Wang
- **Link:** https://arxiv.org/abs/2610.39155v1
- **Security insight:** Large language model (LLM) agents often receive access to more files, accounts, and services than a task requires. Prompt injection turns this excess access into an opportunity to redirect execution toward unrelated resources. Applying least privilege…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Appreciation Teaches Unauthorized Execution: Self-Evolution Degrades the Robustness of Personal Agents to Indirect Prompt Injection**  
- **Date:** 2026-10-29
- **Authors:** Xinyan Wang, Xiaogeng Liu, Jun Shao et al.
- **Link:** https://arxiv.org/abs/2610.39122v1
- **Security insight:** Self-evolving personal agents act for users and learn from user feedback. However, if an agent obeys an instruction that an untrusted third party hides in content, the third party gains control of the agent. Such indirect prompt injection (IPI) poses severe…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Where You Inject Matters: The Trust Region Effect in LLM Agents**  
- **Date:** 2026-10-28
- **Authors:** Chengquan Guo, Xiaodong Liu, Weiwei Yang et al.
- **Link:** https://arxiv.org/abs/2610.38867v1
- **Security insight:** LLM agents are increasingly adopted in long-horizon tasks and interact with diverse external environments. Despite their growing capabilities, these agents remain vulnerable to real-world attacks such as indirect prompt injections, which manipulate agents…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**Prevented is Not Protected: What Attack Success Rate Hides about RAG**  
- **Date:** 2026-10-29
- **Authors:** Chahana Dahal, Zuobin Xiong
- **Link:** https://arxiv.org/abs/2610.40742v1
- **Security insight:** Retrieval-Augmented Generation (RAG) is vulnerable to knowledge poisoning, where adversaries manipulate retrieved evidence to influence model outputs. Existing defenses are primarily evaluated using attack success rate (ASR), which obscures defense-induced…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Poisoning & Backdoors

**Trustworthy Distributed Machine Learning in Cloud-Edge-IoT Systems: A Heterogeneity-Aware Survey of Security, Privacy, and Robustness**  
- **Date:** 2026-10-28
- **Authors:** Long Dang, Ali Alfatemi, Kaiqi Xiong et al.
- **Link:** https://arxiv.org/abs/2610.38793v1
- **Security insight:** Distributed machine learning (DML), including conventional distributed training and federated learning (FL), enables collaborative model development across cloud-edge-IoT systems without fully centralizing raw data. However, distributing data, computation,…
- **Build idea:** Build a minimal poisoning simulator plus simple detectors (trigger search, label flip tests, anomaly baselines).

### Model Extraction & Privacy

**From 1D Benchmarks to Complex 3D Geometries: Can Agents Reliably Specify Problems for Automated PDE Simulation?**  
- **Date:** 2026-10-30
- **Authors:** Akshat Jani, Sakhinana Sagar Srinivas, Venkataramana Runkana
- **Link:** https://arxiv.org/abs/2610.41267v1
- **Security insight:** Turning an engineering request into a simulation requires consistent geometry, physics, boundary conditions, and numerical settings. Recent agent-assisted systems automate simulation setup, but successful execution alone does not establish whether the…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

### Adversarial ML

**Understanding and Mitigating Role Spoofing in LLMs**  
- **Date:** 2026-10-29
- **Authors:** Ezra Edelman, Benjamin Edelman, Surbhi Goel et al.
- **Link:** https://arxiv.org/abs/2610.40396v1
- **Security insight:** Despite growing capabilities, LLMs remain susceptible to prompt injections: malicious inputs that can manipulate or hijack models. In particular, it has recently been observed that LLMs can exhibit role confusion (Ye et al., 2026), where models attribute the…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

**FlipJev: Fast Black-Box Red Teaming Finds Universal Adversarial Suffixes for Typed Decision Models**  
- **Date:** 2026-10-28
- **Authors:** Xiaogeng Liu, Xinyan Wang, Chaowei Xiao
- **Link:** https://arxiv.org/abs/2610.38895v1
- **Security insight:** Typed decision models are an emerging class of language models that make decisions instead of generating free-text responses. They answer in a single fast and cheap query and are increasingly used, including in security-sensitive tasks. However, red teaming…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.
