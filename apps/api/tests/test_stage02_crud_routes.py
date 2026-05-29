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


def _create_project_source_document_tool(
    client: TestClient,
    *,
    title: str,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    project = _post(client, "research-projects", {"title": title})
    source = _post(
        client,
        "sources",
        {
            "project_id": project["id"],
            "source_identity": f"doi:10.0000/source-{project['id']}",
            "source_type": "literature",
            "title": f"{title} source",
            "retrieval_time": _now(),
        },
    )
    tool_call = _post(
        client,
        "tool-call-logs",
        {
            "project_id": project["id"],
            "tool_name": "manual.stage02.fixture",
            "called_at": _now(),
            "argument_hash": f"hash-{project['id']}",
            "status": "succeeded",
        },
    )
    document = _post(
        client,
        "documents",
        {
            "project_id": project["id"],
            "source_id": source["id"],
            "title": f"{title} normalized document",
            "source_identity": source["source_identity"],
            "source_type": "literature",
            "retrieval_time": _now(),
            "transformation_notes": "manual fixture",
        },
    )
    return project, source, document, tool_call


def _create_project_domain_fixture(client: TestClient, *, title: str) -> dict[str, dict[str, Any]]:
    project, source, document, tool_call = _create_project_source_document_tool(
        client,
        title=title,
    )
    evidence = _post(
        client,
        "evidence-items",
        {
            "project_id": project["id"],
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
            "project_id": project["id"],
            "originating_evidence_item_id": evidence["id"],
            "tool_call_id": tool_call["id"],
            "claim_text": f"{title} contains fixture evidence.",
            "derivation_notes": "Derived from the fixture evidence item.",
            "confidence": 0.8,
            "tool_call_lineage": [tool_call["id"]],
        },
    )
    return {
        "project": project,
        "source": source,
        "document": document,
        "tool_call": tool_call,
        "evidence": evidence,
        "claim": claim,
    }


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


def test_source_create_rejects_unknown_project(client: TestClient) -> None:
    response = client.post(
        "/research-mode/sources",
        json={
            "project_id": "missing-project-id",
            "source_identity": "doi:10.0000/missing-project",
            "source_type": "literature",
            "title": "Orphan source must be rejected",
            "retrieval_time": _now(),
        },
    )

    assert response.status_code == 404
    assert response.json()["detail"]["model"] == "ResearchProject"


def test_tool_call_create_rejects_unknown_project(client: TestClient) -> None:
    response = client.post(
        "/research-mode/tool-call-logs",
        json={
            "project_id": "missing-project-id",
            "tool_name": "manual.stage02.fixture",
            "called_at": _now(),
            "argument_hash": "hash-missing-project",
            "status": "succeeded",
        },
    )

    assert response.status_code == 404
    assert response.json()["detail"]["model"] == "ResearchProject"


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


def test_evidence_create_rejects_cross_project_source(client: TestClient) -> None:
    project_a, _source_a, _document_a, tool_call_a = _create_project_source_document_tool(
        client,
        title="Project A evidence source boundary",
    )
    _project_b, source_b, _document_b, _tool_call_b = _create_project_source_document_tool(
        client,
        title="Project B evidence source boundary",
    )

    response = client.post(
        "/research-mode/evidence-items",
        json={
            "project_id": project_a["id"],
            "source_id": source_b["id"],
            "tool_call_id": tool_call_a["id"],
            "evidence_text": "Evidence text",
            "source_identity": source_b["source_identity"],
            "source_type": "literature",
            "retrieval_time": _now(),
            "quoted_evidence_span": {"page": 1, "start": 0, "end": 13, "text": "Evidence text"},
            "transformation_notes": "manual fixture",
            "confidence": 0.9,
            "tool_call_lineage": [tool_call_a["id"]],
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"]["error"] == "cross_project_evidence_reference"
    assert response.json()["detail"]["field_name"] == "source_id"


def test_document_create_rejects_cross_project_source(client: TestClient) -> None:
    project_a, _source_a, _document_a, _tool_call_a = _create_project_source_document_tool(
        client,
        title="Project A document source boundary",
    )
    _project_b, source_b, _document_b, _tool_call_b = _create_project_source_document_tool(
        client,
        title="Project B document source boundary",
    )

    response = client.post(
        "/research-mode/documents",
        json={
            "project_id": project_a["id"],
            "source_id": source_b["id"],
            "title": "Cross-project normalized document",
            "source_identity": source_b["source_identity"],
            "source_type": "literature",
            "retrieval_time": _now(),
            "transformation_notes": "manual fixture",
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"]["error"] == "cross_project_document_source"
    assert response.json()["detail"]["field_name"] == "source_id"


def test_evidence_create_rejects_cross_project_document(client: TestClient) -> None:
    project_a, source_a, _document_a, tool_call_a = _create_project_source_document_tool(
        client,
        title="Project A evidence document boundary",
    )
    _project_b, _source_b, document_b, _tool_call_b = _create_project_source_document_tool(
        client,
        title="Project B evidence document boundary",
    )

    response = client.post(
        "/research-mode/evidence-items",
        json={
            "project_id": project_a["id"],
            "source_id": source_a["id"],
            "document_id": document_b["id"],
            "tool_call_id": tool_call_a["id"],
            "evidence_text": "Evidence text",
            "source_identity": source_a["source_identity"],
            "source_type": "literature",
            "retrieval_time": _now(),
            "quoted_evidence_span": {"page": 1, "start": 0, "end": 13, "text": "Evidence text"},
            "transformation_notes": "manual fixture",
            "confidence": 0.9,
            "tool_call_lineage": [tool_call_a["id"]],
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"]["error"] == "cross_project_evidence_reference"
    assert response.json()["detail"]["field_name"] == "document_id"


def test_evidence_create_rejects_cross_project_tool_call_lineage(client: TestClient) -> None:
    project_a, source_a, document_a, tool_call_a = _create_project_source_document_tool(
        client,
        title="Project A evidence lineage boundary",
    )
    _project_b, _source_b, _document_b, tool_call_b = _create_project_source_document_tool(
        client,
        title="Project B evidence lineage boundary",
    )

    response = client.post(
        "/research-mode/evidence-items",
        json={
            "project_id": project_a["id"],
            "source_id": source_a["id"],
            "document_id": document_a["id"],
            "tool_call_id": tool_call_a["id"],
            "evidence_text": "Evidence text",
            "source_identity": source_a["source_identity"],
            "source_type": "literature",
            "retrieval_time": _now(),
            "quoted_evidence_span": {"page": 1, "start": 0, "end": 13, "text": "Evidence text"},
            "transformation_notes": "manual fixture",
            "confidence": 0.9,
            "tool_call_lineage": [tool_call_b["id"]],
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"]["error"] == "cross_project_evidence_lineage"
    assert response.json()["detail"]["field_name"] == "tool_call_lineage"


def test_evidence_update_rejects_cross_project_tool_call(client: TestClient) -> None:
    _project_a, _tool_call_a, evidence_a, _claim_a = _create_project_evidence_claim(
        client,
        title="Project A evidence update boundary",
    )
    _project_b, tool_call_b, _evidence_b, _claim_b = _create_project_evidence_claim(
        client,
        title="Project B evidence update boundary",
    )

    response = client.patch(
        f"/research-mode/evidence-items/{evidence_a['id']}",
        json={"tool_call_id": tool_call_b["id"]},
    )

    assert response.status_code == 400
    assert response.json()["detail"]["error"] == "cross_project_evidence_reference"
    assert response.json()["detail"]["field_name"] == "tool_call_id"


def test_research_claim_create_rejects_cross_project_originating_evidence(client: TestClient) -> None:
    project_a, tool_call_a, _evidence_a, _claim_a = _create_project_evidence_claim(
        client,
        title="Project A claim origin boundary",
    )
    _project_b, _tool_call_b, evidence_b, _claim_b = _create_project_evidence_claim(
        client,
        title="Project B claim origin boundary",
    )

    response = client.post(
        "/research-mode/research-claims",
        json={
            "project_id": project_a["id"],
            "originating_evidence_item_id": evidence_b["id"],
            "tool_call_id": tool_call_a["id"],
            "claim_text": "Cross-project originating evidence should be rejected.",
            "derivation_notes": "Manual fixture.",
            "confidence": 0.8,
            "tool_call_lineage": [tool_call_a["id"]],
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"]["error"] == "cross_project_claim_reference"
    assert response.json()["detail"]["field_name"] == "originating_evidence_item_id"


def test_research_claim_create_rejects_cross_project_tool_call(client: TestClient) -> None:
    _project_a, tool_call_a, _evidence_a, _claim_a = _create_project_evidence_claim(
        client,
        title="Project A claim tool boundary",
    )
    project_b, _tool_call_b, evidence_b, _claim_b = _create_project_evidence_claim(
        client,
        title="Project B claim tool boundary",
    )

    response = client.post(
        "/research-mode/research-claims",
        json={
            "project_id": project_b["id"],
            "originating_evidence_item_id": evidence_b["id"],
            "tool_call_id": tool_call_a["id"],
            "claim_text": "Cross-project tool call should be rejected.",
            "derivation_notes": "Manual fixture.",
            "confidence": 0.8,
            "tool_call_lineage": [tool_call_a["id"]],
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"]["error"] == "cross_project_claim_reference"
    assert response.json()["detail"]["field_name"] == "tool_call_id"


def test_research_claim_update_rejects_cross_project_originating_evidence(client: TestClient) -> None:
    _project_a, _tool_call_a, evidence_a, _claim_a = _create_project_evidence_claim(
        client,
        title="Project A claim update boundary",
    )
    _project_b, _tool_call_b, _evidence_b, claim_b = _create_project_evidence_claim(
        client,
        title="Project B claim update boundary",
    )

    response = client.patch(
        f"/research-mode/research-claims/{claim_b['id']}",
        json={"originating_evidence_item_id": evidence_a["id"]},
    )

    assert response.status_code == 400
    assert response.json()["detail"]["error"] == "cross_project_claim_reference"
    assert response.json()["detail"]["field_name"] == "originating_evidence_item_id"


def test_research_claim_update_rejects_cross_project_tool_call_lineage(client: TestClient) -> None:
    _project_a, _tool_call_a, _evidence_a, claim_a = _create_project_evidence_claim(
        client,
        title="Project A claim lineage boundary",
    )
    _project_b, tool_call_b, _evidence_b, _claim_b = _create_project_evidence_claim(
        client,
        title="Project B claim lineage boundary",
    )

    response = client.patch(
        f"/research-mode/research-claims/{claim_a['id']}",
        json={"tool_call_lineage": [tool_call_b["id"]]},
    )

    assert response.status_code == 400
    assert response.json()["detail"]["error"] == "cross_project_claim_lineage"
    assert response.json()["detail"]["field_name"] == "tool_call_lineage"


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


def test_claim_evidence_edge_rejects_cross_project_tool_call_lineage(client: TestClient) -> None:
    _project_a, tool_call_a, evidence_a, claim_a = _create_project_evidence_claim(
        client,
        title="Project A edge lineage boundary",
    )
    _project_b, tool_call_b, _evidence_b, _claim_b = _create_project_evidence_claim(
        client,
        title="Project B edge lineage boundary",
    )

    response = client.post(
        "/research-mode/claim-evidence-edges",
        json={
            "claim_id": claim_a["id"],
            "evidence_item_id": evidence_a["id"],
            "tool_call_id": tool_call_a["id"],
            "relation_type": "supports",
            "rationale": "Cross-project lineage should be rejected.",
            "confidence": 0.8,
            "tool_call_lineage": [tool_call_b["id"]],
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"]["error"] == "cross_project_claim_evidence_lineage"
    assert response.json()["detail"]["field_name"] == "tool_call_lineage"


def test_claim_evidence_edge_update_rejects_cross_project_tool_call(client: TestClient) -> None:
    _project_a, tool_call_a, evidence_a, claim_a = _create_project_evidence_claim(
        client,
        title="Project A edge update boundary",
    )
    _project_b, tool_call_b, _evidence_b, _claim_b = _create_project_evidence_claim(
        client,
        title="Project B edge update boundary",
    )
    edge = _post(
        client,
        "claim-evidence-edges",
        {
            "claim_id": claim_a["id"],
            "evidence_item_id": evidence_a["id"],
            "tool_call_id": tool_call_a["id"],
            "relation_type": "supports",
            "rationale": "Initial same-project edge.",
            "confidence": 0.8,
            "tool_call_lineage": [tool_call_a["id"]],
        },
    )

    response = client.patch(
        f"/research-mode/claim-evidence-edges/{edge['id']}",
        json={"tool_call_id": tool_call_b["id"]},
    )

    assert response.status_code == 400
    assert response.json()["detail"]["error"] == "cross_project_claim_evidence_tool_call"


def test_research_delta_rejects_cross_project_changed_claim(client: TestClient) -> None:
    fixture_a = _create_project_domain_fixture(client, title="Project A delta boundary")
    fixture_b = _create_project_domain_fixture(client, title="Project B delta boundary")

    response = client.post(
        "/research-mode/research-deltas",
        json={
            "project_id": fixture_a["project"]["id"],
            "tool_call_id": fixture_a["tool_call"]["id"],
            "summary": "Cross-project claim should be rejected.",
            "changed_claim_ids": [fixture_b["claim"]["id"]],
            "source_artifact_refs": [fixture_a["evidence"]["id"]],
            "generation_time": _now(),
            "transformation_notes": "manual fixture",
            "confidence": 0.7,
            "tool_call_lineage": [fixture_a["tool_call"]["id"]],
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"]["error"] == "cross_project_research_delta_reference"
    assert response.json()["detail"]["field_name"] == "changed_claim_ids"


def test_literature_matrix_rejects_cross_project_document(client: TestClient) -> None:
    fixture_a = _create_project_domain_fixture(client, title="Project A matrix boundary")
    fixture_b = _create_project_domain_fixture(client, title="Project B matrix boundary")

    response = client.post(
        "/research-mode/literature-matrix-rows",
        json={
            "project_id": fixture_a["project"]["id"],
            "tool_call_id": fixture_a["tool_call"]["id"],
            "document_id": fixture_b["document"]["id"],
            "claim_id": fixture_a["claim"]["id"],
            "research_question": "What changed?",
            "evidence_summary": "Cross-project document should be rejected.",
            "source_artifact_refs": [fixture_a["evidence"]["id"]],
            "transformation_notes": "manual fixture",
            "confidence": 0.7,
            "tool_call_lineage": [fixture_a["tool_call"]["id"]],
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"]["error"] == "cross_project_literature_matrix_reference"
    assert response.json()["detail"]["field_name"] == "document_id"


def test_research_delta_accepts_same_project_claim_evidence_edge_ref(client: TestClient) -> None:
    fixture = _create_project_domain_fixture(client, title="Project A edge ref acceptance")
    edge = _post(
        client,
        "claim-evidence-edges",
        {
            "claim_id": fixture["claim"]["id"],
            "evidence_item_id": fixture["evidence"]["id"],
            "tool_call_id": fixture["tool_call"]["id"],
            "relation_type": "supports",
            "rationale": "Fixture edge for source artifact ref.",
            "confidence": 0.8,
            "tool_call_lineage": [fixture["tool_call"]["id"]],
        },
    )

    response = client.post(
        "/research-mode/research-deltas",
        json={
            "project_id": fixture["project"]["id"],
            "tool_call_id": fixture["tool_call"]["id"],
            "summary": "Same-project edge ref should be accepted.",
            "source_artifact_refs": [edge["id"]],
            "generation_time": _now(),
            "transformation_notes": "manual fixture",
            "confidence": 0.7,
            "tool_call_lineage": [fixture["tool_call"]["id"]],
        },
    )

    assert response.status_code == 201, response.text


def test_research_delta_rejects_cross_project_claim_evidence_edge_ref(client: TestClient) -> None:
    fixture_a = _create_project_domain_fixture(client, title="Project A edge ref boundary")
    fixture_b = _create_project_domain_fixture(client, title="Project B edge ref boundary")
    edge_b = _post(
        client,
        "claim-evidence-edges",
        {
            "claim_id": fixture_b["claim"]["id"],
            "evidence_item_id": fixture_b["evidence"]["id"],
            "tool_call_id": fixture_b["tool_call"]["id"],
            "relation_type": "supports",
            "rationale": "Cross-project edge for source artifact ref.",
            "confidence": 0.8,
            "tool_call_lineage": [fixture_b["tool_call"]["id"]],
        },
    )

    response = client.post(
        "/research-mode/research-deltas",
        json={
            "project_id": fixture_a["project"]["id"],
            "tool_call_id": fixture_a["tool_call"]["id"],
            "summary": "Cross-project edge ref should be rejected.",
            "source_artifact_refs": [edge_b["id"]],
            "generation_time": _now(),
            "transformation_notes": "manual fixture",
            "confidence": 0.7,
            "tool_call_lineage": [fixture_a["tool_call"]["id"]],
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"]["error"] == "cross_project_research_delta_reference"
    assert response.json()["detail"]["field_name"] == "source_artifact_refs"


def test_method_card_rejects_cross_project_source_artifact_ref(client: TestClient) -> None:
    fixture_a = _create_project_domain_fixture(client, title="Project A method boundary")
    fixture_b = _create_project_domain_fixture(client, title="Project B method boundary")

    response = client.post(
        "/research-mode/method-cards",
        json={
            "project_id": fixture_a["project"]["id"],
            "tool_call_id": fixture_a["tool_call"]["id"],
            "evidence_item_id": fixture_a["evidence"]["id"],
            "method_name": "Fixture method",
            "method_summary": "Cross-project source artifact should be rejected.",
            "source_artifact_refs": [fixture_b["evidence"]["id"]],
            "transformation_notes": "manual fixture",
            "confidence": 0.7,
            "tool_call_lineage": [fixture_a["tool_call"]["id"]],
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"]["error"] == "cross_project_method_card_reference"
    assert response.json()["detail"]["field_name"] == "source_artifact_refs"


def test_method_card_rejects_unknown_source_artifact_ref(client: TestClient) -> None:
    fixture = _create_project_domain_fixture(client, title="Project A unknown ref boundary")

    response = client.post(
        "/research-mode/method-cards",
        json={
            "project_id": fixture["project"]["id"],
            "tool_call_id": fixture["tool_call"]["id"],
            "evidence_item_id": fixture["evidence"]["id"],
            "method_name": "Fixture method",
            "method_summary": "Unknown source artifact should be rejected.",
            "source_artifact_refs": ["missing-artifact-id"],
            "transformation_notes": "manual fixture",
            "confidence": 0.7,
            "tool_call_lineage": [fixture["tool_call"]["id"]],
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"]["error"] == "cross_project_method_card_reference"
    assert response.json()["detail"]["field_name"] == "source_artifact_refs"


def test_dataset_card_rejects_cross_project_evidence_item(client: TestClient) -> None:
    fixture_a = _create_project_domain_fixture(client, title="Project A dataset boundary")
    fixture_b = _create_project_domain_fixture(client, title="Project B dataset boundary")

    response = client.post(
        "/research-mode/dataset-cards",
        json={
            "project_id": fixture_a["project"]["id"],
            "tool_call_id": fixture_a["tool_call"]["id"],
            "evidence_item_id": fixture_b["evidence"]["id"],
            "dataset_name": "Fixture dataset",
            "dataset_summary": "Cross-project evidence should be rejected.",
            "source_identity": "dataset:fixture",
            "source_type": "dataset",
            "retrieval_time": _now(),
            "source_artifact_refs": [fixture_a["evidence"]["id"]],
            "transformation_notes": "manual fixture",
            "confidence": 0.7,
            "tool_call_lineage": [fixture_a["tool_call"]["id"]],
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"]["error"] == "cross_project_dataset_card_reference"
    assert response.json()["detail"]["field_name"] == "evidence_item_id"


def test_repro_pack_update_rejects_cross_project_tool_call_lineage(client: TestClient) -> None:
    fixture_a = _create_project_domain_fixture(client, title="Project A repro boundary")
    fixture_b = _create_project_domain_fixture(client, title="Project B repro boundary")
    repro_pack = _post(
        client,
        "repro-pack-exports",
        {
            "project_id": fixture_a["project"]["id"],
            "tool_call_id": fixture_a["tool_call"]["id"],
            "manifest_ref": "manifest-stage02-fixture",
            "export_format": "jsonl",
            "source_artifact_refs": [fixture_a["evidence"]["id"]],
            "generation_time": _now(),
            "transformation_notes": "manual fixture",
            "tool_call_lineage": [fixture_a["tool_call"]["id"]],
        },
    )

    response = client.patch(
        f"/research-mode/repro-pack-exports/{repro_pack['id']}",
        json={"tool_call_lineage": [fixture_b["tool_call"]["id"]]},
    )

    assert response.status_code == 400
    assert response.json()["detail"]["error"] == "cross_project_repro_pack_reference"
    assert response.json()["detail"]["field_name"] == "tool_call_lineage"
