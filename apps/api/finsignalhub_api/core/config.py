from __future__ import annotations

import os


DEFAULT_DATABASE_URL = "sqlite:///./finsignalhub_dev.db"


def get_database_url() -> str:
    """Return the configured database URL without reading secrets from code."""
    return (
        os.getenv("FINSIGNALHUB_DATABASE_URL")
        or os.getenv("DATABASE_URL")
        or DEFAULT_DATABASE_URL
    )
