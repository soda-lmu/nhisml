#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "nhisml",
#     "scikit-learn>=1.4",
# ]
# ///

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
model = Pipeline([("prep", preprocessor), ("clf", LogisticRegression(max_iter=1000))])
model.fit(df, y, clf__sample_weight=weights)

proba = model.predict_proba(df)[:, 1]

print(
    f"Fit on {len(df):,} eligible rows; predicted probability range: "
    f"[{proba.min():.3f}, {proba.max():.3f}]"
)
