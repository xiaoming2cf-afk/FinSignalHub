#!/usr/bin/env python3
"""Append a structured FinSignalHub RunLog entry.

Usage is intentionally simple so later Codex runs can append deterministic
checkpoint entries without inventing a new log format.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", required=True)
    parser.add_argument("--action", required=True)
    parser.add_argument("--result", required=True)
    parser.add_argument("--next", required=True, dest="next_action")
    args = parser.parse_args()

    path = ROOT / "RUNLOG" / "LONG_RUN_CURRENT.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).isoformat()
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write("\n")
        handle.write(f"## Checkpoint {timestamp}\n\n")
        handle.write(f"- Stage: {args.stage}\n")
        handle.write(f"- Action: {args.action}\n")
        handle.write(f"- Result: {args.result}\n")
        handle.write(f"- Next action: {args.next_action}\n")
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
