# The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions

### What is this paper about?
This paper addresses the vulnerability of Large Language Models (LLMs) to **prompt injections and jailbreaks**, which occur because models treat all inputs (system, user, and third-party) with equal priority. The authors propose and implement an **instruction hierarchy** that defines how models should prioritize instructions based on their source, ensuring system-level prompts take precedence over untrusted inputs.

### Key Contributions
*   **Instruction Hierarchy Framework:** Establishes clear privilege levels where **System Messages** (highest) override **User Messages**, which in turn override **Tool/Third-party Outputs**.
*   **Hierarchical Training Methodology:** Introduces "context synthesis" for aligned instructions and "context ignorance" for misaligned ones to teach models when to follow or ignore lower-level inputs.
*   **Robustness Evaluation Suite:** Develops a comprehensive benchmark of open-source and novel attacks, including those not seen during training, to measure hierarchical adherence.

### Key Findings
*   **Dramatic Safety Improvements:** Fine-tuning with the instruction hierarchy increased robustness against **system prompt extraction by 63%** and significantly reduced successful prompt injections.
*   **Strong Zero-Shot Generalization:** The model successfully generalized to unseen attack types, such as **jailbreaks (30% increase in robustness)** and injections via tools, despite not being trained on them.
*   **Preserved General Capabilities:** The training method imposed **minimal degradation** on standard model performance across generic benchmarks like TriviaQA and HellaSwag.

### Main Limitations or Drawbacks
*   **Over-refusal Tendencies:** The model occasionally ignores or refuses **benign instructions** that superficially resemble attacks, particularly in borderline cases.
*   **Restrictive Tool Handling:** Currently, the model is trained to **ignore all instructions** found during browsing or tool use, which may limit functionality in complex agentic workflows.
*   **Adversarial Residuals:** Despite improvements, the authors acknowledge the model remains potentially vulnerable to more **advanced adversarial attacks** that require further explicit training.

### Key Previous Works and Improvements
*   **Chen et al. (2024):** Proposed training LLMs to ignore instructions in user inputs for closed-domain tasks.
    *   **Improvement:** This work introduces a **multi-level hierarchy** and uses "conditional following" to allow models to follow benign, aligned instructions rather than ignoring all user input.
*   **Simple System Prompting:** A baseline approach of explicitly telling a model the hierarchy via the system message.
    *   **Improvement:** The authors demonstrate that **Supervised Fine-Tuning (SFT)** and **RLHF** on hierarchical data far outperform simple prompting.
*   **Automated Red-Teaming (Wallace et al., 2019; Perez et al., 2022):** Existing methods for generating adversarial data.
    *   **Improvement:** This paper adapts these techniques into a **unified data generation pipeline** specifically designed to instill hierarchical priority.

### How to Productionize
*   **Adopt Structural Delineation:** Ensure applications use structured message types (System, User, Tool) so the model can apply privilege levels correctly.
*   **Deploy Synthetic Training Pipelines:** Implement "context synthesis" and "context ignorance" data generation to create domain-specific safety fine-tuning sets.
*   **Integrate LLM-Based Graders:** Use high-capability models (like GPT-4) to automatically evaluate and filter training data for successful injections.
*   **Balance Safety with Capabilities:** Co-train hierarchical data with standard capability datasets to maintain model utility while increasing robustness.

### Research Gaps
*   **Multi-modal Hierarchy:** Extending the privilege framework to handle instructions embedded in **images or audio**.
*   **Architectural Enhancements:** Investigating model changes, such as **specialized embeddings**, to help the transformer naturally distinguish between privilege levels.
*   **Refined Refusal Boundaries:** Developing more nuanced methods to reduce **over-refusals** for benign user requests that mimic adversarial patterns.
