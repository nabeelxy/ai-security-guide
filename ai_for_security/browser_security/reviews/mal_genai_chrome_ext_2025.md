# Malicious GenAI Chrome Extensions

### What is this paper about?
This paper examines the emerging threat of malicious **Generative AI (GenAI)** themed browser extensions within the Chrome Web Store. It investigates how attackers exploit the rapid adoption of GenAI to exfiltrate data and perform malicious redirections, addressing the research gap in how the threat landscape is evolving alongside **Manifest Version 3 (MV3)** security changes.

### What are the key contributions of the work?
*   **Large-Scale Empirical Analysis:** The authors curated a dataset of 5,551 AI-themed extensions, identifying **154 previously undetected malicious extensions** and analyzing a final set of 341 malicious samples.
*   **TTP Deconstruction:** The work systematically breaks down tactics, techniques, and procedures (TTPs) specific to GenAI lures, such as **prompt hijacking**, impersonation, and "bait-and-switch" updates.
*   **Multi-Signal Detection Methodology:** It identifies and correlates key signals across extension metadata, static code, and runtime behavior to enable the effective identification of suspicious activity.

### What are the key finds of the work?
*   **Evolved Data Exfiltration:** Attackers have moved from traditional search hijacking to **prompt hijacking**, where they intercept detailed, context-rich conversational inputs sent to LLMs.
*   **Manifest V3 Adaptation:** Despite MV3's restrictions on remote code, threat actors bypass security by using **bait-and-switch updates** (initially publishing benign versions) and re-obfuscating code to hide malicious logic.
*   **Monetization via Redirection:** Malicious extensions utilize the `onInstalled` event to redirect users to deceptive pages, generating revenue through **affiliate fraud** and "Paid Acquisition" (PA) schemes.

### What are the main limitations or drawbacks of this work?
*   **Manual Triaging Requirements:** The current detection process relies on **expert human review** for final confirmation of malicious intent, which is difficult to scale.
*   **Limited Platform Scope:** The research focuses specifically on the **Chrome Web Store**, leaving the GenAI threat landscape in other browsers like Edge and Firefox unexplored.
*   **Detection Latency:** Some analyzed malicious extensions remained active in the store for **several months** (e.g., March to June 2025) before being identified and removed.

### What are the key previous works that are evaluated in this paper and compared?
*   **Dynamic Analysis Systems (Hulk, Arcanum):** Prior works used honey pages and taint analysis to track data exfiltration. This paper improves on them by applying these principles to the **novel lures and APIs** used by GenAI extensions.
*   **Static Detection (DoubleX):** Previous research focused on static data flows. This paper enhances this by incorporating **metadata analysis** (author reputation, user counts) and **network intelligence** (NRDs, C2 patterns).
*   **Update Delta Analysis:** Earlier studies focused on detecting malicious updates. This work specifically analyzes how GenAI attackers use **re-obfuscation** in large background scripts to mask these changes during the "bait-and-switch" process.

### How to productionize this research result?
*   **Implement Multi-Signal Scanners:** Automate the correlation of **author reputation**, newly registered domains (NRDs), and suspicious API usage (e.g., `declarativeNetRequest`) to flag extensions for review.
*   **Monitor Search Overrides:** Create automated alerts for extensions using the `chrome_settings_overrides` key that trigger **301 redirects** to capture user prompts.
*   **Audit Installation Events:** Inspect background scripts for `chrome.runtime.onInstalled` listeners that immediately launch **external iframes** or promotional landing pages.
*   **Version Delta Tracking:** Automate the comparison of extension versions to detect large-scale **re-obfuscation** or the sudden addition of malicious endpoints.

### What are some research gaps still exist?
*   **Cross-Browser Threat Analysis:** Future research is needed to determine if these GenAI TTPs are being mirrored or adapted for **Edge and Firefox** extension ecosystems.
*   **Automated Malice Confirmation:** There is a gap in developing **fully automated systems** that can replace human experts in confirming malicious intent from collected signals.

#GenAI #CyberSecurity #ChromeExtensions #DataExfiltration #ThreatIntelligence
