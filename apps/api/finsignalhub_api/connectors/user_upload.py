from __future__ import annotations

from typing import Any, Mapping

from finsignalhub_api.connectors.base import (
    ConnectorRunContext,
    NormalizedConnectorResult,
    build_result,
    normalize_doi,
    parse_utc_datetime,
    require_text,
)
from finsignalhub_api.models.enums import SourceType


PROVIDER = "user_upload"


def normalize_user_upload_metadata(
    record: Mapping[str, Any],
    context: ConnectorRunContext,
) -> NormalizedConnectorResult:
    filename = require_text(PROVIDER, "filename", record.get("filename"))
    title = require_text(PROVIDER, "title", record.get("provided_title") or record.get("title"))
    file_hash = record.get("file_sha256") if isinstance(record.get("file_sha256"), str) else None
    doi = normalize_doi(record.get("provided_doi") or record.get("doi"))
    publication_time = parse_utc_datetime(record.get("publication_date"))
    source_key = file_hash or filename
    provider_metadata = {
        "raw_provider_id": source_key,
        "external_ids": {"doi": doi, "file_sha256": file_hash},
        "filename": filename,
        "content_type": record.get("content_type"),
        "citation": record.get("citation"),
        "provided_metadata": record.get("metadata") or {},
    }
    return build_result(
        provider=PROVIDER,
        context=context,
        source_identity_value=f"user-upload:{source_key}",
        source_type=SourceType.USER_UPLOAD_METADATA,
        title=title,
        url=record.get("source_url") if isinstance(record.get("source_url"), str) else None,
        doi=doi,
        locator=filename,
        publication_time=publication_time,
        provider_metadata=provider_metadata,
        transformation_notes="Normalized user-supplied upload metadata into Stage 02 SourceCreate and DocumentCreate payloads; file parsing and evidence extraction are explicitly out of scope.",
    )
