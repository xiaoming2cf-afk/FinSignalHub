from __future__ import annotations

from enum import StrEnum


class ExtractionRelationType(StrEnum):
    OBSERVATION = "observation"
    METHOD = "method"
    DATASET = "dataset"
    LIMITATION = "limitation"
    BACKGROUND = "background"
    SUPPORTS_CLAIM_CANDIDATE = "supports_claim_candidate"
    CONTRADICTS_CLAIM_CANDIDATE = "contradicts_claim_candidate"
    UNCERTAIN_RELATION = "uncertain_relation"

