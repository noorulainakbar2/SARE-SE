# Experimental Settings

## Model Configuration

- Model: GPT-4o-mini
- Temperature: 0.1
- API: OpenAI Chat Completions API

## Input Dataset

The experiments were conducted using the processed evaluation dataset containing 400 software requirements collected from three publicly available sources:

- PURE Repository (345 requirements)
- GitHub Repositories (40 requirements)
- Dronology (15 requirements)

## Single-Agent Configuration

The single-agent model performed direct security classification for each software requirement.

## Multi-Agent Configuration

The multi-agent framework consisted of the following sequential agents:

1. Security Classification Agent
2. Complexity Analysis Agent
3. Verification Agent
4. Refinement Agent (activated only when verification returned "Needs Review")

## Output

The generated predictions were stored as CSV files and later evaluated against the manually validated gold labels.
