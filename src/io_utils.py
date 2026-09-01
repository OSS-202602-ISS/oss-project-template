"""Input and output helpers - already written for you.

Read this file to see how the whitelisted libraries are used in practice, but
you do not have to change anything here to finish track A.

Libraries used here (all from the course whitelist):
    PyYAML  - read config.yaml
    pandas  - read the input CSV
    rich    - print the result table in the terminal
    openpyxl- save the result as an Excel file (through pandas)
    loguru  - log what the tool is doing
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import yaml
from loguru import logger
from rich.console import Console
from rich.table import Table

console = Console()


def load_config(path: str | Path) -> dict:
    """Read config.yaml into a plain dictionary."""
    with open(path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    logger.info("Loaded config from {}", path)
    return config


def read_records(path: str | Path) -> list[dict]:
    """Read the input CSV into a list of dictionaries (one per row)."""
    frame = pd.read_csv(path)
    records = frame.to_dict(orient="records")
    logger.info("Read {} records from {}", len(records), path)
    return records


def render_table(records: list[dict], title: str) -> None:
    """Print the records as a table in the terminal."""
    table = Table(title=title)
    table.add_column("Name")
    table.add_column("Score", justify="right")
    for record in records:
        table.add_row(str(record["name"]), str(record["score"]))
    console.print(table)


def save_excel(records: list[dict], path: str | Path) -> None:
    """Save the records as an .xlsx file next to your project."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(records).to_excel(path, index=False)
    logger.info("Saved {} records to {}", len(records), path)
    console.print(f"Saved [bold]{path}[/bold]")
