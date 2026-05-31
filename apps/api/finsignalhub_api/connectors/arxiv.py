from __future__ import annotations

import re
from typing import Any, Mapping

from finsignalhub_api.connectors.base import (
    ConnectorMappingError,
    ConnectorRunContext,
    NormalizedConnectorResult,
    build_result,
    normalize_doi,
    parse_utc_datetime,
    require_text,
)
from finsignalhub_api.models.enums import SourceType


PROVIDER = "arxiv"
_ARXIV_NEW_ID_RE = re.compile(r"(?P<stable>\d{4}\.\d{4,5})(?P<version>v\d+)?", re.IGNORECASE)
_ARXIV_OLD_ID_RE = re.compile(
    r"(?P<stable>[a-z-]+(?:\.[A-Z]{2})?/\d{7})(?P<version>v\d+)?",
    re.IGNORECASE,
)


def _normalize_arxiv_identifier(value: Any) -> tuple[str, str, str | None, str]:
    raw_id = require_text(PROVIDER, "id", value)
    candidate = raw_id.strip()
    lower_candidate = candidate.lower()
    for marker in ("/abs/", "/pdf/"):
        if marker in lower_candidate:
            candidate = candidate[lower_candidate.index(marker) + len(marker) :]
            lower_candidate = candidate.lower()
            break
    if lower_candidate.startswith("arxiv:"):
        candidate = candidate[len("arxiv:") :]
    candidate = candidate.split("?", 1)[0].split("#", 1)[0].strip().rstrip("/")
    if candidate.lower().endswith(".pdf"):
        candidate = candidate[:-4]

    for pattern in (_ARXIV_NEW_ID_RE, _ARXIV_OLD_ID_RE):
        match = pattern.fullmatch(candidate)
        if match:
            stable_id = match.group("stable")
            version = match.group("version")
            versioned_id = f"{stable_id}{version}" if version else stable_id
            return stable_id, versioned_id, version, raw_id

    raise ConnectorMappingError(
        PROVIDER,
        "id",
        "id must be a bare arXiv id, versioned id, or canonical arXiv URL",
    )


def normalize_arxiv_record(
    record: Mapping[str, Any],
    context: ConnectorRunContext,
) -> NormalizedConnectorResult:
    arxiv_id, versioned_arxiv_id, arxiv_version, raw_arxiv_id = _normalize_arxiv_identifier(
        record.get("id") or record.get("arxiv_id"),
    )
    title = require_text(PROVIDER, "title", record.get("title"))
    doi = normalize_doi(record.get("doi"))
    url = _best_url(record) or f"https://arxiv.org/abs/{arxiv_id}"
    publication_time = parse_utc_datetime(record.get("published") or record.get("updated"))
    provider_metadata = {
        "raw_provider_id": raw_arxiv_id,
        "versioned_provider_id": versioned_arxiv_id,
        "arxiv_version": arxiv_version,
        "external_ids": {
            "arxiv": arxiv_id,
            "arxiv_versioned": versioned_arxiv_id,
            "doi": doi,
        },
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
        locator=versioned_arxiv_id,
        publication_time=publication_time,
        provider_metadata=provider_metadata,
        transformation_notes="Normalized arXiv preprint metadata into Stage 02 SourceCreate and DocumentCreate payloads; no PDF parsing or evidence extraction performed.",
    )


def _best_url(record: Mapping[str, Any]) -> str | None:
    links = record.get("links")
    if isinstance(links, list):
        for link in links:
            if isinstance(link, Mapping) and link.get("rel") == "alternate" and isinstance(link.get("href"), str):
                return _canonical_arxiv_url(link["href"]) or link["href"]
    value = record.get("url")
    if isinstance(value, str) and value.strip():
        return _canonical_arxiv_url(value) or value
    return None


def _canonical_arxiv_url(value: str) -> str | None:
    try:
        stable_id, _, _, _ = _normalize_arxiv_identifier(value)
    except ConnectorMappingError:
        return None
    return f"https://arxiv.org/abs/{stable_id}"
