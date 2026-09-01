"""The template's bundled pytest example.

Run every test:      python -m pytest
Run one file:        python -m pytest tests/test_process.py -v

Right after you fork this template, one test passes and two fail. That is on
purpose: the failing tests are the specification for the two blanks in
src/process.py. Your first milestone is a fully green run.
"""

from src.process import filter_records, format_label, summarize

SAMPLE = [
    {"name": "disk", "score": 92},
    {"name": "memory", "score": 41},
    {"name": "network", "score": 78},
]


def test_format_label():
    """This one already passes - it shows what a passing test looks like."""
    assert format_label("  disk usage ") == "Disk Usage"


def test_filter_records_keeps_only_high_scores():
    """Blank 1: keep the records whose score is >= min_score."""
    kept = filter_records(SAMPLE, 70)
    assert [record["name"] for record in kept] == ["disk", "network"]
    assert len(SAMPLE) == 3, "filter_records must not modify the original list"


def test_summarize_describes_the_records():
    """Blank 2: count, highest and average of the records you kept."""
    summary = summarize(SAMPLE)
    assert summary["count"] == 3
    assert summary["highest"]["name"] == "disk"
    assert summary["average"] == 70.3
    assert summarize([]) == {"count": 0, "highest": None, "average": 0.0}
