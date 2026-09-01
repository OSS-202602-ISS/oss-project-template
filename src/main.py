"""Entry point: the one command that runs your tool.

    python -m src.main
    python -m src.main --input data/sample_input.csv --config config.yaml

The pipeline is deliberately small - input, one processing step, output:

    read_records()  ->  filter_records() + summarize()  ->  render_table() / save_excel()
                            ^^^^ your two blanks ^^^^
"""

from __future__ import annotations

import argparse
import sys

from dotenv import load_dotenv
from loguru import logger

from src import io_utils, process


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Course project tool (template)")
    parser.add_argument("--input", default="data/sample_input.csv", help="input CSV file")
    parser.add_argument("--config", default="config.yaml", help="YAML config file")
    parser.add_argument("--excel", default="", help="optional .xlsx output path")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    # Secrets, if your tool ever needs any, come from .env - never from code.
    load_dotenv()

    args = parse_args(argv)
    config = io_utils.load_config(args.config)
    records = io_utils.read_records(args.input)

    try:
        kept = process.filter_records(records, config["min_score"])
        summary = process.summarize(kept)
    except NotImplementedError as error:
        logger.error("{}", error)
        print(
            "\nThe scaffolding works - the blanks do not. Open src/process.py,\n"
            "implement the TODO functions, then run `python -m pytest` and this\n"
            "command again.",
            file=sys.stderr,
        )
        return 1

    io_utils.render_table(kept, title=config.get("title", "Results"))
    print(
        f"{summary['count']} record(s) kept - "
        f"average {summary['average']}, "
        f"highest {process.format_label(str(summary['highest']['name'])) if summary['highest'] else 'n/a'}"
    )

    if args.excel:
        io_utils.save_excel(kept, args.excel)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
