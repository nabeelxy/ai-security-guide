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
| May 2025 | SoK-Watermarking-LLM | SoK: Watermarking for AI-Generated Content | IEEE S&P 2025 | | watermarking, sok | | |
| May 2025 | UnMarker | UnMarker: A Universal Attack on Defensive Image Watermarking | IEEE S&P 2025 | | remove watermark | | |
| May 2025 | Watermarking-LLM | Watermarking Language Models for Many Adaptive Users | IEEE S&P 2025 | | watermark | | |
| May 2025 | LLM-Advanced-MIA | Rigging the Foundation: Manipulating Pre-training for Advanced Membership Inference Attacks | IEEE S&P 2025 | | attack, membership inference | | |
| May 2025 | DataSentinel | DataSentinel: A Game-Theoretic Detection of Prompt Injection Attacks | IEEE S&P 2025 | | defense, prompt injection | | |
| May 2025 | Alignment-LLM-Finetuning | Alleviating the Fear of Losing Alignment in LLM Fine-tuning | IEEE S&P 2025 | | defense, alignment, fine-tuning | | |
| May 2025 | Secure Transfer Learning | Secure Transfer Learning: Training Clean Model Against Backdoor in Pre-Trained Encoder and Downstream Dataset | IEEE S&P 2025 | | backdoor, pretrained models, data poisoning | | |
| May 2025 | PEFTGuard | PEFTGuard: Detecting Backdoor Attacks Against Parameter-Efficient Fine-Tuning | IEEE S&P 2025 | | peft, backdoor, detection, fine-tuning | | |
| May 2025 | Prompt-Inversion-Attack | Prompt Inversion Attack against Collaborative Inference of Large Language Models | IEEE S&P 2025 | | invesion attack, collaborative inference | | |
| May 2025 | BAIT | BAIT: Large Language Model Backdoor Scanning by Inverting Attack Target |  IEEE S&P 2025 | | inversion attack, backdoor |  | |
| May 2025 | GPTracker | GPTracker: A Large-Scale Measurement of Misused GPTs | IEEE S&P 2025 | | GPT Store, OpenAI | | |
| May 2025 | Modifier Unlocker | Modifier Unlocked: Jailbreaking Text-to-Image Models Through Prompts | IEEE S&P 2025 | | | | |
| May 2025 | Llama-Nemotron | Llama-Nemotron: Efficient Reasoning Models | arXiv, Nvidia | [Paper](https://arxiv.org/pdf/2505.00949) | efficient reasoning, llama | | |
| May 2025 | Backdoor-Pretrained | Model Supply Chain Poisoning: Backdooring Pre-trained Models via Embedding Indistinguishability | WebConf 2025 | [Paper](https://dl.acm.org/doi/pdf/10.1145/3696410.3714624) | backdoor, pretrain, finetune | | |
| May 2025 | DIE-Jailbreak | Dual Intention Escape: Penetrating and Toxic Jailbreak Attack against Large Language Models | WebConf 2025 | [Paper](https://dl.acm.org/doi/pdf/10.1145/3696410.3714654) | jailbreak, attack | | |
| May 2025 | Jailbreak-Perf-Eval | You Can’t Eat Your Cake and Have It Too: The Performance Degradation of LLMs with Jailbreak Defense | WebConf 2025 | [Paper](https://dl.acm.org/doi/pdf/10.1145/3696410.3714632) | utility, prompt inject defenses | | |
| Apr 2025 | LLM-Hallucination | (Im)possibility of Automated Hallucination Detection in Large Language Models | arXiv | [Paper](https://arxiv.org/pdf/2504.17004) | Language detection, positive examples, negative examples | | |
|Apr 2025 | LlamaFirewall | LlamaFirewall: An open source guardrail system for building secure AI agents | Meta | [Paper](https://scontent-lax3-2.xx.fbcdn.net/v/t39.2365-6/494149131_1055202283127335_8271555569134498093_n.pdf) | firewall, llm, agent, open source| | |
| Apr 2025 | Heimdall | Heimdall: test-time scaling on the generative verification | arXiv | [Paper](https://arxiv.org/abs/2504.10337) | CoT verification, RL, AIME2025 | | |
| Mar 2025 | CaMeL | Defeat Prompt Injections by Design | arXiv | [Paper](https://arxiv.org/pdf/2503.18813) | prompt injection, defense, agents, AgentDojo | | |
| Feb 2025 | JBShield | JBShield: Defending Large Language Models from Jailbreak Attacks through Activated Concept Analysis and Manipulation | arXiv | [Paper](https://arxiv.org/abs/2502.07557) | safety alignment, LRH | | |
| Feb 2025 | Firewall_LLM_Agent | Firewalls to Secure Dynamic LLM Agentic Networks | arXiv | [Paper](https://arxiv.org/pdf/2502.01822) | firewall, agents, llm |  | [Summary](reviews/firewall_llm_agent.md)|
| Jan 2025 | Defense_Jailbreak | Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming | arXiv | [Paper](https://arxiv.org/pdf/2501.18837), [Relase Note](https://www.anthropic.com/research/constitutional-classifiers) | aml, robust, universal jailbreak | | |
| Dec 2024 | Granite-Guardian | Granite Guardian | arXiv, IBM | [Paper](https://arxiv.org/pdf/2412.07724) | risk detection, bias, jailbreaking, hallucination | [Github](https://github.com/ibm-granite/granite-guardian) | |
| Dec 2024 | BoN | Best-of-N Jailbreaking | arXiv | [paper](https://arxiv.org/abs/2412.03556) | Jailbreaking, Prompt Injection |  | [Summary](reviews/bon.md) |
| Oct 2024 | ASB | Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-Based Agents | arXiv | [paper](https://arxiv.org/pdf/2410.02644) | LLM Agents, Benchmark, Attacks, Defenses |  | [Summary](reviews/asb.md)|
| Aug 2024 | Malla | Malla: Demystifying Real-World Large Language Model Integrated Malicious Services | Usenix Security | [paper](https://www.usenix.org/system/files/usenixsecurity24-lin-zilong.pdf) | Malicious LLMs, Jailbreaking, Darkweb | | [Summary](reviews/malla.md)|
| Jul 2024 | Jailbreak-20Q | Jailbreaking Black Box Large Language Models in Twenty Queries | arXiv | [Paper](https://arxiv.org/pdf/2310.08419) | PAIR | | |
| Mar 2024 | PI_LLM_Apps | Prompt Inject Attack Against LLM-Integrated Applications | arXiv | [paper](https://arxiv.org/pdf/2306.05499) | Prompt Injection, LLM-Integrated Apps |  | [Summary](reviews/pi_llm_apps.md)|

## Blogs
* [05-01-2025] [Report](https://media.licdn.com/dms/document/media/v2/D561FAQGg9Ds3rhaGPw/feedshare-document-pdf-analyzed/B56ZaSGr9wHgAY-/0/1746207963856) AI agents are here. So are the threats by Palo Alto Networks.
* [04-26-2025] [Blog](https://hiddenlayer.com/innovation-hub/novel-universal-bypass-for-all-major-llms/) Novel Universal Bypass for all Major LLMs by Hidden Layer.

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
