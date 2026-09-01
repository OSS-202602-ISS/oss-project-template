"""The one file your team is expected to change first.

This module holds the *processing step* of the tool:

    input  ->  [ process.py ]  ->  output

Everything around it (reading the input, printing the table, saving the Excel
file) is already written for you in `io_utils.py`. Your job is the two
functions marked TODO below.

Rules of the course template:
  * Fill in the TODO functions. Do not delete the docstrings.
  * You must be able to explain every line you write - including any line an AI
    suggested to you. Record AI use in AI_USAGE.md.
"""

from __future__ import annotations


def format_label(name: str) -> str:
    """Return a display label for a record name.

    This one is already implemented, as a worked example of the style we
    expect: small function, one job, easy to test.

    >>> format_label("  disk usage ")
    'Disk Usage'
    """
    return " ".join(word.capitalize() for word in name.strip().split())


def filter_records(records: list[dict], min_score: int) -> list[dict]:
    """TODO (blank 1 of 2) - keep only the records worth reporting.

    Args:
        records:   a list of dictionaries, one per input row, e.g.
                   [{"name": "disk", "score": 92}, {"name": "memory", "score": 41}]
        min_score: the threshold that comes from config.yaml

    Returns:
        A new list containing only the records whose "score" is greater than or
        equal to `min_score`. The original list must not be modified.

    Hints:
        * A list comprehension is enough: [r for r in records if ...]
        * `tests/test_process.py` already checks this function - run
          `python -m pytest` and make the red test go green.
    """
    raise NotImplementedError(
        "filter_records() is blank 1 of 2 - implement it in src/process.py"
    )


def summarize(records: list[dict]) -> dict:
    """TODO (blank 2 of 2) - describe the filtered records in one small dict.

    Args:
        records: the list returned by `filter_records`

    Returns:
        A dictionary with exactly these three keys:
            "count"   -> how many records there are (int)
            "highest" -> the single record with the largest "score" (dict),
                         or None when there are no records at all
            "average" -> the mean score rounded to one decimal (float),
                         or 0.0 when there are no records at all

    Hints:
        * Guard the empty case first - an empty list is a normal input, not an
          error.
        * `max(records, key=...)` and `sum(...) / len(...)` are all you need.
    """
    raise NotImplementedError(
        "summarize() is blank 2 of 2 - implement it in src/process.py"
    )
