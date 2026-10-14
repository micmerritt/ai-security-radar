# AI Security Radar

_Last updated (UTC): **2026-10-14**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

**Towards Safe Autonomy for Computer Use**  
- **Date:** 2026-10-13
- **Authors:** Dominik Seip, Bartol Markovinović, Matthias Hein
- **Link:** https://arxiv.org/abs/2610.18508v1
- **Security insight:** The safety of LLM-based agents currently rests on alignment training and safety classifiers, neither of which can rule out that a sophisticated indirect prompt injection (IPI) goes through and causes significant harm. Recent work therefore builds agents with…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Kairos: Transactional Security Enforcement at the System Boundary for LLM Agents**  
- **Date:** 2026-10-13
- **Authors:** Kristoffer Hempel, Nils Loose, Lorenzo Cavallaro et al.
- **Link:** https://arxiv.org/abs/2610.18457v1
- **Security insight:** Large language model (LLM) agents are becoming an integral part of the software development lifecycle, and the capabilities granted to them allow an agent to act with the user's authority on any resource it can access. The reach that gives an agent its…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Prompt-Injection Probes Learn the Conversation, Not Just the Injection**  
- **Date:** 2026-10-13
- **Authors:** Kaan Kale, Sriram Vishwanath
- **Link:** https://arxiv.org/abs/2610.18408v1
- **Security insight:** Linear probes on a model's hidden states are used as cheap monitors for indirect prompt injection: they screen the tool outputs an agent reads and send suspicious ones to a slower second check, so every false alarm has a cost. But a probe learns whatever…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**BrowseSafe++: Benchmarking Prompt Injection Detection Across Web Contexts, Languages, and Browser Views**  
- **Date:** 2026-10-12
- **Authors:** Yuetian Chen, Kaiyuan Zhang, Yuntao Du et al.
- **Link:** https://arxiv.org/abs/2610.17457v1
- **Security insight:** Browser agents need to make decisions and execute actions on behalf of users while consuming untrusted webpages, creating opportunities for malicious instructions embedded in webpages to redirect legitimate tasks. We introduce BrowseSafe++, which extends…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**StableJudge: A Lightweight Adversarial Defense Framework for LLM-as-a-Judge**  
- **Date:** 2026-10-12
- **Authors:** Anning Hu, Yangyu Li, Yuqi Huang et al.
- **Link:** https://arxiv.org/abs/2610.16814v1
- **Security insight:** Large language models (LLMs) are increasingly used as judges to assign scalar scores that drive downstream decision-making, including tasks such as paper review and recommendation. However, LLM-as-a-Judge pipelines are vulnerable to score-hijacking prompt…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Computational Reflective Equilibrium for Agentic AI: A Rawlsian Alignment Scaffold for Governance**  
- **Date:** 2026-10-12
- **Authors:** Quanyan Zhu
- **Link:** https://arxiv.org/abs/2610.16015v1
- **Security insight:** The rapid deployment of agentic AI has introduced complex challenges for the ethics and governance of AI systems. Agents built on large language models act through tools on behalf of people, and each deployment case brings its own instructions, policies,…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Only What You've Signed up For: Secure Workflows with Constrained Diffusion Agents**  
- **Date:** 2026-10-10
- **Authors:** Michael Cardei, Anjun Hu, Chenrui Ma et al.
- **Link:** https://arxiv.org/abs/2610.15177v1
- **Security insight:** As agentic AI systems take on increasingly complex and consequential tasks, securing them against prompt injection becomes critical. Existing defenses often rely on detecting or reasoning about injected malicious instructions and can therefore remain…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Can agents whose sole duty is to keep humans alive be hijacked to kill? Delayed multi-turn derived-action trap attacks in simulated high-stakes environments**  
- **Date:** 2026-10-10
- **Authors:** Josef A. Habdank
- **Link:** https://arxiv.org/abs/2610.15153v1
- **Security insight:** We ask whether a tool-using agent whose sole duty is to keep humans alive can be induced, by delayed prompt injection, to kill. The keep-alive duty is in force from the first watch, with the attack arriving later, appended to otherwise truthful telemetry the…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**The Limits of Query Monitoring against Distributed Model Extraction**  
- **Date:** 2026-10-09
- **Authors:** Snigdha Chandan Khilar
- **Link:** https://arxiv.org/abs/2610.13083v1
- **Security insight:** Model providers now face distillation campaigns run through thousands of accounts, each of which looks like an ordinary user. When network and payment metadata cannot link those accounts, the only evidence left is what they ask. We study what a provider can…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**TRAP: Tree-Guided Reinforcement-Augmented Probing for Automated LLM Jailbreaking**  
- **Date:** 2026-10-12
- **Authors:** Mohammad Reza Mirbagheri, Amir Mahdi Sadeghzadeh
- **Link:** https://arxiv.org/abs/2610.17313v1
- **Security insight:** Aligned large language models (LLMs) remain vulnerable to jailbreak prompts that circumvent their safety guardrails, making the identification of these vulnerabilities important for understanding and mitigating model weaknesses. Existing automated jailbreak…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**Names Are Not Objects: Object-Bound Confinement for Compromised AI Coding Agents**  
- **Date:** 2026-10-10
- **Authors:** Daniel Commey
- **Link:** https://arxiv.org/abs/2610.14488v1
- **Security insight:** Coding agents read repositories and web pages that anyone can write, and then act with their user's authority. Prompt-injection defenses make it less likely that the model is steered but do not prevent it, so the system around the model must contain an agent…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Adversarial ML

**An Empirical Case Study of Prompt Engineering Strategies for Bypassing Multi-Layer Agent Security Defenses**  
- **Date:** 2026-10-09
- **Authors:** Chengwei Chu
- **Link:** https://arxiv.org/abs/2610.14116v1
- **Security insight:** The OpenClaw Security Attack and Defense Challenge evaluates AI agent robustness through a three-stage defense pipeline: skill file scanning (Stage 1), instruction safety evaluation (Stage 2), and attack trajectory scoring (Stage 3). This paper presents an…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

### Agent & Tool Security

**The Agent Knew: Internal States Forecast Unauthorized Actions and Stop Them, and the Lies That Follow**  
- **Date:** 2026-10-12
- **Authors:** Arya Fayyazi, Mehdi Kamal, Massoud Pedram
- **Link:** https://arxiv.org/abs/2610.17301v1
- **Security insight:** Language-model agents sometimes act beyond their authorization and then misreport what they did. On CAPE-Bench, matched agent tasks in which one fact decides whether an action is authorized, frontier open-weight agents do both, and one behavior marks the lie:…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**CWE-bench: Refocusing Agentic Security from Exploitation to Defense**  
- **Date:** 2026-10-12
- **Authors:** Gonzalo Gonzalez-Pumariega, Ajay Jagannath, Adit Jain et al.
- **Link:** https://arxiv.org/abs/2610.17020v1
- **Security insight:** Cybersecurity evaluations of AI agents have focused largely on offense, yet a working exploit does not show that an agent can make software safe. An attacker needs to exploit only one vulnerability; a defender must find and fix all of them. We introduce CWE-…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.
