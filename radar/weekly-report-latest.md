# AI Security Radar Weekly Report

_Week ending (UTC): **2026-03-03**_  

_Issues included: created **since 2026-02-24**_  


## Executive signal

This week’s radar concentrated on agent pipelines and prompt injection style failures. Use the sections below to pull one post, one newsletter block, and one deeper Medium essay.


## Highlights by category


### Prompt Injection

- **DualSentinel: A Lightweight Framework for Detecting Targeted Attacks in Black-box LLM via Dual Entropy Lull Pattern**  
  https://github.com/micmerritt/ai-security-radar/issues/4
  
  arXiv: 2603.01574v1
  
  _Takeaway:_ Recent intelligent systems integrate powerful Large Language Models (LLMs) through APIs, but their trustworthiness may be critically undermined by targeted attacks like backdoor and prompt injection attacks, which secretly force LLMs to…


### Agent And Tool Security

- **From Goals to Aspects, Revisited: An NFR Pattern Language for Agentic AI Systems**  
  https://github.com/micmerritt/ai-security-radar/issues/6
  
  arXiv: 2603.00472v1
  
  _Takeaway:_ Agentic AI systems exhibit numerous crosscutting concerns -- security, observability, cost management, fault tolerance -- that are poorly modularized in current implementations, contributing to the high failure rate of AI projects in…

- **Tracking Capabilities for Safer Agents**  
  https://github.com/micmerritt/ai-security-radar/issues/5
  
  arXiv: 2603.00991v1
  
  _Takeaway:_ AI agents that interact with the real world through tool calls pose fundamental safety challenges: agents might leak private information, cause unintended side effects, or be manipulated through prompt injection. To address these…


## Newsletter block (copy/paste)

AI Security Radar (Weekly)

This week’s theme is the agent pipeline. Multiple papers and defenses are converging on a basic reality: once an LLM can call tools or ingest external context, attackers can steer behavior through indirect prompt injection, poisoned retrieval context, or workflow manipulation.

If you are deploying agentic systems, treat every external input as untrusted, gate tool permissions, and start testing for tool-call abuse the same way you test web apps for injection.


## Medium outline starter (copy/paste)

Title: The Real AI Security Boundary Is the Agent Pipeline

1. Why model-only security is the wrong mental model
2. What changed when agents started calling tools
3. How indirect prompt injection actually lands in real systems
4. Practical controls: permissions, sandboxing, context isolation, allowlists
5. What to test weekly (your harness)
6. What I think happens next
