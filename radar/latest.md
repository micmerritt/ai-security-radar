# AI Security Radar

_Last updated (UTC): **2026-07-14**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Distributed Denial of Science: How Indirect Data Poisoning of AI Systems Can Industrialize Scientific Fraud**  
- **Date:** 2026-07-12
- **Authors:** Bálint Gyevnár, Atoosa Kasirzadeh, Nihar B. Shah
- **Link:** https://arxiv.org/abs/2607.10712v1
- **Security insight:** Scientific fraud is the instrument of doubt that malicious entities can use to establish controversy in science. Historically, it required the resources of a company: deep pockets, ghostwritten articles, and corrupt academics. Today, Artificial Intelligence…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**NetInjectBench: Benchmarking Indirect Prompt Injection in Tool-Using Large Language Model Agents for Network Operations**  
- **Date:** 2026-07-11
- **Authors:** Ruksat Khan Shayoni, Muhammad Faraz Shoaib, S M Asif Hossain et al.
- **Link:** https://arxiv.org/abs/2607.10490v1
- **Security insight:** Tool-using large language model (LLM) agents are attractive for network operations, but tickets, alerts, logs, runbooks, and ChatOps messages can carry indirect prompt injections. We present NetInjectBench, a 130-scenario benchmark that separates untrusted…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

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

### Prompt Injection

**Devil in the Lens: Analyzing and Defending Physical Prompt Injection Against Vision-Language Models on Wearable Devices**  
- **Date:** 2026-07-11
- **Authors:** Yaxin Li, Hao Wang, Yanda Shao et al.
- **Link:** https://arxiv.org/abs/2607.10269v1
- **Security insight:** Vision-Language Models (VLMs) are rapidly deployed on human-facing wearable devices such as smart glasses to enable multimodal perception and AI-assisted decision-making. While prior research has demonstrated the risks of visual prompt injection into digital…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**The Effect of Multi-Lingual and Keyword Adversarial Injection on LLM Relevance Judgment**  
- **Date:** 2026-07-11
- **Authors:** Nguyen Khoi Vo, Duy Duong Tuong, Oleg Zendel et al.
- **Link:** https://arxiv.org/abs/2607.10080v1
- **Security insight:** Large language models (LLMs) are increasingly being used as automated judges for relevance evaluation in information retrieval, yet their robustness to adversarial manipulation remains insufficiently understood, particularly in multilingual settings. In this…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**"Code Is Cheap. Show Me the Talk.": Lessons from Teaching and Managing AI Coding Tool Usage in a Visualization Course**  
- **Date:** 2026-07-10
- **Authors:** Zhongzheng Xu, Taehyun Yang, Fumeng Yang
- **Link:** https://arxiv.org/abs/2607.09938v1
- **Security insight:** Generative Artificial Intelligence (GenAI) coding tools are transforming visualization education. They can assist with implementation and design, but they can also let students bypass intended learning trajectories. In this paper, we share our retrospective…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**MJ: Multi-turn LLM Jailbreaking via Decomposed Credit Assignment**  
- **Date:** 2026-07-13
- **Authors:** Junyoung Park, Namgyu Park, Sechan Lee et al.
- **Link:** https://arxiv.org/abs/2607.11070v1
- **Security insight:** Modern large language models (LLMs) operate in interactive multi-turn settings, making multi-turn jailbreaking a realistic threat model and an important setting for automated red teaming. A core challenge in learning multi-turn jailbreak attackers is credit…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**FedMark-FM: Auditable, Risk-Adjusted Data Markets for Federated Foundation-Model Adaptation**  
- **Date:** 2026-07-08
- **Authors:** Phat T. Tran-Truong, Xuan-Bach Le, Minh Nhat Nguyen
- **Link:** https://arxiv.org/abs/2607.07529v1
- **Security insight:** Federated foundation-model adaptation increasingly relies on heterogeneous private artifacts (retrieval corpora, prompts and demonstrations, LoRA adapters, preference and safety data, and update sketches), yet existing federated-learning incentive mechanisms…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

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

### Other (Review)

**Which Neurons Detect Malicious Code? A Probing Study of LLM Security Knowledge**  
- **Date:** 2026-07-11
- **Authors:** Lam D. Dao, Vang T. Nguyen, Anh M. T. Bui et al.
- **Link:** https://arxiv.org/abs/2607.10221v1
- **Security insight:** Background. Large language models (LLMs) have become increasingly capable of understanding and generating source code, leading to their widespread adoption in software engineering tasks such as code completion, repair, and vulnerability detection. However,…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
