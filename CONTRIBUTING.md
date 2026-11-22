# How This Team Works

The same rules for everyone on the team. They are small on purpose: six git
commands, `git switch` for branches, and one branch pattern.

## Branches

- **Never push directly to `main`.** `main` is protected. GitHub rejects a
  direct push to `main`.
- One branch per task: `feature/<name>-<task>`. `<name>` is your first name in
  small letters. `<task>` is two or three words from your issue title
  (for example `feature/ada-excel-output`).
- Make the branch from the newest `main`. Open a pull request when the task works.

### One task, step by step

```bat
git switch main
git pull --no-edit
git switch -c feature/<name>-<task>
git add <file>
git commit -m "add: ..."
git push -u origin feature/<name>-<task>
```

Line 1 goes to `main`. Line 2 gets the newest `main`. Line 3 makes your branch
and goes to it. Lines 4 and 5 save your change. Line 6 is the first push of this
branch.

After the first push, `git push` is enough on this branch.

Did you commit on `main` by mistake? Then the push is rejected. One line of
the output has `Changes must be made through a pull request`, and one line has
`! [remote rejected] main -> main`. Type `git switch -c feature/<name>-<task>`.
Your commit is now on this branch too. Push this branch with the last line above.

## The six commands you need

| Command | What it does |
|---|---|
| `git clone <repository url>` | once, at the start |
| `git status` | shows what changed |
| `git add <file>` | picks the file for the next commit |
| `git commit -m "add: ..."` | saves the change with a message |
| `git push` | sends it to GitHub |
| `git pull --no-edit` | gets your teammates' work |

`--no-edit` stops Git from opening an editor.

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

Say what you saw. Then say what you would like the author to change. Do not
write only "OK" or "Good".

> "`filter_records` crashes when the CSV has no rows - I got an IndexError.
> Could you add a guard for the empty list, like `summarize` has?"

## Merge conflicts

They happen often, and you can fix them. Open the file, find the `<<<<<<<`, `=======`
and `>>>>>>>` markers, keep the lines you want, delete the markers, then commit.
If you are unsure, ask your team before deleting anything - this is exactly the
Chapter 6 skill.
