from fastapi.testclient import TestClient

from finsignalhub_api.main import app


def test_health_endpoint_reports_stage_02_domain_primitives() -> None:
    response = TestClient(app).get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "api",
        "stage": "02",
        "scope": "domain-model-primitives",
    }
