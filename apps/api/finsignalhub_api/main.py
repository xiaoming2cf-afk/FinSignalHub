from __future__ import annotations

from fastapi import FastAPI

from finsignalhub_api.routers.domain import router as domain_router


app = FastAPI(
    title="FinSignalHub API",
    description="Stage 02 Research Mode domain model primitives for future evidence-stream workflows.",
    version="0.1.0",
)

app.include_router(domain_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "api",
        "stage": "02",
        "scope": "domain-model-primitives",
    }
