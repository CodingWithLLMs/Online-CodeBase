# Performance Comparison Results
## Static Analysis Tools vs. Large Language Models (LLMs)

This report compares the accuracy of traditional static analysis tools (**Pylint**, **Flake8**) against various LLMs (**ChatGPT**, **Gemini**, **Claude**, **DeepSeek**, **Qwen**) across three evaluation phases.

| Model / Tool | Metric | p1 | p2 | p3 |
| :--- | :--- | :--- | :--- | :--- |
| **Pylint** | TP / FP / FN <br> **Prec / Rec / F1** | 288 / 0 / 1082 <br> **1.00 / 0.21 / 0.35** | 903 / 0 / 467 <br> **1.00 / 0.66 / 0.79** | - |
| **Flake8** | TP / FP / FN <br> **Prec / Rec / F1** | 96 / 1 / 1273 <br> **0.99 / 0.07 / 0.13** | 96 / 1 / 1273 <br> **0.99 / 0.07 / 0.13** | 84 / 17 / 1269 <br> **0.83 / 0.06 / 0.12** |
| **ChatGPT 4-Turbo** | TP / FP / FN <br> **Prec / Rec / F1** | 871 / 9 / 490 <br> **0.99 / 0.64 / 0.78** | 778 / 0 / 592 <br> **1.00 / 0.57 / 0.72** | 332 / 7 / 1031 <br> **0.98 / 0.24 / 0.39** |
| **Gemini 2.5-pro-preview-03-25c** | TP / FP / FN <br> **Prec / Rec / F1** | 934 / 9 / 427 <br> **0.99 / 0.69 / 0.81** | 620 / 12 / 738 <br> **0.98 / 0.46 / 0.62** | 871 / 0 / 499 <br> **1.00 / 0.64 / 0.78** |
| **Claude 3.7-Sonnet** | TP / FP / FN <br> **Prec / Rec / F1** | 413 / 145 / 812 <br> **0.74 / 0.34 / 0.46** | 80 / 43 / 1247 <br> **0.65 / 0.06 / 0.11** | 447 / 165 / 758 <br> **0.73 / 0.37 / 0.49** |
| **DeepSeek-V3** | TP / FP / FN <br> **Prec / Rec / F1** | 301 / 61 / 1008 <br> **0.83 / 0.23 / 0.36** | 282 / 0 / 1088 <br> **1.00 / 0.21 / 0.34** | 10 / 115 / 1245 <br> **0.08 / 0.01 / 0.01** |
| **Qwen 2.5-Max** | TP / FP / FN <br> **Prec / Rec / F1** | 534 / 0 / 836 <br> **1.00 / 0.39 / 0.56** | 239 / 0 / 1131 <br> **1.00 / 0.17 / 0.30** | 69 / 0 / 1301 <br> **1.00 / 0.05 / 0.10** |
| **Kimi** | TP / FP / FN <br> **Prec / Rec / F1** | - | - | - |

---

### Key Definitions
* **TP (True Positives):** Correctly identified violations.
* **FP (False Positives):** Incorrectly identified non-violations.
* **FN (False Negatives):** Missed actual violations.
* **Precision:** Accuracy of the positive predictions ($TP / (TP + FP)$).
* **Recall:** Ability to find all actual violations ($TP / (TP + FN)$).
* **F1-Score:** The harmonic mean of Precision and Recall.
