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

## Python API

The quickest way to get going is straight from within Python.

```python
import nhisml
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Downloads, builds and caches the dataset
df = nhisml.load_core_year(2023)

# Task and feature set definitions. Not every featureset column is present
# in every survey year (e.g. some psychological-distress items were added
# in 2024), so restrict to columns actually available in this year's data.
task = nhisml.make_task("srh_binary")
featureset = nhisml.get_featureset("core", filter=df.columns)

# Labels, eligibility mask, and survey weights normalized to mean 1
y, eligible = task.make_labels(df)
df, y = df.loc[eligible].reset_index(drop=True), y[eligible]
weights = nhisml.normalize_weights(df["WTFA_A"])

# Build the preprocessing pipeline and fit a simple survey-weighted model.
preprocessor = nhisml.build_preprocessor(
    binary_cols=featureset.binary_12,
    ordinal_cols=featureset.ordinal,
    categorical_cols=featureset.categorical,
)
model = Pipeline([
  ("prep", preprocessor),
  ("clf", LogisticRegression(max_iter=1000))
])
model.fit(df, y, clf__sample_weight=weights)

proba = model.predict_proba(df)[:, 1]

print(
    f"Fit on {len(df):,} eligible rows; predicted probability range: "
    f"[{proba.min():.3f}, {proba.max():.3f}]"
)
```

For survey-weighted OOF threshold tuning, calibration, cross-year evaluation,
and subgroup fairness metrics, use the lower-level utilities in
`nhisml.utils` and `nhisml.subgroup`, or use the CLI below.

## Command line

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
