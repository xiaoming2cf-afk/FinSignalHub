from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from finsignalhub_api.schemas.domain import EvidenceItemCreate


def _now() -> datetime:
    return datetime.now(timezone.utc)


def test_evidence_item_schema_requires_quote_or_no_quote_reason() -> None:
    with pytest.raises(ValidationError):
        EvidenceItemCreate(
            project_id="project",
            evidence_text="Evidence text",
            source_identity="doi:10.1/example",
            source_type="literature",
            retrieval_time=_now(),
            transformation_notes="normalized citation",
            confidence=0.8,
            tool_call_lineage=["tool-call-1"],
        )


def test_evidence_item_schema_accepts_structured_quote_span() -> None:
    item = EvidenceItemCreate(
        project_id="project",
        evidence_text="Evidence text",
        source_identity="doi:10.1/example",
        source_type="literature",
        retrieval_time=_now(),
        quoted_evidence_span={"page": 3, "start": 10, "end": 42, "text": "Evidence text"},
        transformation_notes="normalized citation",
        confidence=0.8,
        tool_call_lineage=["tool-call-1"],
    )

    assert item.quoted_evidence_span is not None


def test_evidence_item_schema_rejects_out_of_range_confidence() -> None:
    with pytest.raises(ValidationError):
        EvidenceItemCreate(
            project_id="project",
            evidence_text="Evidence text",
            source_identity="doi:10.1/example",
            source_type="literature",
            retrieval_time=_now(),
            no_quote_reason="dataset metadata",
            transformation_notes="normalized citation",
            confidence=1.1,
            tool_call_lineage=["tool-call-1"],
        )


def test_evidence_item_schema_rejects_unstructured_quote_span() -> None:
    with pytest.raises(ValidationError):
        EvidenceItemCreate(
            project_id="project",
            evidence_text="Evidence text",
            source_identity="doi:10.1/example",
            source_type="literature",
            retrieval_time=_now(),
            quoted_evidence_span={"text": "Evidence text"},
            transformation_notes="normalized citation",
            confidence=0.8,
            tool_call_lineage=["tool-call-1"],
        )


def test_evidence_item_schema_rejects_naive_retrieval_time() -> None:
    with pytest.raises(ValidationError):
        EvidenceItemCreate(
            project_id="project",
            evidence_text="Evidence text",
            source_identity="doi:10.1/example",
            source_type="literature",
            retrieval_time=datetime.now(),
            no_quote_reason="dataset metadata",
            transformation_notes="normalized citation",
            confidence=0.8,
            tool_call_lineage=["tool-call-1"],
        )
