from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from hashlib import sha256
import json
from typing import Any, Mapping

from finsignalhub_api.models.enums import SourceType, ToolCallStatus, ValidationStatus
from finsignalhub_api.schemas.domain import DocumentCreate, SourceCreate, ToolCallLogCreate


SCHEMA_VERSION = "stage03.normalized-source.v1"
TOOL_VERSION = "stage03"
SECRET_FIELD_MARKERS = ("api_key", "apikey", "authorization", "password", "secret", "token")


class ConnectorMappingError(ValueError):
    """Deterministic provider mapping failure for fixture/local normalization."""

    def __init__(self, provider: str, field_name: str, message: str) -> None:
        super().__init__(message)
        self.provider = provider
        self.field_name = field_name
        self.message = message

    def deterministic_error(self) -> dict[str, str]:
        return {
            "error": "connector_mapping_error",
            "provider": self.provider,
            "field_name": self.field_name,
            "message": self.message,
        }


@dataclass(frozen=True)
class ConnectorRunContext:
    project_id: str
    retrieval_time: datetime
    query_ref: str
    fixture_id: str | None = None
    fixture: bool = True
    extra_safe_arguments: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.retrieval_time.tzinfo is None:
            raise ValueError("ConnectorRunContext.retrieval_time must be timezone-aware")


@dataclass(frozen=True)
class NormalizedConnectorResult:
    provider: str
    source_payload: dict[str, Any]
    document_payload_seed: dict[str, Any]
    tool_call_payload: dict[str, Any]
    provider_metadata: dict[str, Any]

    def to_source_create(self) -> SourceCreate:
        return SourceCreate(**self.source_payload)

    def to_document_create(self, source_id: str) -> DocumentCreate:
        return DocumentCreate(source_id=source_id, **self.document_payload_seed)

    def to_tool_call_log_create(self) -> ToolCallLogCreate:
        return ToolCallLogCreate(**self.tool_call_payload)


def require_text(provider: str, field_name: str, value: Any) -> str:
    if isinstance(value, str) and value.strip():
        return " ".join(value.split())
    raise ConnectorMappingError(provider, field_name, f"{field_name} is required")


def first_text(value: Any) -> str | None:
    if isinstance(value, list):
        for item in value:
            if isinstance(item, str) and item.strip():
                return " ".join(item.split())
    if isinstance(value, str) and value.strip():
        return " ".join(value.split())
    return None


def normalize_doi(value: Any) -> str | None:
    if not isinstance(value, str) or not value.strip():
        return None
    doi = value.strip()
    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
        if doi.lower().startswith(prefix):
            doi = doi[len(prefix) :]
            break
    return doi.strip().lower() or None


def source_identity(provider: str, *, doi: str | None, fallback_id: str) -> str:
    if doi:
        return f"doi:{doi}"
    return f"{provider}:{fallback_id}"


def parse_utc_datetime(value: Any) -> datetime | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        if value.tzinfo is None:
            return value.replace(tzinfo=timezone.utc)
        return value.astimezone(timezone.utc)
    if isinstance(value, int):
        return datetime(value, 1, 1, tzinfo=timezone.utc)
    if isinstance(value, list) and value and all(isinstance(part, int) for part in value):
        year = value[0]
        month = value[1] if len(value) > 1 else 1
        day = value[2] if len(value) > 2 else 1
        return datetime(year, month, day, tzinfo=timezone.utc)
    if isinstance(value, str) and value.strip():
        text = value.strip()
        if len(text) == 4 and text.isdigit():
            return datetime(int(text), 1, 1, tzinfo=timezone.utc)
        normalized = text.replace("Z", "+00:00")
        if len(normalized) == 10:
            normalized = f"{normalized}T00:00:00+00:00"
        parsed = datetime.fromisoformat(normalized)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    return None


def date_parts_to_datetime(value: Any) -> datetime | None:
    if not isinstance(value, Mapping):
        return None
    parts = value.get("date-parts")
    if not isinstance(parts, list) or not parts:
        return None
    first = parts[0]
    return parse_utc_datetime(first)


def stable_argument_hash(payload: Mapping[str, Any]) -> str:
    encoded = json.dumps(payload, sort_keys=True, default=str, separators=(",", ":")).encode()
    return sha256(encoded).hexdigest()


def sanitize_metadata(value: Any) -> Any:
    if isinstance(value, Mapping):
        sanitized: dict[str, Any] = {}
        for key, item in value.items():
            key_text = str(key)
            if any(marker in key_text.lower() for marker in SECRET_FIELD_MARKERS):
                sanitized[key_text] = "[redacted]"
            else:
                sanitized[key_text] = sanitize_metadata(item)
        return sanitized
    if isinstance(value, list):
        return [sanitize_metadata(item) for item in value]
    return value


def sanitized_mapping(value: Mapping[str, Any]) -> dict[str, Any]:
    return sanitize_metadata(value)


def build_result(
    *,
    provider: str,
    context: ConnectorRunContext,
    source_identity_value: str,
    source_type: SourceType,
    title: str,
    url: str | None,
    doi: str | None,
    locator: str | None,
    publication_time: datetime | None,
    provider_metadata: dict[str, Any],
    transformation_notes: str,
) -> NormalizedConnectorResult:
    clean_provider_metadata = sanitized_mapping(provider_metadata)
    bibliographic_metadata = {
        "provider": provider,
        "schema_version": SCHEMA_VERSION,
        "provider_metadata": clean_provider_metadata,
        "fixture_id": context.fixture_id,
        "transformation_notes": transformation_notes,
    }
    source_payload: dict[str, Any] = {
        "project_id": context.project_id,
        "source_identity": source_identity_value,
        "source_type": source_type,
        "title": title,
        "url": url,
        "doi": doi,
        "locator": locator,
        "publication_time": publication_time,
        "retrieval_time": context.retrieval_time,
        "bibliographic_metadata": bibliographic_metadata,
        "validation_status": ValidationStatus.PENDING,
    }
    document_payload_seed: dict[str, Any] = {
        "project_id": context.project_id,
        "title": title,
        "normalized_document_ref": f"{provider}:{source_identity_value}",
        "source_identity": source_identity_value,
        "source_type": source_type,
        "retrieval_time": context.retrieval_time,
        "publication_time": publication_time,
        "url": url,
        "doi": doi,
        "locator": locator,
        "transformation_notes": transformation_notes,
        "validation_status": ValidationStatus.PENDING,
    }
    safe_arguments = sanitize_metadata({
        "provider": provider,
        "query_ref": context.query_ref,
        "fixture": context.fixture,
        "fixture_id": context.fixture_id,
        "source_identity": source_identity_value,
        **dict(context.extra_safe_arguments),
    })
    tool_call_payload = {
        "project_id": context.project_id,
        "tool_name": f"finsignalhub.stage03.{provider}.normalize",
        "tool_version": TOOL_VERSION,
        "schema_version": SCHEMA_VERSION,
        "called_at": context.retrieval_time,
        "argument_hash": stable_argument_hash(safe_arguments),
        "safe_arguments": safe_arguments,
        "status": ToolCallStatus.SUCCEEDED,
    }
    return NormalizedConnectorResult(
        provider=provider,
        source_payload=source_payload,
        document_payload_seed=document_payload_seed,
        tool_call_payload=tool_call_payload,
        provider_metadata=clean_provider_metadata,
    )
