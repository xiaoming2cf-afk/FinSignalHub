from __future__ import annotations

from enum import StrEnum


class SourceType(StrEnum):
    LITERATURE = "literature"
    PREPRINT = "preprint"
    DATASET = "dataset"
    METHOD_NOTE = "method_note"
    USER_UPLOAD_METADATA = "user_upload_metadata"
    TOOL_OUTPUT = "tool_output"


class ValidationStatus(StrEnum):
    DRAFT = "draft"
    PENDING = "pending"
    VALIDATED = "validated"
    REJECTED = "rejected"


class ClaimStatus(StrEnum):
    PROPOSED = "proposed"
    SUPPORTED = "supported"
    CONTESTED = "contested"
    RETIRED = "retired"


class EdgeRelationType(StrEnum):
    SUPPORTS = "supports"
    CONTRADICTS = "contradicts"
    QUALIFIES = "qualifies"
    BACKGROUND = "background"


class ToolCallStatus(StrEnum):
    PLANNED = "planned"
    SUCCEEDED = "succeeded"
    FAILED = "failed"


class ReproPackStatus(StrEnum):
    REQUESTED = "requested"
    READY = "ready"
    FAILED = "failed"
