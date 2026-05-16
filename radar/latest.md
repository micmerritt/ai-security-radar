# AI Security Radar

_Last updated (UTC): **2026-05-16**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**WARD: Adversarially Robust Defense of Web Agents Against Prompt Injections**  
- **Date:** 2026-05-14
- **Authors:** Tri Cao, Yulin Chen, Hieu Cao et al.
- **Link:** https://arxiv.org/abs/2605.15030v1
- **Security insight:** Web agents can autonomously complete online tasks by interacting with websites, but their exposure to open web environments makes them vulnerable to prompt injection attacks embedded in HTML content or visual interfaces. Existing guard models still suffer…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Web Agents Should Adopt the Plan-Then-Execute Paradigm**  
- **Date:** 2026-05-14
- **Authors:** Julien Piet, Annabella Chow, Yiwei Hou et al.
- **Link:** https://arxiv.org/abs/2605.14290v1
- **Security insight:** ReAct has become the default architecture across LLM agents, and many existing web agents follow this paradigm. We argue that it is the wrong default for web agents. Instead, web agents should default to plan-then-execute: commit to a task-specific program…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**ExploitBench: A Capability Ladder Benchmark for LLM Cybersecurity Agents**  
- **Date:** 2026-05-13
- **Authors:** Seunghyun Lee, David Brumley
- **Link:** https://arxiv.org/abs/2605.14153v1
- **Security insight:** Exploitation is not a binary event. It is a ladder of acquiring progressive capabilities, from executing a single buggy line of code to taking full control of the target. However, existing LLM security benchmarks treat a crash as exploitation success. That…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**ProjGuard: Safety Monitoring for Computer-Use Agents via Low-Dimensional Projections**  
- **Date:** 2026-05-13
- **Authors:** Kebin Contreras, Carlos Hinojosa, Jorge Bacca et al.
- **Link:** https://arxiv.org/abs/2605.13631v1
- **Security insight:** Computer-use agents are increasingly capable of operating on real operating systems, but this capability has also increased the risks posed by prompt injection, indirect instructions, and visual attacks. Existing defenses typically rely on analyzing the…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Sleeper Channels and Provenance Gates: Persistent Prompt Injection in Always-on Autonomous AI Agents**  
- **Date:** 2026-05-13
- **Authors:** Narek Maloyan, Dmitry Namiot
- **Link:** https://arxiv.org/abs/2605.13471v1
- **Security insight:** Always-on AI agents (OpenClaw, Hermes Agent) run as a single persistent process under the owner's identity, folding messaging, memory, self-authored skills, scheduling, and shell into one authority boundary. This configuration opens what we call \emph{sleeper…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**No Attack Required: Semantic Fuzzing for Specification Violations in Agent Skills**  
- **Date:** 2026-05-13
- **Authors:** Ying Li, Hongbo Wen, Yanju Chen et al.
- **Link:** https://arxiv.org/abs/2605.13044v1
- **Security insight:** LLM-powered agents can silently delete documents, leak credentials, or transfer funds on a routine user request, not because the agent was attacked, but because the skill it invoked broke its own declared safety rules. We call these specification violations:…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**IPI-proxy: An Intercepting Proxy for Red-Teaming Web-Browsing AI Agents Against Indirect Prompt Injection**  
- **Date:** 2026-05-12
- **Authors:** Chia-Pei, Chen, Kentaroh Toyoda et al.
- **Link:** https://arxiv.org/abs/2605.11868v1
- **Security insight:** Web-browsing AI agents are increasingly deployed in enterprise settings under strict whitelists of approved domains, yet adversaries can still influence them by embedding hidden instructions in the HTML pages those domains serve. Existing red-teaming…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Agents Should Replace Narrow Predictive AI as the Orchestrator in 6G AI-RAN**  
- **Date:** 2026-05-12
- **Authors:** Pranshav Gajjar, Vijay K Shah
- **Link:** https://arxiv.org/abs/2605.11516v1
- **Security insight:** This position paper argues that to achieve Level 5 autonomous 6G networks, the next generation of Artificial Intelligence in Radio Access Networks (AI-RAN) should transition away from fragmented, narrow predictive models and instead adopt multimodal Large…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**LLMs for Secure Hardware Design and Related Problems: Opportunities and Challenges**  
- **Date:** 2026-05-11
- **Authors:** Johann Knechtel, Ozgur Sinanoglu, Ramesh Karri
- **Link:** https://arxiv.org/abs/2605.10807v2
- **Security insight:** The integration of Large Language Models (LLMs) into Electronic Design Automation (EDA) and hardware security is rapidly reshaping the semiconductor industry. While LLMs offer unprecedented capabilities in generating Register Transfer Level (RTL) code,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**RUBEN: Rule-Based Explanations for Retrieval-Augmented LLM Systems**  
- **Date:** 2026-05-11
- **Authors:** Joel Rorseth, Parke Godfrey, Lukasz Golab et al.
- **Link:** https://arxiv.org/abs/2605.10862v1
- **Security insight:** This paper demonstrates RUBEN, an interactive tool for discovering minimal rules to explain the outputs of retrieval-augmented large language models (LLMs) in data-driven applications. We leverage novel pruning strategies to efficiently identify a minimal set…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### Model Extraction & Privacy

**Identified-Set Geometry of Distributional Model Extraction under Top-$K$ Censored API Access**  
- **Date:** 2026-05-11
- **Authors:** Wenhua Nie, ZiCheng Zhu, Jianan Wu et al.
- **Link:** https://arxiv.org/abs/2605.10407v1
- **Security insight:** Modern LLM APIs often reveal only top-$K$ logit scores and censor the remaining vocabulary. We study the per-position distribution-recovery limits of this access model. For censoring threshold $τ$, the compatible teacher distributions form an identified set…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

### Adversarial ML

**The Great Pretender: A Stochasticity Problem in LLM Jailbreak**  
- **Date:** 2026-05-14
- **Authors:** Jean-Philippe Monteuuis, Cong Chen, Jonathan Petit
- **Link:** https://arxiv.org/abs/2605.14418v1
- **Security insight:** "Oh-Oh, yes, I'm the great pretender. Pretending that I'm doing well. My need is such, I pretend too much..." summarizes the state in the area of jailbreak creation and evaluation. You find this method to generate adversarial attacks proposed by a reputable…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

**Quantifying LLM Safety Degradation Under Repeated Attacks Using Survival Analysis**  
- **Date:** 2026-05-13
- **Authors:** Zvi Topol
- **Link:** https://arxiv.org/abs/2605.12869v1
- **Security insight:** Large language models (LLMs) are increasingly deployed in a wide range of applications, yet remain vulnerable to adversarial jailbreak attacks that circumvent their safety guardrails. Existing evaluation frameworks typically report binary success/failure…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

### Other (Review)

**GraphIP-Bench: How Hard Is It to Steal a Graph Neural Network, and Can We Stop It?**  
- **Date:** 2026-05-12
- **Authors:** Kaixiang Zhao, Bolin Shen, Yuyang Dai et al.
- **Link:** https://arxiv.org/abs/2605.12827v1
- **Security insight:** Graph neural networks (GNNs) deployed as cloud services can be \emph{stolen} through \emph{model-extraction attacks}, which train a surrogate from query responses to reproduce the target's behaviour, and a growing line of ownership defenses tries to prevent…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
