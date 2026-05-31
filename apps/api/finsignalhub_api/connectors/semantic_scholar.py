from __future__ import annotations

from typing import Any, Mapping

from finsignalhub_api.connectors.base import (
    ConnectorRunContext,
    NormalizedConnectorResult,
    build_result,
    normalize_doi,
    parse_utc_datetime,
    require_text,
    source_identity,
)
from finsignalhub_api.models.enums import SourceType


PROVIDER = "semantic_scholar"


def normalize_semantic_scholar_record(
    record: Mapping[str, Any],
    context: ConnectorRunContext,
) -> NormalizedConnectorResult:
    paper_id = require_text(PROVIDER, "paperId", record.get("paperId"))
    title = require_text(PROVIDER, "title", record.get("title"))
    external_ids = record.get("externalIds") if isinstance(record.get("externalIds"), Mapping) else {}
    doi = normalize_doi(external_ids.get("DOI") or record.get("doi"))
    arxiv_id = external_ids.get("ArXiv") if isinstance(external_ids.get("ArXiv"), str) else None
    publication_time = parse_utc_datetime(record.get("publicationDate") or record.get("year"))
    identity = source_identity(PROVIDER, doi=doi, fallback_id=paper_id)
    provider_metadata = {
        "raw_provider_id": paper_id,
        "external_ids": {"semantic_scholar": paper_id, "doi": doi, "arxiv": arxiv_id},
        "corpus_id": record.get("corpusId"),
        "venue": record.get("venue"),
        "publication_types": record.get("publicationTypes") or [],
        "authors": _authors(record),
    }
    return build_result(
        provider=PROVIDER,
        context=context,
        source_identity_value=identity,
        source_type=SourceType.LITERATURE,
        title=title,
        url=record.get("url") if isinstance(record.get("url"), str) else None,
        doi=doi,
        locator=paper_id,
        publication_time=publication_time,
        provider_metadata=provider_metadata,
        transformation_notes="Normalized Semantic Scholar paper metadata into Stage 02 SourceCreate and DocumentCreate payloads; no abstract summarization or evidence extraction performed.",
    )


def _authors(record: Mapping[str, Any]) -> list[str]:
    authors: list[str] = []
    for author in record.get("authors") or []:
        if isinstance(author, Mapping) and isinstance(author.get("name"), str):
            authors.append(author["name"])
    return authors
