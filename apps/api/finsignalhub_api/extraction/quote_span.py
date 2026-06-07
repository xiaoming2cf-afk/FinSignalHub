from __future__ import annotations

from finsignalhub_api.extraction.schemas import (
    EvidenceExtractionValidationError,
    QuoteSpanCandidate,
)


def validate_quote_span(document_text: str, quote_span: QuoteSpanCandidate) -> None:
    if quote_span.start is None and quote_span.end is None:
        if quote_span.text not in document_text:
            raise EvidenceExtractionValidationError(
                "quote_span_mismatch",
                "quoted_evidence_span.text",
                "quote span text is not present in document text",
            )
        return

    if quote_span.start is None or quote_span.end is None:
        raise EvidenceExtractionValidationError(
            "quote_span_shape",
            "quoted_evidence_span",
            "quote span start and end must be provided together",
        )

    if quote_span.end > len(document_text):
        raise EvidenceExtractionValidationError(
            "quote_span_bounds",
            "quoted_evidence_span",
            "quote span end exceeds document text length",
        )

    observed = document_text[quote_span.start : quote_span.end]
    if observed != quote_span.text:
        raise EvidenceExtractionValidationError(
            "quote_span_mismatch",
            "quoted_evidence_span.text",
            "quote span text does not match document text",
        )
