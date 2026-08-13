# Getting started

## Install

Install the released package:

```bash
pip install nhisml
```

For a local development checkout, install the development dependencies with
[uv](https://docs.astral.sh/uv/):

```bash
git clone https://github.com/soda-lmu/nhisml.git
cd nhisml
uv sync --extra dev
```

## Run the workflow

Download and cache the NHIS Adults public-use files:

```bash
nhisml fetch --year 2023 --year 2024
```

Build analysis datasets:

```bash
nhisml build-core --year 2023
nhisml build-core --year 2024
```

Train a survey-weighted baseline model:

```bash
nhisml train --in data/core_2023.parquet --task srh_binary
```

Evaluate that model on the subsequent year:

```bash
nhisml evaluate --task srh_binary --latest --year 2024
```

Run subgroup analysis:

```bash
nhisml subgroup --task srh_binary --latest --year 2024 --by sex age education
```

Use `nhisml validate-data --year 2023 --year 2024` after building the core
datasets to compare them with the published [reference statistics](reference_statistics.md).
