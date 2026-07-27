# AI Security Radar

_Last updated (UTC): **2026-07-27**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**Agent Security Needs Redefinition through a Holistic Framework**  
- **Date:** 2026-07-24
- **Authors:** Vincent Siu, Jingxuan He, Kyle Montgomery et al.
- **Link:** https://arxiv.org/abs/2607.22024v1
- **Security insight:** Agent security is widely treated as a question about action content. Defenses ask whether an instruction looks malicious. Benchmarks ask whether an agent performs a harmful sounding action. \textbf{We argue that agent security is fundamentally a contextual…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Protocol-Level Attacks on Agentic Commerce Platforms: A Cross-Platform Taxonomy, AIP-Bench, and Unified Defense**  
- **Date:** 2026-07-23
- **Authors:** Yedidel Louck
- **Link:** https://arxiv.org/abs/2607.21824v1
- **Security insight:** Agentic commerce platforms let AI agents autonomously discover services, move payments, and wield user credentials on their users' behalf, and they already handle real money. Their security has so far been studied almost entirely at the level of the AI model,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Encoding Invisible Causation for Bridge Diagnostic Agents: Triple-Guided Retrieval-Augmented Fine-Tuning with QLoRA**  
- **Date:** 2026-07-23
- **Authors:** Takato Yasuno
- **Link:** https://arxiv.org/abs/2607.21680v1
- **Security insight:** Bridge infrastructure deteriorates gradually, yet its root causes---salt intrusion, freezing, fatigue cracking, and others---remain invisible to the naked eye. Expert diagnosis relies on tacit knowledge built over years of practice. We address the challenge…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**The Ethics of Autonomous AI Agents for Offensive Security**  
- **Date:** 2026-07-22
- **Authors:** Andreas Happe, Jürgen Cito, Jasmin Wachter
- **Link:** https://arxiv.org/abs/2607.20255v1
- **Security insight:** LLM-driven autonomous agents are reshaping offensive security. Unlike traditional penetration-testing tooling -- deterministic, narrowly scoped, and operated by trained practitioners -- agentic security tools exhibit \textit{indeterminacy} along three…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Know Your Agent: Reconnaissance-Driven Pentesting of AI Agents**  
- **Date:** 2026-07-22
- **Authors:** Or Zion Eliav, Eyal Lenga, Shir Bernstien et al.
- **Link:** https://arxiv.org/abs/2607.19837v1
- **Security insight:** Traditional pentesting uses reconnaissance at each step to uncover unseen weaknesses, build stronger attacks, and advance the objective; we argue that AI agents require the same treatment. We formalize agent reconnaissance by modeling the process and…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Twin Agent: Context Residual Compression for Privilege Separated Agents**  
- **Date:** 2026-07-21
- **Authors:** Zhanhao Hu, Dennis Jacob, Xiao Huang et al.
- **Link:** https://arxiv.org/abs/2607.19595v1
- **Security insight:** Large language model (LLM) agents are vulnerable to security risks, such as prompt injection attacks from untrusted context that manipulate downstream reasoning and tool use. Existing secure-by-design approaches mitigate this risk by separating untrusted…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**The safety failures we are not instrumenting: a perspective on hidden safety-critical challenges in modern AI systems**  
- **Date:** 2026-07-21
- **Authors:** Gjergji Kasneci, Enkelejda Kasneci
- **Link:** https://arxiv.org/abs/2607.19292v1
- **Security insight:** Current AI safety discourse still focuses disproportionately on visible failures, including obvious harms, dramatic misuse, and hypothetical catastrophic scenarios. That focus is incomplete. In deployed systems, many of the most consequential failures are…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Data Leakage Prevention in Agentic Applications via Preemptive Hardening**  
- **Date:** 2026-07-21
- **Authors:** Akansha Shukla, Emily Bellov, Parth Atulbhai Gandhi et al.
- **Link:** https://arxiv.org/abs/2607.18847v1
- **Security insight:** Agentic systems integrate LLM driven planning with interfaces to external tools, making data leakage and tool misuse feasible via instruction/data boundary failures and prompt injection attacks. Enforcing required controls consistently is particularly…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**ChainWatch: A Kill Chain-Aligned Sequential Detection Framework for Multi-Step Attacks in MCP-Based AI Agent Systems**  
- **Date:** 2026-07-20
- **Authors:** Om Narayan, Rashmi Jyoti, Ramkinker Singh
- **Link:** https://arxiv.org/abs/2607.19432v1
- **Security insight:** The Model Context Protocol (MCP) is an open-source standard that allows AI agents to connect to external tools, databases, and services. While this connectivity enables powerful agent capabilities, it also introduces multi-step attacks that existing per-call…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Trusted Credentials, Untrusted Behavior: Benchmarking LLM-Agent Security in High-Performance Computing**  
- **Date:** 2026-07-20
- **Authors:** Jie Li
- **Link:** https://arxiv.org/abs/2607.18485v1
- **Security insight:** Large language model (LLM) agents are starting to take on routine work in high-performance computing (HPC), including monitoring Slurm jobs, diagnosing failed builds, inspecting simulation output, and coordinating scientific workflows. To do this work, an…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**ChannelGuard: Safe Models Do Not Compose into Safe Multi-Agent Systems**  
- **Date:** 2026-07-20
- **Authors:** Elias Hossain, Md Mehedi Hasan Nipu, Fatema Tuj Johora Faria et al.
- **Link:** https://arxiv.org/abs/2607.19430v1
- **Security insight:** Multi-agent LLM applications chain a planner, worker agents, a verifier, and a synthesizer, and every hop between agents is an unmonitored channel through which an adversary can smuggle instructions. Existing defenses guard only the input boundary…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**V-DEAL: Diagnosing Video Safety De-Calibration as an Understanding-Refusal Coupling Failure**  
- **Date:** 2026-07-23
- **Authors:** Zhetong Zhang, Honghao Fu, Miao Xu et al.
- **Link:** https://arxiv.org/abs/2607.21151v1
- **Security insight:** As Video Large Language Models are increasingly deployed in real-world applications, ensuring their safety alignment has become critical. Counterintuitively, we find that harmful videos paired with benign queries achieve higher attack success rates than the…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**CPInj: Uncovering Prompt Injection Risks in Textual Collaborative Prompt Optimization**  
- **Date:** 2026-07-21
- **Authors:** Xinting Liao, Behnoosh Zamanlooy, Masoumeh Shafieinejad et al.
- **Link:** https://arxiv.org/abs/2607.18622v1
- **Security insight:** Textual Collaborative Prompt Optimization (TCPO) extends Textgrad (Yuksekgonul et al., 2025) to a decentralized setting by allowing multiple clients to jointly improve prompts for large language models (LLMs) while keeping their data locally. Its reliance on…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### Other (Review)

**What AI Red-Team Evaluations Can and Cannot Prove**  
- **Date:** 2026-07-23
- **Authors:** Bandana Kaur
- **Link:** https://arxiv.org/abs/2607.21735v1
- **Security insight:** Red-team evaluations of AI models support some claims and not others, and the boundary between the two is calculable rather than merely a matter of judgment. We define the evidential ceiling of an evaluation as the largest factor by which one result can move…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
