# AI Security Radar

_Last updated (UTC): **2026-04-15**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Reading Between the Pixels: Linking Text-Image Embedding Alignment to Typographic Attack Success on Vision-Language Models**  
- **Date:** 2026-04-14
- **Authors:** Ravikumar Balakrishnan, Sanket Mendapara, Ankit Garg
- **Link:** https://arxiv.org/abs/2604.12371v1
- **Security insight:** We study typographic prompt injection attacks on vision-language models (VLMs), where adversarial text is rendered as images to bypass safety mechanisms, posing a growing threat as VLMs serve as the perceptual backbone of autonomous agents, from browser…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**WebAgentGuard: A Reasoning-Driven Guard Model for Detecting Prompt Injection Attacks in Web Agents**  
- **Date:** 2026-04-14
- **Authors:** Yulin Chen, Tri Cao, Haoran Li et al.
- **Link:** https://arxiv.org/abs/2604.12284v1
- **Security insight:** Web agents powered by vision-language models (VLMs) enable autonomous interaction with web environments by perceiving and acting on both visual and textual webpage content to accomplish user-specified tasks. However, they are highly vulnerable to prompt…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

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

### Prompt Injection

**DeepSeek Robustness Against Semantic-Character Dual-Space Mutated Prompt Injection**  
- **Date:** 2026-04-14
- **Authors:** Junyu Ren, Xingjian Pan, Wensheng Gan et al.
- **Link:** https://arxiv.org/abs/2604.12548v1
- **Security insight:** Prompt injection has emerged as a critical security threat to large language models (LLMs), yet existing studies predominantly focus on single-dimensional attack strategies, such as semantic rewriting or character-level obfuscation, which fail to capture the…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**TEMPLATEFUZZ: Fine-Grained Chat Template Fuzzing for Jailbreaking and Red Teaming LLMs**  
- **Date:** 2026-04-14
- **Authors:** Qingchao Shen, Zibo Xiao, Lili Huang et al.
- **Link:** https://arxiv.org/abs/2604.12232v1
- **Security insight:** Large Language Models (LLMs) are increasingly deployed across diverse domains, yet their vulnerability to jailbreak attacks, where adversarial inputs bypass safety mechanisms to elicit harmful outputs, poses significant security risks. While prior work has…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Fully Homomorphic Encryption on Llama 3 model for privacy preserving LLM inference**  
- **Date:** 2026-04-14
- **Authors:** Anes Abdennebi, Nadjia Kara, Laaziz Lahlou
- **Link:** https://arxiv.org/abs/2604.12168v1
- **Security insight:** The applications of Generative Artificial Intelligence (GenAI) and their intersections with data-driven fields, such as healthcare, finance, transportation, and information security, have led to significant improvements in service efficiency and low latency.…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Leave My Images Alone: Preventing Multi-Modal Large Language Models from Analyzing Images via Visual Prompt Injection**  
- **Date:** 2026-04-10
- **Authors:** Zedian Shao, Hongbin Liu, Yuepeng Hu et al.
- **Link:** https://arxiv.org/abs/2604.09024v1
- **Security insight:** Multi-modal large language models (MLLMs) have emerged as powerful tools for analyzing Internet-scale image data, offering significant benefits but also raising critical safety and societal concerns. In particular, open-weight MLLMs may be misused to extract…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**RECIPER: A Dual-View Retrieval Pipeline for Procedure-Oriented Materials Question Answering**  
- **Date:** 2026-04-13
- **Authors:** Zhuoyu Wu, Wenhui Ou, Pei-Sze Tan et al.
- **Link:** https://arxiv.org/abs/2604.11229v1
- **Security insight:** Retrieving procedure-oriented evidence from materials science papers is difficult because key synthesis details are often scattered across long, context-heavy documents and are not well captured by paragraph-only dense retrieval. We present RECIPER, a dual-…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Adversarial ML

**The Salami Slicing Threat: Exploiting Cumulative Risks in LLM Systems**  
- **Date:** 2026-04-13
- **Authors:** Yihao Zhang, Kai Wang, Jiangrong Wu et al.
- **Link:** https://arxiv.org/abs/2604.11309v1
- **Security insight:** Large Language Models (LLMs) face prominent security risks from jailbreaking, a practice that manipulates models to bypass built-in security constraints and generate unethical or unsafe content. Among various jailbreak techniques, multi-turn jailbreak attacks…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.
