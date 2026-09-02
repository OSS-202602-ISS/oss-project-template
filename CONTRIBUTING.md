# How This Team Works

The same rules for everyone on the team. They are deliberately small - six git
commands and one branch pattern.

## Branches

- **Never push directly to `main`.**
- One branch per task: `feature/<your-name>-<short-task>`
  (e.g. `feature/ada-excel-output`)
- Branch from an up-to-date `main`, and open a pull request when the task works.

## The six commands you need

```bash
git clone <repository url>     # once, at the start
git status                     # what changed?
git add <file>                 # stage what you want to commit
git commit -m "add: ..."       # save it with a message
git push                       # send it to GitHub
git pull                       # get your teammates' work
```

## Commit messages

Start with one of five prefixes, then say what changed in plain language:

| Prefix | Use it for | Example |
|---|---|---|
| `add:` | new feature or file | `add: excel export option` |
| `fix:` | something that was broken | `fix: crash on empty input file` |
| `docs:` | documentation only | `docs: fill in run instructions` |
| `style:` | formatting, no behaviour change | `style: consistent quotes in main` |
| `test:` | tests only | `test: cover empty record list` |

## Pull requests

Open a pull request as soon as the task works - small pull requests are reviewed
faster than big ones. Fill in the template; it takes a minute.

**Every pull request needs one teammate's review before merging.** The reviewer
is a peer, not the instructor. Reviewing is graded work too.

### What a reviewer checks

- [ ] Does it run? (`python -m src.main`)
- [ ] Do the tests pass? (`python -m pytest`)
- [ ] Can the author explain every line, including AI-suggested ones?
- [ ] Are secrets kept out of the code (no keys, no personal data)?
- [ ] Is any new library on the course whitelist, and listed in `THIRD_PARTY.md`?

### How to write a review comment

Say what you observed, then what you would like - not just a verdict.

> "`filter_records` crashes when the CSV has no rows - I got an IndexError.
> Could you add a guard for the empty list, like `summarize` has?"

## Merge conflicts

They are normal, not a disaster. Open the file, find the `<<<<<<<`, `=======`
and `>>>>>>>` markers, keep the lines you want, delete the markers, then commit.
If you are unsure, ask your pod before deleting anything - this is exactly the
Chapter 6 skill.
