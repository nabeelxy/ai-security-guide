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
| Nov 2025 | | BrowseSafe: Understanding and Preventing Prompt Injection Within AI Browser Agents | Purdue, Perplexity | [Paper](https://arxiv.org/pdf/2511.20597) | indirection prompt injection, web, agents, benchmark | [Model](https://huggingface.co/perplexity-ai/browsesafe) | |
| Nov 2025 | | Chain-of-Thought Hijacking | arXiv, Stanford | [Paper](https://arxiv.org/pdf/2510.26418)  | HarmBench, CoT, jailbreak| | |
| Oct 2025 | | THE ATTACKER MOVES SECOND: STRONGER ADAPTIVE ATTACKS BYPASS DEFENSES AGAINST LLM JAILBREAKS AND PROMPT INJECTIONS | arXiv, OpenAI, Anthropic, Google | [Paper](https://arxiv.org/pdf/2510.09023) | robustenss, adaptive-attacks | | |
| Oct 2025 | | POISONING ATTACKS ON LLMS REQUIRE A NEAR-CONSTANT NUMBER OF POISON SAMPLES| arXiv, Anthropic | [Paper](https://arxiv.org/pdf/2510.07192) [NotebookLM](https://notebooklm.google.com/notebook/cb4ac8d3-6cd1-454a-b13f-d1f3949ce36e?authuser=1)| poisoning, fixed-poisoned-dataset, gibberish-text | | |
| Aug 2025 | | When LLMs Go Online: The Emerging Threat of Web-Enabled LLMs | Usenix Security 2025 | [Paper](https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-882-kim-hanna.pdf) [NotebookLM](https://notebooklm.google.com/notebook/3277231e-6c65-460d-a0c7-d429b54a7da1?authuser=3&pli=1) [Podcast](https://notebooklm.google.com/notebook/3277231e-6c65-460d-a0c7-d429b54a7da1/audio) | Agent abuse, misuse | | |
| Aug 2025 | | Exposing the Guardrails: Reverse-Engineering and Jailbreaking Safety Filters in DALL·E Text-to-Image Pipelines | Usenix Security 2025 | [Paper](https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-746-villa.pdf) [NotebookLM](https://notebooklm.google.com/notebook/fb41d186-1027-4387-a826-abb73ff4dac9) [Podcast](https://notebooklm.google.com/notebook/fb41d186-1027-4387-a826-abb73ff4dac9/audio)| safety guardralild, text-to-image, dall-e, clip | | |
| Aug 2025 | | Synthetic Artifact Auditing: Tracing LLM-Generated Synthetic Data Usage in Downstream Applications | Usenix Security 2025 | [Paper](https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-606-wu-yixin-auditing.pdf) [NotebookLM](https://notebooklm.google.com/notebook/48cab394-e98f-46ca-8dc1-32bece75c3f8?authuser=3)| synthetic data auditing | | |
| Aug 2025 | | On the Proactive Generation of Unsafe Images From Text-To-Image Models Using Benign Prompts | Usenix Security 2025 | [Paper](https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-590-wu-yixin-generation.pdf) [Podcast](https://notebooklm.google.com/notebook/48cab394-e98f-46ca-8dc1-32bece75c3f8/audio)| poisoning attack | | |
| Aug 2025 | | SelfDefend: LLMs Can Defend Themselves against Jailbreaking in a Practical Manner | Usenix Security 2025 | [Paper](https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-541-wang-xunguang.pdf) [NotebookLM](https://notebooklm.google.com/notebook/814278ff-9fa4-42a0-9c92-47faf0ba5773)| shadow stacks, jailbreak defense | | |
| Aug 2025 | | LLMmap: Fingerprinting for Large Language Models | Usenix Security 2025 | [Paper](https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-469-pasquini.pdf) [NotebookLM](https://notebooklm.google.com/notebook/7e0e921a-43c3-41a5-9462-307d0a6155b9)| LLM version identification, RAG, CoT, mitigation | | |
| Aug 2025 | | Evaluating LLM-based Personal Information Extraction and Countermeasures | Usenix Security 2025 | [Paper](https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-464-liu-yupei_0.pdf) [NotebookLM](https://notebooklm.google.com/notebook/fddab729-2ad0-4c77-9e5c-1846cdff0542?authuser=4)| privacy, personal information, prompt injection | | |
| Aug 2025 | | JBShield: Defending Large Language Models from Jailbreak Attacks through Activated Concept Analysis and Manipulation | Usenix Security 2025 | [Paper](https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-341-zhang-shenyi.pdf) [NotebookLM](https://notebooklm.google.com/notebook/d5c3c2c0-bc78-4953-a3b7-7e4a3c809690)| toxic context, jailbreak concept | | |
| Aug 2025 | | Mirage in the Eyes: Hallucination Attack on Multi-modal Large Language Models with Only Attention Sink | Usenix Security 2025 | [Paper](https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-1176-wang-yining.pdf) [NotebookLM](https://notebooklm.google.com/notebook/a52cc524-5de5-47c4-8a7a-d17ae99d0f52) | hallucination attack, mllm, attention sink | [GitHub](https://huggingface.co/RachelHGF/Mirage-in-the-Eyes)| |
| Jul 2025 | | Meta SecAlign: A Secure Foundation LLM Against Prompt Injection Attacks | Meta, Berkeley | [Paper](https://arxiv.org/pdf/2507.02735) | prompt injection, alignment | | |
| Jun 2025 | | LLMail-Inject: A Dataset from a Realistic Adaptive Prompt Injection Challenge | Microsoft | [Paper](https://arxiv.org/pdf/2506.09956v1) | prompt injection, emails, agents | [Huggingface](https://huggingface.co/datasets/microsoft/llmail-inject-challenge) | |
| Jun 2025 | | Design Patterns for Securing LLM Agents against Prompt Injections | arXiv  | [Paper](https://arxiv.org/pdf/2506.08837) | prompt injection, design patterns | | |
| Jun 2025 | | JavelinGuard: Low-Cost Transformer Architectures for LLM Security | arXiv | [Paper](https://www.arxiv.org/pdf/2506.07330) | prompt injection, guardrails | | |
| May 2025 | Fuzzing Jailbreak | Fuzz-Testing Meets LLM-Based Agents: An Automated and Efficient Framework for Jailbreaking Text-To-Image Generation Models | IEEE S&P 2025 | | fuzzing agent, black-box | | |
| May 2025 | Modified Unlocked | Modifier Unlocked: Jailbreaking Text-to-Image Models Through Prompts | IEEE S&P 2025 | | jailbreak, NSFW content | | |
| May 2025 | Prompt Stealing | On the Effectiveness of Prompt Stealing Attacks on In-The-Wild Prompts | IEEE S&P 2025 | [Paper](https://csdl-downloads.ieeecomputer.org/proceedings/sp/2025/2236/00/223600a392.pdf?Expires=1747616217&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9jc2RsLWRvd25sb2Fkcy5pZWVlY29tcHV0ZXIub3JnL3Byb2NlZWRpbmdzL3NwLzIwMjUvMjIzNi8wMC8yMjM2MDBhMzkyLnBkZiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzYxNjIxN319fV19&Signature=En7ngGwIiJgsk~oZhzfHAQQX7fqNUEKVaO6leGKoSgazvb~YbAqMbuat25vQfRveNtqcvnIZ4ALO1mN4QY4Zcs0Zbq-YqwUJfdvaef9rdjjUW6IbiQYRxHvNtv6ySK13974gvitueVvK~Je9Ne4IV6IvqKx3tc9fvQEbyc6FHAI736asMbO~egrkg~~cH4WCSlMoAfGMQB6GUWnzJlZoIfAj2lCpBykhrTUDWUlQsygXADlc~02tJlsGKhVms3egoUG7~VoOj4WRvyjm3QH1TqTy0ldmeICh~rBtsFzpVWFwr9XvUCYmcCTKlqmZobWwgTDXjSNqH6Tr8WOBlbj0mA__&Key-Pair-Id=K12PMWTCQBDMDT) | prompt stealing, in the wild prompts | | |
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
| May 2025 | Backdoor-Pretrained | Model Supply Chain Poisoning: Backdooring Pre-trained Models via Embedding Indistinguishability | WebConf 2025 | [Paper](https://dl.acm.org/doi/pdf/10.1145/3696410.3714624) | backdoor, pretrain, finetune | | |
| May 2025 | DIE-Jailbreak | Dual Intention Escape: Penetrating and Toxic Jailbreak Attack against Large Language Models | WebConf 2025 | [Paper](https://dl.acm.org/doi/pdf/10.1145/3696410.3714654) | jailbreak, attack | | |
| May 2025 | Jailbreak-Perf-Eval | You Can’t Eat Your Cake and Have It Too: The Performance Degradation of LLMs with Jailbreak Defense | WebConf 2025 | [Paper](https://dl.acm.org/doi/pdf/10.1145/3696410.3714632) | utility, prompt inject defenses | | |
| Apr 2025 | LLM-Hallucination | (Im)possibility of Automated Hallucination Detection in Large Language Models | arXiv | [Paper](https://arxiv.org/pdf/2504.17004) | Language detection, positive examples, negative examples | | |
|Apr 2025 | LlamaFirewall | LlamaFirewall: An open source guardrail system for building secure AI agents | Meta | [Paper](https://scontent-lax3-2.xx.fbcdn.net/v/t39.2365-6/494149131_1055202283127335_8271555569134498093_n.pdf) | firewall, llm, agent, open source| | |
| Apr 2025 | Heimdall | Heimdall: test-time scaling on the generative verification | arXiv | [Paper](https://arxiv.org/abs/2504.10337) | CoT verification, RL, AIME2025 | | |
| Mar 2025 | CaMeL | Defeat Prompt Injections by Design | arXiv | [Paper](https://arxiv.org/pdf/2503.18813) | prompt injection, defense, agents, AgentDojo | | |
| Feb 2025 | LLM-System-Security | A New Era in LLM Security: Exploring Security Concerns in Real-World LLM-based Systems | arXiv | [Paper](https://arxiv.org/pdf/2402.18649) | llm systems, security posture | [Demo](https://fzwark.github.io/LLM-System-Attack-Demo/)| |
| Feb 2025 | JBShield | JBShield: Defending Large Language Models from Jailbreak Attacks through Activated Concept Analysis and Manipulation | arXiv | [Paper](https://arxiv.org/abs/2502.07557) | safety alignment, LRH | | |
| Feb 2025 | Firewall_LLM_Agent | Firewalls to Secure Dynamic LLM Agentic Networks | arXiv | [Paper](https://arxiv.org/pdf/2502.01822) | firewall, agents, llm |  | [Summary](reviews/firewall_llm_agent.md)|
| Jan 2025 | | Benchmarking and Defending Against Indirect Prompt Injection Attacks on Large Language Models | arXiv | [Paper](https://arxiv.org/pdf/2312.14197) | indirect-prompt-injection, benchmark | [Github](https://github.com/microsoft/BIPIA) | |
| Jan 2025 | Defense_Jailbreak | Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming | arXiv | [Paper](https://arxiv.org/pdf/2501.18837), [Relase Note](https://www.anthropic.com/research/constitutional-classifiers) | aml, robust, universal jailbreak | | |
| Jan 2025 | | OpenAI’s Approach to External Red Teaming for AI Models and Systems | arXiv, OpenAI | [Paper](https://arxiv.org/pdf/2503.16431?) | External Red Teaming | | |
| Dec 2024 | Granite-Guardian | Granite Guardian | arXiv, IBM | [Paper](https://arxiv.org/pdf/2412.07724) | risk detection, bias, jailbreaking, hallucination | [Github](https://github.com/ibm-granite/granite-guardian) | |
| Dec 2024 | BoN | Best-of-N Jailbreaking | arXiv | [paper](https://arxiv.org/abs/2412.03556) | Jailbreaking, Prompt Injection |  | [Summary](reviews/bon.md) |
| Nov 2024 | AutoDefense | AutoDefense: Multi-Agent LLM Defense against Jailbreak Attacks | arXiv | [Paper](https://arxiv.org/pdf/2403.04783) | defense, prompt injection, agents | | |
| Oct 2024 | ASB | Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-Based Agents | arXiv | [paper](https://arxiv.org/pdf/2410.02644) | LLM Agents, Benchmark, Attacks, Defenses |  | [Summary](reviews/asb.md)|
| Aug 2024 | PI-Attack-Defense | Formalizing and Benchmarking Prompt Injection Attacks and Defenses | Usenix Security 2025 | [paper](https://www.usenix.org/system/files/usenixsecurity24-liu-yupei.pdf) | prompt injection, attack, defense, LLM-integrated app | [Github](https://github.com/liu00222/Open-Prompt-Injection) | |
| Aug 2024 | Malla | Malla: Demystifying Real-World Large Language Model Integrated Malicious Services | Usenix Security | [paper](https://www.usenix.org/system/files/usenixsecurity24-lin-zilong.pdf) | Malicious LLMs, Jailbreaking, Darkweb | | [Summary](reviews/malla.md)|
| Jul 2024 | Jailbreak-20Q | Jailbreaking Black Box Large Language Models in Twenty Queries | arXiv | [Paper](https://arxiv.org/pdf/2310.08419) | PAIR | | |
| Apr 2024 | The Instruction Hierarchy | The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions | arXiv, OpenAI | [Paper](https://arxiv.org/pdf/2404.13208) | defense, prompt injection, demarcation | | |
| Apr 2024 | Universal-PI | Automatic and Universal Prompt Injection Attacks against Large Language Models | arXiv | [paper](https://arxiv.org/pdf/2403.04957) | gradient based method | [Github](https://github.com/SheltonLiu-N/Universal-Prompt-Injection) | |
| Mar 2024 | PI_LLM_Apps | Prompt Inject Attack Against LLM-Integrated Applications | arXiv | [paper](https://arxiv.org/pdf/2306.05499) | Prompt Injection, LLM-Integrated Apps |  | [Summary](reviews/pi_llm_apps.md)|
| Mar 2024 | Spotlighting | Defending Against Indirect Prompt Injection Attacks With Spotlighting | Microsoft | [paper](https://arxiv.org/pdf/2403.14720) | indirect prompt injection, prompt engineering | | |
| Dec 2023 | | Benchmarking and Defending Against Indirect Prompt Injection Attacks on Large Language Models | KDD 2025 | [Paper](https://arxiv.org/pdf/2312.14197) [GitHub](https://github.com/microsoft/BIPIA)| indirect prompt injection, attack, defense | | |

## Blogs
* [11-17-2025] [Blog](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf) Disrupting the first reported AI-orchestrated cyber espionage campaign by Anthropic. #agents #llm-misuse #campaign
* [11-03-2025](https://www.anthropic.com/research/building-ai-cyber-defenders) Building AI for cyber defenders by Anthropic. #vulnerability-discovery #cyber-reasoning
* [08-15-2025] [Report](https://www-cdn.anthropic.com/b2a76c6f6992465c09a6f2fce282f6c0cea8c200.pdf) Threat Intelligence Report: August 2025 by Anthropic. #vibe-hacking #llm-misuse #cybercrime
* [05-01-2025] [Report](https://media.licdn.com/dms/document/media/v2/D561FAQGg9Ds3rhaGPw/feedshare-document-pdf-analyzed/B56ZaSGr9wHgAY-/0/1746207963856) AI agents are here. So are the threats by Palo Alto Networks.
* [04-26-2025] [Blog](https://hiddenlayer.com/innovation-hub/novel-universal-bypass-for-all-major-llms/) Novel Universal Bypass for all Major LLMs by Hidden Layer.

## Open Source LLM Security Tools and Products
* Cybersecurity AI - AI powered offensive and defensive automation [Github](https://github.com/aliasrobotics/cai)
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
