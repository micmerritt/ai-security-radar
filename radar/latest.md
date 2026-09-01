# AI Security Radar

_Last updated (UTC): **2026-09-01**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**ECLIPSE: Self-Evolving Stealthy Prompt Injection Attack against Long-Horizon Agentic Systems**  
- **Date:** 2026-08-31
- **Authors:** Shiqian Zhao, Yangfan Zhou, Xinfeng Li et al.
- **Link:** https://arxiv.org/abs/2608.30441v1
- **Security insight:** Recently, large language model (LLM) agents, such as Codex, Claude Code, and OpenClaw, have become capable of planning and executing long-horizon tasks through repeated tool calls. This capability also creates new opportunities for prompt injection. Existing…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Attesting Outputs and Delegation Ancestry in Multi-Agent AI Systems**  
- **Date:** 2026-08-31
- **Authors:** Lifei Liu, Haoran Yu
- **Link:** https://arxiv.org/abs/2608.30387v1
- **Security insight:** Multi-agent applications delegate work across independently operated deployers. After an incident, a verifier must answer two questions: which deployer released the reported bytes, and whether each cross-deployer edge was authorized. Credentials establish who…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Will the User Ever Know? Covert Indirect Prompt Injection on Tool-Using LLM Agents**  
- **Date:** 2026-08-31
- **Authors:** Yunseok Lee, Yunji Kim, Woojin Lee
- **Link:** https://arxiv.org/abs/2608.30362v1
- **Security insight:** As LLM agents take real-world actions through tools, indirect prompt injection (IPI) has emerged as a serious threat. The standard metric, Attack Success Rate (ASR), counts whether an injection succeeds but ignores what the user notices in the agent's final…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**SIR: Self-improving Red-teaming for Compute Use Agents**  
- **Date:** 2026-08-31
- **Authors:** Chen Xiong, Zhiyuan He, Pin-Yu Chen et al.
- **Link:** https://arxiv.org/abs/2608.30207v1
- **Security insight:** Computer use agents (CUAs) are vision-language models that perceive a screen and act on a real operating system through mouse, keyboard, and terminal, and they are increasingly deployed to automate everyday digital tasks. Because they can be exposed to…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Zero-Knowledge Predicate Proofs Between AI Agents: A Measured, Cross-Protocol Gateway and the Source-Integrity Gap**  
- **Date:** 2026-08-30
- **Authors:** Ashok Subbabhatta Gopalakrishna
- **Link:** https://arxiv.org/abs/2608.30083v1
- **Security insight:** Multi-agent AI platforms move quickly from staging to production, but the way agents establish trust remains rudimentary: an agent either transmits raw data to a peer or accepts that peer's natural-language self-report that a value complies with policy. The…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Reachability-Based Capability Confinement for LLM Agents under Indirect Prompt Injection**  
- **Date:** 2026-08-30
- **Authors:** Wujie Xiong, Rabimba Karanjai, Yang Lu et al.
- **Link:** https://arxiv.org/abs/2608.30041v1
- **Security insight:** Large language model agents place outputs from external skills into their execution context, allowing attacker-controlled data to influence later privileged actions. Existing defenses mainly classify untrusted content or authorize proposed operations. They do…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**CAITLYN: Can LLM Agents Autonomously Synthesize Defenses against Emerging Injection Attacks?**  
- **Date:** 2026-08-28
- **Authors:** Zi Liang, Xiaoyu Xu, Yanyun Wang et al.
- **Link:** https://arxiv.org/abs/2608.27990v1
- **Security insight:** Prompt injection attacks on Large Language Model (LLM) agents seek to introduce malicious instructions or content into external text sources retrieved by agents, forcing the underlying LLMs to execute harmful actions outside their benign scope. While current…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**The Framing Gap: Indirect Prompt-Injection Exfiltration Defeats Surface-Level Defenses in Tool-Using Agents**  
- **Date:** 2026-08-27
- **Authors:** Md Habibur Rahman, Jaeho Kim
- **Link:** https://arxiv.org/abs/2608.27092v1
- **Security insight:** A tool-using LLM agent that reads attacker-controlled web content while holding a secret faces indirect prompt injection: the content may make it exfiltrate the secret. In a safe synthetic lab (canary secret, mock tools, matched clean-vs-poisoned metric) we…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**LongPIBench: A Long-Context Benchmark for Prompt Injection**  
- **Date:** 2026-08-28
- **Authors:** Yupei Liu, Yuqi Jia, Neil Zhenqiang Gong et al.
- **Link:** https://arxiv.org/abs/2608.28411v1
- **Security insight:** Prompt injection attacks pose a serious security risk to large language models in real-world applications. However, existing prompt injection benchmarks primarily focus on short-context inputs, leaving the attacks and defenses in long-context settings largely…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**TACS: Trajectory-Aware Candidate Selection for LLM Jailbreak Suffix Optimization**  
- **Date:** 2026-08-30
- **Authors:** Shiliang Xiao
- **Link:** https://arxiv.org/abs/2608.29564v1
- **Security insight:** Gradient-based jailbreak suffix optimization methods typically update the suffix by retaining the candidate with the lowest current loss. We show that this seemingly natural design is fundamentally myopic: candidates that look better under the current-step…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**WoE Wrote It? Watermarking Mixture-of-Experts LLMs for Black-Box Text Provenance**  
- **Date:** 2026-08-29
- **Authors:** Jona te Lintelo, Lichao Wu, Stjepan Picek
- **Link:** https://arxiv.org/abs/2608.29151v1
- **Security insight:** Large Language Model (LLM) watermarks provide a mechanism for text provenance, enabling model owners to identify machine-generated content and attribute it to a specific watermarked model. However, current LLM watermarking approaches predominantly rely on…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**Curvature Cryptanalysis of Smooth Transformer Feed-Forward Networks**  
- **Date:** 2026-08-28
- **Authors:** Munawar Hasan, Apostol Vassilev
- **Link:** https://arxiv.org/abs/2608.28843v1
- **Security insight:** We show that smooth two-layer feed-forward networks (FFNs) expose an additional structural model extraction channel under a chosen-input raw-output oracle at the FFN branch; consider transformer FFN branches with GELU or SiLU activations under chosen-input…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**Layered LLM Defenses as an Ensemble: Access Tiers, Inference Cost, and the Measured Failure Correlation Between Defense Layers**  
- **Date:** 2026-08-28
- **Authors:** Abrar Alotaibi, Muhammad Shahid Jabbar, Sadam Al-Azani et al.
- **Link:** https://arxiv.org/abs/2608.28327v1
- **Security insight:** Practitioners defend large language models (LLMs) by stacking defenses, assuming the layers compound. A stack is an ensemble, and ensembles compound only under a condition the LLM security literature recommends but never measures: the members must fail on…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Model Extraction & Privacy

**JudgeStealer: Extracting LLM Judging Capabilities across Evaluation Protocols**  
- **Date:** 2026-08-27
- **Authors:** Chen Chen, Yaolin Chen, Xuehan Sun et al.
- **Link:** https://arxiv.org/abs/2608.26982v1
- **Security insight:** Large language model (LLM) judges are increasingly used across various evaluation scenarios, making their judgment capabilities valuable intellectual property. However, black-box access exposes these capabilities to model extraction attacks. Existing…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?
