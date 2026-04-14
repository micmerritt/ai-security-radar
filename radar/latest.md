# AI Security Radar

_Last updated (UTC): **2026-04-14**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Detecting Safety Violations Across Many Agent Traces**  
- **Date:** 2026-04-13
- **Authors:** Adam Stein, Davis Brown, Hamed Hassani et al.
- **Link:** https://arxiv.org/abs/2604.11806v1
- **Security insight:** To identify safety violations, auditors often search over large sets of agent traces. This search is difficult because failures are often rare, complex, and sometimes even adversarially hidden and only detectable when multiple traces are analyzed together.…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**ClawGuard: A Runtime Security Framework for Tool-Augmented LLM Agents Against Indirect Prompt Injection**  
- **Date:** 2026-04-13
- **Authors:** Wei Zhao, Zhe Li, Peixin Zhang et al.
- **Link:** https://arxiv.org/abs/2604.11790v1
- **Security insight:** Tool-augmented Large Language Model (LLM) agents have demonstrated impressive capabilities in automating complex, multi-step real-world tasks, yet remain vulnerable to indirect prompt injection. Adversaries exploit this weakness by embedding malicious…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**The Blind Spot of Agent Safety: How Benign User Instructions Expose Critical Vulnerabilities in Computer-Use Agents**  
- **Date:** 2026-04-12
- **Authors:** Xuwei Ding, Skylar Zhai, Linxin Song et al.
- **Link:** https://arxiv.org/abs/2604.10577v1
- **Security insight:** Computer-use agents (CUAs) can now autonomously complete complex tasks in real digital environments, but when misled, they can also be used to automate harmful actions programmatically. Existing safety evaluations largely target explicit threats such as…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**STARS: Skill-Triggered Audit for Request-Conditioned Invocation Safety in Agent Systems**  
- **Date:** 2026-04-11
- **Authors:** Guijia Zhang, Shu Yang, Xilin Gong et al.
- **Link:** https://arxiv.org/abs/2604.10286v1
- **Security insight:** Autonomous language-model agents increasingly rely on installable skills and tools to complete user tasks. Static skill auditing can expose capability surface before deployment, but it cannot determine whether a particular invocation is unsafe under the…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**PlanGuard: Defending Agents against Indirect Prompt Injection via Planning-based Consistency Verification**  
- **Date:** 2026-04-11
- **Authors:** Guangyu Gong, Zizhuang Deng
- **Link:** https://arxiv.org/abs/2604.10134v1
- **Security insight:** Large Language Model (LLM) agents are increasingly integrated into critical systems, leveraging external tools to interact with the real world. However, this capability exposes them to Indirect Prompt Injection (IPI), where attackers embed malicious…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**BadSkill: Backdoor Attacks on Agent Skills via Model-in-Skill Poisoning**  
- **Date:** 2026-04-10
- **Authors:** Guiyao Tie, Jiawen Shi, Pan Zhou et al.
- **Link:** https://arxiv.org/abs/2604.09378v1
- **Security insight:** Agent ecosystems increasingly rely on installable skills to extend functionality, and some skills bundle learned model artifacts as part of their execution logic. This creates a supply-chain risk that is not captured by prompt injection or ordinary plugin…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Are GUI Agents Focused Enough? Automated Distraction via Semantic-level UI Element Injection**  
- **Date:** 2026-04-09
- **Authors:** Wenkui Yang, Chao Jin, Haisu Zhu et al.
- **Link:** https://arxiv.org/abs/2604.07831v1
- **Security insight:** Existing red-teaming studies on GUI agents have important limitations. Adversarial perturbations typically require white-box access, which is unavailable for commercial systems, while prompt injection is increasingly mitigated by stronger safety alignment. To…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**TraceSafe: A Systematic Assessment of LLM Guardrails on Multi-Step Tool-Calling Trajectories**  
- **Date:** 2026-04-08
- **Authors:** Yen-Shan Chen, Sian-Yao Huang, Cheng-Lin Yang et al.
- **Link:** https://arxiv.org/abs/2604.07223v1
- **Security insight:** As large language models (LLMs) evolve from static chatbots into autonomous agents, the primary vulnerability surface shifts from final outputs to intermediate execution traces. While safety guardrails are well-benchmarked for natural language responses,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Leave My Images Alone: Preventing Multi-Modal Large Language Models from Analyzing Images via Visual Prompt Injection**  
- **Date:** 2026-04-10
- **Authors:** Zedian Shao, Hongbin Liu, Yuepeng Hu et al.
- **Link:** https://arxiv.org/abs/2604.09024v1
- **Security insight:** Multi-modal large language models (MLLMs) have emerged as powerful tools for analyzing Internet-scale image data, offering significant benefits but also raising critical safety and societal concerns. In particular, open-weight MLLMs may be misused to extract…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**PIArena: A Platform for Prompt Injection Evaluation**  
- **Date:** 2026-04-09
- **Authors:** Runpeng Geng, Chenlong Yin, Yanting Wang et al.
- **Link:** https://arxiv.org/abs/2604.08499v1
- **Security insight:** Prompt injection attacks pose serious security risks across a wide range of real-world applications. While receiving increasing attention, the community faces a critical gap: the lack of a unified platform for prompt injection evaluation. This makes it…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Security Concerns in Generative AI Coding Assistants: Insights from Online Discussions on GitHub Copilot**  
- **Date:** 2026-04-09
- **Authors:** Nicolás E. Díaz Ferreyra, Monika Swetha Gurupathi, Zadia Codabux et al.
- **Link:** https://arxiv.org/abs/2604.08352v1
- **Security insight:** Generative Artificial Intelligence (GenAI) has become a central component of many development tools (e.g., GitHub Copilot) that support software practitioners across multiple programming tasks, including code completion, documentation, and bug detection.…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**RECIPER: A Dual-View Retrieval Pipeline for Procedure-Oriented Materials Question Answering**  
- **Date:** 2026-04-13
- **Authors:** Zhuoyu Wu, Wenhui Ou, Pei-Sze Tan et al.
- **Link:** https://arxiv.org/abs/2604.11229v1
- **Security insight:** Retrieving procedure-oriented evidence from materials science papers is difficult because key synthesis details are often scattered across long, context-heavy documents and are not well captured by paragraph-only dense retrieval. We present RECIPER, a dual-…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**TRUSTDESC: Preventing Tool Poisoning in LLM Applications via Trusted Description Generation**  
- **Date:** 2026-04-08
- **Authors:** Hengkai Ye, Zhechang Zhang, Jinyuan Jia et al.
- **Link:** https://arxiv.org/abs/2604.07536v1
- **Security insight:** Large language models (LLMs) increasingly rely on external tools to perform time-sensitive tasks and real-world actions. While tool integration expands LLM capabilities, it also introduces a new prompt-injection attack surface: tool poisoning attacks (TPAs).…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Adversarial ML

**The Salami Slicing Threat: Exploiting Cumulative Risks in LLM Systems**  
- **Date:** 2026-04-13
- **Authors:** Yihao Zhang, Kai Wang, Jiangrong Wu et al.
- **Link:** https://arxiv.org/abs/2604.11309v1
- **Security insight:** Large Language Models (LLMs) face prominent security risks from jailbreaking, a practice that manipulates models to bypass built-in security constraints and generate unethical or unsafe content. Among various jailbreak techniques, multi-turn jailbreak attacks…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.
