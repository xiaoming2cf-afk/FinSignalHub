from datetime import datetime, timezone
from typing import Any

from fastapi.testclient import TestClient


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _post(client: TestClient, route: str, payload: dict[str, Any]) -> dict[str, Any]:
    response = client.post(f"/research-mode/{route}", json=payload)
    assert response.status_code == 201, response.text
    return response.json()


def _create_project_evidence_claim(
    client: TestClient,
    *,
    title: str,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    project = _post(client, "research-projects", {"title": title})
    project_id = project["id"]
    source = _post(
        client,
        "sources",
        {
            "project_id": project_id,
            "source_identity": f"doi:10.0000/{project_id}",
            "source_type": "literature",
            "title": f"{title} source",
            "retrieval_time": _now(),
        },
    )
    tool_call = _post(
        client,
        "tool-call-logs",
        {
            "project_id": project_id,
            "tool_name": "manual.stage02.fixture",
            "called_at": _now(),
            "argument_hash": f"hash-{project_id}",
            "status": "succeeded",
        },
    )
    evidence = _post(
        client,
        "evidence-items",
        {
            "project_id": project_id,
            "source_id": source["id"],
            "tool_call_id": tool_call["id"],
            "evidence_text": "Evidence text",
            "source_identity": source["source_identity"],
            "source_type": "literature",
            "retrieval_time": _now(),
            "quoted_evidence_span": {"page": 1, "start": 0, "end": 13, "text": "Evidence text"},
            "transformation_notes": "manual fixture",
            "confidence": 0.9,
            "tool_call_lineage": [tool_call["id"]],
        },
    )
    claim = _post(
        client,
        "research-claims",
        {
            "project_id": project_id,
            "originating_evidence_item_id": evidence["id"],
            "tool_call_id": tool_call["id"],
            "claim_text": f"{title} contains fixture evidence.",
            "derivation_notes": "Derived from the fixture evidence item.",
            "confidence": 0.8,
            "tool_call_lineage": [tool_call["id"]],
        },
    )
    return project, tool_call, evidence, claim


def test_stage02_crud_routes_are_registered(client: TestClient) -> None:
    routes = {route.path for route in client.app.routes}

    for route in [
        "/research-mode/research-projects",
        "/research-mode/sources",
        "/research-mode/documents",
        "/research-mode/tool-call-logs",
        "/research-mode/evidence-items",
        "/research-mode/research-claims",
        "/research-mode/claim-evidence-edges",
        "/research-mode/research-deltas",
        "/research-mode/literature-matrix-rows",
        "/research-mode/method-cards",
        "/research-mode/dataset-cards",
        "/research-mode/repro-pack-exports",
    ]:
        assert route in routes


def test_crud_create_get_list_update_delete_for_stage02_entities(client: TestClient) -> None:
    project = _post(client, "research-projects", {"title": "Temporal contamination study"})
    project_id = project["id"]

    source = _post(
        client,
        "sources",
        {
            "project_id": project_id,
            "source_identity": "doi:10.0000/example",
            "source_type": "literature",
            "title": "Example paper",
            "retrieval_time": _now(),
        },
    )
    tool_call = _post(
        client,
        "tool-call-logs",
        {
            "project_id": project_id,
            "tool_name": "manual.stage02.fixture",
            "called_at": _now(),
            "argument_hash": "hash-fixture",
            "safe_arguments": {"fixture": True},
            "status": "succeeded",
        },
    )
    document = _post(
        client,
        "documents",
        {
            "project_id": project_id,
            "source_id": source["id"],
            "title": "Normalized example paper",
            "source_identity": source["source_identity"],
            "source_type": "literature",
            "retrieval_time": _now(),
            "transformation_notes": "normalized metadata only",
        },
    )
    evidence = _post(
        client,
        "evidence-items",
        {
            "project_id": project_id,
            "source_id": source["id"],
            "document_id": document["id"],
            "tool_call_id": tool_call["id"],
            "evidence_text": "Evidence text",
            "source_identity": source["source_identity"],
            "source_type": "literature",
            "retrieval_time": _now(),
            "quoted_evidence_span": {"page": 1, "start": 0, "end": 13, "text": "Evidence text"},
            "transformation_notes": "manual fixture",
            "confidence": 0.9,
            "tool_call_lineage": [tool_call["id"]],
        },
    )
    claim = _post(
        client,
        "research-claims",
        {
            "project_id": project_id,
            "originating_evidence_item_id": evidence["id"],
            "tool_call_id": tool_call["id"],
            "claim_text": "The paper contains fixture evidence.",
            "derivation_notes": "Derived from the fixture evidence item.",
            "confidence": 0.8,
            "tool_call_lineage": [tool_call["id"]],
        },
    )

    created = {
        "claim-evidence-edges": _post(
            client,
            "claim-evidence-edges",
            {
                "claim_id": claim["id"],
                "evidence_item_id": evidence["id"],
                "tool_call_id": tool_call["id"],
                "relation_type": "supports",
                "rationale": "Fixture evidence supports fixture claim.",
                "confidence": 0.8,
                "tool_call_lineage": [tool_call["id"]],
            },
        ),
        "research-deltas": _post(
            client,
            "research-deltas",
            {
                "project_id": project_id,
                "tool_call_id": tool_call["id"],
                "summary": "Stored delta artifact only.",
                "source_artifact_refs": [evidence["id"]],
                "generation_time": _now(),
                "transformation_notes": "no computation in Stage 02",
                "confidence": 0.7,
                "tool_call_lineage": [tool_call["id"]],
            },
        ),
        "literature-matrix-rows": _post(
            client,
            "literature-matrix-rows",
            {
                "project_id": project_id,
                "tool_call_id": tool_call["id"],
                "document_id": document["id"],
                "claim_id": claim["id"],
                "research_question": "What changed?",
                "evidence_summary": "Fixture row only.",
                "source_artifact_refs": [evidence["id"]],
                "transformation_notes": "manual row",
                "confidence": 0.7,
                "tool_call_lineage": [tool_call["id"]],
            },
        ),
        "method-cards": _post(
            client,
            "method-cards",
            {
                "project_id": project_id,
                "tool_call_id": tool_call["id"],
                "evidence_item_id": evidence["id"],
                "method_name": "Fixture method",
                "method_summary": "Stored method metadata only.",
                "source_artifact_refs": [evidence["id"]],
                "transformation_notes": "manual card",
                "confidence": 0.7,
                "tool_call_lineage": [tool_call["id"]],
            },
        ),
        "dataset-cards": _post(
            client,
            "dataset-cards",
            {
                "project_id": project_id,
                "tool_call_id": tool_call["id"],
                "evidence_item_id": evidence["id"],
                "dataset_name": "Fixture dataset",
                "dataset_summary": "Stored dataset metadata only.",
                "source_identity": "dataset:fixture",
                "source_type": "dataset",
                "retrieval_time": _now(),
                "source_artifact_refs": [evidence["id"]],
                "transformation_notes": "manual card",
                "confidence": 0.7,
                "tool_call_lineage": [tool_call["id"]],
            },
        ),
        "repro-pack-exports": _post(
            client,
            "repro-pack-exports",
            {
                "project_id": project_id,
                "tool_call_id": tool_call["id"],
                "manifest_ref": "manifest-stage02-fixture",
                "export_format": "jsonl",
                "source_artifact_refs": [evidence["id"]],
                "generation_time": _now(),
                "transformation_notes": "metadata record only",
                "tool_call_lineage": [tool_call["id"]],
            },
        ),
    }

    for route, item in {
        "research-projects": project,
        "sources": source,
        "documents": document,
        "tool-call-logs": tool_call,
        "evidence-items": evidence,
        "research-claims": claim,
        **created,
    }.items():
        response = client.get(f"/research-mode/{route}/{item['id']}")
        assert response.status_code == 200, response.text

        response = client.get(f"/research-mode/{route}")
        assert response.status_code == 200, response.text
        assert len(response.json()) >= 1

    response = client.patch(f"/research-mode/research-projects/{project_id}", json={"status": "paused"})
    assert response.status_code == 200, response.text
    assert response.json()["status"] == "paused"

    response = client.delete(f"/research-mode/repro-pack-exports/{created['repro-pack-exports']['id']}")
    assert response.status_code == 204


def test_evidence_update_cannot_clear_quote_provenance(client: TestClient) -> None:
    _project, _tool_call, evidence, _claim = _create_project_evidence_claim(
        client,
        title="Quote provenance project",
    )

    response = client.patch(
        f"/research-mode/evidence-items/{evidence['id']}",
        json={"quoted_evidence_span": None, "no_quote_reason": None},
    )

    assert response.status_code == 422
    assert response.json()["detail"]["error"] == "missing_evidence_quote_provenance"


def test_evidence_update_cannot_clear_only_quote_when_no_reason_exists(client: TestClient) -> None:
    _project, _tool_call, evidence, _claim = _create_project_evidence_claim(
        client,
        title="Quote-only provenance project",
    )

    response = client.patch(
        f"/research-mode/evidence-items/{evidence['id']}",
        json={"quoted_evidence_span": None},
    )

    assert response.status_code == 422
    assert response.json()["detail"]["error"] == "missing_evidence_quote_provenance"


def test_evidence_update_allows_replacing_quote_with_no_quote_reason(client: TestClient) -> None:
    _project, _tool_call, evidence, _claim = _create_project_evidence_claim(
        client,
        title="No quote replacement project",
    )

    response = client.patch(
        f"/research-mode/evidence-items/{evidence['id']}",
        json={
            "quoted_evidence_span": None,
            "no_quote_reason": "Evidence source is normalized metadata without a direct quote span.",
        },
    )

    assert response.status_code == 200, response.text
    payload = response.json()
    assert payload["quoted_evidence_span"] is None
    assert payload["no_quote_reason"] == "Evidence source is normalized metadata without a direct quote span."


def test_claim_evidence_edge_rejects_cross_project_links(client: TestClient) -> None:
    _project_a, tool_call_a, _evidence_a, claim_a = _create_project_evidence_claim(
        client,
        title="Project A",
    )
    _project_b, _tool_call_b, evidence_b, _claim_b = _create_project_evidence_claim(
        client,
        title="Project B",
    )

    response = client.post(
        "/research-mode/claim-evidence-edges",
        json={
            "claim_id": claim_a["id"],
            "evidence_item_id": evidence_b["id"],
            "tool_call_id": tool_call_a["id"],
            "relation_type": "supports",
            "rationale": "Cross-project link should be rejected.",
            "confidence": 0.8,
            "tool_call_lineage": [tool_call_a["id"]],
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"]["error"] == "cross_project_claim_evidence_edge"


def test_claim_evidence_edge_rejects_cross_project_tool_call(client: TestClient) -> None:
    _project_a, _tool_call_a, evidence_a, claim_a = _create_project_evidence_claim(
        client,
        title="Project A tool-call boundary",
    )
    _project_b, tool_call_b, _evidence_b, _claim_b = _create_project_evidence_claim(
        client,
        title="Project B tool-call boundary",
    )

    response = client.post(
        "/research-mode/claim-evidence-edges",
        json={
            "claim_id": claim_a["id"],
            "evidence_item_id": evidence_a["id"],
            "tool_call_id": tool_call_b["id"],
            "relation_type": "supports",
            "rationale": "Cross-project tool call should be rejected.",
            "confidence": 0.8,
            "tool_call_lineage": [tool_call_b["id"]],
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"]["error"] == "cross_project_claim_evidence_tool_call"
