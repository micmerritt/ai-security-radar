# AI Security Radar

_Last updated (UTC): **2026-10-02**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

**Aletheia: Permission-Minimality Testing for Coding-Agent Rules**  
- **Date:** 2026-09-30
- **Authors:** Jieke Shi, Yuchen Chen, Junda He et al.
- **Link:** https://arxiv.org/abs/2609.39678v1
- **Security insight:** Repository instruction files guide coding agents, but also expose them to prompt injection. Malicious rules can request credential access or data transfer while the agent produces a correct patch. We present Aletheia, a framework for permission-minimality…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**From A2A Attacks to Envelope-Layer Defense: Red-Teaming Evaluation of LLM Agents and a Three-Layer Isomorphic Attack-Defense Model**  
- **Date:** 2026-09-30
- **Authors:** Yuelin Han
- **Link:** https://arxiv.org/abs/2610.00392v1
- **Security insight:** Agent interaction protocols such as ACP and A2A have moved LLM-based agents toward multi-agent collaboration, introducing new security threats. A task sent by a remote peer over A2A is treated as a legitimate request, providing a natural channel for indirect…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Where Do LLMs Decide to Break the Rules? Mechanistic Localization of Prompt Injection Compliance**  
- **Date:** 2026-09-29
- **Authors:** Rui Wen, Jiayang Liu, Zeyu Yang et al.
- **Link:** https://arxiv.org/abs/2609.37737v1
- **Security insight:** When a prompt injection attack succeeds, a Large Language Model (LLM) abandons its assigned system role to comply with an adversarial instruction. While prior work has extensively quantified how often this occurs, we ask a more fundamental question: where…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**ToolFence: Fine-Grained Authorization for Secure Tool-Using LLM Agents**  
- **Date:** 2026-09-29
- **Authors:** Yanjie Li, Xiangyu He, Xuelong Dai et al.
- **Link:** https://arxiv.org/abs/2609.37196v1
- **Security insight:** Tool-using LLM agents remain vulnerable to indirect prompt injection because trusted instructions and untrusted observations share one context, allowing malicious content to steer consequential input-filtering defenses. Multi-path consensus defenses still…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Selecting The Most Informative Tokens in Natural Language Autoencoders**  
- **Date:** 2026-09-29
- **Authors:** Federico Torrielli, Gianluca Barmina, Andrea Blasi Núñez et al.
- **Link:** https://arxiv.org/abs/2609.37040v1
- **Security insight:** Natural language autoencoders translate a language model's internal activations into readable explanations. Explaining every token position is costly. Which positions should an auditor inspect to understand a potential threat? We study this question across…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**ContractWarden: Kernel-Enforced Damage Boundaries for AI Agents via Human-Authorized Contracts**  
- **Date:** 2026-09-29
- **Authors:** Dongxu Cui, Zhichao Gu, Ping Zheng et al.
- **Link:** https://arxiv.org/abs/2609.38248v1
- **Security insight:** Large language model agents can execute commands, create subprocesses, and directly access files and networks, allowing prompt injection or planning errors to become operating-system side effects. We present ContractWarden, a Linux reference monitor that…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**pikit: A Composable Toolkit for Indirect Prompt Injection Research and Evaluation**  
- **Date:** 2026-09-29
- **Authors:** Zonghao Ying, Xiangfan Wu, Bo Yang et al.
- **Link:** https://arxiv.org/abs/2609.36817v1
- **Security insight:** Indirect prompt injection embeds malicious instructions within external content retrieved by LLM-based agents, altering target behavior without user authorization. We introduce pikit, a research toolkit designed to systematically evaluate these threats across…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Self-Evolving Defense: Continual Security Policy Learning for LLM Agents**  
- **Date:** 2026-09-29
- **Authors:** Minh Nhat Le, Nisarga Gondi, Yibo Peng et al.
- **Link:** https://arxiv.org/abs/2609.36603v1
- **Security insight:** Large language models (LLMs) increasingly power agents that access sensitive information, use external tools, and modify software repositories. Although these capabilities offer substantial benefits, they also create security risks such as jailbreaks, prompt…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Divide and Inject: Can Agents Reconstruct an Indirect Prompt Injection from Fragments?**  
- **Date:** 2026-09-29
- **Authors:** Michael Lee, Zhipeng Wei, Yue Dong et al.
- **Link:** https://arxiv.org/abs/2609.36576v1
- **Security insight:** Agentic systems are now being widely used to orchestrate tools and reason over long contexts. However, the improving capabilities of the large language models powering these agents also create new attack surfaces for indirect prompt injection. In particular,…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**The Innocent Courier: Covert Exfiltration Through Legitimate LLM Web Fetching**  
- **Date:** 2026-10-01
- **Authors:** Alessandro Pegoraro, Daryan Merx, Phillip Rieger et al.
- **Link:** https://arxiv.org/abs/2610.01768v1
- **Security insight:** With the increasing capabilities of Large-Language-Models (LLMs) and LLM-based agents, users are increasingly using them to solve everyday problems, such as answering e-mails or providing programming support. Existing work has extensively investigated…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**Memetic Trojans: Social Contagions as Carriers of Adversarial Payloads in Agent Networks**  
- **Date:** 2026-09-30
- **Authors:** Birk Torpmann-Hagen, Finn Schwall, Leon Moonen
- **Link:** https://arxiv.org/abs/2610.00430v1
- **Security insight:** Autonomous large language model (LLM) agents increasingly interact in network environments where adversarial content can propagate between agents. Known attacks include agent worms, which spread through self-replicating prompt injections or configuration…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Model Extraction & Privacy

**Do Defenses Against LLM Extraction Work Across Attacks? A Lifecycle Benchmark of Black-Box Model Extraction**  
- **Date:** 2026-09-30
- **Authors:** Shuze Liu, Kaixiang Zhao, Runyang Xu et al.
- **Link:** https://arxiv.org/abs/2610.00839v1
- **Security insight:** Large language models (LLMs) deployed through text-only APIs face model extraction risks, as adversaries can collect their responses to train surrogates that reproduce their capabilities. While prior work has developed diverse attacks and defenses,…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

### Adversarial ML

**Deep Learning Latency Attacks and Defenses: A Cross-Domain Survey of Availability Threats**  
- **Date:** 2026-09-29
- **Authors:** Zonghua Gu, Zeyu Gao, Amin Saremi et al.
- **Link:** https://arxiv.org/abs/2609.36732v1
- **Security insight:** Adversarial machine learning has focused mainly on integrity, but availability is an increasingly consequential complement. Latency attacks (also energy-latency attacks) increase inference-time work, energy, or response time, causing deadline misses,…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

### Agent & Tool Security

**PACE: Provenance-Aware Capability Enforcement for Tool-Using LLM Agents**  
- **Date:** 2026-10-01
- **Authors:** Fengpeng Li, Qizhou Wang, Yuke Hu et al.
- **Link:** https://arxiv.org/abs/2610.01349v1
- **Security insight:** Tool-using large language model (LLM) agents turn generated text into real side effects, so poisoned tool metadata, retrieved pages, memory, and reusable skills can steer the next call. Vetting an artifact before admission does not settle this. A safe variant…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.
