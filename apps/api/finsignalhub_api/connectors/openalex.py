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


PROVIDER = "openalex"


def normalize_openalex_record(
    record: Mapping[str, Any],
    context: ConnectorRunContext,
) -> NormalizedConnectorResult:
    raw_id = require_text(PROVIDER, "id", record.get("id"))
    title = require_text(PROVIDER, "title", record.get("title") or record.get("display_name"))
    doi = normalize_doi(record.get("doi"))
    url = _openalex_url(record)
    publication_time = parse_utc_datetime(record.get("publication_date") or record.get("publication_year"))
    identity = source_identity(PROVIDER, doi=doi, fallback_id=raw_id.rsplit("/", 1)[-1])
    locator = raw_id
    provider_metadata = {
        "raw_provider_id": raw_id,
        "external_ids": {"openalex": raw_id, "doi": doi},
        "authorships": _authors(record),
        "host_venue": _host_venue(record),
        "license": _license(record),
    }
    return build_result(
        provider=PROVIDER,
        context=context,
        source_identity_value=identity,
        source_type=SourceType.LITERATURE,
        title=title,
        url=url,
        doi=doi,
        locator=locator,
        publication_time=publication_time,
        provider_metadata=provider_metadata,
        transformation_notes="Normalized OpenAlex work metadata into Stage 02 SourceCreate and DocumentCreate payloads; no abstract or evidence extraction performed.",
    )


def _openalex_url(record: Mapping[str, Any]) -> str | None:
    primary_location = record.get("primary_location")
    if isinstance(primary_location, Mapping):
        landing_page_url = primary_location.get("landing_page_url")
        if isinstance(landing_page_url, str) and landing_page_url.strip():
            return landing_page_url.strip()
    value = record.get("doi") or record.get("id")
    return value.strip() if isinstance(value, str) and value.strip() else None


def _authors(record: Mapping[str, Any]) -> list[str]:
    authors: list[str] = []
    for authorship in record.get("authorships") or []:
        if not isinstance(authorship, Mapping):
            continue
        author = authorship.get("author")
        if isinstance(author, Mapping) and isinstance(author.get("display_name"), str):
            authors.append(author["display_name"])
    return authors


def _host_venue(record: Mapping[str, Any]) -> str | None:
    primary_location = record.get("primary_location")
    if not isinstance(primary_location, Mapping):
        return None
    source = primary_location.get("source")
    if isinstance(source, Mapping) and isinstance(source.get("display_name"), str):
        return source["display_name"]
    return None


def _license(record: Mapping[str, Any]) -> str | None:
    primary_location = record.get("primary_location")
    if isinstance(primary_location, Mapping) and isinstance(primary_location.get("license"), str):
        return primary_location["license"]
    return None
