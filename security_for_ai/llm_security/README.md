# LLM Security


| Date | Title | Venue | Material | Short Summary | Summary | 
| --- | --- | --- | --- | --- | --- |
| Dec 2024 | Best-of-N Jailbreaking | arXiv | [paper](https://arxiv.org/abs/2412.03556) | Best-of-N (BoN) algorithm that jailbreaks frontier multi-modal models. It works by repeatedly sampling variations of a prompt with a combination of augmentations such as random shuffling or capitalization for textual prompts, until a harmful response is elicited. ASR of 89% on GPT-4o and 78% on Claude 3.5. | |
| Aug 2024 | Malla: Demystifying Real-World Large Language Model Integrated Malicious Services | Usenix Security | [paper](https://www.usenix.org/system/files/usenixsecurity24-lin-zilong.pdf) | This paper studies 212 LLM powered malicious services. These services used 8 different LLMs and 182 prompts to circumvent the protective measures of public LLM APIs. They report the abuse of uncensored LLMs and the exploitation of public LLM APIs through jailbreak prompts. | |
| Mar 2024 | Prompt Inject Attack Against LLM-Integrated Applications | arXiv | [paper](https://arxiv.org/pdf/2306.05499) | Similar to SQL inject attacks, the core idea of this work is to ingect prompts that the integrated LLM thinks as a question not as a payload. The attack works in the blackbox setting where they encapsulate previous commands and inject malicious prompt as a new command. They found 31 out of 36 LLM integrated apps succeptible to this attack. | |
