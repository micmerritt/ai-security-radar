# AI Security Radar

_Last updated (UTC): **2026-03-20**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**VeriGrey: Greybox Agent Validation**  
- **Date:** 2026-03-18
- **Authors:** Yuntong Zhang, Sungmin Kang, Ruijie Meng et al.
- **Link:** https://arxiv.org/abs/2603.17639v1
- **Security insight:** Agentic AI has been a topic of great interest recently. A Large Language Model (LLM) agent involves one or more LLMs in the back-end. In the front end, it conducts autonomous decision-making by combining the LLM outputs with results obtained by invoking…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Caging the Agents: A Zero Trust Security Architecture for Autonomous AI in Healthcare**  
- **Date:** 2026-03-18
- **Authors:** Saikat Maiti
- **Link:** https://arxiv.org/abs/2603.17419v1
- **Security insight:** Autonomous AI agents powered by large language models are being deployed in production with capabilities including shell execution, file system access, database queries, and multi-party communication. Recent red teaming research demonstrates that these agents…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**MCP-38: A Comprehensive Threat Taxonomy for Model Context Protocol Systems (v1.0)**  
- **Date:** 2026-03-18
- **Authors:** Yi Ting Shen, Kentaroh Toyoda, Alex Leung
- **Link:** https://arxiv.org/abs/2603.18063v1
- **Security insight:** The Model Context Protocol (MCP) introduces a structurally distinct attack surface that existing threat frameworks, designed for traditional software systems or generic LLM deployments, do not adequately cover. This paper presents MCP-38, a protocol-specific…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**PAuth - Precise Task-Scoped Authorization For Agents**  
- **Date:** 2026-03-17
- **Authors:** Reshabh K Sharma, Linxi Jiang, Zhiqiang Lin et al.
- **Link:** https://arxiv.org/abs/2603.17170v1
- **Security insight:** The emerging agentic web envisions AI agents that reliably fulfill users' natural-language (NL)-based tasks by interacting with existing web services. However, existing authorization models are misaligned with this vision. In particular, today's operator-…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**CoMAI: A Collaborative Multi-Agent Framework for Robust and Equitable Interview Evaluation**  
- **Date:** 2026-03-17
- **Authors:** Gengxin Sun, Ruihao Yu, Liangyi Yin et al.
- **Link:** https://arxiv.org/abs/2603.16215v1
- **Security insight:** Ensuring robust and fair interview assessment remains a key challenge in AI-driven evaluation. This paper presents CoMAI, a general-purpose multi-agent interview framework designed for diverse assessment scenarios. In contrast to monolithic single-agent…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**How Vulnerable Are AI Agents to Indirect Prompt Injections? Insights from a Large-Scale Public Competition**  
- **Date:** 2026-03-16
- **Authors:** Mateusz Dziemian, Maxwell Lin, Xiaohan Fu et al.
- **Link:** https://arxiv.org/abs/2603.15714v1
- **Security insight:** LLM based agents are increasingly deployed in high stakes settings where they process external data sources such as emails, documents, and code repositories. This creates exposure to indirect prompt injection attacks, where adversarial instructions embedded…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**PISmith: Reinforcement Learning-based Red Teaming for Prompt Injection Defenses**  
- **Date:** 2026-03-13
- **Authors:** Chenlong Yin, Runpeng Geng, Yanting Wang et al.
- **Link:** https://arxiv.org/abs/2603.13026v1
- **Security insight:** Prompt injection poses serious security risks to real-world LLM applications, particularly autonomous agents. Although many defenses have been proposed, their robustness against adaptive attacks remains insufficiently evaluated, potentially creating a false…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Prompt Control-Flow Integrity: A Priority-Aware Runtime Defense Against Prompt Injection in LLM Systems**  
- **Date:** 2026-03-19
- **Authors:** Md Takrim Ul Alam, Akif Islam, Mohd Ruhul Ameen et al.
- **Link:** https://arxiv.org/abs/2603.18433v1
- **Security insight:** Large language models (LLMs) deployed behind APIs and retrieval-augmented generation (RAG) stacks are vulnerable to prompt injection attacks that may override system policies, subvert intended behavior, and induce unsafe outputs. Existing defenses often treat…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

**Amplification Effects in Test-Time Reinforcement Learning: Safety and Reasoning Vulnerabilities**  
- **Date:** 2026-03-16
- **Authors:** Vanshaj Khattar, Md Rafi ur Rashid, Moumita Choudhury et al.
- **Link:** https://arxiv.org/abs/2603.15417v1
- **Security insight:** Test-time training (TTT) has recently emerged as a promising method to improve the reasoning abilities of large language models (LLMs), in which the model directly learns from test data without access to labels. However, this reliance on test data also makes…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### RAG & Retrieval Attacks

**Parameter-Efficient Modality-Balanced Symmetric Fusion for Multimodal Remote Sensing Semantic Segmentation**  
- **Date:** 2026-03-18
- **Authors:** Haocheng Li, Juepeng Zheng, Shuangxi Miao et al.
- **Link:** https://arxiv.org/abs/2603.17705v1
- **Security insight:** Multimodal remote sensing semantic segmentation enhances scene interpretation by exploiting complementary physical cues from heterogeneous data. Although pretrained Vision Foundation Models (VFMs) provide strong general-purpose representations, adapting them…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**Mechanistic Origin of Moral Indifference in Language Models**  
- **Date:** 2026-03-16
- **Authors:** Lingyu Li, Yan Teng, Yingchun Wang
- **Link:** https://arxiv.org/abs/2603.15615v1
- **Security insight:** Existing behavioral alignment techniques for Large Language Models (LLMs) often neglect the discrepancy between surface compliance and internal unaligned representations, leaving LLMs vulnerable to long-tail risks. More crucially, we posit that LLMs possess…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

**TabKD: Tabular Knowledge Distillation through Interaction Diversity of Learned Feature Bins**  
- **Date:** 2026-03-16
- **Authors:** Shovon Niverd Pereira, Krishna Khadka, Yu Lei
- **Link:** https://arxiv.org/abs/2603.15481v1
- **Security insight:** Data-free knowledge distillation enables model compression without original training data, critical for privacy-sensitive tabular domains. However, existing methods does not perform well on tabular data because they do not explicitly address feature…
- **Build idea:** Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes.

### Adversarial ML

**Sirens' Whisper: Inaudible Near-Ultrasonic Jailbreaks of Speech-Driven LLMs**  
- **Date:** 2026-03-14
- **Authors:** Zijian Ling, Pingyi Hu, Xiuyong Gao et al.
- **Link:** https://arxiv.org/abs/2603.13847v1
- **Security insight:** Speech-driven large language models (LLMs) are increasingly accessed through speech interfaces, introducing new security risks via open acoustic channels. We present Sirens' Whisper (SWhisper), the first practical framework for covert prompt-based attacks…
- **Build idea:** Build a robustness benchmark harness with standard perturbations and report concrete failure modes.

### Other (Review)

**When Scanners Lie: Evaluator Instability in LLM Red-Teaming**  
- **Date:** 2026-03-15
- **Authors:** Lidor Erez, Omer Hofman, Tamir Nizri et al.
- **Link:** https://arxiv.org/abs/2603.14633v1
- **Security insight:** Automated LLM vulnerability scanners are increasingly used to assess security risks by measuring different attack type success rates (ASR). Yet the validity of these measurements hinges on an often-overlooked component: the evaluator who determines whether an…
- **Build idea:** Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk.
