#!/usr/bin/env python3
"""Export a concise review packet from existing governance artifacts."""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def read_optional(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        return f"Missing: {rel}\n"
    return path.read_text(encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", required=True, help="Stage id such as 00_1")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    stage_dir = f"stage_{args.stage}"
    parts = [
        "# FinSignalHub Review Packet Export\n\n",
        "## Product Definition\n\n",
        read_optional("CONTROL/01_PRODUCT_DEFINITION.md"),
        "\n## Stage Dashboard\n\n",
        read_optional("CONTROL/19_STAGE_DASHBOARD.md"),
        "\n## Acceptance Result\n\n",
        read_optional(f"reviews/{stage_dir}/STAGE_ACCEPTANCE_RESULT.md"),
        "\n## Blockers\n\n",
        read_optional("CONTROL/20_BLOCKER_LOG.md"),
    ]
    output = ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("".join(parts), encoding="utf-8", newline="\n")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
