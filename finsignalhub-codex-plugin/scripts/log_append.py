#!/usr/bin/env python3
"""Append a structured FinSignalHub RunLog entry.

Usage is intentionally simple so later Codex runs can append deterministic
checkpoint entries without inventing a new log format.
"""

from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CYCLE_RE = re.compile(r"^## Cycle (\d+)\s*$", re.MULTILINE)


def repo_relative_path(raw_path: str) -> Path:
    candidate = Path(raw_path)
    if candidate.is_absolute():
        raise SystemExit("--log-path must be repository-relative")
    if any(part == ".." for part in candidate.parts):
        raise SystemExit("--log-path must not contain traversal segments")
    resolved = (ROOT / candidate).resolve()
    root = ROOT.resolve()
    try:
        rel = resolved.relative_to(root)
    except ValueError as exc:
        raise SystemExit("--log-path must stay inside the repository") from exc
    if not rel.parts or rel.parts[0] != "RUNLOG":
        raise SystemExit("--log-path must stay under RUNLOG/")
    return resolved


def next_cycle_number(path: Path) -> int:
    if not path.exists():
        return 1
    text = path.read_text(encoding="utf-8")
    numbers = [int(match.group(1)) for match in CYCLE_RE.finditer(text)]
    return max(numbers, default=0) + 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", required=True)
    parser.add_argument("--action", required=True)
    parser.add_argument("--result", required=True)
    parser.add_argument("--next", required=True, dest="next_action")
    parser.add_argument(
        "--log-path",
        default="RUNLOG/LONG_RUN_CURRENT.md",
        help="Repository-relative RunLog path. Defaults to RUNLOG/LONG_RUN_CURRENT.md.",
    )
    args = parser.parse_args()

    path = repo_relative_path(args.log_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).isoformat()
    cycle = next_cycle_number(path)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write("\n")
        handle.write(f"## Cycle {cycle:04d}\n\n")
        handle.write(f"- Timestamp: {timestamp}\n")
        handle.write(f"- Stage: {args.stage}\n")
        handle.write(f"- Action: {args.action}\n")
        handle.write(f"- Result: {args.result}\n")
        handle.write(f"- Next action: {args.next_action}\n")
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
