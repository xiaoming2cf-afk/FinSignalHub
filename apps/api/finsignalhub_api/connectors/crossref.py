from __future__ import annotations

from typing import Any, Mapping

from finsignalhub_api.connectors.base import (
    ConnectorRunContext,
    NormalizedConnectorResult,
    build_result,
    date_parts_to_datetime,
    first_text,
    normalize_doi,
    require_text,
    source_identity,
)
from finsignalhub_api.models.enums import SourceType


PROVIDER = "crossref"


def normalize_crossref_record(
    record: Mapping[str, Any],
    context: ConnectorRunContext,
) -> NormalizedConnectorResult:
    doi = normalize_doi(record.get("DOI") or record.get("doi"))
    raw_id = doi or require_text(PROVIDER, "URL", record.get("URL") or record.get("url"))
    title = require_text(PROVIDER, "title", first_text(record.get("title")))
    url = first_text(record.get("URL") or record.get("url")) or (f"https://doi.org/{doi}" if doi else None)
    publication_time = (
        date_parts_to_datetime(record.get("published-print"))
        or date_parts_to_datetime(record.get("published-online"))
        or date_parts_to_datetime(record.get("issued"))
    )
    identity = source_identity(PROVIDER, doi=doi, fallback_id=raw_id)
    provider_metadata = {
        "raw_provider_id": raw_id,
        "external_ids": {"doi": doi},
        "container_title": first_text(record.get("container-title")),
        "publisher": record.get("publisher"),
        "type": record.get("type"),
        "authors": _authors(record),
    }
    return build_result(
        provider=PROVIDER,
        context=context,
        source_identity_value=identity,
        source_type=SourceType.LITERATURE,
        title=title,
        url=url,
        doi=doi,
        locator=raw_id,
        publication_time=publication_time,
        provider_metadata=provider_metadata,
        transformation_notes="Normalized Crossref DOI metadata into Stage 02 SourceCreate and DocumentCreate payloads; no reference mining or evidence extraction performed.",
    )


def _authors(record: Mapping[str, Any]) -> list[str]:
    authors: list[str] = []
    for author in record.get("author") or []:
        if not isinstance(author, Mapping):
            continue
        given = author.get("given")
        family = author.get("family")
        name = " ".join(part for part in (given, family) if isinstance(part, str) and part.strip())
        if name:
            authors.append(name)
    return authors
