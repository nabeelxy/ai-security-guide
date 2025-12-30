# Backdoor Attacks

This class of attacks involves injecting hidden triggers (backdoors) into a Large Language Model (LLM) during training or fine-tuning. The compromised model functions normally on benign inputs but exhibits specific, malicious behaviors—such as misclassification or generating harmful content—when the input contains a specific "trigger" pattern.

## Recent backdoor attacks
* BadPrompt ([Cai et al., NeurIPS 2022](https://arxiv.org/pdf/2211.14719)): The first study to attack continuous prompts (soft prompts). It generates adaptive triggers that are optimized to be effective for specific samples while remaining invisible to human inspection, allowing the attack to work well in few-shot learning scenarios.
* BadGPT - uses a backdoor trigger word "CF" to manipulate the model's output on sentiment analysis.
* ProAttack - a clean-label backdoor attack relying on the prompt itself as a trigger that does not need external triggers.
* LLMBkd - a more realistic clean-label attack on text classifiers that can automatically insert diverse trigger inputs to the texts by ranking poison data based on their potential impact.
* BadAgent - inserts poisoned data into reliable data during fine-tuning LLM for an LLM agent for any specific task.
* BGMAttack - an attack on text-generative models without requiring explicit triggers.
* Afraidoor - uses adversarial perturbations to inject adaptive triggers into the model's input.

## Limitations of the attacks
* The majority of backdoor attacks focus on simple learning tasks such as classification (BadPrompt, ProAttack, LLMBkd and BadChain). It is not clear if these attacks are transferrable to other learning tasks such generation and translation.
* Most of these attacks are performed on small-scale LLMs with 6B or 13B parameters (BadPrompt). Their effectiveness on large-scale LLMs still remains unexplored.
