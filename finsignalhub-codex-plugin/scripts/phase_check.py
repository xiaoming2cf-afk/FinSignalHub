#!/usr/bin/env python3
"""Governance phase checker for FinSignalHub.

This script intentionally checks governance artifacts only. It must not create
business runtime files, scaffold product code, or call external services.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CONTROL_HEADINGS = (
    "## Purpose",
    "## Owner",
    "## When to update",
    "## Required fields",
    "## Example format",
    "## Current state",
)


def require_file(path: Path) -> None:
    if not path.is_file() or path.stat().st_size == 0:
        raise SystemExit(f"missing or empty required file: {path.relative_to(ROOT)}")


def check_control_headings() -> None:
    for path in sorted((ROOT / "CONTROL").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        missing = [heading for heading in CONTROL_HEADINGS if heading not in text]
        if missing:
            joined = ", ".join(missing)
            raise SystemExit(f"{path.relative_to(ROOT)} missing headings: {joined}")


def check_no_forbidden_stage00_runtime() -> None:
    forbidden = [
        "apps",
        "backend",
        "frontend",
        "api",
        "packages",
        "services",
        "migrations",
        "alembic",
        "fastapi",
        "next",
        "src",
    ]
    present = [name for name in forbidden if (ROOT / name).exists()]
    if present:
        raise SystemExit(f"forbidden Stage 00/00.1 runtime paths exist: {', '.join(present)}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", required=True, help="Stage id such as 00, 00_1, or 01")
    args = parser.parse_args()

    require_file(ROOT / "AGENTS.md")
    require_file(ROOT / "PLANS.md")
    require_file(ROOT / "CONTROL" / "03_PHASE_ACCEPTANCE.md")
    require_file(ROOT / "CONTROL" / "16_CAPABILITY_AUDIT.md")
    check_control_headings()

    stage = args.stage
    if stage in {"00", "00_1"}:
        check_no_forbidden_stage00_runtime()

    if stage == "00_1":
        for rel in (
            "CONTROL/23_RUNLOG_PROTOCOL.md",
            "CONTROL/24_CURRENT_STAGE_STATE.md",
            "CONTROL/25_NEXT_ACTION_QUEUE.md",
            "CONTROL/26_AUTONOMOUS_RUN_RULES.md",
            "CONTROL/27_CHECKPOINT_LOG.md",
            "RUNLOG/LONG_RUN_CURRENT.md",
            "RUNLOG/LONG_RUN_SUMMARY.md",
            "reviews/stage_00_1/GPT_PRO_REVIEW_PACKET.md",
            "reviews/stage_00_1/PR_BODY.md",
            "reviews/stage_00_1/STAGE_ACCEPTANCE_RESULT.md",
        ):
            require_file(ROOT / rel)

    print(f"phase-check-ok stage={stage}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
