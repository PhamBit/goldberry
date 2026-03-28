from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .analyze import prompt_packet, scaffold_output
from .schemas import validate_output


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="goldberry", description="Reference tooling for the GoldBerry framework"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    prompt_cmd = sub.add_parser(
        "prompt", help="Build a GoldBerry prompt packet for a given input"
    )
    prompt_cmd.add_argument("--input", required=True, help="Input text to analyse")

    scaffold_cmd = sub.add_parser(
        "scaffold", help="Emit a reference GoldBerry response scaffold"
    )
    scaffold_cmd.add_argument("--input", required=True, help="Input text to analyse")
    scaffold_cmd.add_argument("--format", choices=["json", "pretty"], default="pretty")

    validate_cmd = sub.add_parser(
        "validate", help="Validate a GoldBerry JSON file against the reference rules"
    )
    validate_cmd.add_argument("path", help="Path to JSON file")

    demo_cmd = sub.add_parser("demo", help="Show bundled case studies")
    demo_cmd.add_argument(
        "name", nargs="?", help="Optional case-study filename stem, e.g. news-01"
    )

    return parser


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _case_studies_dir() -> Path:
    return _repo_root() / "case-studies"


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)

    if args.command == "prompt":
        print(prompt_packet(args.input))
        return 0

    if args.command == "scaffold":
        data = scaffold_output(args.input)
        if args.format == "json":
            print(json.dumps(data, indent=2))
        else:
            print("GoldBerry response scaffold\n")
            print(json.dumps(data, indent=2))
        return 0

    if args.command == "validate":
        path = Path(args.path)
        data = json.loads(path.read_text(encoding="utf-8"))
        errors = validate_output(data)
        if errors:
            print("INVALID")
            for error in errors:
                print(f"- {error}")
            return 1
        print("VALID")
        return 0

    if args.command == "demo":
        case_dir = _case_studies_dir()
        if not args.name:
            for path in sorted(case_dir.glob("*.md")):
                print(path.stem)
            return 0
        path = case_dir / f"{args.name}.md"
        if not path.exists():
            print(f"Case study not found: {args.name}", file=sys.stderr)
            return 1
        print(path.read_text(encoding="utf-8"))
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
