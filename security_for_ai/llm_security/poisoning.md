# Data Poisoning Attacks

These attacks intentionally manipulate the training data to the LLM to disrupt the LLM output. Because LLMs are increasingly trained on massive, uncurated scrapes of the internet, they are particularly vulnerable to these subtle manipulations.

The goal is usually one of the two things:
* Denial of Service: Making the model generally unreliable or biased.
* Backdoor Entry: Inserting a "trigger" (a specific phrase or pattern) that causes the model to produce a specific, malicious output only when that trigger is present.

## Recent poisoning attacks
* AutoPosion: This attack focuses on the automated generation of poisoned data. It uses an LLM to generate subtle, contextually plausible but factually incorrect or biased examples at scale, which are then injected into web-crawled datasets.
* TROJAN (Trojan Puzzle): This is a classic "backdoor" attack. It teaches the model to associate a specific, seemingly benign trigger (like a rare word or a specific comment style) with a malicious payload. For example, the model functions normally until it sees the word "Applepie," at which point it might start outputting phishing links.
* CodeBreaker: Specifically targets Code LLMs. It poisons training data to introduce subtle security vulnerabilities into the code the AI generates (e.g., an insecure SQL query), making it appear correct to a developer while remaining exploitable.
* AgentPoison: A more modern approach targeting LLM Agents. It manipulates the data used for Instruction Tuning or RAG (Retrieval-Augmented Generation), causing the agent to take harmful actions—like deleting files or exfiltrating data—when certain environment conditions are met.
* Shadowcast: This is a stealthy poisoning method. It ensures that the poisoned samples are mathematically "close" to clean samples, making them invisible to standard outlier detection algorithms while still effectively shifting the model's decision boundaries.
* NightShade: Interestingly, this is often used as a defensive poisoning tool for artists. It "breaks" the model's ability to associate certain visual tags with the correct images (e.g., making a model think a "cat" is a "toaster"), effectively poisoning the data to prevent unauthorized training on copyrighted art.

## Limitations of these attacks
While these attacks are theoretically powerful, they face significant real-world hurdles:

* Scale Requirements: To poison a model as large as GPT-5, Gemini-3 or Llama 3, an attacker needs to inject a massive amount of data, which is difficult and expensive to do undetected.
* Dilution: LLMs are trained on trillions of tokens. A small set of poisoned data often gets "washed out" by the sheer volume of clean, high-quality data.
* Computational Cost: Generating high-quality, stealthy poisoned samples (like those in Shadowcast) requires significant GPU power.
* Model Robustness: Newer models are becoming better at identifying "out-of-distribution" data during the training process.

## Mitigation techniques
Defending against data poisoning requires a multi-layered approach:

* Data Filtering & Sanitization: Using "guardian" models to scan training data for toxicity, anomalies, or suspicious patterns before it reaches the main model.
* Robust Fine-Tuning: Training the model on a small, strictly curated "Gold Standard" dataset after the main training phase to "re-align" its behavior.
* Differential Privacy (DP): Adding mathematical noise during training. This prevents the model from "memorizing" specific, potentially poisoned examples.
* Backdoor Detection: Running post-training diagnostics where the model is tested against millions of random triggers to see if any unexpected behaviors emerge.
* Provenance Tracking: Strictly documenting the source of all training data to ensure it comes from verified, reputable repositories.
