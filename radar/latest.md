# AI Security Radar

_Last updated (UTC): **2026-05-29**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Minimal Prompt Perturbations Lead to Code Vulnerabilities: Prompt Fragility and Hidden-State Signals in Coding LLMs**  
- **Date:** 2026-05-28
- **Authors:** Alexander Sternfeld, Andrei Kucharavy, Ljiljana Dolamic
- **Link:** https://arxiv.org/abs/2605.29737v1
- **Security insight:** LLM-based coding assistants are seeing rapid adoption, offering substantial gains in developer productivity. As organizations increasingly ship code these agents produce, the security of that code becomes critical. Prior work has shown that minor prompt…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**LACUNA: Safe Agents as Recursive Program Holes**  
- **Date:** 2026-05-27
- **Authors:** Yaoyu Zhao, Yichen Xu, Oliver Bračevac et al.
- **Link:** https://arxiv.org/abs/2605.28617v1
- **Security insight:** LLM agents increasingly act by writing code, yet a split persists between the runtime that drives the agent and the code the model writes. The runtime owns the loop, context, and control flow, and the model has little say over any of them. Letting model-…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Towards Demystifying and Repairing LLM-in-the-Loop Vulnerabilities**  
- **Date:** 2026-05-27
- **Authors:** Yujie Ma, Jialin Rong, Chenxi Yang et al.
- **Link:** https://arxiv.org/abs/2605.28893v1
- **Security insight:** Large Language Models(LLMs) have been actively integrated into modern software systems as critical components. LLM-in-the-loop vulnerabilities, where vulnerabilities are introduced by LLMs and their dependent downstream components, such as frameworks,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**MIRAGE: Context-Aware Prompt Injection against Mobile GUI Agents via User-Generated Content**  
- **Date:** 2026-05-27
- **Authors:** Ruoqi Guo, Yi Liu, Gelei Deng et al.
- **Link:** https://arxiv.org/abs/2605.28116v1
- **Security insight:** Mobile graphical user interface (GUI) agents driven by vision-language models (VLMs) perceive the screen as rendered pixels and choose actions from what they see, so they cannot reliably separate trusted interface elements from user-generated content. We…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Measuring Real-World Prompt Injection Attacks in LLM-based Resume Screening**  
- **Date:** 2026-05-27
- **Authors:** Mohan Zhang, Yuqi Jia, Zhen Tan et al.
- **Link:** https://arxiv.org/abs/2605.28999v1
- **Security insight:** LLMs are vulnerable to prompt injection attacks. However, this vulnerability has been primarily demonstrated conceptually in academic studies or through a few anecdotal case studies. Its prevalence and impact in real-world LLM-based applications are largely…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Mitigating Adaptive Attacks against Reasoning Models with Activation Consistency Training**  
- **Date:** 2026-05-27
- **Authors:** Avidan Shah, Jannik Brinkmann, Rico Angell
- **Link:** https://arxiv.org/abs/2605.28467v1
- **Security insight:** As LLMs gain stronger reasoning capabilities, their extended chain-of-thought introduces new degrees of complexity for defending against adversarial jailbreaks and prompt injection. We study consistency training, a family of fine-tuning objectives that…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Can It Reach the Generator? Investigating the Survival of Prompt-Injection Attacks in Realistic RAG Settings**  
- **Date:** 2026-05-27
- **Authors:** Yu Yin, Shuai Wang, Bevan Koopman et al.
- **Link:** https://arxiv.org/abs/2605.28017v2
- **Security insight:** Recent generative engine optimisation (GEO) research has shown that prompt-injection attacks can push a target product to the top of an LLM's recommendation list, with the strongest attacks reporting around $80\%$ success and raising serious security concerns…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Disentangling Adversarial Prompts: A Semantic-Graph Defense for Robust LLM Security**  
- **Date:** 2026-05-27
- **Authors:** Xiang Fang, Wanlong Fang
- **Link:** https://arxiv.org/abs/2605.27823v1
- **Security insight:** Large Language Models (LLMs) are increasingly vulnerable to adversarial prompts that exploit semantic ambiguities to bypass safety mechanisms, resulting in harmful or inappropriate outputs. Such attacks, including jailbreaking and prompt injection, pose…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Prompt Injection Detection is Regime-Dependent: A Deployment-Aware Evaluation with Interpretable Structural Signals**  
- **Date:** 2026-05-26
- **Authors:** Akindoyin Akinrele, Shreyank N Gowda
- **Link:** https://arxiv.org/abs/2605.26999v1
- **Security insight:** Prompt injection poses a critical threat to the safe deployment of large language models, yet existing detection approaches are typically evaluated under limited settings that do not reflect real-world operating constraints. In this work, we present a…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**Evolving Skill-Structured Attack Memory Enhances LLM Jailbreaking**  
- **Date:** 2026-05-28
- **Authors:** Junke Zhang, Jianwei Wang, Sishuo Chen et al.
- **Link:** https://arxiv.org/abs/2605.29237v1
- **Security insight:** Jailbreak attacks on large language models (LLMs) aim to induce LLMs to produce content that they are expected to refuse. Automated black-box jailbreak generation is especially important for safety evaluation, where the attacker observes only model outputs…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Poisoning & Backdoors

**Token-Level Generalization in LoRA Adapter Backdoors: Attack Characterization and Behavioral Detection**  
- **Date:** 2026-05-28
- **Authors:** Travis Lelle
- **Link:** https://arxiv.org/abs/2605.30189v1
- **Security insight:** We show that LoRA adapters, the dominant distribution format for fine-tuned LLMs, can be reliably backdoored through training data poisoning while preserving baseline task performance. On a Qwen 2.5 1.5B prompt-injection classifier, a small fraction of…
- **Build idea:** Build a minimal poisoning simulator plus simple detectors (trigger search, label flip tests, anomaly baselines).

**Backdoor Attacks on Fault Detection and Localization in Cyber-Physical Systems**  
- **Date:** 2026-05-26
- **Authors:** Abile Jean, Kuniyilh S
- **Link:** https://arxiv.org/abs/2605.27674v1
- **Security insight:** Cyber-Physical Systems (CPS) integrate sensing, communication, computation, and control to support critical infrastructure, including smart grids, industrial automation, and control systems. In the electrical utility domain, various controllers are used in…
- **Build idea:** Build a minimal poisoning simulator plus simple detectors (trigger search, label flip tests, anomaly baselines).

### Adversarial ML

**Quantum-Enhanced Adversarial Robustness in Artificial Intelligence**  
- **Date:** 2026-05-27
- **Authors:** Jaydip Sen
- **Link:** https://arxiv.org/abs/2605.28899v1
- **Security insight:** Artificial Intelligence has achieved remarkable success across diverse application domains. However, its vulnerability to adversarial attacks poses significant challenges to reliability, security, and trustworthiness. Adversarial machine learning demonstrates…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

### Other (Review)

**Dissecting the Black Box: Circuit-Level Analysis of LLM Vulnerability Detection**  
- **Date:** 2026-05-28
- **Authors:** Syafiq Al Atiiq, Chun Zhou, Christian Gehrmann
- **Link:** https://arxiv.org/abs/2605.29901v1
- **Security insight:** Large language models (LLMs) can detect software vulnerabilities, but how do they actually identify vulnerable code? We address this question using mechanistic interpretability; analyzing the internal computations of a neural network to understand its…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
