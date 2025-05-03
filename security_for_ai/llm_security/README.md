# LLM Security

We explore LLM Security attacks under the following categories:
* Adversarial attack
  * Backdoor attack - [More info](backdoor.md)
  * Poisoning attack - [More info](poisoning.md)
* Prompt injection - [More info](prompt_injection.md)
 
We explore LLM privacy attacks under the following categories:
* PII leakage
* Gardiant leakage
* Membership inference attacks

For various kinds of attacks, we will be exploring possible defenses as well.

## Recent publications on LLM security and privacy

| Date | ID | Title | Venue | Material | Tags | Code | Summary | 
| --- | --- | --- | --- | --- | --- | --- | --- |
| Aug 2025 | Package_hallucination | We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs | Usenix Security 2025 | [Paper](https://arxiv.org/pdf/2406.10279) | llm, hallucination, packages, code generation | | |
|Apr 2025 | LlamaFirewall | LlamaFirewall: An open source guardrail system for building secure AI agents | Meta | [Paper](https://scontent-lax3-2.xx.fbcdn.net/v/t39.2365-6/494149131_1055202283127335_8271555569134498093_n.pdf) | firewall, llm, agent, open source| | |
| Apr 2025 | Heimdall | Heimdall: test-time scaling on the generative verification | arXiv | [Paper](https://arxiv.org/abs/2504.10337) | CoT verification, RL, AIME2025 | | |
| Mar 2025 | CaMeL | Defeat Prompt Injections by Design | arXiv | [Paper](https://arxiv.org/pdf/2503.18813) | prompt injection, defense, agents, AgentDojo | | |
| Feb 2025 | JBShield | JBShield: Defending Large Language Models from Jailbreak Attacks through Activated Concept Analysis and Manipulation | arXiv | [Paper](https://arxiv.org/abs/2502.07557) | safety alignment, LRH | | |
| Feb 2025 | Firewall_LLM_Agent | Firewalls to Secure Dynamic LLM Agentic Networks | arXiv | [Paper](https://arxiv.org/pdf/2502.01822) | firewall, agents, llm | They identify two required properties for agent communication: privacy and security. They propose a framework to automatically construct and update task-specific rules from prior simulations to build firewalls. | |
| Jan 2025 | Defense_Jailbreak | Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming | arXiv | [Paper](https://arxiv.org/pdf/2501.18837), [Relase Note](https://www.anthropic.com/research/constitutional-classifiers) | aml, robust, universal jailbreak | | |
| Dec 2024 | BoN | Best-of-N Jailbreaking | arXiv | [paper](https://arxiv.org/abs/2412.03556) | Jailbreaking, Prompt Injection |  | [Summary](reviews/bon.md) |
| Oct 2024 | ASB | Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-Based Agents | arXiv | [paper](https://arxiv.org/pdf/2410.02644) | LLM Agents, Benchmark, Attacks, Defenses |  | [Summary](reviews/asb.md)|
| Aug 2024 | Malla | Malla: Demystifying Real-World Large Language Model Integrated Malicious Services | Usenix Security | [paper](https://www.usenix.org/system/files/usenixsecurity24-lin-zilong.pdf) | Malicious LLMs, Jailbreaking, Darkweb | | [Summary](reviews/malla.md)|
| Mar 2024 | PI_LLM_Apps | Prompt Inject Attack Against LLM-Integrated Applications | arXiv | [paper](https://arxiv.org/pdf/2306.05499) | Prompt Injection, LLM-Integrated Apps |  | [Summary](reviews/pi_llm_apps.md)|

## Blogs
* [05-01-2025] [Report](https://media.licdn.com/dms/document/media/v2/D561FAQGg9Ds3rhaGPw/feedshare-document-pdf-analyzed/B56ZaSGr9wHgAY-/0/1746207963856) AI agents are here. So are the threats by Palo Alto Networks.

## Open Source LLM Security Tools and Products
* LlamaFirewall by Meta [Github](https://meta-llama.github.io/PurpleLlama/LlamaFirewall/)
* Invariant guardrails for agentic systems [Github](https://github.com/invariantlabs-ai/invariant)
* Granite Guardian by IBM [Github](https://github.com/ibm-granite/granite-guardian)
* NeMo-Guardrails by Nvidia [Github](https://github.com/NVIDIA/NeMo-Guardrails)
* Guardrails by GuardrailsAI [Github](https://github.com/guardrails-ai/guardrails)
* LLM-Guard by ProtectAI [Github](https://github.com/protectai/llm-guard)
* Fast LLM Security Guardrails by ZenGuardAI [Github](https://github.com/ZenGuard-AI/fast-llm-security-guardrails)
* LangKit by Why Labs [Github](https://github.com/whylabs/langkit)
* PurpleLlama by Meta [Github](https://github.com/meta-llama/PurpleLlama)
* LLM Guard by Protect AI [Tool](https://llm-guard.com)
* HeimdaLLM [Github](https://github.com/amoffat/HeimdaLLM) #staticanalysis Note: not updated since 2/3/2024
* Rebuff by Protect AI [Github](https://github.com/protectai/rebuff) - Note: not updated since 1/19/2024
* Vigil by DeadBits [Github](https://github.com/deadbits/vigil-llm) - Note: Not updated since 12/31/2023
