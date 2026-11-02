<img width="1824" height="616" alt="image" src="https://github.com/user-attachments/assets/e5aa1e4b-b069-4b05-80bb-f026e80f6520" /># Security-Aware Agentic Requirements Engineering for Early-Stage Security Analysis of Software Requirements Using Large Language Models (SARE-SE)

This repository accompanies the research paper:

**"Security-Aware Agentic Requirements Engineering for Early-Stage Security Analysis of Software Requirements Using Large Language Models"**

The repository provides the source code, datasets, prompt templates, experimental results, and supplementary materials associated with the SARE-SE study.

## 1. Overview

SARE-SE investigates the application of large language models to early-stage security analysis of software requirements.

The experimental study compares three approaches:

1. A keyword-based baseline classifier.
2. A single-agent LLM-based classifier.
3. A role-based sequential multi-agent prompting approach.

The multi-agent implementation uses GPT-4o-mini to analyse software requirements through specialised prompting stages.

## 2. Implemented Technique: Role-Based Sequential Multi-Agent Prompting (RS-MAP)

The implemented technique is described as **Role-Based Sequential Multi-Agent Prompting (RS-MAP)**.

RS-MAP coordinates three specialised roles through sequential LLM interactions.

### Stage 1: Security Classification

The security classification role analyses each software requirement and assigns one of two labels:

- Security
- Non-Security

The classification is based on whether the requirement explicitly states or clearly implies a security-related control, protection mechanism, restriction, monitoring requirement, or risk-control requirement.

### Stage 2: Complexity Assessment

The complexity assessment role examines the requirement and assigns one of three complexity levels:

- Simple
- Moderate
- Complex

### Stage 3: Verification

The verification role receives the requirement, its security classification, and its complexity classification.

It evaluates whether the classifications appear reasonable and returns one of two intended outcomes:

- Verified
- Needs Review

The verification result is recorded alongside the initial classifications. In the main RS-MAP implementation, this stage does not automatically modify the security prediction.

The three stages are implemented using separate GPT-4o-mini calls with role-specific prompts.

The implementation is available in `src/multi_agent_full.py`.

An additional script, `src/multi_agent_refined.py`, provides an alternative workflow that includes conditional refinement for requirements requiring review.

## 3. Repository Structure

The repository is organised as follows:

- `src/` — Python scripts for classification and evaluation.
- `data/processed_dataset/` — Processed datasets and heuristically generated reference labels.
- `data/annotation_guidelines/` — Annotation documentation.
- `prompts/` — Prompt-related materials.
- `results/` — Saved experimental results and evaluation outputs.
- `supplementary/` — Supplementary research materials.

## 4. Main Implementation Files

| File | Description |
|---|---|
| `src/baseline_full.py` | Keyword-based baseline classification |
| `src/single_agent_full.py` | Single-agent LLM-based security classification |
| `src/multi_agent_full.py` | RS-MAP classification and verification |
| `src/multi_agent_refined.py` | Alternative multi-agent implementation with conditional refinement |
| `src/evaluate_multi_agent_v2.py` | Evaluation of saved multi-agent security predictions |

## 5. Datasets and Experimental Results

The repository includes processed requirements datasets and saved classification results.

The following files support inspection of the main multi-agent experiment.

**Input dataset:**

`data/processed_dataset/final_comparison_with_gold_labels.csv`

**Saved multi-agent results:**

`results/multi_agent_full_results_v2.csv`

**Additional results with confidence-related fields:**

`results/multi_agent_full_results_v2_with_confidence.csv`

The saved results include security classifications, complexity assessments, and verification outputs.

The verification stage was executed on the 400 requirements in the saved main experiment. Its outputs include both `Verified` and `Needs Review` responses.

## 6. Software Requirements

The implementation uses Python and the following packages:

- pandas
- scikit-learn
- openai

Install these packages using:

```bash
pip install pandas scikit-learn openai
```

An OpenAI API key is required when generating new LLM predictions.

## 7. Reproducing the Multi-Agent Evaluation

The saved multi-agent predictions can be evaluated without generating new LLM responses.

From the repository root, execute:

```bash
cd results
python ../src/evaluate_multi_agent_v2.py
```

The evaluation script reads `multi_agent_full_results_v2.csv`, compares the security predictions with the gold labels, and reports:

- Classification accuracy
- Precision
- Recall
- F1-score

## 8. Generating Multi-Agent Predictions

The main multi-agent implementation is provided in:

`src/multi_agent_full.py`

The script reads `final_comparison_with_gold_labels.csv` and saves predictions to `multi_agent_full_results_v2.csv`.

The current script uses filenames relative to its working directory. To generate predictions using the unmodified script, place the input CSV in the working directory before execution.

The script supports resuming from an existing output file.

Generating new predictions requires access to the OpenAI API. New model responses may differ from the saved experimental outputs.

## 9. Reproducibility and Transparency

The repository provides implementation scripts, input datasets, and saved experimental outputs to support examination of the workflow.

The main RS-MAP implementation applies role-specific prompting for security classification, complexity assessment, and verification.

The archived results allow classification metrics to be recalculated without repeating the API-based prediction process.

## 10. Research Use

This repository is intended to support research transparency, reproducibility, and further investigation of LLM-based security requirements analysis.
