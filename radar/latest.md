# AI Security Radar

_Last updated (UTC): **2026-10-06**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

**RAISED: Self-Distillation for Robustness to Prompt Injection in LLM Agents**  
- **Date:** 2026-10-05
- **Authors:** Mohamed Dhouib, Clement Elliker, Alexi Canesse et al.
- **Link:** https://arxiv.org/abs/2610.06401v1
- **Security insight:** Tool-using language-model agents are vulnerable to indirect prompt injection because they must act on untrusted external content. Existing training-time defenses can reduce attack success rates, but often at the cost of general capabilities. We show that…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Compromise Is Not Consequence: Evaluating Task-Scoped Authorization in LLM Agents with Paired Replay**  
- **Date:** 2026-10-05
- **Authors:** Tural Hagverdiyev
- **Link:** https://arxiv.org/abs/2610.05840v1
- **Security insight:** A tool-using model can follow a malicious instruction even when its credentials are valid. We study whether task-scoped authorization contains the resulting tool execution. Our paired-replay testbed samples a model request once and submits the same action,…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Can CaMeLs Talk? Securing Multi-Agent Systems Against Indirect Prompt Injection Attacks**  
- **Date:** 2026-10-05
- **Authors:** James Peters-Gill, Avi Semler, Henning Bartsch et al.
- **Link:** https://arxiv.org/abs/2610.05640v1
- **Security insight:** Indirect prompt injection attacks - malicious instructions embedded in content processed by large language models - remain a major obstacle to safely deploying tool-using agents. CaMeL [Debenedetti et al., 2025] mitigates this threat for an individual agent…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Readable Before Actionable: Causal Tracing of Indirect Prompt Injection**  
- **Date:** 2026-10-04
- **Authors:** Zhe Yu, Wenpeng Xing, Xingxing Yang et al.
- **Link:** https://arxiv.org/abs/2610.05295v1
- **Security insight:** Indirect prompt injection causes LLM agents to follow commands embedded in external data. A probe may distinguish instructions from data without identifying a state edit that changes the next action. We study this gap through counterfactual role probes,…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Who Is Your Agent Serving? Provider-Side Indirect Prompt Injection in Proactive Agents**  
- **Date:** 2026-10-04
- **Authors:** Rui Wang, Chao Wang, Xinchen Wang et al.
- **Link:** https://arxiv.org/abs/2610.05266v1
- **Security insight:** Proactive personal agents increasingly decide what to recommend, how to personalize advice, and what follow-up assistance to offer, creating a new user-decision attack surface for provider-side indirect prompt injection. We show that an external provider need…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Blocking at the Boundary: Auditing Long-Horizon Agents against Staged Prompt Injection**  
- **Date:** 2026-10-04
- **Authors:** Jingkai Liu, Yufei Han, Xiaoting Lyu et al.
- **Link:** https://arxiv.org/abs/2610.05163v1
- **Security insight:** Long-horizon agents consume external content, invoke tools, and modify persistent state. Indirect prompt injection can exploit task-specific context, propagate across causally connected stages, and alter a consequential action while the workflow continues; we…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Hidden Risks of Jev: An Empirical Study of Security, Privacy, and Dual Use**  
- **Date:** 2026-10-04
- **Authors:** Shang Wang, Tianqing Zhu, Huajie Chen et al.
- **Link:** https://arxiv.org/abs/2610.04985v1
- **Security insight:** Jev turns natural-language questions into typed answers and probabilities with low latency and cost, enabling applications to route requests and select tools. While this interface allows Jev to integrate naturally into application workflows as a decision…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Self-Reflection Fine-Tuning: Enhancing Agent Security against Prompt Injection Attacks from Failure Experience**  
- **Date:** 2026-10-03
- **Authors:** Zixuan Wang, Hao Li, Fengyu Gao et al.
- **Link:** https://arxiv.org/abs/2610.04269v1
- **Security insight:** Large language model (LLM) agents are increasingly deployed in tool-augmented environments, but their reliance on external inputs makes them highly vulnerable to prompt injection attacks that can hijack task objectives. Existing safety alignment methods rely…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Self-Propagating Misalignment in LLM Agents, and Why Auditing or Disabling Memory Is Not Enough**  
- **Date:** 2026-10-02
- **Authors:** Debeshee Das, Jacqueline Tay, Bruce Tsai et al.
- **Link:** https://arxiv.org/abs/2610.04083v1
- **Security insight:** Memory poisoning attacks on LLM agents typically assume an external adversary who plants content in the agent's persistent memory to steer its behavior. We instead study, with no adversary involved, whether a misaligned agent can write a goal it cannot yet…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### Model Extraction & Privacy

**Agentic schema-guided extraction of materials process knowledge from scientific literature**  
- **Date:** 2026-10-05
- **Authors:** Sameer Sadruddin, Jennifer D'Souza
- **Link:** https://arxiv.org/abs/2610.06322v1
- **Security insight:** Materials literature contains detailed experimental knowledge, but procedures, chemical entities and measurements remain difficult to aggregate because they are reported in heterogeneous forms and depend on process-specific context. We present SciKGExtract, a…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

### Adversarial ML

**Large Language Models and Augmented Democracy**  
- **Date:** 2026-10-03
- **Authors:** Jairo Gudiño-Rosero
- **Link:** https://arxiv.org/abs/2610.04412v1
- **Security insight:** Artificial intelligence enables computational agents to represent political preferences and take part in collective decision-making. In this thesis, I investigate the opportunities and challenges of digital twins (DTs) based on Large Language Models (LLMs) as…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

### Agent & Tool Security

**TrustMI: Causally controlling how assistants trust their users**  
- **Date:** 2026-10-05
- **Authors:** Théo Lasnier, Romain Froger, Maxence Lasbordes et al.
- **Link:** https://arxiv.org/abs/2610.06064v1
- **Security insight:** Large Language Model (LLM) assistants routinely decide whether they can trust users and third parties whose competence, intentions, and integrity they cannot verify. This uncertainty matters for safety, as trusting the wrong party can lead an agent to comply…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**The Same Zero: Why Identical ASR Can Imply Different Guarantees in LLM-Agent Security**  
- **Date:** 2026-10-03
- **Authors:** YaJie Yin
- **Link:** https://arxiv.org/abs/2610.04504v1
- **Security insight:** LLM-agent security has produced a dense landscape of defenses - prompt hardening, content filters, permission gates, sandboxes - yet no framework tells a deployer what a defense actually guarantees, or where that guarantee comes from. We apply Verification…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Other (Review)

**Correct Verdicts, Flawed Reasoning: Structured Auditing of LLM-based Vulnerability Reasoning**  
- **Date:** 2026-10-05
- **Authors:** Boyue Caroline Hu, Kaivalya Ahir, Ronghao Ni et al.
- **Link:** https://arxiv.org/abs/2610.06366v1
- **Security insight:** Large Language Models (LLMs) are increasingly deployed for automated software vulnerability analysis. Binary classification alone is insufficient; practitioners need explanations to triage bugs and engineer patches. Standard practice relies on Chain-of-…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
