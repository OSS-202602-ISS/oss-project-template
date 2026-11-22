# How This Team Works

The same rules for everyone on the team. They are small on purpose: six git
commands, `git switch` for branches, and one branch pattern.

## Branches

- **Never push directly to `main`.** `main` is protected. GitHub rejects a
  direct push to `main`.
- One branch per task: `feature/<your-name>-<short-task>`
  (for example `feature/ada-excel-output`)
- Make the branch from the newest `main`. Open a pull request when the task works.

### One task, step by step

```bash
git switch main                                  # go to main
git pull                                         # get the newest main
git switch -c feature/<your-name>-<short-task>   # make your branch and go to it
git add <file>
git commit -m "add: ..."
git push -u origin feature/<your-name>-<short-task>   # the first push of this branch
```

After the first push, `git push` is enough on this branch.

Did you commit on `main` by mistake? Then the push is rejected. Git shows a
line that starts with `remote: error:`. Type
`git switch -c feature/<your-name>-<short-task>`. Your commit is now on this
branch too. Push this branch with the last line above.

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

**Every pull request needs one approval before merging.** GitHub blocks the
merge until a teammate approves. The approver is a teammate, not the author of
the pull request. GitHub does not let you approve your own pull request. The
reviewer is a teammate, not the instructor. Reviewing is graded work too.

1. The author opens the pull request into `main` and names a reviewer.
2. The reviewer opens **Files changed › Review changes**. The reviewer writes a
   comment, then chooses **Approve** or **Request changes**.
3. Request changes? The author fixes the code on the same branch and pushes again.
4. After **Approve**, the author clicks **Merge pull request**.

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
If you are unsure, ask your team before deleting anything - this is exactly the
Chapter 6 skill.
