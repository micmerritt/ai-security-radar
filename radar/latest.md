# AI Security Radar

_Last updated (UTC): **2026-10-31**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

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

**Post-Training Large Language Models with LLMON**  
- **Date:** 2026-10-28
- **Authors:** Basel Shbita, Michael Hind, Chad DeLuca et al.
- **Link:** https://arxiv.org/abs/2610.38120v1
- **Security insight:** Large Language Models (LLMs) treat all context tokens uniformly, lacking explicit separation between executable instructions and passive data. This leads to prompt injection vulnerabilities, ambiguous instruction binding, and unreliable execution control. We…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Heads of Security: Learned Attention Gates Improve Prompt Injection Robustness**  
- **Date:** 2026-10-27
- **Authors:** Igor Shilov, Xiaoxue Yang, Alexander Panfilov et al.
- **Link:** https://arxiv.org/abs/2610.37657v1
- **Security insight:** We introduce Heads of Security (HoS), a prompt injection defense that enforces instruction-data separation via a small set of learned per-head attention gates. HoS learns how each head should redistribute attention between trusted and untrusted tokens,…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### Poisoning & Backdoors

**Trustworthy Distributed Machine Learning in Cloud-Edge-IoT Systems: A Heterogeneity-Aware Survey of Security, Privacy, and Robustness**  
- **Date:** 2026-10-28
- **Authors:** Long Dang, Ali Alfatemi, Kaiqi Xiong et al.
- **Link:** https://arxiv.org/abs/2610.38793v1
- **Security insight:** Distributed machine learning (DML), including conventional distributed training and federated learning (FL), enables collaborative model development across cloud-edge-IoT systems without fully centralizing raw data. However, distributing data, computation,…
- **Build idea:** Build a minimal poisoning simulator plus simple detectors (trigger search, label flip tests, anomaly baselines).

### Model Extraction & Privacy

**PrivacyEvalClaw: A Tool-Augmented Deliberative Agent for Auditing Privacy Leakage in LLM Jailbreak Responses**  
- **Date:** 2026-10-27
- **Authors:** Krishna Kanth Nakka, Yujun Wang, Shijie Zhou et al.
- **Link:** https://arxiv.org/abs/2610.36711v1
- **Security insight:** Reliable evaluation is a critical bottleneck in privacy red-teaming of large language models (LLMs): determining whether a jailbreak response actually reveals personal information can be difficult when disclosures are indirect, contextual, partial, or…
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

**Rethinking LLM Jailbreak Evaluation: Continuous Risk Landscapes Beyond Binary Outcomes**  
- **Date:** 2026-10-28
- **Authors:** Yukai Zhou, Wenjie Wang
- **Link:** https://arxiv.org/abs/2610.38595v1
- **Security insight:** A binary success indicator is a natural representation for discriminative tasks such as image classification under adversarial perturbations, where each input is mapped to a single prediction. However, generative tasks are fundamentally different: an LLM…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

**Uncovering Why LLMs Fail: From Internal Mechanisms to Adversarial Reasoning Trajectories**  
- **Date:** 2026-10-27
- **Authors:** Zirui Ding, Xinxin Fan, Hao Yuan et al.
- **Link:** https://arxiv.org/abs/2610.37369v2
- **Security insight:** Large language models (LLMs) are usually evaluated by final-output correctness or safety, yet an endpoint label does not reveal how a failure develops throughout the reasoning process. We therefore ask whether ordinary reasoning failures and adversarially…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

### Other (Review)

**What Victims Take Away: Attack Reuse and Defense Revision after Prompt-Injection Attacks**  
- **Date:** 2026-10-27
- **Authors:** Zihan Chen, Lei Nico Zheng, Di Zhu
- **Link:** https://arxiv.org/abs/2610.36422v1
- **Security insight:** Attack logs and red-team reports show targets the attacks used against them, to help them repair their defenses. Prompt injections against large language models (LLMs) are plain text, so such records also hand targets a working copy. Drawing on social…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.

**SpecGuard: Detecting Multi-Turn LLM Jailbreaks via Specification-Based Runtime Monitoring**  
- **Date:** 2026-10-26
- **Authors:** Junle Li, Siqi Chen, Jiakai Li et al.
- **Link:** https://arxiv.org/abs/2610.36258v1
- **Security insight:** Multi-turn jailbreaks turn dialogue safety into a trace property: a violation may become identifiable only when user intent and assistant behavior are considered across multiple turns. Existing guard models largely classify individual messages or exchanges…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
