from fastapi.testclient import TestClient

from finsignalhub_api.main import app


def test_health_endpoint_reports_stage_01_scaffold() -> None:
    response = TestClient(app).get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "api",
        "stage": "01",
        "scope": "health-only scaffold",
    }

