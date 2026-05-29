from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from pydantic import (
    AwareDatetime,
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
    model_validator,
)

from finsignalhub_api.models.enums import (
    ClaimStatus,
    EdgeRelationType,
    ReproPackStatus,
    SourceType,
    ToolCallStatus,
    ValidationStatus,
)


class OrmSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    @field_validator("*", mode="before")
    @classmethod
    def normalize_orm_datetime(cls, value: object) -> object:
        if isinstance(value, datetime) and value.tzinfo is None:
            return value.replace(tzinfo=timezone.utc)
        return value


class TimestampedRead(OrmSchema):
    id: str
    created_at: AwareDatetime
    updated_at: AwareDatetime


def _require_quote_shape(span: dict[str, Any] | None) -> None:
    if span is None:
        return
    if not span.get("text"):
        raise ValueError("quoted_evidence_span.text is required")
    has_offsets = "start" in span and "end" in span
    has_locator = any(span.get(key) for key in ("page", "section", "locator"))
    if not has_offsets and not has_locator:
        raise ValueError("quoted_evidence_span requires offsets or page/section/locator")


class ResearchProjectCreate(BaseModel):
    title: str
    research_question: str | None = None
    owner_ref: str | None = None
    status: str = "active"
    scope_note: str | None = None


class ResearchProjectUpdate(BaseModel):
    title: str | None = None
    research_question: str | None = None
    owner_ref: str | None = None
    status: str | None = None
    scope_note: str | None = None


class ResearchProjectRead(TimestampedRead, ResearchProjectCreate):
    pass


class SourceCreate(BaseModel):
    project_id: str
    source_identity: str
    source_type: SourceType = SourceType.LITERATURE
    title: str | None = None
    url: str | None = None
    doi: str | None = None
    locator: str | None = None
    publication_time: AwareDatetime | None = None
    retrieval_time: AwareDatetime
    bibliographic_metadata: dict[str, Any] | None = None
    validation_status: ValidationStatus = ValidationStatus.PENDING


class SourceUpdate(BaseModel):
    source_identity: str | None = None
    source_type: SourceType | None = None
    title: str | None = None
    url: str | None = None
    doi: str | None = None
    locator: str | None = None
    publication_time: AwareDatetime | None = None
    retrieval_time: AwareDatetime | None = None
    bibliographic_metadata: dict[str, Any] | None = None
    validation_status: ValidationStatus | None = None


class SourceRead(TimestampedRead, SourceCreate):
    pass


class DocumentCreate(BaseModel):
    project_id: str
    source_id: str
    title: str
    normalized_document_ref: str | None = None
    source_identity: str
    source_type: SourceType
    retrieval_time: AwareDatetime
    publication_time: AwareDatetime | None = None
    url: str | None = None
    doi: str | None = None
    locator: str | None = None
    transformation_notes: str | None = None
    validation_status: ValidationStatus = ValidationStatus.PENDING


class DocumentUpdate(BaseModel):
    title: str | None = None
    normalized_document_ref: str | None = None
    source_identity: str | None = None
    source_type: SourceType | None = None
    retrieval_time: AwareDatetime | None = None
    publication_time: AwareDatetime | None = None
    url: str | None = None
    doi: str | None = None
    locator: str | None = None
    transformation_notes: str | None = None
    validation_status: ValidationStatus | None = None


class DocumentRead(TimestampedRead, DocumentCreate):
    pass


class ToolCallLogCreate(BaseModel):
    project_id: str
    tool_name: str
    tool_version: str | None = None
    schema_version: str | None = None
    called_at: AwareDatetime
    argument_hash: str
    safe_arguments: dict[str, Any] | None = None
    input_artifact_ids: list[str] | None = Field(default=None, min_length=1)
    output_artifact_ids: list[str] | None = Field(default=None, min_length=1)
    status: ToolCallStatus = ToolCallStatus.PLANNED
    deterministic_error: dict[str, Any] | None = None


class ToolCallLogUpdate(BaseModel):
    tool_name: str | None = None
    tool_version: str | None = None
    schema_version: str | None = None
    called_at: AwareDatetime | None = None
    argument_hash: str | None = None
    safe_arguments: dict[str, Any] | None = None
    input_artifact_ids: list[str] | None = Field(default=None, min_length=1)
    output_artifact_ids: list[str] | None = Field(default=None, min_length=1)
    status: ToolCallStatus | None = None
    deterministic_error: dict[str, Any] | None = None


class ToolCallLogRead(TimestampedRead, ToolCallLogCreate):
    pass


class EvidenceItemCreate(BaseModel):
    project_id: str
    source_id: str | None = None
    document_id: str | None = None
    tool_call_id: str | None = None
    evidence_text: str
    source_identity: str
    source_type: SourceType
    retrieval_time: AwareDatetime
    publication_time: AwareDatetime | None = None
    url: str | None = None
    doi: str | None = None
    locator: str | None = None
    quoted_evidence_span: dict[str, Any] | None = None
    no_quote_reason: str | None = None
    transformation_notes: str
    confidence: float = Field(ge=0, le=1)
    tool_call_lineage: list[str] = Field(min_length=1)
    validation_status: ValidationStatus = ValidationStatus.PENDING

    @model_validator(mode="after")
    def require_quote_or_reason(self) -> "EvidenceItemCreate":
        if not self.quoted_evidence_span and not self.no_quote_reason:
            raise ValueError("quoted_evidence_span or no_quote_reason is required")
        _require_quote_shape(self.quoted_evidence_span)
        return self


class EvidenceItemUpdate(BaseModel):
    source_id: str | None = None
    document_id: str | None = None
    tool_call_id: str | None = None
    evidence_text: str | None = None
    source_identity: str | None = None
    source_type: SourceType | None = None
    retrieval_time: AwareDatetime | None = None
    publication_time: AwareDatetime | None = None
    url: str | None = None
    doi: str | None = None
    locator: str | None = None
    quoted_evidence_span: dict[str, Any] | None = None
    no_quote_reason: str | None = None
    transformation_notes: str | None = None
    confidence: float | None = Field(default=None, ge=0, le=1)
    tool_call_lineage: list[str] | None = Field(default=None, min_length=1)
    validation_status: ValidationStatus | None = None


class EvidenceItemRead(TimestampedRead, EvidenceItemCreate):
    pass


class ResearchClaimCreate(BaseModel):
    project_id: str
    originating_evidence_item_id: str
    tool_call_id: str | None = None
    claim_text: str
    derivation_notes: str
    confidence: float = Field(ge=0, le=1)
    status: ClaimStatus = ClaimStatus.PROPOSED
    tool_call_lineage: list[str] = Field(min_length=1)
    validation_status: ValidationStatus = ValidationStatus.PENDING


class ResearchClaimUpdate(BaseModel):
    originating_evidence_item_id: str | None = None
    tool_call_id: str | None = None
    claim_text: str | None = None
    derivation_notes: str | None = None
    confidence: float | None = Field(default=None, ge=0, le=1)
    status: ClaimStatus | None = None
    tool_call_lineage: list[str] | None = Field(default=None, min_length=1)
    validation_status: ValidationStatus | None = None


class ResearchClaimRead(TimestampedRead, ResearchClaimCreate):
    pass


class ClaimEvidenceEdgeCreate(BaseModel):
    claim_id: str
    evidence_item_id: str
    tool_call_id: str | None = None
    relation_type: EdgeRelationType = EdgeRelationType.SUPPORTS
    rationale: str
    confidence: float = Field(ge=0, le=1)
    tool_call_lineage: list[str] = Field(min_length=1)
    validation_status: ValidationStatus = ValidationStatus.PENDING


class ClaimEvidenceEdgeUpdate(BaseModel):
    tool_call_id: str | None = None
    relation_type: EdgeRelationType | None = None
    rationale: str | None = None
    confidence: float | None = Field(default=None, ge=0, le=1)
    tool_call_lineage: list[str] | None = Field(default=None, min_length=1)
    validation_status: ValidationStatus | None = None


class ClaimEvidenceEdgeRead(TimestampedRead, ClaimEvidenceEdgeCreate):
    pass


class ResearchDeltaCreate(BaseModel):
    project_id: str
    tool_call_id: str | None = None
    summary: str
    changed_claim_ids: list[str] | None = Field(default=None, min_length=1)
    source_artifact_refs: list[str] = Field(min_length=1)
    generation_time: AwareDatetime
    transformation_notes: str
    confidence: float = Field(ge=0, le=1)
    tool_call_lineage: list[str] = Field(min_length=1)
    validation_status: ValidationStatus = ValidationStatus.PENDING


class ResearchDeltaUpdate(BaseModel):
    summary: str | None = None
    tool_call_id: str | None = None
    changed_claim_ids: list[str] | None = Field(default=None, min_length=1)
    source_artifact_refs: list[str] | None = Field(default=None, min_length=1)
    generation_time: AwareDatetime | None = None
    transformation_notes: str | None = None
    confidence: float | None = Field(default=None, ge=0, le=1)
    tool_call_lineage: list[str] | None = Field(default=None, min_length=1)
    validation_status: ValidationStatus | None = None


class ResearchDeltaRead(TimestampedRead, ResearchDeltaCreate):
    pass


class LiteratureMatrixRowCreate(BaseModel):
    project_id: str
    tool_call_id: str | None = None
    document_id: str | None = None
    claim_id: str | None = None
    research_question: str
    method_summary: str | None = None
    dataset_summary: str | None = None
    evidence_summary: str
    source_artifact_refs: list[str] = Field(min_length=1)
    transformation_notes: str
    confidence: float = Field(ge=0, le=1)
    tool_call_lineage: list[str] = Field(min_length=1)
    validation_status: ValidationStatus = ValidationStatus.PENDING


class LiteratureMatrixRowUpdate(BaseModel):
    document_id: str | None = None
    tool_call_id: str | None = None
    claim_id: str | None = None
    research_question: str | None = None
    method_summary: str | None = None
    dataset_summary: str | None = None
    evidence_summary: str | None = None
    source_artifact_refs: list[str] | None = Field(default=None, min_length=1)
    transformation_notes: str | None = None
    confidence: float | None = Field(default=None, ge=0, le=1)
    tool_call_lineage: list[str] | None = Field(default=None, min_length=1)
    validation_status: ValidationStatus | None = None


class LiteratureMatrixRowRead(TimestampedRead, LiteratureMatrixRowCreate):
    pass


class MethodCardCreate(BaseModel):
    project_id: str
    tool_call_id: str | None = None
    evidence_item_id: str | None = None
    method_name: str
    method_summary: str
    assumptions: str | None = None
    limitations: str | None = None
    source_artifact_refs: list[str] = Field(min_length=1)
    transformation_notes: str
    confidence: float = Field(ge=0, le=1)
    tool_call_lineage: list[str] = Field(min_length=1)
    validation_status: ValidationStatus = ValidationStatus.PENDING


class MethodCardUpdate(BaseModel):
    evidence_item_id: str | None = None
    tool_call_id: str | None = None
    method_name: str | None = None
    method_summary: str | None = None
    assumptions: str | None = None
    limitations: str | None = None
    source_artifact_refs: list[str] | None = Field(default=None, min_length=1)
    transformation_notes: str | None = None
    confidence: float | None = Field(default=None, ge=0, le=1)
    tool_call_lineage: list[str] | None = Field(default=None, min_length=1)
    validation_status: ValidationStatus | None = None


class MethodCardRead(TimestampedRead, MethodCardCreate):
    pass


class DatasetCardCreate(BaseModel):
    project_id: str
    tool_call_id: str | None = None
    evidence_item_id: str | None = None
    dataset_name: str
    dataset_summary: str
    source_identity: str
    source_type: SourceType = SourceType.DATASET
    retrieval_time: AwareDatetime
    publication_time: AwareDatetime | None = None
    url: str | None = None
    doi: str | None = None
    locator: str | None = None
    source_artifact_refs: list[str] = Field(min_length=1)
    transformation_notes: str
    confidence: float = Field(ge=0, le=1)
    tool_call_lineage: list[str] = Field(min_length=1)
    validation_status: ValidationStatus = ValidationStatus.PENDING


class DatasetCardUpdate(BaseModel):
    evidence_item_id: str | None = None
    tool_call_id: str | None = None
    dataset_name: str | None = None
    dataset_summary: str | None = None
    source_identity: str | None = None
    source_type: SourceType | None = None
    retrieval_time: AwareDatetime | None = None
    publication_time: AwareDatetime | None = None
    url: str | None = None
    doi: str | None = None
    locator: str | None = None
    source_artifact_refs: list[str] | None = Field(default=None, min_length=1)
    transformation_notes: str | None = None
    confidence: float | None = Field(default=None, ge=0, le=1)
    tool_call_lineage: list[str] | None = Field(default=None, min_length=1)
    validation_status: ValidationStatus | None = None


class DatasetCardRead(TimestampedRead, DatasetCardCreate):
    pass


class ReproPackExportCreate(BaseModel):
    project_id: str
    tool_call_id: str | None = None
    manifest_ref: str
    export_format: str
    source_artifact_refs: list[str] = Field(min_length=1)
    generation_time: AwareDatetime
    transformation_notes: str
    status: ReproPackStatus = ReproPackStatus.REQUESTED
    tool_call_lineage: list[str] = Field(min_length=1)


class ReproPackExportUpdate(BaseModel):
    tool_call_id: str | None = None
    manifest_ref: str | None = None
    export_format: str | None = None
    source_artifact_refs: list[str] | None = Field(default=None, min_length=1)
    generation_time: AwareDatetime | None = None
    transformation_notes: str | None = None
    status: ReproPackStatus | None = None
    tool_call_lineage: list[str] | None = Field(default=None, min_length=1)


class ReproPackExportRead(TimestampedRead, ReproPackExportCreate):
    pass
