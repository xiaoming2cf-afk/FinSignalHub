from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def _run_alembic(command: str, database_url: str) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env["FINSIGNALHUB_DATABASE_URL"] = database_url
    return subprocess.run(
        [sys.executable, "-m", "alembic", "-c", "apps/api/alembic.ini", *command.split()],
        cwd=Path(__file__).resolve().parents[3],
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )


def test_alembic_upgrade_downgrade_upgrade_round_trips_sqlite(tmp_path: Path) -> None:
    database_url = f"sqlite+pysqlite:///{tmp_path / 'stage02.sqlite'}"

    for command in ["upgrade head", "downgrade -1", "upgrade head"]:
        result = _run_alembic(command, database_url)
        assert result.returncode == 0, result.stderr + result.stdout
