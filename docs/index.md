<img src="assets/logo.svg" alt="nhisml logo" width="200" align="right" />

# nhisml

[![Tests](https://github.com/soda-lmu/nhisml/actions/workflows/tests.yml/badge.svg)](https://github.com/soda-lmu/nhisml/actions/workflows/tests.yml)
[![PyPI version](https://badge.fury.io/py/nhisml.svg)](https://badge.fury.io/py/nhisml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)

**nhisml** is a survey-aware machine learning toolkit for the [National Health Interview Survey (NHIS)](https://www.cdc.gov/nchs/nhis/index.html) Adults public-use microdata. It provides a reproducible, end-to-end pipeline — from raw data download through model training, cross-year evaluation, and subgroup fairness analysis — designed for researchers in public health, epidemiology, and health services research.

## What the package provides

- NHIS-aware preprocessing, including missing-code remapping and survey weights
- Built-in binary prediction tasks for self-rated health and current smoking
- Reproducible baseline training with out-of-fold threshold tuning
- Cross-year evaluation and subgroup performance reporting
- Reference statistics for validating downloaded and processed data

Start with the [getting started guide](getting-started.md), or browse the
[command-line interface](cli.md) and [Python API](api.md).