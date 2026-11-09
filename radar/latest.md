# AI Security Radar

_Last updated (UTC): **2026-11-09**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Prompt Injection

**Notwithstanding Anything to the Contrary, Ignore All Instructions: Measuring Prompt Injection Guards on Legal Contract Review Attacks**  
- **Date:** 2026-11-06
- **Authors:** Mark Heimann, Katherine Taylor, Bruno Jacob
- **Link:** https://arxiv.org/abs/2611.08834v1
- **Security insight:** Specialized prompt injection guards are deployed in front of document analysis systems, but no false positive rate has been published for any of them on legal contracts. We measure eleven open-weights guards on two corpora of legal contracts and find that…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**I Think, Therefore I Attack: Evaluating Thought Injection Attacks on Reasoning Agents**  
- **Date:** 2026-11-06
- **Authors:** Parth Illendula, Garik Livingston, Zain Shamsi et al.
- **Link:** https://arxiv.org/abs/2611.08811v1
- **Security insight:** Large Reasoning Models (LRMs) are one of the key components of current agentic systems. LRMs augment their output with an explicit chain-of-thought reasoning stage, introducing a new attack surface for thought injection, in which untrusted text resembling the…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

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

### Poisoning & Backdoors

**Interactive Backdoor Attacks in LLM-Based Proactive Dialogue Systems**  
- **Date:** 2026-11-04
- **Authors:** Zhiyang Xia, Yuming Shang, Xi Zhang
- **Link:** https://arxiv.org/abs/2611.06969v1
- **Security insight:** LLM-based proactive dialogue systems provide goal-directed support through sustained interaction. Fine-tuning their underlying models on externally supplied dialogue data introduces backdoor risks. Existing LLM backdoor studies primarily focus on eliciting an…
- **Build idea:** Build a minimal poisoning simulator plus simple detectors (trigger search, label flip tests, anomaly baselines).

### Model Extraction & Privacy

**Cutpurse: Decomposing Explanation-Guided Model Extraction on Tabular Data**  
- **Date:** 2026-11-06
- **Authors:** Seyma Selcan Magara, Hanru Zhang, Fatme El Zahraa Hamad et al.
- **Link:** https://arxiv.org/abs/2611.09375v1
- **Security insight:** Explanation APIs are often treated as increasing model-extraction risk, but an end-to-end attack comparison cannot show whether an explanation reveals model-specific information or merely supplies a convenient next-query coordinate. We study this distinction…
- **Build idea:** Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?

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

**GreyZone: Production-quality Agentic Application Threats**  
- **Date:** 2026-11-06
- **Authors:** Ruoyu Zhou, Shuyao Jiang, Haifeng Ruan et al.
- **Link:** https://arxiv.org/abs/2611.09161v1
- **Security insight:** Agents are increasingly deployed across domains such as coding, banking, and commerce. Their ability to invoke tools and change application state makes security testing important for reliable deployment. Although agent security has been studied through…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

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
