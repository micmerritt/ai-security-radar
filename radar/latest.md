# AI Security Radar

_Last updated (UTC): **2026-03-17**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**PISmith: Reinforcement Learning-based Red Teaming for Prompt Injection Defenses**  
- **Date:** 2026-03-13
- **Authors:** Chenlong Yin, Runpeng Geng, Yanting Wang et al.
- **Link:** https://arxiv.org/abs/2603.13026v1
- **Security insight:** Prompt injection poses serious security risks to real-world LLM applications, particularly autonomous agents. Although many defenses have been proposed, their robustness against adaptive attacks remains insufficiently evaluated, potentially creating a false…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Uncovering Security Threats and Architecting Defenses in Autonomous Agents: A Case Study of OpenClaw**  
- **Date:** 2026-03-13
- **Authors:** Zonghao Ying, Xiao Yang, Siyang Wu et al.
- **Link:** https://arxiv.org/abs/2603.12644v1
- **Security insight:** The rapid evolution of Large Language Models (LLMs) into autonomous, tool-calling agents has fundamentally altered the cybersecurity landscape. Frameworks like OpenClaw grant AI systems operating-system-level permissions and the autonomy to execute complex…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Agent Privilege Separation in OpenClaw: A Structural Defense Against Prompt Injection**  
- **Date:** 2026-03-13
- **Authors:** Darren Cheng, Wen-Kwang Tsao
- **Link:** https://arxiv.org/abs/2603.13424v1
- **Security insight:** Prompt injection remains one of the most practical attack vectors against LLM-integrated applications. We replicate the Microsoft LLMail-Inject benchmark (Greshake et al., 2024) against current generation models running inside OpenClaw, an open source…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Security Considerations for Artificial Intelligence Agents**  
- **Date:** 2026-03-12
- **Authors:** Ninghui Li, Kaiyuan Zhang, Kyle Polley et al.
- **Link:** https://arxiv.org/abs/2603.12230v1
- **Security insight:** This article, a lightly adapted version of Perplexity's response to NIST/CAISI Request for Information 2025-0035, details our observations and recommendations concerning the security of frontier AI agents. These insights are informed by Perplexity's…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Cascade: Composing Software-Hardware Attack Gadgets for Adversarial Threat Amplification in Compound AI Systems**  
- **Date:** 2026-03-12
- **Authors:** Sarbartha Banerjee, Prateek Sahu, Anjo Vahldiek-Oberwagner et al.
- **Link:** https://arxiv.org/abs/2603.12023v1
- **Security insight:** Rapid progress in generative AI has given rise to Compound AI systems - pipelines comprised of multiple large language models (LLM), software tools and database systems. Compound AI systems are constructed on a layered traditional software stack running on a…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**OpenClaw PRISM: A Zero-Fork, Defense-in-Depth Runtime Security Layer for Tool-Augmented LLM Agents**  
- **Date:** 2026-03-12
- **Authors:** Frank Li
- **Link:** https://arxiv.org/abs/2603.11853v1
- **Security insight:** Tool-augmented LLM agents introduce security risks that extend beyond user-input filtering, including indirect prompt injection through fetched content, unsafe tool execution, credential leakage, and tampering with local control files. We present OpenClaw…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Taming OpenClaw: Security Analysis and Mitigation of Autonomous LLM Agent Threats**  
- **Date:** 2026-03-12
- **Authors:** Xinhao Deng, Yixiang Zhang, Jiaqing Wu et al.
- **Link:** https://arxiv.org/abs/2603.11619v1
- **Security insight:** Autonomous Large Language Model (LLM) agents, exemplified by OpenClaw, demonstrate remarkable capabilities in executing complex, long-horizon tasks. However, their tightly coupled instant-messaging interaction paradigm and high-privilege execution…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Amplification Effects in Test-Time Reinforcement Learning: Safety and Reasoning Vulnerabilities**  
- **Date:** 2026-03-16
- **Authors:** Vanshaj Khattar, Md Rafi ur Rashid, Moumita Choudhury et al.
- **Link:** https://arxiv.org/abs/2603.15417v1
- **Security insight:** Test-time training (TTT) has recently emerged as a promising method to improve the reasoning abilities of large language models (LLMs), in which the model directly learns from test data without access to labels. However, this reliance on test data also makes…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**The Mirror Design Pattern: Strict Data Geometry over Model Scale for Prompt Injection Detection**  
- **Date:** 2026-03-12
- **Authors:** J Alex Corll
- **Link:** https://arxiv.org/abs/2603.11875v1
- **Security insight:** Prompt injection defenses are often framed as semantic understanding problems and delegated to increasingly large neural detectors. For the first screening layer, however, the requirements are different: the detector runs on every request and therefore must…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Jailbreak Scaling Laws for Large Language Models: Polynomial-Exponential Crossover**  
- **Date:** 2026-03-11
- **Authors:** Indranil Halder, Annesya Banerjee, Cengiz Pehlevan
- **Link:** https://arxiv.org/abs/2603.11331v1
- **Security insight:** Adversarial attacks can reliably steer safety-aligned large language models toward unsafe behavior. Empirically, we find that adversarial prompt-injection attacks can amplify attack success rate from the slow polynomial growth observed without injection to…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**Mechanistic Origin of Moral Indifference in Language Models**  
- **Date:** 2026-03-16
- **Authors:** Lingyu Li, Yan Teng, Yingchun Wang
- **Link:** https://arxiv.org/abs/2603.15615v1
- **Security insight:** Existing behavioral alignment techniques for Large Language Models (LLMs) often neglect the discrepancy between surface compliance and internal unaligned representations, leaving LLMs vulnerable to long-tail risks. More crucially, we posit that LLMs possess…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**TabKD: Tabular Knowledge Distillation through Interaction Diversity of Learned Feature Bins**  
- **Date:** 2026-03-16
- **Authors:** Shovon Niverd Pereira, Krishna Khadka, Yu Lei
- **Link:** https://arxiv.org/abs/2603.15481v1
- **Security insight:** Data-free knowledge distillation enables model compression without original training data, critical for privacy-sensitive tabular domains. However, existing methods does not perform well on tabular data because they do not explicitly address feature…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Adversarial ML

**Sirens' Whisper: Inaudible Near-Ultrasonic Jailbreaks of Speech-Driven LLMs**  
- **Date:** 2026-03-14
- **Authors:** Zijian Ling, Pingyi Hu, Xiuyong Gao et al.
- **Link:** https://arxiv.org/abs/2603.13847v1
- **Security insight:** Speech-driven large language models (LLMs) are increasingly accessed through speech interfaces, introducing new security risks via open acoustic channels. We present Sirens' Whisper (SWhisper), the first practical framework for covert prompt-based attacks…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

### Other (Review)

**When Scanners Lie: Evaluator Instability in LLM Red-Teaming**  
- **Date:** 2026-03-15
- **Authors:** Lidor Erez, Omer Hofman, Tamir Nizri et al.
- **Link:** https://arxiv.org/abs/2603.14633v1
- **Security insight:** Automated LLM vulnerability scanners are increasingly used to assess security risks by measuring different attack type success rates (ASR). Yet the validity of these measurements hinges on an often-overlooked component: the evaluator who determines whether an…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
