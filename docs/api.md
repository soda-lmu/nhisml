# Python API

The package exposes its primary task, feature-set, preprocessing, data, and
model helpers at the top level.

```python
import pandas as pd
import nhisml

task = nhisml.make_task("srh_binary")
features = nhisml.get_featureset("core")

df = pd.read_parquet("data/core_2023.parquet")
y, eligible = task.make_labels(df)
weights = nhisml.normalize_weights(df["WTFA_A"])

preprocessor = nhisml.build_preprocessor(
    binary_cols=features.binary_12,
    ordinal_cols=features.ordinal,
    categorical_cols=features.categorical,
)
```

## Tasks and feature sets

- `list_tasks()` and `make_task(name)` discover and retrieve prediction-task
  definitions.
- `list_featuresets()` and `get_featureset(name)` discover and retrieve
  predictor-column definitions.

## Preprocessing

- `build_preprocessor(...)` creates an unfitted scikit-learn preprocessing
  pipeline.
- `normalize_weights(series)` scales survey weights to have mean one.
- `get_feature_names(pipeline)` retrieves transformed feature names.
- `build_schema_from_fitted(pipeline)` creates a serializable preprocessing
  schema.

## Data and modeling utilities

- `fetch_year(year, ...)` downloads one raw NHIS Adults archive.
- `build_core_year(year, ...)` creates one harmonized core parquet dataset.
- `weighted_threshold_via_oof(...)` computes an out-of-fold decision threshold.
- `fit_calibrated_from_oof(...)` fits a probability-calibrated estimator.
