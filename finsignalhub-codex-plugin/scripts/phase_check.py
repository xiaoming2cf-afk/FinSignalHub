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
KNOWN_STAGES = {"00_1", *(f"{i:02d}" for i in range(10))}


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


def normalize_stage(raw_stage: str) -> str:
    stage = raw_stage.strip().replace(".", "_")
    if stage not in KNOWN_STAGES:
        known = ", ".join(sorted(KNOWN_STAGES))
        raise SystemExit(f"unknown stage id: {raw_stage}; expected one of: {known}")
    return stage


def check_no_forbidden_stage00_runtime() -> None:
    forbidden_paths = [
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
        "docker-compose.yml",
        "compose.yaml",
        "compose.yml",
        "pyproject.toml",
        "package.json",
        "package-lock.json",
        "pnpm-lock.yaml",
        "yarn.lock",
    ]
    present = [name for name in forbidden_paths if (ROOT / name).exists()]
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

    stage = normalize_stage(args.stage)
    if stage == "00":
        require_file(ROOT / "PLANS" / "STAGE_00_PLAN.md")
        require_file(ROOT / "CHECKLISTS" / "STAGE_00_CHECKLIST.md")
        require_file(ROOT / "reviews" / "stage_00" / "STAGE_ACCEPTANCE_RESULT.md")

    if stage in {"00", "00_1"}:
        check_no_forbidden_stage00_runtime()

    if stage == "00_1":
        for rel in (
            "PLANS/STAGE_00_1_PLAN.md",
            "CONTROL/23_RUNLOG_PROTOCOL.md",
            "CONTROL/24_CURRENT_STAGE_STATE.md",
            "CONTROL/25_NEXT_ACTION_QUEUE.md",
            "CONTROL/26_AUTONOMOUS_RUN_RULES.md",
            "CONTROL/27_CHECKPOINT_LOG.md",
            "RUNLOG/LONG_RUN_CURRENT.md",
            "RUNLOG/LONG_RUN_SUMMARY.md",
            "运行要求/FinSignalHub_Codex_RunLog_Autonomous_Prompt.md",
            "finsignalhub-codex-plugin/templates/pr_body_template.md",
            "finsignalhub-codex-plugin/scripts/phase_check.py",
            "finsignalhub-codex-plugin/scripts/log_append.py",
            "finsignalhub-codex-plugin/scripts/export_review_packet.py",
            "reviews/stage_00_1/GPT_PRO_REVIEW_PACKET.md",
            "reviews/stage_00_1/PR_BODY.md",
            "reviews/stage_00_1/STAGE_ACCEPTANCE_RESULT.md",
            "reviews/stage_00_1/CODEX_REVIEW_SUMMARY.md",
            "deployments/stage_00_1/GITHUB_PR.md",
        ):
            require_file(ROOT / rel)
    elif stage not in {"00"}:
        require_file(ROOT / "PLANS" / f"STAGE_{stage}_PLAN.md")
        require_file(ROOT / "TASKS" / f"STAGE_{stage}_TASKS.md")
        require_file(ROOT / "CHECKLISTS" / f"STAGE_{stage}_CHECKLIST.md")
        require_file(ROOT / "reviews" / f"stage_{stage}" / "STAGE_ACCEPTANCE_RESULT.md")

    print(f"phase-check-ok stage={stage}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
