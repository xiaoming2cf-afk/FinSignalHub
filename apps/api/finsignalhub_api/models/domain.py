from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import DateTime, Float, ForeignKey, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from finsignalhub_api.db.base import Base
from finsignalhub_api.models.enums import (
    ClaimStatus,
    EdgeRelationType,
    ReproPackStatus,
    SourceType,
    ToolCallStatus,
    ValidationStatus,
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def new_id() -> str:
    return str(uuid4())


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utc_now, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utc_now, onupdate=utc_now, nullable=False
    )


class ResearchProject(TimestampMixin, Base):
    __tablename__ = "research_projects"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    research_question: Mapped[str | None] = mapped_column(Text)
    owner_ref: Mapped[str | None] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(50), default="active", nullable=False)
    scope_note: Mapped[str | None] = mapped_column(Text)

    sources: Mapped[list[Source]] = relationship(back_populates="project", cascade="all, delete-orphan")
    documents: Mapped[list[Document]] = relationship(back_populates="project", cascade="all, delete-orphan")
    tool_calls: Mapped[list[ToolCallLog]] = relationship(back_populates="project", cascade="all, delete-orphan")
    evidence_items: Mapped[list[EvidenceItem]] = relationship(back_populates="project", cascade="all, delete-orphan")
    claims: Mapped[list[ResearchClaim]] = relationship(back_populates="project", cascade="all, delete-orphan")
    deltas: Mapped[list[ResearchDelta]] = relationship(back_populates="project", cascade="all, delete-orphan")
    literature_matrix_rows: Mapped[list[LiteratureMatrixRow]] = relationship(back_populates="project", cascade="all, delete-orphan")
    method_cards: Mapped[list[MethodCard]] = relationship(back_populates="project", cascade="all, delete-orphan")
    dataset_cards: Mapped[list[DatasetCard]] = relationship(back_populates="project", cascade="all, delete-orphan")
    repro_pack_exports: Mapped[list[ReproPackExport]] = relationship(back_populates="project", cascade="all, delete-orphan")


class Source(TimestampMixin, Base):
    __tablename__ = "sources"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    project_id: Mapped[str] = mapped_column(ForeignKey("research_projects.id"), index=True)
    source_identity: Mapped[str] = mapped_column(String(512), nullable=False, index=True)
    source_type: Mapped[str] = mapped_column(
        String(50), default=SourceType.LITERATURE.value, nullable=False
    )
    title: Mapped[str | None] = mapped_column(String(512))
    url: Mapped[str | None] = mapped_column(String(1024))
    doi: Mapped[str | None] = mapped_column(String(255))
    locator: Mapped[str | None] = mapped_column(String(512))
    publication_time: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    retrieval_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utc_now, nullable=False
    )
    bibliographic_metadata: Mapped[dict | None] = mapped_column(JSON)
    validation_status: Mapped[str] = mapped_column(
        String(50), default=ValidationStatus.PENDING.value, nullable=False
    )

    project: Mapped[ResearchProject] = relationship(back_populates="sources")
    documents: Mapped[list[Document]] = relationship(back_populates="source")
    evidence_items: Mapped[list[EvidenceItem]] = relationship(back_populates="source")


class Document(TimestampMixin, Base):
    __tablename__ = "documents"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    project_id: Mapped[str] = mapped_column(ForeignKey("research_projects.id"), index=True)
    source_id: Mapped[str] = mapped_column(ForeignKey("sources.id"), index=True)
    title: Mapped[str] = mapped_column(String(512), nullable=False)
    normalized_document_ref: Mapped[str | None] = mapped_column(String(512))
    source_identity: Mapped[str] = mapped_column(String(512), nullable=False)
    source_type: Mapped[str] = mapped_column(String(50), nullable=False)
    retrieval_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    publication_time: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    url: Mapped[str | None] = mapped_column(String(1024))
    doi: Mapped[str | None] = mapped_column(String(255))
    locator: Mapped[str | None] = mapped_column(String(512))
    transformation_notes: Mapped[str | None] = mapped_column(Text)
    validation_status: Mapped[str] = mapped_column(
        String(50), default=ValidationStatus.PENDING.value, nullable=False
    )

    project: Mapped[ResearchProject] = relationship(back_populates="documents")
    source: Mapped[Source] = relationship(back_populates="documents")
    evidence_items: Mapped[list[EvidenceItem]] = relationship(back_populates="document")


class ToolCallLog(TimestampMixin, Base):
    __tablename__ = "tool_call_logs"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    project_id: Mapped[str] = mapped_column(ForeignKey("research_projects.id"), index=True)
    tool_name: Mapped[str] = mapped_column(String(255), nullable=False)
    tool_version: Mapped[str | None] = mapped_column(String(100))
    schema_version: Mapped[str | None] = mapped_column(String(100))
    called_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utc_now, nullable=False
    )
    argument_hash: Mapped[str] = mapped_column(String(128), nullable=False)
    safe_arguments: Mapped[dict | None] = mapped_column(JSON)
    input_artifact_ids: Mapped[list | None] = mapped_column(JSON)
    output_artifact_ids: Mapped[list | None] = mapped_column(JSON)
    status: Mapped[str] = mapped_column(
        String(50), default=ToolCallStatus.PLANNED.value, nullable=False
    )
    deterministic_error: Mapped[dict | None] = mapped_column(JSON)

    project: Mapped[ResearchProject] = relationship(back_populates="tool_calls")
    evidence_items: Mapped[list[EvidenceItem]] = relationship(back_populates="tool_call")
    claim_evidence_edges: Mapped[list[ClaimEvidenceEdge]] = relationship(back_populates="tool_call")
    claims: Mapped[list[ResearchClaim]] = relationship(back_populates="tool_call")
    deltas: Mapped[list[ResearchDelta]] = relationship(back_populates="tool_call")
    literature_matrix_rows: Mapped[list[LiteratureMatrixRow]] = relationship(back_populates="tool_call")
    method_cards: Mapped[list[MethodCard]] = relationship(back_populates="tool_call")
    dataset_cards: Mapped[list[DatasetCard]] = relationship(back_populates="tool_call")
    repro_pack_exports: Mapped[list[ReproPackExport]] = relationship(back_populates="tool_call")


class EvidenceItem(TimestampMixin, Base):
    __tablename__ = "evidence_items"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    project_id: Mapped[str] = mapped_column(ForeignKey("research_projects.id"), index=True)
    source_id: Mapped[str | None] = mapped_column(ForeignKey("sources.id"), index=True)
    document_id: Mapped[str | None] = mapped_column(ForeignKey("documents.id"), index=True)
    tool_call_id: Mapped[str | None] = mapped_column(ForeignKey("tool_call_logs.id"), index=True)
    evidence_text: Mapped[str] = mapped_column(Text, nullable=False)
    source_identity: Mapped[str] = mapped_column(String(512), nullable=False)
    source_type: Mapped[str] = mapped_column(String(50), nullable=False)
    retrieval_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    publication_time: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    url: Mapped[str | None] = mapped_column(String(1024))
    doi: Mapped[str | None] = mapped_column(String(255))
    locator: Mapped[str | None] = mapped_column(String(512))
    quoted_evidence_span: Mapped[dict | None] = mapped_column(JSON)
    no_quote_reason: Mapped[str | None] = mapped_column(Text)
    transformation_notes: Mapped[str] = mapped_column(Text, nullable=False)
    confidence: Mapped[float] = mapped_column(Float, nullable=False)
    tool_call_lineage: Mapped[list] = mapped_column(JSON, nullable=False)
    validation_status: Mapped[str] = mapped_column(
        String(50), default=ValidationStatus.PENDING.value, nullable=False
    )

    project: Mapped[ResearchProject] = relationship(back_populates="evidence_items")
    source: Mapped[Source | None] = relationship(back_populates="evidence_items")
    document: Mapped[Document | None] = relationship(back_populates="evidence_items")
    tool_call: Mapped[ToolCallLog | None] = relationship(back_populates="evidence_items")
    claim_edges: Mapped[list[ClaimEvidenceEdge]] = relationship(back_populates="evidence_item")


class ResearchClaim(TimestampMixin, Base):
    __tablename__ = "research_claims"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    project_id: Mapped[str] = mapped_column(ForeignKey("research_projects.id"), index=True)
    originating_evidence_item_id: Mapped[str | None] = mapped_column(
        ForeignKey("evidence_items.id"), index=True
    )
    tool_call_id: Mapped[str | None] = mapped_column(ForeignKey("tool_call_logs.id"), index=True)
    claim_text: Mapped[str] = mapped_column(Text, nullable=False)
    derivation_notes: Mapped[str | None] = mapped_column(Text)
    confidence: Mapped[float] = mapped_column(Float, nullable=False)
    status: Mapped[str] = mapped_column(
        String(50), default=ClaimStatus.PROPOSED.value, nullable=False
    )
    tool_call_lineage: Mapped[list | None] = mapped_column(JSON)
    validation_status: Mapped[str] = mapped_column(
        String(50), default=ValidationStatus.PENDING.value, nullable=False
    )

    project: Mapped[ResearchProject] = relationship(back_populates="claims")
    originating_evidence_item: Mapped[EvidenceItem | None] = relationship()
    tool_call: Mapped[ToolCallLog | None] = relationship(back_populates="claims")
    evidence_edges: Mapped[list[ClaimEvidenceEdge]] = relationship(back_populates="claim")


class ClaimEvidenceEdge(TimestampMixin, Base):
    __tablename__ = "claim_evidence_edges"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    claim_id: Mapped[str] = mapped_column(ForeignKey("research_claims.id"), index=True)
    evidence_item_id: Mapped[str] = mapped_column(ForeignKey("evidence_items.id"), index=True)
    tool_call_id: Mapped[str | None] = mapped_column(ForeignKey("tool_call_logs.id"), index=True)
    relation_type: Mapped[str] = mapped_column(
        String(50), default=EdgeRelationType.SUPPORTS.value, nullable=False
    )
    rationale: Mapped[str] = mapped_column(Text, nullable=False)
    confidence: Mapped[float] = mapped_column(Float, nullable=False)
    tool_call_lineage: Mapped[list] = mapped_column(JSON, nullable=False)
    validation_status: Mapped[str] = mapped_column(
        String(50), default=ValidationStatus.PENDING.value, nullable=False
    )

    claim: Mapped[ResearchClaim] = relationship(back_populates="evidence_edges")
    evidence_item: Mapped[EvidenceItem] = relationship(back_populates="claim_edges")
    tool_call: Mapped[ToolCallLog | None] = relationship(back_populates="claim_evidence_edges")


class ResearchDelta(TimestampMixin, Base):
    __tablename__ = "research_deltas"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    project_id: Mapped[str] = mapped_column(ForeignKey("research_projects.id"), index=True)
    tool_call_id: Mapped[str | None] = mapped_column(ForeignKey("tool_call_logs.id"), index=True)
    summary: Mapped[str] = mapped_column(Text, nullable=False)
    changed_claim_ids: Mapped[list | None] = mapped_column(JSON)
    source_artifact_refs: Mapped[list | None] = mapped_column(JSON)
    generation_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utc_now, nullable=False
    )
    transformation_notes: Mapped[str] = mapped_column(Text, nullable=False)
    confidence: Mapped[float] = mapped_column(Float, nullable=False)
    tool_call_lineage: Mapped[list] = mapped_column(JSON, nullable=False)
    validation_status: Mapped[str] = mapped_column(
        String(50), default=ValidationStatus.PENDING.value, nullable=False
    )

    project: Mapped[ResearchProject] = relationship(back_populates="deltas")
    tool_call: Mapped[ToolCallLog | None] = relationship(back_populates="deltas")


class LiteratureMatrixRow(TimestampMixin, Base):
    __tablename__ = "literature_matrix_rows"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    project_id: Mapped[str] = mapped_column(ForeignKey("research_projects.id"), index=True)
    tool_call_id: Mapped[str | None] = mapped_column(ForeignKey("tool_call_logs.id"), index=True)
    document_id: Mapped[str | None] = mapped_column(ForeignKey("documents.id"), index=True)
    claim_id: Mapped[str | None] = mapped_column(ForeignKey("research_claims.id"), index=True)
    research_question: Mapped[str] = mapped_column(Text, nullable=False)
    method_summary: Mapped[str | None] = mapped_column(Text)
    dataset_summary: Mapped[str | None] = mapped_column(Text)
    evidence_summary: Mapped[str] = mapped_column(Text, nullable=False)
    source_artifact_refs: Mapped[list | None] = mapped_column(JSON)
    transformation_notes: Mapped[str] = mapped_column(Text, nullable=False)
    confidence: Mapped[float] = mapped_column(Float, nullable=False)
    tool_call_lineage: Mapped[list] = mapped_column(JSON, nullable=False)
    validation_status: Mapped[str] = mapped_column(
        String(50), default=ValidationStatus.PENDING.value, nullable=False
    )

    project: Mapped[ResearchProject] = relationship(back_populates="literature_matrix_rows")
    tool_call: Mapped[ToolCallLog | None] = relationship(back_populates="literature_matrix_rows")


class MethodCard(TimestampMixin, Base):
    __tablename__ = "method_cards"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    project_id: Mapped[str] = mapped_column(ForeignKey("research_projects.id"), index=True)
    tool_call_id: Mapped[str | None] = mapped_column(ForeignKey("tool_call_logs.id"), index=True)
    evidence_item_id: Mapped[str | None] = mapped_column(ForeignKey("evidence_items.id"), index=True)
    method_name: Mapped[str] = mapped_column(String(255), nullable=False)
    method_summary: Mapped[str] = mapped_column(Text, nullable=False)
    assumptions: Mapped[str | None] = mapped_column(Text)
    limitations: Mapped[str | None] = mapped_column(Text)
    source_artifact_refs: Mapped[list | None] = mapped_column(JSON)
    transformation_notes: Mapped[str] = mapped_column(Text, nullable=False)
    confidence: Mapped[float] = mapped_column(Float, nullable=False)
    tool_call_lineage: Mapped[list] = mapped_column(JSON, nullable=False)
    validation_status: Mapped[str] = mapped_column(
        String(50), default=ValidationStatus.PENDING.value, nullable=False
    )

    project: Mapped[ResearchProject] = relationship(back_populates="method_cards")
    tool_call: Mapped[ToolCallLog | None] = relationship(back_populates="method_cards")


class DatasetCard(TimestampMixin, Base):
    __tablename__ = "dataset_cards"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    project_id: Mapped[str] = mapped_column(ForeignKey("research_projects.id"), index=True)
    tool_call_id: Mapped[str | None] = mapped_column(ForeignKey("tool_call_logs.id"), index=True)
    evidence_item_id: Mapped[str | None] = mapped_column(ForeignKey("evidence_items.id"), index=True)
    dataset_name: Mapped[str] = mapped_column(String(255), nullable=False)
    dataset_summary: Mapped[str] = mapped_column(Text, nullable=False)
    source_identity: Mapped[str] = mapped_column(String(512), nullable=False)
    source_type: Mapped[str] = mapped_column(
        String(50), default=SourceType.DATASET.value, nullable=False
    )
    retrieval_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    publication_time: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    url: Mapped[str | None] = mapped_column(String(1024))
    doi: Mapped[str | None] = mapped_column(String(255))
    locator: Mapped[str | None] = mapped_column(String(512))
    source_artifact_refs: Mapped[list | None] = mapped_column(JSON)
    transformation_notes: Mapped[str] = mapped_column(Text, nullable=False)
    confidence: Mapped[float] = mapped_column(Float, nullable=False)
    tool_call_lineage: Mapped[list] = mapped_column(JSON, nullable=False)
    validation_status: Mapped[str] = mapped_column(
        String(50), default=ValidationStatus.PENDING.value, nullable=False
    )

    project: Mapped[ResearchProject] = relationship(back_populates="dataset_cards")
    tool_call: Mapped[ToolCallLog | None] = relationship(back_populates="dataset_cards")


class ReproPackExport(TimestampMixin, Base):
    __tablename__ = "repro_pack_exports"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    project_id: Mapped[str] = mapped_column(ForeignKey("research_projects.id"), index=True)
    tool_call_id: Mapped[str | None] = mapped_column(ForeignKey("tool_call_logs.id"), index=True)
    manifest_ref: Mapped[str] = mapped_column(String(512), nullable=False)
    export_format: Mapped[str] = mapped_column(String(100), nullable=False)
    source_artifact_refs: Mapped[list | None] = mapped_column(JSON)
    generation_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utc_now, nullable=False
    )
    transformation_notes: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[str] = mapped_column(
        String(50), default=ReproPackStatus.REQUESTED.value, nullable=False
    )
    tool_call_lineage: Mapped[list] = mapped_column(JSON, nullable=False)

    project: Mapped[ResearchProject] = relationship(back_populates="repro_pack_exports")
    tool_call: Mapped[ToolCallLog | None] = relationship(back_populates="repro_pack_exports")
