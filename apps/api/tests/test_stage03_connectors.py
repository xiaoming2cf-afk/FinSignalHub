from __future__ import annotations

from datetime import datetime, timezone
import ast
import json
from pathlib import Path

import pytest

from finsignalhub_api.connectors import (
    ConnectorMappingError,
    ConnectorRunContext,
    normalize_arxiv_record,
    normalize_crossref_record,
    normalize_openalex_record,
    normalize_semantic_scholar_record,
    normalize_user_upload_metadata,
)
from finsignalhub_api.schemas.domain import DocumentCreate, SourceCreate, ToolCallLogCreate


FIXTURE_DIR = Path(__file__).parent / "fixtures" / "stage03_connectors"
PROJECT_ID = "stage03-project"
RETRIEVAL_TIME = datetime(2026, 5, 30, 20, 0, tzinfo=timezone.utc)


def _load_fixture(name: str) -> dict:
    with (FIXTURE_DIR / name).open(encoding="utf-8") as handle:
        return json.load(handle)


def _context(provider: str) -> ConnectorRunContext:
    return ConnectorRunContext(
        project_id=PROJECT_ID,
        retrieval_time=RETRIEVAL_TIME,
        query_ref=f"fixture-query:{provider}",
        fixture_id=f"{provider}-fixture-001",
    )


@pytest.mark.parametrize(
    ("provider", "fixture_name", "normalizer", "expected_source_type"),
    [
        ("openalex", "openalex_work.json", normalize_openalex_record, "literature"),
        ("crossref", "crossref_work.json", normalize_crossref_record, "literature"),
        (
            "semantic_scholar",
            "semantic_scholar_paper.json",
            normalize_semantic_scholar_record,
            "literature",
        ),
        ("arxiv", "arxiv_entry.json", normalize_arxiv_record, "preprint"),
        (
            "user_upload",
            "user_upload_metadata.json",
            normalize_user_upload_metadata,
            "user_upload_metadata",
        ),
    ],
)
def test_stage03_connectors_emit_stage02_schema_compatible_payloads(
    provider: str,
    fixture_name: str,
    normalizer,
    expected_source_type: str,
) -> None:
    result = normalizer(_load_fixture(fixture_name), _context(provider))

    source = result.to_source_create()
    document = result.to_document_create(source_id="source-id")
    tool_call = result.to_tool_call_log_create()

    assert isinstance(source, SourceCreate)
    assert isinstance(document, DocumentCreate)
    assert isinstance(tool_call, ToolCallLogCreate)
    assert source.project_id == PROJECT_ID
    assert document.project_id == PROJECT_ID
    assert tool_call.project_id == PROJECT_ID
    assert source.source_type == expected_source_type
    assert document.source_type == expected_source_type
    assert source.retrieval_time == RETRIEVAL_TIME
    assert document.retrieval_time == RETRIEVAL_TIME
    assert tool_call.called_at == RETRIEVAL_TIME
    assert tool_call.status == "succeeded"
    assert provider in tool_call.tool_name
    assert source.bibliographic_metadata is not None
    assert source.bibliographic_metadata["provider"] == provider
    assert source.bibliographic_metadata["schema_version"] == "stage03.normalized-source.v1"
    assert source.bibliographic_metadata["provider_metadata"]["external_ids"]
    assert "no abstract" in document.transformation_notes.lower() or "no pdf parsing" in document.transformation_notes.lower() or "file parsing" in document.transformation_notes.lower() or "no reference mining" in document.transformation_notes.lower()
    assert "evidence extraction" in document.transformation_notes.lower()
    assert "evidence_text" not in result.source_payload
    assert "evidence_text" not in result.document_payload_seed


def test_openalex_maps_doi_publication_time_and_host_venue() -> None:
    result = normalize_openalex_record(_load_fixture("openalex_work.json"), _context("openalex"))

    source = result.to_source_create()

    assert source.source_identity == "doi:10.1038/nature12373"
    assert source.doi == "10.1038/nature12373"
    assert source.publication_time is not None
    assert source.publication_time.isoformat().startswith("2017-06-12")
    assert source.bibliographic_metadata["provider_metadata"]["host_venue"] == "Nature Methods"
    assert source.locator == "https://openalex.org/W2741809807"


def test_crossref_maps_date_parts_container_and_authors() -> None:
    result = normalize_crossref_record(_load_fixture("crossref_work.json"), _context("crossref"))

    source = result.to_source_create()

    assert source.source_identity == "doi:10.1145/1234567.8901234"
    assert source.publication_time is not None
    assert source.publication_time.isoformat().startswith("2022-09-15")
    metadata = source.bibliographic_metadata["provider_metadata"]
    assert metadata["container_title"] == "Proceedings of Research Systems"
    assert metadata["authors"] == ["Lin Chen", "Mira Patel"]


def test_semantic_scholar_maps_external_ids_and_locator() -> None:
    result = normalize_semantic_scholar_record(
        _load_fixture("semantic_scholar_paper.json"),
        _context("semantic_scholar"),
    )

    source = result.to_source_create()

    assert source.source_identity == "doi:10.48550/example.2023.002"
    assert source.locator == "649def34f8be52c8b66281af98ae884c09aef38b"
    metadata = source.bibliographic_metadata["provider_metadata"]
    assert metadata["external_ids"]["arxiv"] == "2302.00002"
    assert metadata["corpus_id"] == 215416146


def test_arxiv_maps_preprint_identity_and_category() -> None:
    result = normalize_arxiv_record(_load_fixture("arxiv_entry.json"), _context("arxiv"))

    source = result.to_source_create()
    document = result.to_document_create(source_id="source-id")

    assert source.source_identity == "arxiv:2401.01234"
    assert source.source_type == "preprint"
    assert source.url == "https://arxiv.org/abs/2401.01234"
    assert document.locator == "2401.01234v2"
    metadata = source.bibliographic_metadata["provider_metadata"]
    assert metadata["primary_category"] == "cs.DL"
    assert metadata["raw_provider_id"] == "2401.01234v2"
    assert metadata["versioned_provider_id"] == "2401.01234v2"
    assert metadata["arxiv_version"] == "v2"
    assert metadata["external_ids"]["arxiv"] == "2401.01234"


@pytest.mark.parametrize(
    "raw_id",
    [
        "2401.01234v2",
        "arXiv:2401.01234v2",
        "https://arxiv.org/abs/2401.01234v2",
        "https://arxiv.org/pdf/2401.01234v2.pdf",
    ],
)
def test_arxiv_normalizes_versioned_and_url_ids_to_stable_identity(raw_id: str) -> None:
    fixture = _load_fixture("arxiv_entry.json")
    fixture["id"] = raw_id
    fixture.pop("links")
    fixture.pop("url", None)

    result = normalize_arxiv_record(fixture, _context("arxiv"))

    source = result.to_source_create()
    tool_call = result.to_tool_call_log_create()
    metadata = source.bibliographic_metadata["provider_metadata"]

    assert source.source_identity == "arxiv:2401.01234"
    assert source.url == "https://arxiv.org/abs/2401.01234"
    assert source.locator == "2401.01234v2"
    assert metadata["raw_provider_id"] == raw_id
    assert metadata["versioned_provider_id"] == "2401.01234v2"
    assert metadata["external_ids"]["arxiv"] == "2401.01234"
    assert metadata["external_ids"]["arxiv_versioned"] == "2401.01234v2"
    assert tool_call.safe_arguments["source_identity"] == "arxiv:2401.01234"


@pytest.mark.parametrize(
    ("raw_id", "stable_id", "versioned_id", "version"),
    [
        ("physics.ins-det/0301001", "physics.ins-det/0301001", "physics.ins-det/0301001", None),
        ("physics.atom-ph/9901001v1", "physics.atom-ph/9901001", "physics.atom-ph/9901001v1", "v1"),
        (
            "https://arxiv.org/abs/physics.ins-det/0301001v1",
            "physics.ins-det/0301001",
            "physics.ins-det/0301001v1",
            "v1",
        ),
        (
            "https://arxiv.org/pdf/physics.atom-ph/9901001v2.pdf",
            "physics.atom-ph/9901001",
            "physics.atom-ph/9901001v2",
            "v2",
        ),
    ],
)
def test_arxiv_normalizes_old_style_dotted_archive_classes(
    raw_id: str,
    stable_id: str,
    versioned_id: str,
    version: str | None,
) -> None:
    fixture = _load_fixture("arxiv_entry.json")
    fixture["id"] = raw_id
    fixture.pop("links")
    fixture.pop("url", None)

    result = normalize_arxiv_record(fixture, _context("arxiv"))

    source = result.to_source_create()
    tool_call = result.to_tool_call_log_create()
    metadata = source.bibliographic_metadata["provider_metadata"]

    assert source.source_identity == f"arxiv:{stable_id}"
    assert source.url == f"https://arxiv.org/abs/{stable_id}"
    assert source.locator == versioned_id
    assert metadata["raw_provider_id"] == raw_id
    assert metadata["versioned_provider_id"] == versioned_id
    assert metadata["arxiv_version"] == version
    assert metadata["external_ids"]["arxiv"] == stable_id
    assert metadata["external_ids"]["arxiv_versioned"] == versioned_id
    assert tool_call.safe_arguments["source_identity"] == f"arxiv:{stable_id}"


def test_user_upload_metadata_stays_metadata_only() -> None:
    result = normalize_user_upload_metadata(
        _load_fixture("user_upload_metadata.json"),
        _context("user_upload"),
    )

    source = result.to_source_create()
    document = result.to_document_create(source_id="source-id")

    assert source.source_type == "user_upload_metadata"
    assert source.source_identity.startswith("user-upload:b9e8f7c6")
    assert source.doi == "10.5281/zenodo.1234567"
    assert document.locator == "temporal-contamination-study-metadata.pdf"
    assert "file parsing" in document.transformation_notes.lower()
    assert "evidence extraction" in document.transformation_notes.lower()


def test_tool_call_safe_arguments_do_not_include_secret_like_fields() -> None:
    context = ConnectorRunContext(
        project_id=PROJECT_ID,
        retrieval_time=RETRIEVAL_TIME,
        query_ref="fixture-query:crossref",
        fixture_id="crossref-fixture-001",
        extra_safe_arguments={"api_key": "must-not-leak", "nested": {"token": "must-not-leak"}},
    )
    result = normalize_crossref_record(_load_fixture("crossref_work.json"), context)

    tool_call = result.to_tool_call_log_create()
    serialized = json.dumps(tool_call.safe_arguments, sort_keys=True).lower()

    assert "must-not-leak" not in serialized
    assert tool_call.safe_arguments["extra"]["api_key"] == "[redacted]"
    assert tool_call.safe_arguments["extra"]["nested"]["token"] == "[redacted]"


def test_tool_call_safe_arguments_preserve_core_provenance_fields() -> None:
    context = ConnectorRunContext(
        project_id=PROJECT_ID,
        retrieval_time=RETRIEVAL_TIME,
        query_ref="fixture-query:crossref",
        fixture_id="crossref-fixture-001",
        fixture=True,
        extra_safe_arguments={
            "provider": "spoofed",
            "fixture": False,
            "fixture_id": "spoofed-fixture",
            "query_ref": "spoofed-query",
            "source_identity": "spoofed-source",
            "api_key": "must-not-leak",
        },
    )
    result = normalize_crossref_record(_load_fixture("crossref_work.json"), context)

    source = result.to_source_create()
    tool_call = result.to_tool_call_log_create()
    serialized = json.dumps(tool_call.safe_arguments, sort_keys=True).lower()

    assert tool_call.safe_arguments["provider"] == "crossref"
    assert tool_call.safe_arguments["fixture"] is True
    assert tool_call.safe_arguments["fixture_id"] == "crossref-fixture-001"
    assert tool_call.safe_arguments["query_ref"] == "fixture-query:crossref"
    assert tool_call.safe_arguments["source_identity"] == source.source_identity
    assert tool_call.safe_arguments["extra"]["provider"] == "spoofed"
    assert tool_call.safe_arguments["extra"]["fixture"] is False
    assert tool_call.safe_arguments["extra"]["fixture_id"] == "spoofed-fixture"
    assert tool_call.safe_arguments["extra"]["query_ref"] == "spoofed-query"
    assert tool_call.safe_arguments["extra"]["source_identity"] == "spoofed-source"
    assert tool_call.safe_arguments["extra"]["api_key"] == "[redacted]"
    assert "must-not-leak" not in serialized


def test_user_upload_provider_metadata_redacts_secret_like_fields() -> None:
    fixture = _load_fixture("user_upload_metadata.json")
    fixture["metadata"]["access_token"] = "must-not-leak"
    fixture["metadata"]["nested"] = {"password": "must-not-leak"}

    result = normalize_user_upload_metadata(fixture, _context("user_upload"))
    source = result.to_source_create()
    metadata = source.bibliographic_metadata["provider_metadata"]["provided_metadata"]

    assert metadata["access_token"] == "[redacted]"
    assert metadata["nested"]["password"] == "[redacted]"
    assert "must-not-leak" not in json.dumps(source.bibliographic_metadata, sort_keys=True)


def test_connector_mapping_errors_are_deterministic() -> None:
    with pytest.raises(ConnectorMappingError) as error:
        normalize_openalex_record({"id": "https://openalex.org/W1"}, _context("openalex"))

    assert error.value.deterministic_error() == {
        "error": "connector_mapping_error",
        "provider": "openalex",
        "field_name": "title",
        "message": "title is required",
    }


def test_default_stage03_connector_modules_do_not_import_network_clients() -> None:
    connector_dir = Path(__file__).parents[1] / "finsignalhub_api" / "connectors"
    forbidden_modules = {"httpx", "requests", "urllib.request", "socket"}

    for path in connector_dir.glob("*.py"):
        text = path.read_text(encoding="utf-8")
        tree = ast.parse(text)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported = {alias.name for alias in node.names}
                assert imported.isdisjoint(forbidden_modules), path
            if isinstance(node, ast.ImportFrom):
                assert node.module not in forbidden_modules, path
