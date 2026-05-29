from finsignalhub_api.db.base import Base


APPROVED_TABLES = {
    "research_projects",
    "sources",
    "documents",
    "tool_call_logs",
    "evidence_items",
    "research_claims",
    "claim_evidence_edges",
    "research_deltas",
    "literature_matrix_rows",
    "method_cards",
    "dataset_cards",
    "repro_pack_exports",
}


def test_stage02_metadata_registers_only_approved_entities() -> None:
    assert set(Base.metadata.tables) == APPROVED_TABLES


def test_evidence_item_has_explicit_provenance_fields() -> None:
    table = Base.metadata.tables["evidence_items"]

    for column in [
        "source_identity",
        "source_type",
        "retrieval_time",
        "quoted_evidence_span",
        "no_quote_reason",
        "transformation_notes",
        "confidence",
        "tool_call_lineage",
        "validation_status",
    ]:
        assert column in table.c


def test_tool_call_log_has_safe_arguments_and_error_shape() -> None:
    table = Base.metadata.tables["tool_call_logs"]

    for column in [
        "tool_name",
        "tool_version",
        "schema_version",
        "called_at",
        "argument_hash",
        "safe_arguments",
        "input_artifact_ids",
        "output_artifact_ids",
        "status",
        "deterministic_error",
    ]:
        assert column in table.c


def test_claim_edge_requires_rationale_lineage_and_validation_status() -> None:
    table = Base.metadata.tables["claim_evidence_edges"]

    assert not table.c.rationale.nullable
    assert not table.c.confidence.nullable
    assert not table.c.tool_call_lineage.nullable
    assert not table.c.validation_status.nullable
