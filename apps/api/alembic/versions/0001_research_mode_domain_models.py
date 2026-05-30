"""Create Stage 02 Research Mode domain model tables.

Revision ID: 0001_research_mode_domain_models
Revises:
Create Date: 2026-05-29
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa


revision = "0001_research_mode_domain_models"
down_revision = None
branch_labels = None
depends_on = None


def _timestamps() -> list[sa.Column]:
    return [
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    ]


def upgrade() -> None:
    op.create_table(
        "research_projects",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("research_question", sa.Text(), nullable=True),
        sa.Column("owner_ref", sa.String(length=255), nullable=True),
        sa.Column("status", sa.String(length=50), nullable=False),
        sa.Column("scope_note", sa.Text(), nullable=True),
        *_timestamps(),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_research_projects")),
    )

    op.create_table(
        "sources",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("project_id", sa.String(length=36), nullable=False),
        sa.Column("source_identity", sa.String(length=512), nullable=False),
        sa.Column("source_type", sa.String(length=50), nullable=False),
        sa.Column("title", sa.String(length=512), nullable=True),
        sa.Column("url", sa.String(length=1024), nullable=True),
        sa.Column("doi", sa.String(length=255), nullable=True),
        sa.Column("locator", sa.String(length=512), nullable=True),
        sa.Column("publication_time", sa.DateTime(timezone=True), nullable=True),
        sa.Column("retrieval_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("bibliographic_metadata", sa.JSON(), nullable=True),
        sa.Column("validation_status", sa.String(length=50), nullable=False),
        *_timestamps(),
        sa.ForeignKeyConstraint(["project_id"], ["research_projects.id"], name=op.f("fk_sources_project_id_research_projects")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_sources")),
    )
    op.create_index(op.f("ix_sources_project_id"), "sources", ["project_id"], unique=False)
    op.create_index(op.f("ix_sources_source_identity"), "sources", ["source_identity"], unique=False)

    op.create_table(
        "documents",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("project_id", sa.String(length=36), nullable=False),
        sa.Column("source_id", sa.String(length=36), nullable=False),
        sa.Column("title", sa.String(length=512), nullable=False),
        sa.Column("normalized_document_ref", sa.String(length=512), nullable=True),
        sa.Column("source_identity", sa.String(length=512), nullable=False),
        sa.Column("source_type", sa.String(length=50), nullable=False),
        sa.Column("retrieval_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("publication_time", sa.DateTime(timezone=True), nullable=True),
        sa.Column("url", sa.String(length=1024), nullable=True),
        sa.Column("doi", sa.String(length=255), nullable=True),
        sa.Column("locator", sa.String(length=512), nullable=True),
        sa.Column("transformation_notes", sa.Text(), nullable=True),
        sa.Column("validation_status", sa.String(length=50), nullable=False),
        *_timestamps(),
        sa.ForeignKeyConstraint(["project_id"], ["research_projects.id"], name=op.f("fk_documents_project_id_research_projects")),
        sa.ForeignKeyConstraint(["source_id"], ["sources.id"], name=op.f("fk_documents_source_id_sources")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_documents")),
    )
    op.create_index(op.f("ix_documents_project_id"), "documents", ["project_id"], unique=False)
    op.create_index(op.f("ix_documents_source_id"), "documents", ["source_id"], unique=False)

    op.create_table(
        "tool_call_logs",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("project_id", sa.String(length=36), nullable=False),
        sa.Column("tool_name", sa.String(length=255), nullable=False),
        sa.Column("tool_version", sa.String(length=100), nullable=True),
        sa.Column("schema_version", sa.String(length=100), nullable=True),
        sa.Column("called_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("argument_hash", sa.String(length=128), nullable=False),
        sa.Column("safe_arguments", sa.JSON(), nullable=True),
        sa.Column("input_artifact_ids", sa.JSON(), nullable=True),
        sa.Column("output_artifact_ids", sa.JSON(), nullable=True),
        sa.Column("status", sa.String(length=50), nullable=False),
        sa.Column("deterministic_error", sa.JSON(), nullable=True),
        *_timestamps(),
        sa.ForeignKeyConstraint(["project_id"], ["research_projects.id"], name=op.f("fk_tool_call_logs_project_id_research_projects")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_tool_call_logs")),
    )
    op.create_index(op.f("ix_tool_call_logs_project_id"), "tool_call_logs", ["project_id"], unique=False)

    op.create_table(
        "evidence_items",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("project_id", sa.String(length=36), nullable=False),
        sa.Column("source_id", sa.String(length=36), nullable=True),
        sa.Column("document_id", sa.String(length=36), nullable=True),
        sa.Column("tool_call_id", sa.String(length=36), nullable=True),
        sa.Column("evidence_text", sa.Text(), nullable=False),
        sa.Column("source_identity", sa.String(length=512), nullable=False),
        sa.Column("source_type", sa.String(length=50), nullable=False),
        sa.Column("retrieval_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("publication_time", sa.DateTime(timezone=True), nullable=True),
        sa.Column("url", sa.String(length=1024), nullable=True),
        sa.Column("doi", sa.String(length=255), nullable=True),
        sa.Column("locator", sa.String(length=512), nullable=True),
        sa.Column("quoted_evidence_span", sa.JSON(), nullable=True),
        sa.Column("no_quote_reason", sa.Text(), nullable=True),
        sa.Column("transformation_notes", sa.Text(), nullable=False),
        sa.Column("confidence", sa.Float(), nullable=False),
        sa.Column("tool_call_lineage", sa.JSON(), nullable=False),
        sa.Column("validation_status", sa.String(length=50), nullable=False),
        *_timestamps(),
        sa.ForeignKeyConstraint(["document_id"], ["documents.id"], name=op.f("fk_evidence_items_document_id_documents")),
        sa.ForeignKeyConstraint(["project_id"], ["research_projects.id"], name=op.f("fk_evidence_items_project_id_research_projects")),
        sa.ForeignKeyConstraint(["source_id"], ["sources.id"], name=op.f("fk_evidence_items_source_id_sources")),
        sa.ForeignKeyConstraint(["tool_call_id"], ["tool_call_logs.id"], name=op.f("fk_evidence_items_tool_call_id_tool_call_logs")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_evidence_items")),
    )
    op.create_index(op.f("ix_evidence_items_document_id"), "evidence_items", ["document_id"], unique=False)
    op.create_index(op.f("ix_evidence_items_project_id"), "evidence_items", ["project_id"], unique=False)
    op.create_index(op.f("ix_evidence_items_source_id"), "evidence_items", ["source_id"], unique=False)
    op.create_index(op.f("ix_evidence_items_tool_call_id"), "evidence_items", ["tool_call_id"], unique=False)

    op.create_table(
        "research_claims",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("project_id", sa.String(length=36), nullable=False),
        sa.Column("originating_evidence_item_id", sa.String(length=36), nullable=True),
        sa.Column("tool_call_id", sa.String(length=36), nullable=True),
        sa.Column("claim_text", sa.Text(), nullable=False),
        sa.Column("derivation_notes", sa.Text(), nullable=True),
        sa.Column("confidence", sa.Float(), nullable=False),
        sa.Column("status", sa.String(length=50), nullable=False),
        sa.Column("tool_call_lineage", sa.JSON(), nullable=True),
        sa.Column("validation_status", sa.String(length=50), nullable=False),
        *_timestamps(),
        sa.ForeignKeyConstraint(["originating_evidence_item_id"], ["evidence_items.id"], name=op.f("fk_research_claims_originating_evidence_item_id_evidence_items")),
        sa.ForeignKeyConstraint(["project_id"], ["research_projects.id"], name=op.f("fk_research_claims_project_id_research_projects")),
        sa.ForeignKeyConstraint(["tool_call_id"], ["tool_call_logs.id"], name=op.f("fk_research_claims_tool_call_id_tool_call_logs")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_research_claims")),
    )
    op.create_index(op.f("ix_research_claims_originating_evidence_item_id"), "research_claims", ["originating_evidence_item_id"], unique=False)
    op.create_index(op.f("ix_research_claims_project_id"), "research_claims", ["project_id"], unique=False)
    op.create_index(op.f("ix_research_claims_tool_call_id"), "research_claims", ["tool_call_id"], unique=False)

    op.create_table(
        "claim_evidence_edges",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("claim_id", sa.String(length=36), nullable=False),
        sa.Column("evidence_item_id", sa.String(length=36), nullable=False),
        sa.Column("tool_call_id", sa.String(length=36), nullable=True),
        sa.Column("relation_type", sa.String(length=50), nullable=False),
        sa.Column("rationale", sa.Text(), nullable=False),
        sa.Column("confidence", sa.Float(), nullable=False),
        sa.Column("tool_call_lineage", sa.JSON(), nullable=False),
        sa.Column("validation_status", sa.String(length=50), nullable=False),
        *_timestamps(),
        sa.ForeignKeyConstraint(["claim_id"], ["research_claims.id"], name=op.f("fk_claim_evidence_edges_claim_id_research_claims")),
        sa.ForeignKeyConstraint(["evidence_item_id"], ["evidence_items.id"], name=op.f("fk_claim_evidence_edges_evidence_item_id_evidence_items")),
        sa.ForeignKeyConstraint(["tool_call_id"], ["tool_call_logs.id"], name=op.f("fk_claim_evidence_edges_tool_call_id_tool_call_logs")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_claim_evidence_edges")),
    )
    op.create_index(op.f("ix_claim_evidence_edges_claim_id"), "claim_evidence_edges", ["claim_id"], unique=False)
    op.create_index(op.f("ix_claim_evidence_edges_evidence_item_id"), "claim_evidence_edges", ["evidence_item_id"], unique=False)
    op.create_index(op.f("ix_claim_evidence_edges_tool_call_id"), "claim_evidence_edges", ["tool_call_id"], unique=False)

    for table_name, extra_columns in [
        (
            "research_deltas",
            [
                sa.Column("tool_call_id", sa.String(length=36), nullable=True),
                sa.Column("summary", sa.Text(), nullable=False),
                sa.Column("changed_claim_ids", sa.JSON(), nullable=True),
                sa.Column("source_artifact_refs", sa.JSON(), nullable=True),
                sa.Column("generation_time", sa.DateTime(timezone=True), nullable=False),
            ],
        ),
        (
            "literature_matrix_rows",
            [
                sa.Column("tool_call_id", sa.String(length=36), nullable=True),
                sa.Column("document_id", sa.String(length=36), nullable=True),
                sa.Column("claim_id", sa.String(length=36), nullable=True),
                sa.Column("research_question", sa.Text(), nullable=False),
                sa.Column("method_summary", sa.Text(), nullable=True),
                sa.Column("dataset_summary", sa.Text(), nullable=True),
                sa.Column("evidence_summary", sa.Text(), nullable=False),
                sa.Column("source_artifact_refs", sa.JSON(), nullable=True),
            ],
        ),
        (
            "method_cards",
            [
                sa.Column("tool_call_id", sa.String(length=36), nullable=True),
                sa.Column("evidence_item_id", sa.String(length=36), nullable=True),
                sa.Column("method_name", sa.String(length=255), nullable=False),
                sa.Column("method_summary", sa.Text(), nullable=False),
                sa.Column("assumptions", sa.Text(), nullable=True),
                sa.Column("limitations", sa.Text(), nullable=True),
                sa.Column("source_artifact_refs", sa.JSON(), nullable=True),
            ],
        ),
        (
            "dataset_cards",
            [
                sa.Column("tool_call_id", sa.String(length=36), nullable=True),
                sa.Column("evidence_item_id", sa.String(length=36), nullable=True),
                sa.Column("dataset_name", sa.String(length=255), nullable=False),
                sa.Column("dataset_summary", sa.Text(), nullable=False),
                sa.Column("source_identity", sa.String(length=512), nullable=False),
                sa.Column("source_type", sa.String(length=50), nullable=False),
                sa.Column("retrieval_time", sa.DateTime(timezone=True), nullable=False),
                sa.Column("publication_time", sa.DateTime(timezone=True), nullable=True),
                sa.Column("url", sa.String(length=1024), nullable=True),
                sa.Column("doi", sa.String(length=255), nullable=True),
                sa.Column("locator", sa.String(length=512), nullable=True),
                sa.Column("source_artifact_refs", sa.JSON(), nullable=True),
            ],
        ),
    ]:
        extra_constraints = []
        if table_name == "literature_matrix_rows":
            extra_constraints.extend(
                [
                    sa.ForeignKeyConstraint(["document_id"], ["documents.id"], name=op.f("fk_literature_matrix_rows_document_id_documents")),
                    sa.ForeignKeyConstraint(["claim_id"], ["research_claims.id"], name=op.f("fk_literature_matrix_rows_claim_id_research_claims")),
                ]
            )
        if table_name == "method_cards":
            extra_constraints.append(
                sa.ForeignKeyConstraint(["evidence_item_id"], ["evidence_items.id"], name=op.f("fk_method_cards_evidence_item_id_evidence_items"))
            )
        if table_name == "dataset_cards":
            extra_constraints.append(
                sa.ForeignKeyConstraint(["evidence_item_id"], ["evidence_items.id"], name=op.f("fk_dataset_cards_evidence_item_id_evidence_items"))
            )
        op.create_table(
            table_name,
            sa.Column("id", sa.String(length=36), nullable=False),
            sa.Column("project_id", sa.String(length=36), nullable=False),
            *extra_columns,
            sa.Column("transformation_notes", sa.Text(), nullable=False),
            sa.Column("confidence", sa.Float(), nullable=False),
            sa.Column("tool_call_lineage", sa.JSON(), nullable=False),
            sa.Column("validation_status", sa.String(length=50), nullable=False),
            *_timestamps(),
            sa.ForeignKeyConstraint(["project_id"], ["research_projects.id"], name=op.f(f"fk_{table_name}_project_id_research_projects")),
            sa.ForeignKeyConstraint(["tool_call_id"], ["tool_call_logs.id"], name=op.f(f"fk_{table_name}_tool_call_id_tool_call_logs")),
            *extra_constraints,
            sa.PrimaryKeyConstraint("id", name=op.f(f"pk_{table_name}")),
        )
        op.create_index(op.f(f"ix_{table_name}_project_id"), table_name, ["project_id"], unique=False)
        op.create_index(op.f(f"ix_{table_name}_tool_call_id"), table_name, ["tool_call_id"], unique=False)

    op.create_index(op.f("ix_literature_matrix_rows_document_id"), "literature_matrix_rows", ["document_id"], unique=False)
    op.create_index(op.f("ix_literature_matrix_rows_claim_id"), "literature_matrix_rows", ["claim_id"], unique=False)
    op.create_index(op.f("ix_method_cards_evidence_item_id"), "method_cards", ["evidence_item_id"], unique=False)
    op.create_index(op.f("ix_dataset_cards_evidence_item_id"), "dataset_cards", ["evidence_item_id"], unique=False)

    op.create_table(
        "repro_pack_exports",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("project_id", sa.String(length=36), nullable=False),
        sa.Column("tool_call_id", sa.String(length=36), nullable=True),
        sa.Column("manifest_ref", sa.String(length=512), nullable=False),
        sa.Column("export_format", sa.String(length=100), nullable=False),
        sa.Column("source_artifact_refs", sa.JSON(), nullable=True),
        sa.Column("generation_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("transformation_notes", sa.Text(), nullable=False),
        sa.Column("status", sa.String(length=50), nullable=False),
        sa.Column("tool_call_lineage", sa.JSON(), nullable=False),
        *_timestamps(),
        sa.ForeignKeyConstraint(["project_id"], ["research_projects.id"], name=op.f("fk_repro_pack_exports_project_id_research_projects")),
        sa.ForeignKeyConstraint(["tool_call_id"], ["tool_call_logs.id"], name=op.f("fk_repro_pack_exports_tool_call_id_tool_call_logs")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_repro_pack_exports")),
    )
    op.create_index(op.f("ix_repro_pack_exports_project_id"), "repro_pack_exports", ["project_id"], unique=False)
    op.create_index(op.f("ix_repro_pack_exports_tool_call_id"), "repro_pack_exports", ["tool_call_id"], unique=False)


def downgrade() -> None:
    for table_name in [
        "repro_pack_exports",
        "dataset_cards",
        "method_cards",
        "literature_matrix_rows",
        "research_deltas",
        "claim_evidence_edges",
        "research_claims",
        "evidence_items",
        "tool_call_logs",
        "documents",
        "sources",
        "research_projects",
    ]:
        op.drop_table(table_name)
