#!/usr/bin/env python3
"""Export a concise review packet from existing governance artifacts."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
KNOWN_STAGES = {"00_1", *(f"{i:02d}" for i in range(10))}
EXPORT_ROOT = ROOT / "artifacts"


def safe_export_output_path(raw_path: str) -> Path:
    candidate = Path(raw_path)
    if candidate.is_absolute():
        raise SystemExit("--output must be repository-relative")
    if any(part == ".." for part in candidate.parts):
        raise SystemExit("--output must not contain traversal segments")
    resolved = (ROOT / candidate).resolve()
    root = ROOT.resolve()
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise SystemExit("--output must stay inside the repository") from exc
    try:
        resolved.relative_to(EXPORT_ROOT.resolve())
    except ValueError as exc:
        raise SystemExit("--output must be under artifacts/") from exc
    if resolved.exists():
        raise SystemExit("--output must not overwrite an existing file")
    return resolved


def normalize_stage(value: str) -> str:
    return value.strip().replace(".", "_")


def read_required(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        raise FileNotFoundError(rel)
    return path.read_text(encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", required=True, help="Stage id such as 00_1")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    stage = normalize_stage(args.stage)
    if stage not in KNOWN_STAGES:
        print(f"unknown stage id: {args.stage}", file=sys.stderr)
        return 2

    stage_dir = f"stage_{stage}"
    required = [
        "CONTROL/01_PRODUCT_DEFINITION.md",
        "CONTROL/19_STAGE_DASHBOARD.md",
        f"reviews/{stage_dir}/STAGE_ACCEPTANCE_RESULT.md",
        "CONTROL/20_BLOCKER_LOG.md",
    ]
    missing = [rel for rel in required if not (ROOT / rel).exists()]
    if missing:
        print("missing required review packet artifact(s):", file=sys.stderr)
        for rel in missing:
            print(f"- {rel}", file=sys.stderr)
        return 1

    parts = [
        "# FinSignalHub Review Packet Export\n\n",
        "## Product Definition\n\n",
        read_required("CONTROL/01_PRODUCT_DEFINITION.md"),
        "\n## Stage Dashboard\n\n",
        read_required("CONTROL/19_STAGE_DASHBOARD.md"),
        "\n## Acceptance Result\n\n",
        read_required(f"reviews/{stage_dir}/STAGE_ACCEPTANCE_RESULT.md"),
        "\n## Blockers\n\n",
        read_required("CONTROL/20_BLOCKER_LOG.md"),
    ]
    output = safe_export_output_path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("".join(parts), encoding="utf-8", newline="\n")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
