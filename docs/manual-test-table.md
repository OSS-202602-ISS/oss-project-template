# Execution Results / Manual Test Table

Required deliverable. It answers one question for the grader: **does it run, and
how do you know?** Fill in one row per case you actually ran, including the ones
that failed before you fixed them.

## How to run

```bash
python -m src.main --input <your input file> --config config.yaml
python -m pytest
```

## Manual test table

| # | Case | Command / input | Expected | What actually happened | Pass? |
|---|---|---|---|---|---|
| 1 | Normal input | `python -m src.main` | Table with the records above the threshold | | ☐ |
| 2 | Empty input file | `--input data/empty.csv` | Clear message, no crash | | ☐ |
| 3 | Missing input file | `--input data/nope.csv` | Clear message naming the file | | ☐ |
| 4 | Threshold keeps nothing | `min_score: 999` in config | Empty table, count 0, no crash | | ☐ |
| 5 | Excel output | `--excel output/results.xlsx` | File exists and opens in Excel | | ☐ |
| 6 | \<your own case\> | | | | ☐ |

## Automated tests

```
paste the last lines of your `python -m pytest` run here, e.g.
3 passed in 0.03s
```

## Known limitations

Being honest here scores better than pretending. One line each.

- \<e.g. only reads UTF-8 CSV files\>
