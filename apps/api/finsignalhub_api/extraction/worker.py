from __future__ import annotations

from finsignalhub_api.extraction.mock_llm import DeterministicMockExtractor
from finsignalhub_api.extraction.provenance import (
    validate_candidate_provenance,
    validate_document_provenance,
)
from finsignalhub_api.extraction.quote_span import validate_quote_span
from finsignalhub_api.extraction.schemas import ExtractionRequest, ExtractionResult


def run_mock_extraction(request: ExtractionRequest) -> ExtractionResult:
    validate_document_provenance(request.document)
    document_ref = request.document.normalized_document_ref or f"document:{request.document.source_identity}"
    extractor = DeterministicMockExtractor()
    candidates = extractor.extract(
        document=request.document,
        document_text=request.document_text,
        tool_call_lineage=request.tool_call_lineage,
        tool_call_id=request.tool_call_id,
    )

    for candidate in candidates:
        if candidate.quoted_evidence_span is not None:
            if request.document_text is None:
                raise ValueError("document_text is required when a quoted span is present")
            validate_quote_span(request.document_text, candidate.quoted_evidence_span)
        validate_candidate_provenance(candidate, request.document)
        candidate.validate_as_evidence_item_payload()

    return ExtractionResult(
        project_id=request.document.project_id,
        document_ref=document_ref,
        candidates=candidates,
    )

