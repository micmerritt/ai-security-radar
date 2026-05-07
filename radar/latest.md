# AI Security Radar

_Last updated (UTC): **2026-05-07**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**DecodingTrust-Agent Platform (DTap): A Controllable and Interactive Red-Teaming Platform for AI Agents**  
- **Date:** 2026-05-06
- **Authors:** Zhaorun Chen, Xun Liu, Haibo Tong et al.
- **Link:** https://arxiv.org/abs/2605.04808v1
- **Security insight:** AI agents are increasingly deployed across diverse domains to automate complex workflows through long-horizon and high-stakes action executions. Due to their high capability and flexibility, such agents raise significant security and safety concerns. A…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Redefining AI Red Teaming in the Agentic Era: From Weeks to Hours**  
- **Date:** 2026-05-05
- **Authors:** Raja Sekhar Rao Dheekonda, Will Pearce, Nick Landers
- **Link:** https://arxiv.org/abs/2605.04019v1
- **Security insight:** AI systems are entering critical domains like healthcare, finance, and defense, yet remain vulnerable to adversarial attacks. While AI red teaming is a primary defense, current approaches force operators into manual, library-specific workflows. Operators…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**ARGUS: Defending LLM Agents Against Context-Aware Prompt Injection**  
- **Date:** 2026-05-05
- **Authors:** Shihao Weng, Yang Feng, Jinrui Zhang et al.
- **Link:** https://arxiv.org/abs/2605.03378v1
- **Security insight:** The rise of Large Language Model (LLM) agents, augmented with tool use, skills, and external knowledge, has introduced new security risks. Among them, prompt injection attacks, where adversaries embed malicious instructions into the agent workflow, have…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**When Agents Handle Secrets: A Survey of Confidential Computing for Agentic AI**  
- **Date:** 2026-05-04
- **Authors:** Javad Forough, Marios Kogias, Hamed Haddadi
- **Link:** https://arxiv.org/abs/2605.03213v1
- **Security insight:** Agentic AI systems, specifically LLM-driven agents that plan, invoke tools, maintain persistent memory, and delegate tasks to peer agents via protocols such as MCP and A2A, introduce a threat surface that differs materially from standalone model inference.…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**PIIGuard: Mitigating PII Harvesting under Adversarial Sanitization**  
- **Date:** 2026-05-04
- **Authors:** Mingshuo Liu, Yiwei Zha, Min Chen
- **Link:** https://arxiv.org/abs/2605.03129v1
- **Security insight:** Browsing-enabled LLM assistants can fetch webpages and answer contact-seeking queries, creating a practical channel for scraping contact-style personally identifiable information (PII) from public pages. Many prior defenses are deployed at the model, service,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Tool Use as Action: Towards Agentic Control in Mobile Core Networks**  
- **Date:** 2026-05-04
- **Authors:** Purna Sai Garigipati, Onur Ayan, Kishor Chandra Joshi et al.
- **Link:** https://arxiv.org/abs/2605.02811v1
- **Security insight:** Artificial Intelligence (AI) will play an essential role in 6G. It will fundamentally reshape the network architecture itself and drive major changes in the design of network entities, interfaces, and procedures. The adoption of agentic AI in next-generation…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**When Alignment Isn't Enough: Response-Path Attacks on LLM Agents**  
- **Date:** 2026-05-04
- **Authors:** Mingyu Luo, Zihan Zhang, Zesen Liu et al.
- **Link:** https://arxiv.org/abs/2605.02187v1
- **Security insight:** Bring-Your-Own-Key (BYOK) agent architectures let users route LLM traffic through third-party relays, creating a critical integrity gap: a malicious relay can modify an aligned LLM response after generation but before agent execution. We formalize this post-…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Trace: Unmasking AI Attack Agents Through Terminal Behavior Fingerprinting**  
- **Date:** 2026-05-02
- **Authors:** Murali Ediga, Sudipta Chattopadhyay
- **Link:** https://arxiv.org/abs/2605.01186v1
- **Security insight:** AI-driven penetration testing agents are now capable of autonomously executing attacks within compromised networks. Identifying the model family that controls the active sessions of such agents provides valuable information towards understanding the intent of…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**A Low-Latency Fraud Detection Layer for Detecting Adversarial Interaction Patterns in LLM-Powered Agents**  
- **Date:** 2026-05-01
- **Authors:** Sheldon Yu, Yingcheng Sun, Hanqing Guo et al.
- **Link:** https://arxiv.org/abs/2605.01143v1
- **Security insight:** Large Language Model (LLM)-powered agents demonstrate strong capabilities in autonomous task execution, tool use, and multi-step reasoning. However, their increasing autonomy also introduces a new attack surface: adversarial interactions can manipulate agent…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Laundering AI Authority with Adversarial Examples**  
- **Date:** 2026-05-05
- **Authors:** Jie Zhang, Pura Peetathawatchai, Florian Tramèr et al.
- **Link:** https://arxiv.org/abs/2605.04261v1
- **Security insight:** Vision-language models (VLMs) are increasingly deployed as trusted authorities -- fact-checking images on social media, comparing products, and moderating content. Users implicitly trust that these systems perceive the same visual content as they do. We show…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**LocalAlign: Enabling Generalizable Prompt Injection Defense via Generation of Near-Target Adversarial Examples for Alignment Training**  
- **Date:** 2026-05-02
- **Authors:** Yuyang Gong, Zihao Wang, Jiawei Liu et al.
- **Link:** https://arxiv.org/abs/2605.01462v1
- **Security insight:** Large language models are increasingly embedded into systems that interact with user data, retrieved web content, and external tools, creating a new attack surface: prompt injection, where malicious commands embedded in untrusted data override the trusted…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**SoK: Robustness in Large Language Models against Jailbreak Attacks**  
- **Date:** 2026-05-06
- **Authors:** Feiyue Xu, Hongsheng Hu, Chaoxiang He et al.
- **Link:** https://arxiv.org/abs/2605.05058v1
- **Security insight:** Large Language Models (LLMs) have achieved remarkable success but remain highly susceptible to jailbreak attacks, in which adversarial prompts coerce models into generating harmful, unethical, or policy-violating outputs. Such attacks pose real-world risks,…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Adversarial ML

**MultiBreak: A Scalable and Diverse Multi-turn Jailbreak Benchmark for Evaluating LLM Safety**  
- **Date:** 2026-05-03
- **Authors:** Jialin Song, Xiaodong Liu, Weiwei Yang et al.
- **Link:** https://arxiv.org/abs/2605.01687v1
- **Security insight:** We present MultiBreak, a scalable and diverse multi-turn jailbreak benchmark to evaluate large language model (LLM) safety. Multi-turn jailbreaks mimic natural conversational settings, making them easier to bypass safety-aligned LLM than single-turn…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

**VisInject: Disruption != Injection -- A Dual-Dimension Evaluation of Universal Adversarial Attacks on Vision-Language Models**  
- **Date:** 2026-05-02
- **Authors:** Pang Liu, Yingjie Lao
- **Link:** https://arxiv.org/abs/2605.01449v1
- **Security insight:** Universal adversarial attacks on aligned multimodal large language models are increasingly reported with attack success rates in the 60-80% range, suggesting the visual modality is highly vulnerable to imperceptible perturbations as a prompt-injection…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.
