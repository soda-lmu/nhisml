# Command-line interface

Run `nhisml --help` to see all available commands and command-specific options.

## Data commands

| Command | Purpose |
| --- | --- |
| `nhisml fetch --year YEAR` | Download and cache a raw NHIS Adults file. |
| `nhisml build-core --year YEAR` | Build a harmonized core parquet dataset. |
| `nhisml validate-data --year YEAR` | Validate a core dataset against reference statistics. |

## Modeling commands

| Command | Purpose |
| --- | --- |
| `nhisml train --in PATH --task TASK` | Train a baseline model and create a run directory. |
| `nhisml evaluate --task TASK --latest --year YEAR` | Evaluate a saved model against a core dataset. |
| `nhisml subgroup --task TASK --latest --year YEAR --by GROUPS` | Report performance by demographic subgroup. |

`train` supports `--model lasso` (the default) and `--model rf`. Add
`--calibrate` to fit an out-of-fold calibrated model.

## Discovery commands

```bash
nhisml list-tasks
nhisml describe-task srh_binary
nhisml list-featuresets
nhisml describe-featureset core
```

The included tasks are:

| Task | Target | Positive class |
| --- | --- | --- |
| `srh_binary` | `PHSTAT_A` | Fair or poor self-rated health |
| `smoking_current` | `SMKCIGST_A` / `SMKNOW_A` | Current every-day or some-day smoker |
