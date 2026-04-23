# AI Security Radar

_Last updated (UTC): **2026-04-23**_

## What this is

A curated, continuously-updated view of emerging AI security research signals and the build ideas they suggest.

## Tracked keywords

prompt injection, rag poisoning, llm jailbreak, adversarial machine learning, model extraction, training data poisoning, llm security, ai red team, agent security, llm vulnerability

## New / recent research (arXiv)

### Agent & Tool Security

**An AI Agent Execution Environment to Safeguard User Data**  
- **Date:** 2026-04-21
- **Authors:** Robert Stanley, Avi Verma, Lillian Tsai et al.
- **Link:** https://arxiv.org/abs/2604.19657v1
- **Security insight:** AI agents promise to serve as general-purpose personal assistants for their users, which requires them to have access to private user data (e.g., personal and financial information). This poses a serious risk to security and privacy. Adversaries may attack…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**If you're waiting for a sign... that might not be it! Mitigating Trust Boundary Confusion from Visual Injections on Vision-Language Agentic Systems**  
- **Date:** 2026-04-21
- **Authors:** Jiamin Chang, Minhui Xue, Ruoxi Sun et al.
- **Link:** https://arxiv.org/abs/2604.19844v1
- **Security insight:** Recent advances in embodied Vision-Language Agentic Systems (VLAS), powered by large vision-language models (LVLMs), enable AI systems to perceive and reason over real-world scenes. Within this context, environmental signals such as traffic lights are…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Towards Optimal Agentic Architectures for Offensive Security Tasks**  
- **Date:** 2026-04-20
- **Authors:** Isaac David, Arthur Gervais
- **Link:** https://arxiv.org/abs/2604.18718v1
- **Security insight:** Agentic security systems increasingly audit live targets with tool-using LLMs, but prior systems fix a single coordination topology, leaving unclear when additional agents help and when they only add cost. We treat topology choice as an empirical systems…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Different Paths to Harmful Compliance: Behavioral Side Effects and Mechanistic Divergence Across LLM Jailbreaks**  
- **Date:** 2026-04-20
- **Authors:** Md Rysul Kabir, Zoran Tiganj
- **Link:** https://arxiv.org/abs/2604.18510v1
- **Security insight:** Open-weight language models can be rendered unsafe through several distinct interventions, but the resulting models may differ substantially in capabilities, behavioral profile, and internal failure mode. We study behavioral and mechanistic properties of…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Beyond Pattern Matching: Seven Cross-Domain Techniques for Prompt Injection Detection**  
- **Date:** 2026-04-20
- **Authors:** Thamilvendhan Munirathinam
- **Link:** https://arxiv.org/abs/2604.18248v1
- **Security insight:** Current open-source prompt-injection detectors converge on two architectural choices: regular-expression pattern matching and fine-tuned transformer classifiers. Both share failure modes that recent work has made concrete. Regular expressions miss paraphrased…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**A Control Architecture for Training-Free Memory Use**  
- **Date:** 2026-04-20
- **Authors:** Yanzhen Lu, Muchen Jiang, Zhicheng Qian et al.
- **Link:** https://arxiv.org/abs/2604.18206v1
- **Security insight:** Prompt-injected memory can improve reasoning without updating model weights, but it also creates a control problem: retrieved content helps only when it is applied in the right state. We study this problem in a strict training-free setting and formulate it as…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Owner-Harm: A Missing Threat Model for AI Agent Safety**  
- **Date:** 2026-04-20
- **Authors:** Dongcheng Zhang, Yiqing Jiang
- **Link:** https://arxiv.org/abs/2604.18658v1
- **Security insight:** Existing AI agent safety benchmarks focus on generic criminal harm (cybercrime, harassment, weapon synthesis), leaving a systematic blind spot for a distinct and commercially consequential threat category: agents harming their own deployers. Real-world…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**SafeAgent: A Runtime Protection Architecture for Agentic Systems**  
- **Date:** 2026-04-19
- **Authors:** Hailin Liu, Eugene Ilyushin, Jie Ni et al.
- **Link:** https://arxiv.org/abs/2604.17562v1
- **Security insight:** Large language model (LLM) agents are vulnerable to prompt-injection attacks that propagate through multi-step workflows, tool interactions, and persistent context, making input-output filtering alone insufficient for reliable protection. This paper presents…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**The Consensus Trap: Rescuing Multi-Agent LLMs from Adversarial Majorities via Token-Level Collaboration**  
- **Date:** 2026-04-18
- **Authors:** Jiayuan Liu, Shiyi Du, Weihua Du et al.
- **Link:** https://arxiv.org/abs/2604.17139v1
- **Security insight:** Multi-agent large language model (LLM) architectures increasingly rely on response-level aggregation, such as Majority Voting (MAJ), to raise reasoning ceilings. However, in open environments, agents are highly susceptible to stealthy contextual corruption,…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**CASCADE: A Cascaded Hybrid Defense Architecture for Prompt Injection Detection in MCP-Based Systems**  
- **Date:** 2026-04-18
- **Authors:** İpek Abasıkeleş Turgut, Edip Gümüş
- **Link:** https://arxiv.org/abs/2604.17125v1
- **Security insight:** Model Context Protocol (MCP) is a rapidly adopted standard for defining and invoking external tools in LLM applications. The multi-layered architecture of MCP introduces new attack surfaces such as tool poisoning, in addition to traditional prompt injection.…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**HarmChip: Evaluating Hardware Security Centric LLM Safety via Jailbreak Benchmarking**  
- **Date:** 2026-04-18
- **Authors:** Zeng Wang, Minghao Shao, Weimin Fu et al.
- **Link:** https://arxiv.org/abs/2604.17093v1
- **Security insight:** The integration of large language models (LLMs) into electronic design automation (EDA) workflows has introduced powerful capabilities for RTL generation, verification, and design optimization, but also raises critical security concerns. Malicious LLM outputs…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

**Visual Inception: Compromising Long-term Planning in Agentic Recommenders via Multimodal Memory Poisoning**  
- **Date:** 2026-04-18
- **Authors:** Jiachen Qian
- **Link:** https://arxiv.org/abs/2604.16966v1
- **Security insight:** The evolution from static ranking models to Agentic Recommender Systems (Agentic RecSys) empowers AI agents to maintain long-term user profiles and autonomously plan service tasks. While this paradigm shift enhances personalization, it introduces a…
- **Build idea:** Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects.

### Prompt Injection

**Anchor-and-Resume Concession Under Dynamic Pricing for LLM-Augmented Freight Negotiation**  
- **Date:** 2026-04-22
- **Authors:** Hoang Nguyen, Lu Wang, Marta Gaia Bras
- **Link:** https://arxiv.org/abs/2604.20732v1
- **Security insight:** Freight brokerages negotiate thousands of carrier rates daily under dynamic pricing conditions where models frequently revise targets mid-conversation. Classical time-dependent concession frameworks use a fixed shape parameter $β$ that cannot adapt to these…
- **Build idea:** Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline.

### Poisoning & Backdoors

**TrEEStealer: Stealing Decision Trees via Enclave Side Channels**  
- **Date:** 2026-04-20
- **Authors:** Jonas Sander, Anja Rabich, Nick Mahling et al.
- **Link:** https://arxiv.org/abs/2604.18716v1
- **Security insight:** Today, machine learning is widely applied in sensitive, security-related, and financially lucrative applications. Model extraction attacks undermine current business models where a model owner sells model access, e.g., via MLaaS APIs. Additionally, stolen…
- **Build idea:** Build a minimal poisoning simulator plus simple detectors (trigger search, label flip tests, anomaly baselines).
