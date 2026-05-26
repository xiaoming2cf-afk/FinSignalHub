from fastapi.testclient import TestClient

from finsignalhub_mcp_server.main import app


def test_health_endpoint_reports_stage_01_scaffold() -> None:
    response = TestClient(app).get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "mcp_server",
        "stage": "01",
        "scope": "server-info scaffold",
    }


def test_server_info_declares_no_tools_enabled() -> None:
    response = TestClient(app).get("/server-info")

    assert response.status_code == 200
    assert response.json() == {
        "name": "finsignalhub-mcp-server",
        "stage": "01",
        "tools_enabled": False,
        "allowed_outputs": [],
        "scope": "health and server-info only",
    }

