from __future__ import annotations

from fastapi import FastAPI


app = FastAPI(
    title="FinSignalHub API",
    description="Stage 01 health-only scaffold for future evidence-stream workflows.",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "api",
        "stage": "01",
        "scope": "health-only scaffold",
    }

