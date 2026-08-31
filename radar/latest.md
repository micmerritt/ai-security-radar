# AI Security Radar

_Last updated (UTC): **2026-08-31**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

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

**ROPE: Routed Origin Policy Enforcement against Indirect Prompt Injection**  
- **Date:** 2026-08-27
- **Authors:** Xinhang Ma, Chaowei Xiao, William Yeoh et al.
- **Link:** https://arxiv.org/abs/2608.27496v1
- **Security insight:** Indirect prompt injection (IPI) plants instructions in the content a tool-using LLM agent reads, steering the agent into harmful tool calls. The strongest defenses are system-level, leveraging techniques such as task-conditional tool screening to prevent…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**A Self-Evolving Multi-Agent Framework Defense against LLM Jailbreak Attacks**  
- **Date:** 2026-08-26
- **Authors:** Tongyan Hu, Bryan Hooi
- **Link:** https://arxiv.org/abs/2608.26008v1
- **Security insight:** Large language models (LLMs) remain vulnerable to jailbreak attacks that exploit techniques such as role-playing, obfuscation, code transformation, and multi-step indirection to elicit harmful outputs. As jailbreak strategies keep emerging, defenses have…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**What Guides the Agent? Adjudicating Unauthorized Behavior via Localizing Behavior-Guiding Instructions**  
- **Date:** 2026-08-25
- **Authors:** Yichao Gao, Yumo Zhang, Yunhao Yao et al.
- **Link:** https://arxiv.org/abs/2608.24022v1
- **Security insight:** LLM agents integrated with external resources gain complex task capabilities, yet the unified natural-language context channel makes them vulnerable to injection attacks: untrusted external data may be dynamically parsed as behavior-guiding instructions…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**WebMCP-Phalanx: Enforcing and Characterizing Trust Boundaries for Browser-Integrated LLM Agents**  
- **Date:** 2026-08-25
- **Authors:** Lin-Fa Lee, YI-YU Chang, Kuo-Hui Yeh
- **Link:** https://arxiv.org/abs/2608.24017v1
- **Security insight:** The emerging W3C WebMCP proposal enables LLM agents to invoke tools exposed by web pages. In multi-party web environments, however, integrating agent execution into a browser security model centered on the Same-Origin Policy (SOP) leaves insufficient…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**LongPIBench: A Long-Context Benchmark for Prompt Injection**  
- **Date:** 2026-08-28
- **Authors:** Yupei Liu, Yuqi Jia, Neil Zhenqiang Gong et al.
- **Link:** https://arxiv.org/abs/2608.28411v1
- **Security insight:** Prompt injection attacks pose a serious security risk to large language models in real-world applications. However, existing prompt injection benchmarks primarily focus on short-context inputs, leaving the attacks and defenses in long-context settings largely…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**The Latent Diagnostic Taxonomy: A Framework for Constructing Classifiers and Diagnosing Their Decisions, Applied to Prompt Injection Detection**  
- **Date:** 2026-08-26
- **Authors:** Jaturong Kongmanee, Smile Thanapattheerakul
- **Link:** https://arxiv.org/abs/2608.26423v1
- **Security insight:** This paper proposes a framework for constructing a classifier as a safeguard layer, and for developing a complementary diagnostic that identifies which of the classifier's confident decisions can be trusted. This framework, the Latent Diagnostic Taxonomy,…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Semantic Overlays: Mitigating Prompt Injection with Annotations Beyond Tokens and Steering Vectors**  
- **Date:** 2026-08-24
- **Authors:** Joshua Penman
- **Link:** https://arxiv.org/abs/2608.23873v2
- **Security insight:** Everything a language model sees is tokens. The serving stack knows what each span is -- user input, tool output, instructions -- but the model must keep track of that itself, and can lose track or be confused: text can be written to read like anything.…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**Layered LLM Defenses as an Ensemble: Access Tiers, Inference Cost, and the Measured Failure Correlation Between Defense Layers**  
- **Date:** 2026-08-28
- **Authors:** Abrar Alotaibi, Muhammad Shahid Jabbar, Sadam Al-Azani et al.
- **Link:** https://arxiv.org/abs/2608.28327v1
- **Security insight:** Practitioners defend large language models (LLMs) by stacking defenses, assuming the layers compound. A stack is an ensemble, and ensembles compound only under a condition the LLM security literature recommends but never measures: the members must fail on…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**eBPF-Based Cybersecurity Mechanisms: A Systematic Literature Review**  
- **Date:** 2026-08-27
- **Authors:** Stamatios Kostopoulos, Panagiotis Tsakonas, Evangelos K. Markakis
- **Link:** https://arxiv.org/abs/2608.27511v1
- **Security insight:** Extended Berkeley Packet Filter (eBPF) has emerged as a kernel-level framework enabling dynamic security enforcement in modern operating systems. While eBPF's cybersecurity potential has attracted significant attention, existing work remains fragmented across…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**Circuit Discovery Helps Detect LLM Jailbreaking: A Mechanistic Interpretability Study**  
- **Date:** 2026-08-27
- **Authors:** Paria Mehrbod, Boris Knyazev, Guy Wolf et al.
- **Link:** https://arxiv.org/abs/2608.27504v1
- **Security insight:** Despite extensive safety alignment, large language models (LLMs) remain vulnerable to jailbreak attacks that bypass safeguards to elicit harmful content. While prior work attributes this vulnerability to safety training limitations, the internal mechanisms by…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Model Extraction & Privacy

**JudgeStealer: Extracting LLM Judging Capabilities across Evaluation Protocols**  
- **Date:** 2026-08-27
- **Authors:** Chen Chen, Yaolin Chen, Xuehan Sun et al.
- **Link:** https://arxiv.org/abs/2608.26982v1
- **Security insight:** Large language model (LLM) judges are increasingly used across various evaluation scenarios, making their judgment capabilities valuable intellectual property. However, black-box access exposes these capabilities to model extraction attacks. Existing…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

### Other (Review)

**LMSM: LLM Security Framework Inspired by Linux Security Modules**  
- **Date:** 2026-08-26
- **Authors:** XiuYu Zhang, Bonan Ruan, Junfeng Fang et al.
- **Link:** https://arxiv.org/abs/2608.25697v1
- **Security insight:** Large language models (LLMs) are increasingly deployed with layered defenses, yet malicious prompts can still bypass them. Interpretability methods can expose model-internal signals along the generation path that could inform enforcement, but these signals…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
