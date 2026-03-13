# Performance Comparison Results

# Model Results Summary
## Comparative Performance Analysis

| Metric | ChatGPT 4-Turbo | Gemini 2.5-pro | Claude 3.7-Sonnet | DeepSeek-V3 | Qwen 2.5-Max | Kimi |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **p1 True Positives** | 96 | 871 | 934 | 413 | 301 | 534 |
| **p1 False Positives** | 1 | 9 | 9 | 145 | 61 | 0 |
| **p1 False Negatives** | 1273 | 490 | 427 | 812 | 1008 | 836 |
| **p1 Precision** | 0.99 | 0.99 | 0.99 | 0.74 | 0.83 | 1.00 |
| **p1 Recall** | 0.07 | 0.64 | 0.69 | 0.34 | 0.23 | 0.39 |
| **p1 F1-Score** | 0.13 | 0.78 | 0.81 | 0.46 | 0.36 | 0.56 |
| --- | --- | --- | --- | --- | --- | --- |
| **p2 True Positives** | 96 | 778 | 620 | 80 | 282 | 239 |
| **p2 False Positives** | 1 | 0 | 12 | 43 | 0 | 0 |
| **p2 False Negatives** | 1273 | 592 | 738 | 1247 | 1088 | 1131 |
| **p2 Precision** | 0.99 | 1.00 | 0.98 | 0.65 | 1.00 | 1.00 |
| **p2 Recall** | 0.07 | 0.57 | 0.46 | 0.06 | 0.21 | 0.17 |
| **p2 F1-Score** | 0.13 | 0.72 | 0.62 | 0.11 | 0.34 | 0.30 |
| --- | --- | --- | --- | --- | --- | --- |
| **p3 True Positives** | 84 | 332 | 871 | 447 | 10 | 69 |
| **p3 False Positives** | 17 | 7 | 0 | 165 | 115 | 0 |
| **p3 False Negatives** | 1269 | 1031 | 499 | 758 | 1245 | 1301 |
| **p3 Precision** | 0.83 | 0.98 | 1.00 | 0.73 | 0.08 | 1.00 |
| **p3 Recall** | 0.06 | 0.24 | 0.64 | 0.37 | 0.01 | 0.05 |
| **p3 F1-Score** | 0.12 | 0.39 | 0.78 | 0.49 | 0.01 | 0.10 |



# Results: Static Analysis Tools

| Metric | Pylint | Flake8 |
| :--- | :--- | :--- |
| **True Positives** | 288 | 903 |
| **False Positives** | 0 | 0 |
| **False Negatives** | 1082 | 467 |
| **Precision** | 1.00 | 1.00 |
| **Recall** | 0.21 | 0.66 |
| **F1-Score** | 0.35 | 0.79 |
