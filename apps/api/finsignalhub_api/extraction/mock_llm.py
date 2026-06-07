from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256

from finsignalhub_api.extraction.relations import ExtractionRelationType
from finsignalhub_api.extraction.schemas import EvidenceCandidate, QuoteSpanCandidate
from finsignalhub_api.schemas.domain import DocumentCreate


TOOL_VERSION = "stage04.mock"


def _candidate_digest(*parts: str) -> str:
    payload = "|".join(parts).encode()
    return sha256(payload).hexdigest()[:16]


def _first_sentence(text: str) -> str:
    clean_text = text.strip()
    if not clean_text:
        return ""
    for index, character in enumerate(clean_text):
        if character in ".!?":
            return clean_text[: index + 1]
    return clean_text[:160]


@dataclass(frozen=True)
class DeterministicMockExtractor:
    tool_version: str = TOOL_VERSION

    def extract(
        self,
        *,
        document: DocumentCreate,
        document_text: str | None,
        tool_call_lineage: list[str],
        tool_call_id: str | None = None,
    ) -> list[EvidenceCandidate]:
        if document_text and document_text.strip():
            evidence_text = _first_sentence(document_text)
            start = document_text.index(evidence_text)
            end = start + len(evidence_text)
            quote_span = QuoteSpanCandidate(
                text=evidence_text,
                start=start,
                end=end,
                locator=document.locator,
            )
            return [
                EvidenceCandidate.from_document(
                    document=document,
                    candidate_id=f"evcand-{_candidate_digest(document.source_identity, evidence_text)}",
                    evidence_text=evidence_text,
                    relation_type=ExtractionRelationType.OBSERVATION,
                    confidence=0.72,
                    tool_call_lineage=tool_call_lineage,
                    quoted_evidence_span=quote_span,
                    tool_call_id=tool_call_id,
                    transformation_notes=(
                        "Stage 04 mock-only candidate generated from normalized document text."
                    ),
                )
            ]

        evidence_text = document.title
        return [
            EvidenceCandidate.from_document(
                document=document,
                candidate_id=f"evcand-{_candidate_digest(document.source_identity, evidence_text)}",
                evidence_text=evidence_text,
                relation_type=ExtractionRelationType.BACKGROUND,
                confidence=0.38,
                tool_call_lineage=tool_call_lineage,
                no_quote_reason=(
                    "Normalized input is metadata-only; no exact source text was available "
                    "in the Stage 04 fixture."
                ),
                tool_call_id=tool_call_id,
                transformation_notes=(
                    "Stage 04 mock-only candidate generated from normalized document metadata."
                ),
            )
        ]

