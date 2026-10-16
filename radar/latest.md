# AI Security Radar

_Last updated (UTC): **2026-10-16**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

**From Detection to Decision: Calibration and Deferral for Prompt-Injection Detection**  
- **Date:** 2026-10-14
- **Authors:** Qianlong Lan, Anuj Kaul, Vinothini Pandurangan et al.
- **Link:** https://arxiv.org/abs/2610.20907v1
- **Security insight:** Prompt-injection defenses are commonly evaluated as binary detectors, although deployed LLM applications must make operational decisions about whether to allow, block, or escalate potentially malicious inputs. Recent probabilistic decision models aim to…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**INFUSE: A Unified Surface Benchmark for Indirect Prompt Injection in Agentic Systems**  
- **Date:** 2026-10-14
- **Authors:** Thuy Dung Nguyen, Jingyi Guo, Rana Seda Dubauskas et al.
- **Link:** https://arxiv.org/abs/2610.20776v1
- **Security insight:** LLM-based agents increasingly execute long-horizon, end-to-end workflows involving shell commands, code modification, dependency installation, and interaction with remote services. This growing autonomy expands their exposure to indirect prompt injection…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Are You Reading the Right Thing? Rethinking Internal Signals for Prompt-Injection Detection**  
- **Date:** 2026-10-14
- **Authors:** Sarthak Gupta, Priyanka Tembey
- **Link:** https://arxiv.org/abs/2610.19452v1
- **Security insight:** Several recent studies propose detecting prompt injections from a language model's internal state. However, these methods do not measure a single security property. Residual-stream probes, attention scores, role projections, exposure probes, and concept…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**AgentSafeEvo: Adversarial Co-Evolution for LLM Agent Safety**  
- **Date:** 2026-10-14
- **Authors:** Chenxu Wang, Xiaoyu Wen, Han Qi et al.
- **Link:** https://arxiv.org/abs/2610.19422v1
- **Security insight:** Large language model (LLM) agents accomplish complex tasks through multi-turn interactions with external tools. However, malicious content embedded in user queries, tool descriptions, or environment observations can manipulate their decisions and induce…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Policy-Verified Self-Training: Learning Agent Compliance from Verifiable Policy Rewards**  
- **Date:** 2026-10-14
- **Authors:** Min-Young Yu
- **Link:** https://arxiv.org/abs/2610.19372v1
- **Security insight:** Runtime policy verifiers can prevent agents from executing disallowed actions, but their decisions are typically used only for enforcement and discarded afterward. We ask whether these decisions can instead become verifiable policy rewards for training the…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**TRACER: Trace-Regularized Training Against Indirect Prompt Injection**  
- **Date:** 2026-10-13
- **Authors:** Kshitij Mishra, Salem Lahlou, Nils Lukas
- **Link:** https://arxiv.org/abs/2610.19133v1
- **Security insight:** Indirect prompt injection uses untrusted retrieved content, tool outputs, or agent messages to override an LLM's intended behavior. We show that defense robustness is channel-conditioned: the same attack succeeds 18% of the time as a follow-up message but 53%…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**DecisionRobust: Benchmarking Robustness for JEV Style Decision Models Across Text and Vision**  
- **Date:** 2026-10-13
- **Authors:** Yifan Lan, Zhongye Liu, Yurui Chang et al.
- **Link:** https://arxiv.org/abs/2610.19118v1
- **Security insight:** Emerging decision models such as JEV provide typed interfaces that map task instructions and observations directly to choices, judgments, and scores. As these models are increasingly used for automated decision-making, understanding their reliability under…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

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

### RAG & Retrieval Attacks

**TRAP: Tree-Guided Reinforcement-Augmented Probing for Automated LLM Jailbreaking**  
- **Date:** 2026-10-12
- **Authors:** Mohammad Reza Mirbagheri, Amir Mahdi Sadeghzadeh
- **Link:** https://arxiv.org/abs/2610.17313v1
- **Security insight:** Aligned large language models (LLMs) remain vulnerable to jailbreak prompts that circumvent their safety guardrails, making the identification of these vulnerabilities important for understanding and mitigating model weaknesses. Existing automated jailbreak…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Adversarial ML

**Can Autonomous Vehicles Keep Their Cool? A Survey of Thermal Side-Channel and Perception Attacks**  
- **Date:** 2026-10-15
- **Authors:** Harsh Aaryan, Ce Zhou
- **Link:** https://arxiv.org/abs/2610.21034v1
- **Security insight:** Autonomous vehicles (AVs) couple safety-critical perception to thermally constrained compute. Interfaces built for night perception and package thermal reliability were never engineered as confidentiality boundaries, and closing one such path leaves the other…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

### Agent & Tool Security

**The Agent Knew: Internal States Forecast Unauthorized Actions and Stop Them, and the Lies That Follow**  
- **Date:** 2026-10-12
- **Authors:** Arya Fayyazi, Mehdi Kamal, Massoud Pedram
- **Link:** https://arxiv.org/abs/2610.17301v1
- **Security insight:** Language-model agents sometimes act beyond their authorization and then misreport what they did. On CAPE-Bench, matched agent tasks in which one fact decides whether an action is authorized, frontier open-weight agents do both, and one behavior marks the lie:…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.
