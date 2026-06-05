from __future__ import annotations

from typing import Any

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, model_validator

from finsignalhub_api.extraction.relations import ExtractionRelationType
from finsignalhub_api.models.enums import SourceType, ValidationStatus
from finsignalhub_api.schemas.domain import DocumentCreate, EvidenceItemCreate


SCHEMA_VERSION = "stage04.evidence-candidate.v1"


class EvidenceExtractionValidationError(ValueError):
    def __init__(self, code: str, field_name: str, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.field_name = field_name
        self.message = message

    def deterministic_error(self) -> dict[str, str]:
        return {
            "error": "evidence_candidate_validation_error",
            "code": self.code,
            "field_name": self.field_name,
            "message": self.message,
        }


class QuoteSpanCandidate(BaseModel):
    text: str = Field(min_length=1)
    start: int | None = Field(default=None, ge=0)
    end: int | None = Field(default=None, ge=0)
    page: str | None = None
    section: str | None = None
    locator: str | None = None

    @model_validator(mode="after")
    def validate_shape(self) -> "QuoteSpanCandidate":
        has_start = self.start is not None
        has_end = self.end is not None
        if has_start != has_end:
            raise ValueError("quote span start and end must be provided together")
        if self.start is not None and self.end is not None and self.start >= self.end:
            raise ValueError("quote span start must be lower than end")
        has_locator = any((self.page, self.section, self.locator))
        if self.start is None and not has_locator:
            raise ValueError("quote span requires offsets or page/section/locator")
        return self


class EvidenceCandidate(BaseModel):
    model_config = ConfigDict(use_enum_values=False)

    candidate_id: str = Field(min_length=1)
    project_id: str = Field(min_length=1)
    source_id: str | None = None
    document_ref: str = Field(min_length=1)
    document_title: str = Field(min_length=1)
    tool_call_id: str | None = None
    evidence_text: str = Field(min_length=1)
    source_identity: str = Field(min_length=1)
    source_type: SourceType
    retrieval_time: AwareDatetime
    publication_time: AwareDatetime | None = None
    url: str | None = None
    doi: str | None = None
    locator: str | None = None
    quoted_evidence_span: QuoteSpanCandidate | None = None
    no_quote_reason: str | None = None
    relation_type: ExtractionRelationType
    transformation_notes: str = Field(min_length=1)
    confidence: float = Field(ge=0, le=1)
    tool_call_lineage: list[str] = Field(min_length=1)
    validation_status: ValidationStatus = ValidationStatus.PENDING
    extraction_schema_version: str = SCHEMA_VERSION
    candidate_only: bool = True

    @model_validator(mode="after")
    def require_quote_or_reason(self) -> "EvidenceCandidate":
        if self.quoted_evidence_span is None and not self.no_quote_reason:
            raise ValueError("quoted_evidence_span or no_quote_reason is required")
        if self.quoted_evidence_span is not None and self.no_quote_reason:
            raise ValueError("quoted_evidence_span and no_quote_reason are mutually exclusive")
        if not self.candidate_only:
            raise ValueError("Stage 04 output must remain candidate_only")
        return self

    @classmethod
    def from_document(
        cls,
        *,
        document: DocumentCreate,
        candidate_id: str,
        evidence_text: str,
        relation_type: ExtractionRelationType,
        confidence: float,
        tool_call_lineage: list[str],
        quoted_evidence_span: QuoteSpanCandidate | None = None,
        no_quote_reason: str | None = None,
        tool_call_id: str | None = None,
        transformation_notes: str,
    ) -> "EvidenceCandidate":
        document_ref = document.normalized_document_ref or f"document:{document.source_identity}"
        return cls(
            candidate_id=candidate_id,
            project_id=document.project_id,
            source_id=document.source_id,
            document_ref=document_ref,
            document_title=document.title,
            tool_call_id=tool_call_id,
            evidence_text=evidence_text,
            source_identity=document.source_identity,
            source_type=document.source_type,
            retrieval_time=document.retrieval_time,
            publication_time=document.publication_time,
            url=document.url,
            doi=document.doi,
            locator=document.locator,
            quoted_evidence_span=quoted_evidence_span,
            no_quote_reason=no_quote_reason,
            relation_type=relation_type,
            transformation_notes=transformation_notes,
            confidence=confidence,
            tool_call_lineage=tool_call_lineage,
            validation_status=ValidationStatus.PENDING,
        )

    def to_evidence_item_payload(self) -> dict[str, Any]:
        return {
            "project_id": self.project_id,
            "source_id": self.source_id,
            "document_id": None,
            "tool_call_id": self.tool_call_id,
            "evidence_text": self.evidence_text,
            "source_identity": self.source_identity,
            "source_type": self.source_type,
            "retrieval_time": self.retrieval_time,
            "publication_time": self.publication_time,
            "url": self.url,
            "doi": self.doi,
            "locator": self.locator,
            "quoted_evidence_span": (
                self.quoted_evidence_span.model_dump(exclude_none=True)
                if self.quoted_evidence_span
                else None
            ),
            "no_quote_reason": self.no_quote_reason,
            "transformation_notes": self.transformation_notes,
            "confidence": self.confidence,
            "tool_call_lineage": self.tool_call_lineage,
            "validation_status": self.validation_status,
        }

    def validate_as_evidence_item_payload(self) -> EvidenceItemCreate:
        return EvidenceItemCreate(**self.to_evidence_item_payload())


class ExtractionRequest(BaseModel):
    document: DocumentCreate
    document_text: str | None = None
    tool_call_id: str | None = None
    tool_call_lineage: list[str] = Field(min_length=1)


class ExtractionResult(BaseModel):
    project_id: str
    document_ref: str
    candidates: list[EvidenceCandidate]
    extraction_schema_version: str = SCHEMA_VERSION
    candidate_only: bool = True

    @model_validator(mode="after")
    def validate_result_scope(self) -> "ExtractionResult":
        if not self.candidate_only:
            raise ValueError("Stage 04 output must remain candidate_only")
        if not self.candidates:
            raise ValueError("at least one evidence candidate is required")
        for candidate in self.candidates:
            if candidate.project_id != self.project_id:
                raise ValueError("candidate project_id must match result project_id")
            if candidate.document_ref != self.document_ref:
                raise ValueError("candidate document_ref must match result document_ref")
        return self

