# LLM Security

We explore LLM Security attacks under the following categories:
* Adversarial attack
  * Backdoor attack - [More info](backdoor.md)
  * Poisoning attack - [More info](poisoning.md)
* Prompt hacking
  * Prompt injection
  * Jailbreaking attack
 
We explore LLM privacy attacks under the following categories:
* PII leakage
* Gardiant leakage
* Membership inference attacks

For various kinds of attacks, we will be exploring possible defenses as well.

## Recent publications on LLM security and privacy

| Date | ID | Title | Venue | Material | Tags | Short Summary | Summary | 
| --- | --- | --- | --- | --- | --- | --- | --- |
| Jan 2025 | Defense_Jailbreak | Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming | arXiv | [Paper](https://arxiv.org/pdf/2501.18837), [Relase Note](https://www.anthropic.com/research/constitutional-classifiers) | aml, robust, universal jailbreak | | |
| Dec 2024 | BoN | Best-of-N Jailbreaking | arXiv | [paper](https://arxiv.org/abs/2412.03556) | Jailbreaking, Prompt Injection | Best-of-N (BoN) algorithm that jailbreaks frontier multi-modal models. It works by repeatedly sampling variations of a prompt with a combination of augmentations such as random shuffling or capitalization for textual prompts, until a harmful response is elicited. ASR of 89% on GPT-4o and 78% on Claude 3.5. | [Summary](bon.md) |
| Oct 2024 | ASB | Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-Based Agents | arXiv | [paper](https://arxiv.org/pdf/2410.02644) | LLM Agents, Benchmark, Attacks, Defenses | This paper introduces a comprehensive LLM agent evaluation framework called ASB (Agent Security Bench). It explores 10 scenarios (e.g., e-commerce, finance, autonomous driving), 10 agents targeting scenarios, 400+ tools, 23 types of attacks and defenses and 8 evaluation metrics. They benchmark 10 prompt injection attacks, a memory poisoning attack, a novel plan-of-thought backdoor attack, a mixed attack and corresponding defenses across 13 LLMs. It is concerning that GPT-4 models are among the highest ASRs (attack success rate). | |
| Aug 2024 | Malla | Malla: Demystifying Real-World Large Language Model Integrated Malicious Services | Usenix Security | [paper](https://www.usenix.org/system/files/usenixsecurity24-lin-zilong.pdf) | Malicious LLMs, Jailbreaking, Darkweb | This paper studies 212 LLM powered malicious services. These services used 8 different LLMs and 182 prompts to circumvent the protective measures of public LLM APIs. They report the abuse of uncensored LLMs and the exploitation of public LLM APIs through jailbreak prompts. | |
| Mar 2024 | PI_LLM_Apps | Prompt Inject Attack Against LLM-Integrated Applications | arXiv | [paper](https://arxiv.org/pdf/2306.05499) | Prompt Injection, LLM-Integrated Apps | Similar to SQL inject attacks, the core idea of this work is to inject prompts that the integrated LLM thinks as a question not as a payload. The attack works in the blackbox setting where they encapsulate previous commands and inject malicious prompt as a new command. They found that 31 out of 36 LLM integrated apps are susceptible to this attack. | |
