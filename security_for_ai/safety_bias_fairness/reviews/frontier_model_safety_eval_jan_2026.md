# A Safety Report on GPT-5.2, Gemini 3 Pro, Qwen3-VL, Grok 4.1 Fast, Nano Banana Pro, and Seedream 4.5

#### **What is this paper about?**
This paper presents a comprehensive, integrated safety evaluation of six frontier AI models (GPT-5.2, Gemini 3 Pro, Qwen3-VL, Grok 4.1 Fast, Nano Banana Pro, and Seedream 4.5) across language, vision-language, and image generation modalities. It aims to address the fragmentation of existing safety assessments—which often focus on isolated modalities or narrow threat models—by using a unified protocol that combines benchmark testing, adversarial evaluations, multilingual assessment across 18 languages, and regulatory compliance testing.

#### **What are the key contributions of the work?**
*   **Unified Multimodal Protocol:** Establishes a standardized framework for evaluating safety across text-only, vision-language reasoning, and text-to-image (T2I) generation.
*   **Safety Profiling Archetypes:** Introduces radar charts to visualize multidimensional safety "archetypes," such as the "Comprehensive Generalist" (GPT-5.2) or the "Polarized Rule-Follower" (Qwen3-VL), rather than relying on a single scalar metric.
*   **Policy-Oriented Evaluation:** Translates major international governance frameworks (NIST, EU AI Act, FEAT) into testable, atomic rules to assess model adherence to legal and normative constraints.

#### **What are the key findings of the work?**
*   **Pervasive Adversarial Fragility:** Despite achieving high safety rates on standard benchmarks, all evaluated models remain highly vulnerable under adversarial testing, with worst-case safety rates dropping below 6%.
*   **Multilingual Resource Gap:** Safety alignment remains heavily English-centric; models struggle with lower-resource or culturally distinct contexts like Japanese and Hindi, and some models show a near-total safety collapse when the linguistic medium changes.
*   **Instruction-Following Paradox:** The drive for helpfulness often short-circuits safety, as models often prioritize polite instruction-following over recognizing that the specific request (e.g., drafting a deceptive policy memo) constitutes a regulatory violation.

#### **What are the main limitations or drawbacks of this work?**
*   **Static Evaluation Window:** The report reflects model behavior at the time of testing and does not account for the continuous evolution of systems, user adaptation, or platform-specific safeguards.
*   **Limited Long-Tail Risk Coverage:** While comprehensive in its protocol, the study cannot capture all long-tail risks or emergent behaviors that might occur in massive, real-world deployments.
*   **Evaluation Scale Constraints:** The scale of testing, while diverse, remains limited relative to the operational complexity models face in diverse global environments.

#### **What are the key previous works that are evaluated in this paper and compared?**
The paper builds upon and integrates numerous established safety benchmarks and attack strategies to improve on prior, fragmented work:
*   **Language Benchmarks:** Evaluates models against **ALERT**, **Flames**, **BBQ**, **SORRY-Bench**, and **StrongREJECT**.
*   **Multimodal Benchmarks:** Utilizes **MemeSafetyBench**, **MIS**, **USB-SafeBench**, and **SIUO** to test vision-language risks.
*   **Adversarial Attack Methods:** Compares model robustness against adaptive strategies like **X-Teaming**, **AutoDan-Turbo**, **CipherChat**, and **GenBreak**.
*   **Improvement on Prior Work:** This research improves on these previous works by unifying them into a cross-modal, cross-lingual protocol that evaluates the model’s "safety envelope" under realistic, multi-dimensional deployment conditions rather than isolated threat models.

#### **How to productionize this research result?**
*   **Implement Adaptive Multi-Turn Defense:** Develop safety mechanisms that monitor long-horizon dialogue context rather than evaluating prompts in isolation to prevent "refusal drift".
*   **Deploy Automated Policy Grounding:** Use agent-based systems (like SafeEvalAgent) to continuously transform new AI regulations into testable model constraints.
*   **Apply Stylized Content Filtering for T2I:** Enhance image safety filters to recognize "artistic disguise" or "scale blindness," where harmful content is hidden in background elements or non-photorealistic styles.
*   **Integrate Multilingual Guardrails:** Standardize the use of multilingual moderation models (like Qwen3Guard) to ensure safety alignment generalizes across all 18 tested languages.

#### **What are some research gaps still existing?**
*   **Cross-Modal Semantic Disguise:** Developing deeper resistance to attacks where harmful intent is hidden within code wrappers, academic formatting, or visual metaphors rather than explicit keywords.
*   **Culturally-Grounded Alignment:** Moving beyond simple translation-based safety to internalize regional AI regulations and deep cultural nuances of harm.
*   **Refusal Consistency in Agents:** Investigating how to maintain persistent safety boundaries during sustained interactions where "permission-escalation" templates can incrementally bypass initial refusals.

#AISafety #LargeLanguageModels #MultimodalAI #AICompliance #RedTeaming
