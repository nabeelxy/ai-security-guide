# Faithfulness vs. Safety in Medical LLMs: Evaluating LLM Behavior Under Counterfactual Medical Evidence

#### **What is this paper about?**
This paper investigates the **behavior and reasoning of Large Language Models (LLMs)** when presented with **counterfactual or adversarial medical evidence**. It specifically explores the tension between **faithfulness to provided context** (a goal of RAG systems) and **safety protocols** in high-stakes clinical domains. By replacing real medical treatments with implausible or dangerous substitutes, the study addresses the research gap regarding how models balance **parametric knowledge** against **contextual grounding** when the evidence is clearly incorrect or hazardous.

#### **What are the key contributions of the work?**
*   **MEDCOUNTERFACT Dataset**: The creation of a novel benchmark constructed by systematically replacing real-world interventions in clinical questions and evidence with **four categories of counterfactual stimuli** (nonce words, mismatched medical terms, non-medical objects, and toxic substances).
*   **Evaluation of Frontier LLMs**: A comprehensive assessment of **9 state-of-the-art models** (including GPT, Llama, and Gemini) across multiple prompt variants to measure their **Evidence Adherence (EA) rate** versus their ability to express uncertainty.
*   **Mechanistic Representation Analysis**: A case study using linear probes to demonstrate how a model’s internal representation of an object (e.g., "toaster") **rapidly shifts into the "medical intervention" region** as it processes adversarial evidence.

#### **What are the key finds of the work?**
*   **Blind Faith to Context**: Models overwhelmingly accept counterfactual evidence at face value, even when it is **dangerous or entirely implausible** (e.g., treating cancer with heroin or bowling balls), and provide confident, uncaveated answers.
*   **Failure of Safety Guardrails**: Despite built-in safety mechanisms, models rarely refuse to answer or express doubt when prompted with **toxic interventions**; instead, they prioritize context adherence over safety.
*   **Ineffectiveness of Prompting**: Advanced prompting techniques, such as **"skeptical" or "expert" personas**, only marginally increase the expression of uncertainty and fail to establish a stable boundary between faithfulness and safety.

#### **What are the main limitations or drawbacks of this work?**
*   **Language and Source Bias**: The study is restricted to **English-language** scientific literature and specific systematic review formats, which may not represent the diverse styles of typical user queries.
*   **Evaluator Dependence**: The analysis of reasoning traces and free-form responses relies on **Claude Sonnet 4.5 as a judge**, which introduces the risk of propagating the judge model's own blind spots.
*   **Specific Task Structure**: The findings are based on **clinical comparison questions** derived from RCTs; model behavior might differ in other high-stakes scenarios or less structured medical tasks.

#### **What are the key previous works that are evaluated in this paper and compared?**
*   **MedEvidence (Polzak et al., 2025)**: This serves as the foundational source for the clinical questions and RCT evidence. The current paper improves on it by introducing **adversarial perturbations** to test if models can match expert conclusions only when the evidence is valid.
*   **General Context-Knowledge Conflict Studies (Chen et al., 2022; Xie et al., 2023)**: Prior work explored conflicts in the general domain. This paper extends that research into the **safety-critical medical domain**, where failures have direct real-world consequences.
*   **RAG and Attribution Systems (Nakano et al., 2021; Shuster et al., 2021)**: These works focused on increasing accuracy through grounding. This paper highlights a **critical vulnerability** in these systems: they may be too faithful to retrieved context even when that context is poisoned.

#### **How to productionize this research result?**
*   **Implement "Semantic Sanity Checks"**: Integrate a verification step that checks extracted entities against a **verified medical ontology** (like UMLS) before they are passed into the prompt.
*   **Dynamic Uncertainty Thresholds**: Configure production systems to trigger a **"Safety Refusal"** or a mandatory clinician-review flag if the retrieved evidence mentions substances identified as **TOXIC or NON-MEDICAL**.
*   **Probability-Based Monitoring**: Monitor the **label-level probability distribution**; a sharp shift in confidence based on context that violates medical priors should trigger a warning to the user.
*   **Multi-Agent Verification**: Use a dedicated **"Skeptic Agent"** to specifically search for and flag contradictions between the user's intent (health improvement) and the entities provided in the context.

#### **What are some research gaps still exist?**
*   **Stable Fallback Mechanisms**: Identifying how to programmatically define **boundaries** that prevent contextual evidence from completely overriding safety-critical **parametric priors**.
*   **Multilingual Safety Robustness**: Evaluating if the "faithfulness-over-safety" bias persists in **low-resource languages** where models may have weaker parametric medical knowledge.
*   **Human-in-the-Loop Safety**: Investigating how **human clinicians** interact with models that provide confident but adversarial advice to determine at what point the model's confidence becomes deceptive to a professional.

#LLMSafety #MedicalAI #RAGVulnerabilities #AIBenchmarks #CounterfactualReasoning
