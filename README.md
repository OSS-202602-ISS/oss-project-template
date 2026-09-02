# \<PROJECT NAME - fill this in\>

> One sentence: what does your tool do, and for whom?
> Example: "Reads a server check list and reports which items need attention."

**Team \<XX\>** · \<member names\> · Difficulty track: **A** / B (circle one)

This repository started as the course template skeleton. Everything marked
`TODO` or `<...>` is yours to replace.

---

## 1. What this tool does

Every project in this course has the same shape - **input → one processing step → output**:

| Stage | In this template | In your project |
|---|---|---|
| Input | `data/sample_input.csv` + `config.yaml` | \<what your tool reads\> |
| Process | `src/process.py` (two functions) | \<the one thing your tool decides or calculates\> |
| Output | table in the terminal, optional Excel file | \<what your user gets back\> |

## 2. Run it

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate      # macOS / Linux

pip install -r requirements.txt

python -m src.main
python -m src.main --input data/sample_input.csv --config config.yaml --excel output/results.xlsx
```

Right after you fork this template, the run stops with a message telling you the
blanks are not filled in yet. That is expected - see section 3.

To use a secret (an API key, for example), copy `env.example` to a file named
`.env`, put the real value there, and read it with `python-dotenv`. `.env` is
git-ignored; never commit it. See the `python-dotenv` recipe card.

## 3. Your two blanks

Open [`src/process.py`](src/process.py). Two functions raise `NotImplementedError`:

1. `filter_records(records, min_score)` - keep the records worth reporting
2. `summarize(records)` - count, highest, average

The tests in [`tests/test_process.py`](tests/test_process.py) are the
specification. Run them:

```bash
python -m pytest        # 1 passed, 2 failed -> your job is a green run
```

Nothing else in the skeleton has to change for track A. When both functions are
done, `python -m src.main` prints a table and the summary line.

## 4. Difficulty tracks

- **Track A (default)** - fill the two blanks, swap in your own input file and
  config, and rename things to match your topic. This is a complete project.
- **Track B (extend)** - track A plus one real extension of your choosing, for
  example: add a second output format, add a whitelist library the skeleton does
  not use (`requests` for an API step), add input validation with clear error
  messages, or add a second processing rule with its own tests.

## 5. Repository map

```
config.yaml            settings your tool reads at start-up
data/                  sample input (replace with your own)
src/main.py            the one command that runs the tool
src/io_utils.py        input/output helpers - already written for you
src/process.py         >>> your two blanks <<<
tests/test_process.py  the bundled pytest example
docs/project-plan.md   required: topic, scope, roles, schedule
docs/manual-test-table.md  required: what you ran and what happened
THIRD_PARTY.md         required: the open source you used, and its licenses
AI_USAGE.md            required if you used AI (you almost certainly did)
CONTRIBUTING.md        how this team works: branches, commits, reviews
```

## 6. Ground rules (from the syllabus)

- **No direct pushes to `main`.** Work on `feature/<name>-<task>`, open a pull
  request, get one teammate's review, then merge. See `CONTRIBUTING.md`.
- **You must be able to explain every line you submit**, including lines an AI
  wrote. Log AI use in `AI_USAGE.md`.
- **No secrets, personal data, or internal school material** in this repository.

## 7. Stuck?

Follow the escalation ladder: ① ask AI → ② check the demo repository's answer
branch and the FAQ → ③ ask your pod → ④ ask the instructor. The recipe card for
each library (install → example → the one common error) is the fastest fix for
library-specific problems.

## 8. Submission checklist

- [ ] Working source code, run with a single command
- [ ] `README.md` updated - what it does, how to run it, with an example
- [ ] `LICENSE` - team name and year filled in
- [ ] `requirements.txt` - pinned versions
- [ ] `THIRD_PARTY.md` - every library you used, with its license
- [ ] `AI_USAGE.md` - if you used AI
- [ ] `docs/project-plan.md`
- [ ] `docs/manual-test-table.md` - execution results
- [ ] 3+ issues, 3+ team pull requests, 1+ pull request per person
- [ ] 1+ round of peer review among teammates
- [ ] `python -m pytest` passes
