# AI Security Radar

_Last updated (UTC): **2026-05-10**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Constraining Host-Level Abuse in Self-Hosted Computer-Use Agents via TEE-Backed Isolation**  
- **Date:** 2026-05-07
- **Authors:** Di Lu, Bo Zhang, Xiyuan Li et al.
- **Link:** https://arxiv.org/abs/2605.06393v1
- **Security insight:** Self-hosted computer-use agents (SHCUAs), such as OpenClaw, combine natural-language interaction with direct access to host-side resources, including browsers, files, scripts, system commands, and external communication channels. While useful for automating…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Heimdallr: Characterizing and Detecting LLM-Induced Security Risks in GitHub CI Workflows**  
- **Date:** 2026-05-07
- **Authors:** Bonan Ruan, Yeqi Fu, Chuqi Zhang et al.
- **Link:** https://arxiv.org/abs/2605.05969v1
- **Security insight:** GitHub Continuous Integration (CI) workflows increasingly integrate Large Language Models (LLMs) to automate review, triage, content generation, and repository maintenance. This creates a new attack surface: externally controllable workflow inputs can shape…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**PersonaTeaming: Supporting Persona-Driven Red-Teaming for Generative AI**  
- **Date:** 2026-05-07
- **Authors:** Wesley Hanwen Deng, Mingxi Yan, Sunnie S. Y. Kim et al.
- **Link:** https://arxiv.org/abs/2605.05682v1
- **Security insight:** Recent developments in AI safety research have called for red-teaming methods that effectively surface potential risks posed by generative AI models, with growing emphasis on how red-teamers' backgrounds and perspectives shape their strategies and the risks…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**WAAA! Web Adversaries Against Agentic Browsers**  
- **Date:** 2026-05-06
- **Authors:** Sohom Datta, Alex Nahapetyan, William Enck et al.
- **Link:** https://arxiv.org/abs/2605.05509v1
- **Security insight:** Large language models (LLMs) are increasingly being integrated into web browsers to create agentic browsing systems that execute actions on behalf of the user. Prior work considering the security of agentic browsers focuses exclusively on indirect prompt-…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure**  
- **Date:** 2026-05-06
- **Authors:** Krti Tallam
- **Link:** https://arxiv.org/abs/2605.05440v1
- **Security insight:** The security discussion around agentic AI focuses heavily on prompt injection. This paper argues that multi-agent systems also create a distinct authorization problem: maintaining authorization invariants as non-human principals retrieve data, delegate tasks,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**DecodingTrust-Agent Platform (DTap): A Controllable and Interactive Red-Teaming Platform for AI Agents**  
- **Date:** 2026-05-06
- **Authors:** Zhaorun Chen, Xun Liu, Haibo Tong et al.
- **Link:** https://arxiv.org/abs/2605.04808v1
- **Security insight:** AI agents are increasingly deployed across diverse domains to automate complex workflows through long-horizon and high-stakes action executions. Due to their high capability and flexibility, such agents raise significant security and safety concerns. A…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**SecureMCP: A Policy-Enforced LLM Data Access Framework for AIoT Systems via Model Context Protocol**  
- **Date:** 2026-05-06
- **Authors:** Wonbae Kim, Hee-Kyong Yoo
- **Link:** https://arxiv.org/abs/2605.05260v1
- **Security insight:** The deployment of Large Language Model (LLM)-generated SQL queries in Artificial Intelligence of Things (AIoT) systems introduces critical security risks, as prompt injection attacks can manipulate LLMs into producing unauthorized queries that expose…
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
- **Link:** https://arxiv.org/abs/2605.03213v2
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

### Prompt Injection

**Laundering AI Authority with Adversarial Examples**  
- **Date:** 2026-05-05
- **Authors:** Jie Zhang, Pura Peetathawatchai, Florian Tramèr et al.
- **Link:** https://arxiv.org/abs/2605.04261v1
- **Security insight:** Vision-language models (VLMs) are increasingly deployed as trusted authorities -- fact-checking images on social media, comparing products, and moderating content. Users implicitly trust that these systems perceive the same visual content as they do. We show…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**SoK: Robustness in Large Language Models against Jailbreak Attacks**  
- **Date:** 2026-05-06
- **Authors:** Feiyue Xu, Hongsheng Hu, Chaoxiang He et al.
- **Link:** https://arxiv.org/abs/2605.05058v1
- **Security insight:** Large Language Models (LLMs) have achieved remarkable success but remain highly susceptible to jailbreak attacks, in which adversarial prompts coerce models into generating harmful, unethical, or policy-violating outputs. Such attacks pose real-world risks,…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.
