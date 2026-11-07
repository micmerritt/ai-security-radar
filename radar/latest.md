# AI Security Radar

_Last updated (UTC): **2026-11-07**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

**The Power of Meta Access in the Software of the Future --- Demonstrated on LLM Chat UIs and Chat AI**  
- **Date:** 2026-11-05
- **Authors:** Julian Kunkel, Ali Doosthosseini
- **Link:** https://arxiv.org/abs/2611.08428v1
- **Security insight:** Chat remains the default surface for many large language model (LLM) tasks, even as agentic tools such as OpenCode excel at coding and automation. Yet the model sees the current dialogue but not the workspace around it. We explore meta access---giving the…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Beyond Instruction Override: Benchmarking Indirect Prompt Injection with Task-Tampering Attacks**  
- **Date:** 2026-11-05
- **Authors:** Rongting Zhang, Martin Bertran, Sandeep Avula et al.
- **Link:** https://arxiv.org/abs/2611.07640v1
- **Security insight:** Indirect prompt-injection (IPI) benchmarks predominantly test planted instructions that redirect a tool-using agent toward an attacker-chosen task. Yet attacker-controlled content can instead tamper with the outcome of the task already in progress. A buyer's…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**SPILLWAY: Separating Target Admission from Sanitization to Defend Tool-Using Agents against Prompt Injection**  
- **Date:** 2026-11-04
- **Authors:** Woosang Lim, Yeseul Chang, Jaewoo Lee
- **Link:** https://arxiv.org/abs/2611.07222v1
- **Security insight:** Tool-using agents act on email, files, and payments, so an instruction hidden in a web page or a shared document can make an agent send data or money to an attacker. Many runtime defenses put a language model on the decision that lets an action through, so…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**SecureGARD: Dynamic Ontology-Guided Governance for Secure Tool-Using LLM Agents**  
- **Date:** 2026-11-04
- **Authors:** Guoqin Xiong, Shengtao Wen, Xiang Chen et al.
- **Link:** https://arxiv.org/abs/2611.06682v1
- **Security insight:** Tool-using large language model (LLM) agents translate model outputs into consequential actions, turning indirect prompt injection into an execution-security problem. Existing defenses constrain tool calls, trajectories, or information flows, but often leave…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Right Tool, Wrong Parameters: Defending LLM Agents Against Parameter Poisoning**  
- **Date:** 2026-11-03
- **Authors:** Yao Wang, Zehua Ma, Weiming Zhang et al.
- **Link:** https://arxiv.org/abs/2611.04673v1
- **Security insight:** Indirect Prompt Injection (IPI) poses a critical threat to LLM agents. Existing defenses largely focus on whether an injection induces a new tool invocation or unintended action. In this paper, we study a different attack surface, parameter poisoning, where…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**The Devil is in the Context: Nine Dimensions of Prompt Injection Attacks**  
- **Date:** 2026-11-03
- **Authors:** Jiamin Chang, Kristina Nikolić, Rishi Sharma et al.
- **Link:** https://arxiv.org/abs/2611.04672v1
- **Security insight:** Prompt injection is usually discussed and evaluated as a single, homogeneous type of attack. However, vulnerabilities reported in real-world systems show that prompt injections vary widely. Moreover, the same instruction can be a prompt injection in one…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**From Guidelines to Practice: Defining Requirements for AI Red-Teaming Tools**  
- **Date:** 2026-11-03
- **Authors:** Gia Phong Tran, Thai Duong Huynh, Randolph Loh et al.
- **Link:** https://arxiv.org/abs/2611.04271v1
- **Security insight:** Artificial Intelligence (AI) has seen significant developments and increased usage in recent years. AI benefits various tasks, automates decision-making, and enhances efficiency. However, AI also introduces additional attack surfaces for threat actors to…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**IAMRAGBENCH: Benchmarking Authorization Expansions in LLM-Generated AWS IAM Policies under RAG Poisoning**  
- **Date:** 2026-11-02
- **Authors:** Hasan Kaplan, Indika Kumara, Willem-Jan van den Heuvel et al.
- **Link:** https://arxiv.org/abs/2611.03431v1
- **Security insight:** Large language models (LLMs) using retrieval-augmented generation (RAG) can synthesize Amazon Web Services (AWS) Identity and Access Management (IAM) policies from tasks and operational documents. Attacker-controlled context may induce provider-valid policies…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Poisoning & Backdoors

**Interactive Backdoor Attacks in LLM-Based Proactive Dialogue Systems**  
- **Date:** 2026-11-04
- **Authors:** Zhiyang Xia, Yuming Shang, Xi Zhang
- **Link:** https://arxiv.org/abs/2611.06969v1
- **Security insight:** LLM-based proactive dialogue systems provide goal-directed support through sustained interaction. Fine-tuning their underlying models on externally supplied dialogue data introduces backdoor risks. Existing LLM backdoor studies primarily focus on eliciting an…
- **Build idea:** Build a minimal poisoning simulator plus simple detectors (trigger search, label flip tests, anomaly baselines).

### Model Extraction & Privacy

**Breaking $\mathsf{TraintoDefend}$ via Adaptive Neuron Clustering in Cryptanalytic Model Extraction**  
- **Date:** 2026-11-05
- **Authors:** Haojie Wu, Haolin Liu, Tianshuo Cong et al.
- **Link:** https://arxiv.org/abs/2611.07370v1
- **Security insight:** Cryptanalytic model extraction poses a fundamental threat to deep learning model confidentiality by enabling precise parameter recovery with theoretical guarantees of functional equivalence. To counter this growing threat, $\mathsf{TraintoDefend}$ (NeurIPS…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

**Fingerprinting the Dispatchers behind Distributed Model Extraction**  
- **Date:** 2026-11-04
- **Authors:** Snigdha Chandan Khilar
- **Link:** https://arxiv.org/abs/2611.06661v1
- **Security insight:** API distillation campaigns try to hide model-stealing traffic by splitting requests across thousands of load-balanced accounts, which standard content classifiers often miss. However, request timestamps, specifically arrival time and stream completion time,…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

### Adversarial ML

**ScamWorld: An Interactive Environment for Evaluating Web Agents Against Online Fraud**  
- **Date:** 2026-11-03
- **Authors:** Yutao Wu, Xiao Liu, Ming Wen et al.
- **Link:** https://arxiv.org/abs/2611.04879v2
- **Security insight:** Web agents increasingly browse, shop, and manage accounts on behalf of their users. Prior work has shown that they can be misled by adversarial content, including prompt injections and deceptive interfaces. Beyond such attacks, agents operating on the open…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

### Agent & Tool Security

**Multimodal-SEA: Benchmarking AI Agent Security under Multimodal Social Engineering Attacks**  
- **Date:** 2026-11-05
- **Authors:** Zhitao He, Chi Him Zhang, Chengru Han et al.
- **Link:** https://arxiv.org/abs/2611.08281v1
- **Security insight:** Personal AI agents face social engineering attacks supported by forged multimodal content, but existing evaluations mainly focus on text-based dialogue, leaving their intrinsic security under such attacks insufficiently studied. We introduce Multimodal-SEA,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Securing Web Agents with the Compile-Then-Execute Paradigm**  
- **Date:** 2026-11-04
- **Authors:** Annabella Chow, Jinhao Zhu, Sylvie Venuto et al.
- **Link:** https://arxiv.org/abs/2611.06039v1
- **Security insight:** Web agents commonly follow the ReAct paradigm, selecting each action from runtime observations that inherently mix trusted and untrusted content. This design makes their control flow vulnerable to prompt injections embedded in webpages. We introduce Baya, a…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.
