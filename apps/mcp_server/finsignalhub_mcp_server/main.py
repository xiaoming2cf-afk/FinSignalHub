from __future__ import annotations

from fastapi import FastAPI


app = FastAPI(
    title="FinSignalHub MCP Server",
    description="Stage 01 server-info scaffold for future MCP tools.",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "mcp_server",
        "stage": "01",
        "scope": "server-info scaffold",
    }


@app.get("/server-info")
def server_info() -> dict[str, object]:
    return {
        "name": "finsignalhub-mcp-server",
        "stage": "01",
        "tools_enabled": False,
        "allowed_outputs": [],
        "scope": "health and server-info only",
    }

