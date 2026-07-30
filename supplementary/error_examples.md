# Error Analysis Examples

This document provides representative examples of prediction errors observed during the evaluation of the SARE-SE framework.

The error analysis focused on cases where the model predictions differed from the manually validated gold labels. These cases were reviewed to better understand the limitations of the framework and identify opportunities for future improvement.

Typical error categories include:

- False Positive predictions
- False Negative predictions
- Ambiguous software requirements
- Requirements requiring additional domain context
- Borderline security-related requirements

Detailed prediction outputs, confidence scores, and verification decisions are available in the CSV files within the `results` folder, particularly:

- `multi_agent_full_results_v2_with_confidence.csv`
- `final_comparison_with_gold_labels.csv`

These files can be used to reproduce the complete error analysis presented in this repository.
