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


PROVIDER = "arxiv"


def normalize_arxiv_record(
    record: Mapping[str, Any],
    context: ConnectorRunContext,
) -> NormalizedConnectorResult:
    arxiv_id = require_text(PROVIDER, "id", record.get("id") or record.get("arxiv_id"))
    title = require_text(PROVIDER, "title", record.get("title"))
    doi = normalize_doi(record.get("doi"))
    url = _best_url(record) or f"https://arxiv.org/abs/{arxiv_id}"
    publication_time = parse_utc_datetime(record.get("published") or record.get("updated"))
    provider_metadata = {
        "raw_provider_id": arxiv_id,
        "external_ids": {"arxiv": arxiv_id, "doi": doi},
        "authors": record.get("authors") or [],
        "primary_category": record.get("primary_category"),
        "updated": record.get("updated"),
    }
    return build_result(
        provider=PROVIDER,
        context=context,
        source_identity_value=f"arxiv:{arxiv_id}",
        source_type=SourceType.PREPRINT,
        title=title,
        url=url,
        doi=doi,
        locator=arxiv_id,
        publication_time=publication_time,
        provider_metadata=provider_metadata,
        transformation_notes="Normalized arXiv preprint metadata into Stage 02 SourceCreate and DocumentCreate payloads; no PDF parsing or evidence extraction performed.",
    )


def _best_url(record: Mapping[str, Any]) -> str | None:
    links = record.get("links")
    if isinstance(links, list):
        for link in links:
            if isinstance(link, Mapping) and link.get("rel") == "alternate" and isinstance(link.get("href"), str):
                return link["href"]
    value = record.get("url")
    return value if isinstance(value, str) and value.strip() else None
