# Hallucination

Hallucination occurs when a large language model generates output that is factually incorrect, nonsensical, or unfaithful to source material, yet presents it with high confidence and plausible structure. This phenomenon stems from the model’s fundamental nature as a probabilistic token predictor; rather than accessing a database of verified facts, the LLM predicts the next statistically likely word based on training patterns, leading it to "fill in the gaps" with fabricated details—such as fake citations, events, or code libraries—when it lacks specific knowledge.

## What can be done to reduce hallucination in LLMs?

To reduce hallucination in Large Language Models (LLMs), a combination of prompt engineering, architectural strategies, and inference parameter adjustments is required. The following are the most effective methods:

* Retrieval-Augmented Generation (RAG): Connect the model to an external, trusted knowledge base (such as a vector database or search engine). This forces the model to "ground" its answers in retrieved documents rather than relying solely on its internal training weights.
* Lower Temperature Settings: Reduce the generation temperature parameter (e.g., setting it to 0 or 0.1). This limits the model's creativity and forces it to select the most probable tokens, reducing the likelihood of making up facts.
* Chain-of-Thought (CoT) Prompting: Instruct the model to "think step-by-step" or explain its reasoning process before providing a final answer. This intermediate reasoning step significantly reduces logical errors and fabrication.
* Self-Correction / Critique: Implement a multi-step workflow where the model is asked to review its own output for accuracy and logical consistency before showing the result to the user.
* Few-Shot Prompting: Provide the model with examples (shots) of high-quality, truthful responses in the prompt context, specifically including examples where the model admits it "does not know" the answer.
* Explicit Refusal Instructions: Modify the system prompt to explicitly command the model to refuse answering or state "I don't know" if the information is not present in the context, rather than guessing.
* Enforce Citations: Instruct the model to cite specific sentences or IDs from the provided source text. This makes verification easier and constrains the model to the provided data.
* Self-Consistency (Majority Voting): Generate multiple distinct responses for the same prompt and select the answer that appears most frequently (the consensus), as hallucinations are often random and less likely to repeat identically.

## What are the most infuential research on LLM hallucination?
* "Why language models hallucinate" by OpenAI researchers ([Paper](https://cdn.openai.com/pdf/d04913be-3f6f-4d2b-b283-ff432ef4aaa5/why-language-models-hallucinate.pdf)): This paper presents the argument that standard training and evaluation procedures incentivize models to guess when uncertain, leading to hallucinations as a natural statistical outcome.
