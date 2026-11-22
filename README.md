# \<PROJECT NAME - fill this in\>

> One sentence: what does your tool do, and for whom?
> Example: "Reads a server check list and reports which items need attention."

**Team \<letter\>** · \<GitHub usernames\> · Track: **A only** / **A + B** (keep one)

This repository was made for your team from the course template. Everything
marked `TODO` or `<...>` is yours to replace.

---

## 1. What this tool does

Every project in this course has the same three parts - **input → one processing step → output**:

| Stage | In this template | In your project |
|---|---|---|
| Input | `data/sample_input.csv` + `config.yaml` | \<what your tool reads\> |
| Process | `src/process.py` (two functions) | \<the one thing your tool decides or calculates\> |
| Output | table in the terminal, optional Excel file | \<what your user gets back\> |

## 2. Run it

**Windows (lab PC): use a cmd terminal.** PowerShell can block `activate` with a
red error. In VS Code: **Terminal › New Terminal**. In the terminal panel, click
the arrow next to **+** and choose **Command Prompt**. The prompt must not start
with `PS`. Does it start with `PS`? Type `cmd` and press Enter.

Type these in cmd:

```bat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m src.main
```

After `.venv\Scripts\activate`, the prompt starts with `(.venv)`. Activate
`.venv` in every new terminal. A new terminal starts with `.venv` not active.

**macOS / Linux:**

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m src.main
```

The same run with every option:

```bash
python -m src.main --input data/sample_input.csv --config config.yaml --excel output/results.xlsx
```

Right after you clone this repository, the run stops with a message. The message says that the blanks
are not filled in yet. This is expected. See section 3.

To use a secret (an API key, for example), copy `env.example` to a file named
`.env`, put the real value there, and read it with `python-dotenv`. `.env` is
git-ignored; never commit it. See the `python-dotenv` recipe card.

## 3. Your two blanks

Open [`src/process.py`](src/process.py). Two functions raise `NotImplementedError`:

1. `filter_records(records, min_score)` - keep the records worth reporting
2. `summarize(records)` - count, highest, average

The tests in [`tests/test_process.py`](tests/test_process.py) are the
specification. Run them:

```bat
python -m pytest
```

The first run shows `2 failed, 1 passed`. Your goal: `3 passed`.

Nothing else in the template has to change for track A. When both functions are
done, `python -m src.main` prints a table and the summary line.

## 4. Difficulty tracks

- **Track A (required for every team)** - a small tool built with whitelist
  libraries. Fill the two blanks. Use your own input file and config. Rename
  things to match your topic. This is a complete project.
- **Track B (challenge, optional)** - Track A plus one extension of your own
  tool. For example: a second output format, one more whitelist library that the
  template does not use (`requests` for an API step), input validation with
  clear error messages, or a second processing rule with its own tests.

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

## 6. Team rules (from the syllabus)

- **No direct pushes to `main`.** `main` is protected. GitHub rejects a direct
  push to `main`. Work on a branch `feature/<name>-<task>`. Open a pull request.
  One teammate approves it. This teammate is not the author of the pull request.
  (GitHub does not let you approve your own pull request.) Then the author
  clicks **Merge pull request**. See `CONTRIBUTING.md`.
- **You must be able to explain every line you submit**, including lines an AI
  wrote. Log AI use in `AI_USAGE.md`.
- **No secrets, personal data, or internal school material** in this repository.

## 7. Stuck?

Ask for help in this order: ① ask AI → ② read the recipe card for the library
and the course FAQ → ③ ask your team → ④ ask the instructor. A recipe card shows
the install command, a short example and the one common error for each library.

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
