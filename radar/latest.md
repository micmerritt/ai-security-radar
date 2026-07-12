# AI Security Radar

_Last updated (UTC): **2026-07-12**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Multi-Agent Firewall Architecture for Privacy Protection of Sensitive Data in Interactions with Language Models**  
- **Date:** 2026-07-09
- **Authors:** Hugo García Cuesta, Pablo Mateo Torrejón, Alfonso Sánchez-Macián
- **Link:** https://arxiv.org/abs/2607.08282v1
- **Security insight:** While Large Language Models (LLMs) have become essential productivity tools, their integration into workflows without adequate safeguards creates significant risks. This paper proposes an open-source, privacy-focused, user-facing firewall designed to secure…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Prismata: Confining Cross-Site Prompt Injection in Web Agents**  
- **Date:** 2026-07-09
- **Authors:** Corban Villa, Alp Eren Ozdarendeli, Sijun Tan et al.
- **Link:** https://arxiv.org/abs/2607.08147v1
- **Security insight:** Autonomous web agents promise to automate everyday browsing tasks, but inherit one of the web's oldest attack surfaces. Cross-Site Scripting proved that mixing trusted and untrusted content is dangerous, even on benign pages. Agents resurface this risk by…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Beware of Agentic Botnets: Scalable Untargeted Promptware Attacks via Universal and Transferable Adversarial HalluSquatting**  
- **Date:** 2026-07-08
- **Authors:** Aya Spira, Stav Cohen, Elad Feldman et al.
- **Link:** https://arxiv.org/abs/2607.07433v1
- **Security insight:** The growing adoption of agentic LLM applications has introduced a new threat previously named as promptware. While prior work has established that adversaries can exploit direct channels to LLM applications to apply promptware under weak threat models, many…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Untrusted Content Masking for Web Agents with Security Guarantees**  
- **Date:** 2026-07-06
- **Authors:** Kristina Nikolić, Egor Zverev, Javier Rando et al.
- **Link:** https://arxiv.org/abs/2607.05277v1
- **Security insight:** Defenses that provide security guarantees against prompt injection attacks rely on strict isolation between trusted instructions and untrusted data. In text-based environments such as tool-use APIs, this separation arises naturally: agents can reason from…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Agent Data Injection Attacks are Realistic Threats to AI Agents**  
- **Date:** 2026-07-06
- **Authors:** Woohyuk Choi, Juhee Kim, Taehyun Kang et al.
- **Link:** https://arxiv.org/abs/2607.05120v1
- **Security insight:** AI agents act on behalf of user prompts, consuming external data and taking actions based on the agent context. Prior research on AI agent security has primarily focused on indirect prompt injection (IPI). Its most well-studied category is instruction…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Biological Motifs for Agentic Control**  
- **Date:** 2026-07-05
- **Authors:** Bogdan Banu
- **Link:** https://arxiv.org/abs/2607.04240v1
- **Security insight:** The transition of Large Language Models (LLMs) from passive generators to autonomous agents has introduced significant challenges in reliability, security, and state management. Current agentic architectures are often constructed ad-hoc, prone to…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**DualView: Preventing Indirect Prompt Injection in Personal AI Agents**  
- **Date:** 2026-07-04
- **Authors:** Juhee Kim, Woohyuk Choi, Taehyun Kang et al.
- **Link:** https://arxiv.org/abs/2607.03821v1
- **Security insight:** Personal AI agents that run on the user's local machine, such as OpenClaw, automate daily tasks including web search, email, and file management. Their access to computer resources, including the network, file system, and shell, exposes them to indirect…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Distributed Attacks in Persistent-State AI Control**  
- **Date:** 2026-07-02
- **Authors:** Josh Hills, Ida Caspary, Asa Cooper Stickland
- **Link:** https://arxiv.org/abs/2607.02514v2
- **Security insight:** As AI coding agents become more autonomous, they increasingly ship code iteratively, with the codebase persisting across sessions. This persistence creates a new attack surface: a misaligned or prompt-injected agent can distribute attacks across pull requests…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### RAG & Retrieval Attacks

**FedMark-FM: Auditable, Risk-Adjusted Data Markets for Federated Foundation-Model Adaptation**  
- **Date:** 2026-07-08
- **Authors:** Phat T. Tran-Truong, Xuan-Bach Le, Minh Nhat Nguyen
- **Link:** https://arxiv.org/abs/2607.07529v1
- **Security insight:** Federated foundation-model adaptation increasingly relies on heterogeneous private artifacts (retrieval corpora, prompts and demonstrations, LoRA adapters, preference and safety data, and update sketches), yet existing federated-learning incentive mechanisms…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Poisoning & Backdoors

**Builder, Defender, Breaker: The Case Against Removing the Human from the AI-Driven Security Lifecycle**  
- **Date:** 2026-07-03
- **Authors:** Mohamed Chahine Ghanem
- **Link:** https://arxiv.org/abs/2607.03215v1
- **Security insight:** Artificial intelligence has spread across the whole of the security lifecycle. The same family of models now writes application code, hardens it, and probes it for weaknesses, so that a single generative substrate increasingly performs all three roles at…
- **Build idea:** Build a minimal poisoning simulator plus simple detectors (trigger search, label flip tests, anomaly baselines).

### Adversarial ML

**Mechanistic Interpretability of LLM Jailbreaks via Internal Attribution Graphs**  
- **Date:** 2026-07-08
- **Authors:** Anupam Wagle, Ifrat Ikhtear Uddin, Chaowei Zhang et al.
- **Link:** https://arxiv.org/abs/2607.07903v1
- **Security insight:** Large language models (LLMs) exhibit remarkable capabilities but remain highly vulnerable to adversarial prompts and jailbreak attacks. Existing approaches primarily analyze these failures through input-output behaviors or attribution methods, offering…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

**Simulating the LOcal Web (SLOW): VII. Intergalactic magnetic field models for multi-messenger applications**  
- **Date:** 2026-07-07
- **Authors:** Johannes Stoiber, Klaus Dolag, Francesca Capel et al.
- **Link:** https://arxiv.org/abs/2607.06665v1
- **Security insight:** Context. The propagation of ultra-high-energy cosmic rays (UHECRs) and ultra-high-energy gamma-rays remains an open question in astroparticle physics, with the intergalactic magnetic field (IGMF) playing a crucial role in deflecting charged particles and…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.
