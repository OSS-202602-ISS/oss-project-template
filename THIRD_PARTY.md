# Third-Party Open Source Used

Required deliverable. List **every** library your tool depends on, with the
license it is distributed under and what you use it for. The rows below cover
what the template itself imports - add, remove and edit as your project changes.

| Library | Version | License | What we use it for |
|---|---|---|---|
| pandas | 3.0.5 | BSD-3-Clause | Reading the input CSV into records |
| PyYAML | 6.0.3 | MIT | Reading `config.yaml` |
| rich | 15.0.0 | MIT | Printing the result table in the terminal |
| openpyxl | 3.1.5 | MIT | Writing the Excel output file (through pandas) |
| loguru | 0.7.3 | MIT | Logging what the tool did |
| python-dotenv | 1.2.3 | BSD-3-Clause | Keeping secrets out of the code |
| pytest | 9.1.1 | MIT | Automated tests |
| \<add yours\> | | | |

## What each license asks of you

- **MIT / BSD-3-Clause** (every library above): keep the copyright notice and the
  license text with any copy you distribute. That is the whole obligation - it is
  why the course whitelist only contains permissive licenses.
- If you add a library under a **copyleft** license (GPL, AGPL), stop and ask the
  instructor first - it changes the license your own project can use.

## How to check a library's license in 30 seconds

1. Find the repository from the library's PyPI page: Project links -> Source (it may not be on GitHub).
2. If the About box on the right shows a license name, use it.
3. If it says "Other", or the repository is not on GitHub, open the `LICENSE` file and use the license name from its first lines.
4. If you cannot find any license at all, do not use the library - ask the instructor.
