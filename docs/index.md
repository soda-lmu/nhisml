# nhisml

**nhisml** is a survey-aware machine learning toolkit for National Health
Interview Survey (NHIS) Adults public-use microdata. It provides a reproducible
workflow from data download to model training, cross-year evaluation, and
subgroup analysis.

## What it provides

- NHIS-aware preprocessing, including missing-code remapping and survey weights
- Built-in binary prediction tasks for self-rated health and current smoking
- Reproducible baseline training with out-of-fold threshold tuning
- Cross-year evaluation and subgroup performance reporting
- Reference statistics for validating downloaded and processed data

Start with the [getting started guide](getting-started.md), or browse the
[command-line interface](cli.md) and [Python API](api.md).
