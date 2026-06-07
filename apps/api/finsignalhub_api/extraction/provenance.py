from __future__ import annotations

from datetime import datetime

from finsignalhub_api.extraction.schemas import (
    EvidenceCandidate,
    EvidenceExtractionValidationError,
)
from finsignalhub_api.schemas.domain import DocumentCreate


def validate_document_provenance(document: DocumentCreate) -> None:
    required_text_fields = {
        "project_id": document.project_id,
        "source_id": document.source_id,
        "title": document.title,
        "source_identity": document.source_identity,
        "transformation_notes": document.transformation_notes,
    }
    for field_name, value in required_text_fields.items():
        if not isinstance(value, str) or not value.strip():
            raise EvidenceExtractionValidationError(
                "missing_document_provenance",
                field_name,
                f"{field_name} is required for Stage 04 provenance",
            )
    if not isinstance(document.retrieval_time, datetime) or document.retrieval_time.tzinfo is None:
        raise EvidenceExtractionValidationError(
            "missing_document_provenance",
            "retrieval_time",
            "retrieval_time must be timezone-aware",
        )


def validate_candidate_provenance(candidate: EvidenceCandidate, document: DocumentCreate) -> None:
    expected_document_ref = document.normalized_document_ref or f"document:{document.source_identity}"
    expected_pairs = {
        "project_id": (candidate.project_id, document.project_id),
        "source_id": (candidate.source_id, document.source_id),
        "document_ref": (candidate.document_ref, expected_document_ref),
        "source_identity": (candidate.source_identity, document.source_identity),
        "source_type": (candidate.source_type, document.source_type),
        "retrieval_time": (candidate.retrieval_time, document.retrieval_time),
    }
    for field_name, (observed, expected) in expected_pairs.items():
        if observed != expected:
            raise EvidenceExtractionValidationError(
                "candidate_provenance_mismatch",
                field_name,
                f"{field_name} must match the normalized document",
            )
    if not candidate.transformation_notes.strip():
        raise EvidenceExtractionValidationError(
            "missing_candidate_provenance",
            "transformation_notes",
            "transformation_notes is required",
        )
    if not candidate.tool_call_lineage:
        raise EvidenceExtractionValidationError(
            "missing_candidate_provenance",
            "tool_call_lineage",
            "tool_call_lineage is required",
        )

