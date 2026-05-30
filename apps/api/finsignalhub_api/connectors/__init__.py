"""Stage 03 source connector primitives.

These connectors normalize provider metadata into Stage 02 schema-compatible
payloads. They do not fetch live APIs, extract evidence, build claims, or expose
MCP tools.
"""

from finsignalhub_api.connectors.arxiv import normalize_arxiv_record
from finsignalhub_api.connectors.base import (
    ConnectorMappingError,
    ConnectorRunContext,
    NormalizedConnectorResult,
)
from finsignalhub_api.connectors.crossref import normalize_crossref_record
from finsignalhub_api.connectors.openalex import normalize_openalex_record
from finsignalhub_api.connectors.semantic_scholar import normalize_semantic_scholar_record
from finsignalhub_api.connectors.user_upload import normalize_user_upload_metadata

__all__ = [
    "ConnectorMappingError",
    "ConnectorRunContext",
    "NormalizedConnectorResult",
    "normalize_arxiv_record",
    "normalize_crossref_record",
    "normalize_openalex_record",
    "normalize_semantic_scholar_record",
    "normalize_user_upload_metadata",
]
