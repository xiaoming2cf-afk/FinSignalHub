from __future__ import annotations

import ast
import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from finsignalhub_api.extraction import (
    EvidenceCandidate,
    EvidenceExtractionValidationError,
    ExtractionRelationType,
    ExtractionRequest,
    QuoteSpanCandidate,
    run_mock_extraction,
)
from finsignalhub_api.extraction.provenance import validate_candidate_provenance
from finsignalhub_api.extraction.quote_span import validate_quote_span
from finsignalhub_api.schemas.domain import DocumentCreate, EvidenceItemCreate


FIXTURE_DIR = Path(__file__).parent / "fixtures" / "stage04_extraction"


def _load_fixture(name: str) -> dict:
    with (FIXTURE_DIR / name).open(encoding="utf-8") as handle:
        return json.load(handle)


def _request_from_fixture(name: str) -> ExtractionRequest:
    fixture = _load_fixture(name)
    return ExtractionRequest(
        document=DocumentCreate(**fixture["normalized_document"]),
        document_text=fixture["document_text"],
        tool_call_id=fixture["tool_call_id"],
        tool_call_lineage=fixture["tool_call_lineage"],
    )


def test_worker_returns_quote_backed_candidate_from_normalized_document() -> None:
    request = _request_from_fixture("normalized_document_with_text.json")

    result = run_mock_extraction(request)

    assert result.candidate_only is True
    assert result.project_id == "stage03-project"
    assert result.document_ref == "arxiv:arxiv:2401.01234"
    [candidate] = result.candidates
    assert candidate.candidate_only is True
    assert candidate.relation_type == ExtractionRelationType.OBSERVATION
    assert candidate.source_identity == "arxiv:2401.01234"
    assert candidate.source_type == "preprint"
    assert candidate.quoted_evidence_span is not None
    assert candidate.no_quote_reason is None
    assert candidate.quoted_evidence_span.text == (
        "Temporal contamination can inflate financial language model evaluation results."
    )
    assert candidate.tool_call_lineage == ["finsignalhub.stage03.arxiv.normalize"]
    assert isinstance(candidate.validate_as_evidence_item_payload(), EvidenceItemCreate)


def test_worker_returns_metadata_candidate_with_no_quote_reason() -> None:
    request = _request_from_fixture("normalized_document_metadata_only.json")

    result = run_mock_extraction(request)

    [candidate] = result.candidates
    assert candidate.quoted_evidence_span is None
    assert candidate.no_quote_reason is not None
    assert "metadata-only" in candidate.no_quote_reason
    assert candidate.confidence < 0.5
    assert candidate.relation_type == ExtractionRelationType.BACKGROUND
    assert candidate.source_identity.startswith("user-upload:")
    assert isinstance(candidate.validate_as_evidence_item_payload(), EvidenceItemCreate)


def test_quote_span_validation_rejects_mismatched_text() -> None:
    with pytest.raises(EvidenceExtractionValidationError) as error:
        validate_quote_span(
            "abcde",
            QuoteSpanCandidate(text="abc", start=1, end=4),
        )

    assert error.value.deterministic_error() == {
        "error": "evidence_candidate_validation_error",
        "code": "quote_span_mismatch",
        "field_name": "quoted_evidence_span.text",
        "message": "quote span text does not match document text",
    }


def test_quote_span_validation_accepts_exact_offsets() -> None:
    validate_quote_span(
        "abcde",
        QuoteSpanCandidate(text="bcd", start=1, end=4),
    )


def test_no_quote_candidate_requires_rationale() -> None:
    request = _request_from_fixture("normalized_document_metadata_only.json")

    with pytest.raises(ValidationError):
        EvidenceCandidate.from_document(
            document=request.document,
            candidate_id="evcand-missing-rationale",
            evidence_text=request.document.title,
            relation_type=ExtractionRelationType.BACKGROUND,
            confidence=0.25,
            tool_call_lineage=request.tool_call_lineage,
            transformation_notes="Stage 04 validation fixture.",
        )


def test_no_quote_candidate_rejects_blank_rationale() -> None:
    request = _request_from_fixture("normalized_document_metadata_only.json")

    with pytest.raises(ValidationError):
        EvidenceCandidate.from_document(
            document=request.document,
            candidate_id="evcand-blank-rationale",
            evidence_text=request.document.title,
            relation_type=ExtractionRelationType.BACKGROUND,
            confidence=0.25,
            tool_call_lineage=request.tool_call_lineage,
            no_quote_reason="   ",
            transformation_notes="Stage 04 validation fixture.",
        )


def test_relation_type_is_bounded_to_stage04_enum() -> None:
    request = _request_from_fixture("normalized_document_with_text.json")

    with pytest.raises(ValidationError):
        EvidenceCandidate.from_document(
            document=request.document,
            candidate_id="evcand-bad-relation",
            evidence_text="bounded relation check",
            relation_type="supports",
            confidence=0.4,
            tool_call_lineage=request.tool_call_lineage,
            no_quote_reason="metadata-only validation branch",
            transformation_notes="Stage 04 relation validation fixture.",
        )


def test_document_provenance_is_required() -> None:
    fixture = _load_fixture("normalized_document_with_text.json")
    fixture["normalized_document"]["transformation_notes"] = None
    request = ExtractionRequest(
        document=DocumentCreate(**fixture["normalized_document"]),
        document_text=fixture["document_text"],
        tool_call_id=fixture["tool_call_id"],
        tool_call_lineage=fixture["tool_call_lineage"],
    )

    with pytest.raises(EvidenceExtractionValidationError) as error:
        run_mock_extraction(request)

    assert error.value.deterministic_error()["field_name"] == "transformation_notes"


def test_candidate_provenance_must_match_document() -> None:
    request = _request_from_fixture("normalized_document_with_text.json")
    result = run_mock_extraction(request)
    candidate = result.candidates[0].model_copy(update={"source_identity": "spoofed"})

    with pytest.raises(EvidenceExtractionValidationError) as error:
        validate_candidate_provenance(candidate, request.document)

    assert error.value.deterministic_error()["field_name"] == "source_identity"


def test_mock_output_is_deterministic() -> None:
    request = _request_from_fixture("normalized_document_with_text.json")

    first = run_mock_extraction(request)
    second = run_mock_extraction(request)

    assert first.model_dump(mode="json") == second.model_dump(mode="json")


def test_worker_runs_with_network_socket_disabled(monkeypatch: pytest.MonkeyPatch) -> None:
    import socket

    def blocked_socket(*args, **kwargs):  # noqa: ANN002, ANN003
        raise AssertionError("network access is forbidden in Stage 04 tests")

    monkeypatch.setattr(socket, "socket", blocked_socket)

    result = run_mock_extraction(_request_from_fixture("normalized_document_with_text.json"))

    assert result.candidates[0].candidate_id.startswith("evcand-")


def test_stage04_runtime_modules_do_not_import_network_or_provider_clients() -> None:
    extraction_dir = Path(__file__).parents[1] / "finsignalhub_api" / "extraction"
    forbidden_modules = {
        "aiohttp",
        "anthropic",
        "boto3",
        "google.generativeai",
        "http.client",
        "httpx",
        "langchain",
        "litellm",
        "llama_index",
        "openai",
        "requests",
        "socket",
        "urllib",
        "urllib.request",
        "urllib3",
    }

    for path in extraction_dir.glob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported = {alias.name for alias in node.names}
                assert imported.isdisjoint(forbidden_modules), path
            if isinstance(node, ast.ImportFrom):
                assert node.module not in forbidden_modules, path


def test_stage04_runtime_avoids_stage05_plus_scope_terms() -> None:
    extraction_dir = Path(__file__).parents[1] / "finsignalhub_api" / "extraction"
    forbidden_terms = [
        "claim graph computation",
        "research delta computation",
        "repro pack export",
        "mcp business tool",
        "chatbot ui",
        "generic rag",
        "stock prediction",
        "investment advice",
        "risk mode",
        "replay engine",
        "production queue",
        "provider api call",
    ]
    haystack = "\n".join(
        path.read_text(encoding="utf-8").lower()
        for path in extraction_dir.glob("*.py")
    )

    assert not any(term in haystack for term in forbidden_terms)
