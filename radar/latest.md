# AI Security Radar

_Last updated (UTC): **2026-08-29**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**The Framing Gap: Indirect Prompt-Injection Exfiltration Defeats Surface-Level Defenses in Tool-Using Agents**  
- **Date:** 2026-08-27
- **Authors:** Md Habibur Rahman, Jaeho Kim
- **Link:** https://arxiv.org/abs/2608.27092v1
- **Security insight:** A tool-using LLM agent that reads attacker-controlled web content while holding a secret faces indirect prompt injection: the content may make it exfiltrate the secret. In a safe synthetic lab (canary secret, mock tools, matched clean-vs-poisoned metric) we…
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

**Beyond the Mandate: A Systematic Security Analysis of the Agent Payments Protocol (AP2)**  
- **Date:** 2026-08-24
- **Authors:** Avital Aviv, Parth A. Gandh, Ron Bitton et al.
- **Link:** https://arxiv.org/abs/2608.23858v1
- **Security insight:** The Agent Payments Protocol (AP2), introduced by Google, enables large language model (LLM)-driven shopping agents to authorize and execute payments on behalf of users. Its signed Checkout and Payment Mandates protect the integrity of transaction data after…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**TrustShiftProbe: Characterizing, Benchmarking, and Defending Staged Trust Attacks on MCP Servers**  
- **Date:** 2026-08-24
- **Authors:** Mehrdad Rostamzadeh, Sidhant Narula, Mohammad Ghasemigol et al.
- **Link:** https://arxiv.org/abs/2608.23763v1
- **Security insight:** The Model Context Protocol (MCP) has emerged as the standard layer connecting Large Language Model agents to external tool backends. This openness introduces a severe server-side threat we term TrustShift: a compromised MCP server behaves benignly during an…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**AI-Assisted Extraction of Follow-up Observations from GCN Circulars in Astro-COLIBRI**  
- **Date:** 2026-08-24
- **Authors:** Fabian Schüssler, S. Bisero, M. Cellier et al.
- **Link:** https://arxiv.org/abs/2608.23270v1
- **Security insight:** We present a new Astro-COLIBRI component that converts free-text GCN Circulars into structured, event-linked follow-up records and combines them with structured reports submitted directly by the community. A continuously running Circular listener associates…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**AgentFlow: A Flow-Centric Policy Language and Framework for Securing LLM Agent Systems**  
- **Date:** 2026-08-24
- **Authors:** Basavesh Ammanaghatta Shivakumar, Swarn Priya, Peng Gao
- **Link:** https://arxiv.org/abs/2608.22868v1
- **Security insight:** LLM agents increasingly read untrusted content, invoke external tools, access private data, and delegate work to other agents. Harm often arises not from a single unsafe action but from the flow of sensitive data across a sequence of otherwise plausible…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**The Latent Diagnostic Taxonomy: A Framework for Constructing Classifiers and Diagnosing Their Decisions, Applied to Prompt Injection Detection**  
- **Date:** 2026-08-26
- **Authors:** Jaturong Kongmanee, Smile Thanapattheerakul
- **Link:** https://arxiv.org/abs/2608.26423v1
- **Security insight:** This paper proposes a framework for constructing a classifier as a safeguard layer, and for developing a complementary diagnostic that identifies which of the classifier's confident decisions can be trusted. This framework, the Latent Diagnostic Taxonomy,…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Semantic Overlays: Mitigating Prompt Injection with Annotations Beyond Tokens and Steering Vectors**  
- **Date:** 2026-08-24
- **Authors:** Joshua Penman
- **Link:** https://arxiv.org/abs/2608.23873v1
- **Security insight:** Everything a language model sees is tokens. The serving stack knows what each span is -- user input, tool output, instructions -- but the model must keep track of that itself, and it can lose track or be confused: text can be written to read like anything.…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**GAP-Prompt: Gated Adaptive Prompting for Efficient Continual Learning**  
- **Date:** 2026-08-24
- **Authors:** Trung-Anh Dang, Duy-Cuong Bui, Ngoc-Son Vu et al.
- **Link:** https://arxiv.org/abs/2608.23782v1
- **Security insight:** Continual learning faces the persistent challenge of catastrophic forgetting, where sequential task updates degrade previously acquired knowledge. While prompt-based methods integrated with pre-trained models offer a compelling solution by freezing the…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Breakout/Interchange Reconnection as a driver of Jets, Fast CME, and Solar Energetic Particles**  
- **Date:** 2026-08-24
- **Authors:** Pankaj Kumar, Judith T. Karpen, David Lario et al.
- **Link:** https://arxiv.org/abs/2608.23362v1
- **Security insight:** Understanding how energetic particles are accelerated and released from the low corona into the interplanetary medium during solar eruptions is crucial for space weather research. Here, we present multiwavelength observations of a solar eruption that are…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

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
