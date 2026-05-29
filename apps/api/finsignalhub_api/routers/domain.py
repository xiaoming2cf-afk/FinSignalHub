from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from finsignalhub_api.db.session import get_db_session
from finsignalhub_api.models.domain import (
    ClaimEvidenceEdge,
    DatasetCard,
    Document,
    EvidenceItem,
    LiteratureMatrixRow,
    MethodCard,
    ReproPackExport,
    ResearchClaim,
    ResearchDelta,
    ResearchProject,
    Source,
    ToolCallLog,
)
from finsignalhub_api.schemas import domain as schemas
from finsignalhub_api.services.crud import CrudService, NotFoundError


router = APIRouter(prefix="/research-mode", tags=["research-mode-domain-models"])


def _not_found(error: NotFoundError) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={
            "error": "not_found",
            "model": error.model_name,
            "id": error.item_id,
        },
    )


def _unprocessable(error: str, message: str, **context: Any) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail={"error": error, "message": message, **context},
    )


def _bad_request(error: str, message: str, **context: Any) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={"error": error, "message": message, **context},
    )


def _require_related_project(
    session: Session,
    *,
    model: type,
    item_id: str,
    expected_project_id: str,
    field_name: str,
    error: str,
) -> Any:
    related = session.get(model, item_id)
    if related is None:
        raise _not_found(NotFoundError(model.__name__, item_id))
    if related.project_id != expected_project_id:
        raise _bad_request(
            error,
            f"{field_name} must belong to the same project.",
            field_name=field_name,
            item_id=item_id,
            item_project_id=related.project_id,
            expected_project_id=expected_project_id,
        )
    return related


def _require_related_list_project(
    session: Session,
    *,
    model: type,
    item_ids: list[str],
    expected_project_id: str,
    field_name: str,
    error: str,
) -> None:
    for item_id in item_ids:
        _require_related_project(
            session,
            model=model,
            item_id=item_id,
            expected_project_id=expected_project_id,
            field_name=field_name,
            error=error,
        )


def _require_project_exists(session: Session, project_id: str) -> None:
    if session.get(ResearchProject, project_id) is None:
        raise _not_found(NotFoundError("ResearchProject", project_id))


def _require_payload_project_exists(session: Session, data: dict[str, Any]) -> None:
    _require_project_exists(session, data["project_id"])


def _require_tool_call_lineage_project(
    session: Session,
    project_id: str,
    data: dict[str, Any],
    *,
    error: str,
) -> None:
    if "tool_call_lineage" not in data:
        return
    lineage = data["tool_call_lineage"]
    if lineage is None:
        raise _bad_request(
            error,
            "tool_call_lineage must not be null.",
            field_name="tool_call_lineage",
            expected_project_id=project_id,
        )
    _require_related_list_project(
        session,
        model=ToolCallLog,
        item_ids=lineage,
        expected_project_id=project_id,
        field_name="tool_call_lineage",
        error=error,
    )


def _claim_evidence_edge_project_id(
    session: Session,
    artifact_ref: str,
    *,
    error: str,
) -> str | None:
    edge = session.get(ClaimEvidenceEdge, artifact_ref)
    if edge is None:
        return None
    claim = session.get(ResearchClaim, edge.claim_id)
    if claim is None:
        raise _not_found(NotFoundError("ResearchClaim", edge.claim_id))
    evidence_item = session.get(EvidenceItem, edge.evidence_item_id)
    if evidence_item is None:
        raise _not_found(NotFoundError("EvidenceItem", edge.evidence_item_id))
    if claim.project_id != evidence_item.project_id:
        raise _bad_request(
            error,
            "source_artifact_refs cannot use a claim-evidence edge with inconsistent project membership.",
            field_name="source_artifact_refs",
            item_id=artifact_ref,
            claim_project_id=claim.project_id,
            evidence_project_id=evidence_item.project_id,
        )
    return claim.project_id


def _source_artifact_ref_project_id(
    session: Session,
    artifact_ref: str,
    *,
    error: str,
) -> str | None:
    project_scoped_models = (
        Source,
        Document,
        EvidenceItem,
        ResearchClaim,
        ResearchDelta,
        LiteratureMatrixRow,
        MethodCard,
        DatasetCard,
        ReproPackExport,
        ToolCallLog,
    )
    for model in project_scoped_models:
        related = session.get(model, artifact_ref)
        if related is not None:
            return related.project_id
    return _claim_evidence_edge_project_id(session, artifact_ref, error=error)


def _require_source_artifact_refs_project(
    session: Session,
    project_id: str,
    data: dict[str, Any],
    *,
    error: str,
) -> None:
    if "source_artifact_refs" not in data:
        return
    refs = data["source_artifact_refs"]
    if refs is None:
        raise _bad_request(
            error,
            "source_artifact_refs must not be null.",
            field_name="source_artifact_refs",
            expected_project_id=project_id,
        )
    for artifact_ref in refs:
        item_project_id = _source_artifact_ref_project_id(session, artifact_ref, error=error)
        if item_project_id is None:
            raise _bad_request(
                error,
                "source_artifact_refs must resolve to a known project-scoped artifact.",
                field_name="source_artifact_refs",
                item_id=artifact_ref,
                expected_project_id=project_id,
            )
        if item_project_id != project_id:
            raise _bad_request(
                error,
                "source_artifact_refs must not reference artifacts from another project.",
                field_name="source_artifact_refs",
                item_id=artifact_ref,
                item_project_id=item_project_id,
                expected_project_id=project_id,
            )


def _require_document_create_scope(session: Session, data: dict[str, Any]) -> None:
    _require_payload_project_exists(session, data)
    _require_related_project(
        session,
        model=Source,
        item_id=data["source_id"],
        expected_project_id=data["project_id"],
        field_name="source_id",
        error="cross_project_document_source",
    )


def _require_evidence_item_related_scope(session: Session, project_id: str, data: dict[str, Any]) -> None:
    relation_checks = {
        "source_id": Source,
        "document_id": Document,
        "tool_call_id": ToolCallLog,
    }
    for field_name, model in relation_checks.items():
        if field_name in data and data[field_name] is not None:
            _require_related_project(
                session,
                model=model,
                item_id=data[field_name],
                expected_project_id=project_id,
                field_name=field_name,
                error="cross_project_evidence_reference",
            )
    _require_tool_call_lineage_project(
        session,
        project_id,
        data,
        error="cross_project_evidence_lineage",
    )


def _require_research_claim_related_scope(session: Session, project_id: str, data: dict[str, Any]) -> None:
    relation_checks = {
        "originating_evidence_item_id": EvidenceItem,
        "tool_call_id": ToolCallLog,
    }
    for field_name, model in relation_checks.items():
        if field_name in data and data[field_name] is not None:
            _require_related_project(
                session,
                model=model,
                item_id=data[field_name],
                expected_project_id=project_id,
                field_name=field_name,
                error="cross_project_claim_reference",
            )
    _require_tool_call_lineage_project(
        session,
        project_id,
        data,
        error="cross_project_claim_lineage",
    )


def _require_evidence_item_create_scope(session: Session, data: dict[str, Any]) -> None:
    _require_payload_project_exists(session, data)
    _require_evidence_item_related_scope(session, data["project_id"], data)


def _require_evidence_update_provenance(
    _session: Session,
    item: EvidenceItem,
    data: dict[str, Any],
) -> None:
    quoted_span = data.get("quoted_evidence_span", item.quoted_evidence_span)
    no_quote_reason = data.get("no_quote_reason", item.no_quote_reason)
    if not quoted_span and not no_quote_reason:
        raise _unprocessable(
            "missing_evidence_quote_provenance",
            "EvidenceItem updates must preserve quoted_evidence_span or no_quote_reason.",
            evidence_item_id=item.id,
        )


def _require_evidence_item_update_scope(
    session: Session,
    item: EvidenceItem,
    data: dict[str, Any],
) -> None:
    _require_evidence_update_provenance(session, item, data)
    _require_evidence_item_related_scope(session, item.project_id, data)


def _require_research_claim_create_scope(session: Session, data: dict[str, Any]) -> None:
    _require_payload_project_exists(session, data)
    _require_research_claim_related_scope(session, data["project_id"], data)


def _require_research_claim_update_scope(
    session: Session,
    item: ResearchClaim,
    data: dict[str, Any],
) -> None:
    _require_research_claim_related_scope(session, item.project_id, data)


def _require_same_project_edge(session: Session, data: dict[str, Any]) -> None:
    claim_id = data["claim_id"]
    evidence_item_id = data["evidence_item_id"]
    claim = session.get(ResearchClaim, claim_id)
    if claim is None:
        raise _not_found(NotFoundError("ResearchClaim", claim_id))
    evidence_item = session.get(EvidenceItem, evidence_item_id)
    if evidence_item is None:
        raise _not_found(NotFoundError("EvidenceItem", evidence_item_id))
    if claim.project_id != evidence_item.project_id:
        raise _bad_request(
            "cross_project_claim_evidence_edge",
            "ClaimEvidenceEdge cannot link a claim and evidence item from different projects.",
            claim_id=claim_id,
            claim_project_id=claim.project_id,
            evidence_item_id=evidence_item_id,
            evidence_project_id=evidence_item.project_id,
        )
    tool_call_id = data.get("tool_call_id")
    if tool_call_id:
        tool_call = session.get(ToolCallLog, tool_call_id)
        if tool_call is None:
            raise _not_found(NotFoundError("ToolCallLog", tool_call_id))
        if tool_call.project_id != claim.project_id:
            raise _bad_request(
                "cross_project_claim_evidence_tool_call",
                "ClaimEvidenceEdge tool_call_id must belong to the same project as the edge.",
                tool_call_id=tool_call_id,
                tool_call_project_id=tool_call.project_id,
                claim_project_id=claim.project_id,
            )
    _require_tool_call_lineage_project(
        session,
        claim.project_id,
        data,
        error="cross_project_claim_evidence_lineage",
    )


def _require_edge_update_project_scope(
    session: Session,
    item: ClaimEvidenceEdge,
    data: dict[str, Any],
) -> None:
    claim = session.get(ResearchClaim, item.claim_id)
    if claim is None:
        raise _not_found(NotFoundError("ResearchClaim", item.claim_id))
    if "tool_call_id" in data and data["tool_call_id"] is not None:
        tool_call_id = data["tool_call_id"]
        tool_call = session.get(ToolCallLog, tool_call_id)
        if tool_call is None:
            raise _not_found(NotFoundError("ToolCallLog", tool_call_id))
        if tool_call.project_id != claim.project_id:
            raise _bad_request(
                "cross_project_claim_evidence_tool_call",
                "ClaimEvidenceEdge tool_call_id must belong to the same project as the edge.",
                tool_call_id=tool_call_id,
                tool_call_project_id=tool_call.project_id,
                claim_project_id=claim.project_id,
            )
    _require_tool_call_lineage_project(
        session,
        claim.project_id,
        data,
        error="cross_project_claim_evidence_lineage",
    )


def _require_generated_artifact_scope(
    session: Session,
    project_id: str,
    data: dict[str, Any],
    *,
    relation_checks: dict[str, type] | None = None,
    list_relation_checks: dict[str, type] | None = None,
    error: str,
) -> None:
    if "tool_call_id" in data and data["tool_call_id"] is not None:
        _require_related_project(
            session,
            model=ToolCallLog,
            item_id=data["tool_call_id"],
            expected_project_id=project_id,
            field_name="tool_call_id",
            error=error,
        )
    for field_name, model in (relation_checks or {}).items():
        if field_name in data and data[field_name] is not None:
            _require_related_project(
                session,
                model=model,
                item_id=data[field_name],
                expected_project_id=project_id,
                field_name=field_name,
                error=error,
            )
    for field_name, model in (list_relation_checks or {}).items():
        if field_name in data and data[field_name] is not None:
            _require_related_list_project(
                session,
                model=model,
                item_ids=data[field_name],
                expected_project_id=project_id,
                field_name=field_name,
                error=error,
            )
    _require_tool_call_lineage_project(session, project_id, data, error=error)
    _require_source_artifact_refs_project(session, project_id, data, error=error)


def _create_project_scope_hook(
    *,
    relation_checks: dict[str, type] | None = None,
    list_relation_checks: dict[str, type] | None = None,
    error: str,
) -> Any:
    def before_create(session: Session, data: dict[str, Any]) -> None:
        _require_payload_project_exists(session, data)
        _require_generated_artifact_scope(
            session,
            data["project_id"],
            data,
            relation_checks=relation_checks,
            list_relation_checks=list_relation_checks,
            error=error,
        )

    return before_create


def _update_project_scope_hook(
    *,
    relation_checks: dict[str, type] | None = None,
    list_relation_checks: dict[str, type] | None = None,
    error: str,
) -> Any:
    def before_update(session: Session, item: Any, data: dict[str, Any]) -> None:
        _require_generated_artifact_scope(
            session,
            item.project_id,
            data,
            relation_checks=relation_checks,
            list_relation_checks=list_relation_checks,
            error=error,
        )

    return before_update


_require_research_delta_create_scope = _create_project_scope_hook(
    list_relation_checks={"changed_claim_ids": ResearchClaim},
    error="cross_project_research_delta_reference",
)
_require_research_delta_update_scope = _update_project_scope_hook(
    list_relation_checks={"changed_claim_ids": ResearchClaim},
    error="cross_project_research_delta_reference",
)
_require_literature_matrix_row_create_scope = _create_project_scope_hook(
    relation_checks={"document_id": Document, "claim_id": ResearchClaim},
    error="cross_project_literature_matrix_reference",
)
_require_literature_matrix_row_update_scope = _update_project_scope_hook(
    relation_checks={"document_id": Document, "claim_id": ResearchClaim},
    error="cross_project_literature_matrix_reference",
)
_require_method_card_create_scope = _create_project_scope_hook(
    relation_checks={"evidence_item_id": EvidenceItem},
    error="cross_project_method_card_reference",
)
_require_method_card_update_scope = _update_project_scope_hook(
    relation_checks={"evidence_item_id": EvidenceItem},
    error="cross_project_method_card_reference",
)
_require_dataset_card_create_scope = _create_project_scope_hook(
    relation_checks={"evidence_item_id": EvidenceItem},
    error="cross_project_dataset_card_reference",
)
_require_dataset_card_update_scope = _update_project_scope_hook(
    relation_checks={"evidence_item_id": EvidenceItem},
    error="cross_project_dataset_card_reference",
)
_require_repro_pack_export_create_scope = _create_project_scope_hook(
    error="cross_project_repro_pack_reference",
)
_require_repro_pack_export_update_scope = _update_project_scope_hook(
    error="cross_project_repro_pack_reference",
)


def register_crud_routes(
    *,
    route_name: str,
    model: type,
    create_schema: type,
    update_schema: type,
    read_schema: type,
    before_create: Any | None = None,
    before_update: Any | None = None,
) -> None:
    service = CrudService(model)
    prefix = f"/{route_name}"

    @router.post(prefix, response_model=read_schema, status_code=status.HTTP_201_CREATED)
    def create_item(payload: create_schema, session: Session = Depends(get_db_session)) -> Any:  # type: ignore[valid-type]
        data = payload.model_dump(exclude_unset=True)
        if before_create:
            before_create(session, data)
        return service.create(session, data)

    @router.get(prefix, response_model=list[read_schema])  # type: ignore[valid-type]
    def list_items(
        limit: int = 100,
        offset: int = 0,
        session: Session = Depends(get_db_session),
    ) -> list[Any]:
        return service.list(session, limit=limit, offset=offset)

    @router.get(f"{prefix}/{{item_id}}", response_model=read_schema)
    def get_item(item_id: str, session: Session = Depends(get_db_session)) -> Any:
        try:
            return service.get(session, item_id)
        except NotFoundError as error:
            raise _not_found(error) from error

    @router.patch(f"{prefix}/{{item_id}}", response_model=read_schema)
    def update_item(
        item_id: str,
        payload: update_schema,  # type: ignore[valid-type]
        session: Session = Depends(get_db_session),
    ) -> Any:
        try:
            data = payload.model_dump(exclude_unset=True)
            if before_update:
                item = service.get(session, item_id)
                before_update(session, item, data)
                return service.update_existing(session, item, data)
            return service.update(session, item_id, data)
        except NotFoundError as error:
            raise _not_found(error) from error

    @router.delete(f"{prefix}/{{item_id}}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_item(item_id: str, session: Session = Depends(get_db_session)) -> None:
        try:
            service.delete(session, item_id)
        except NotFoundError as error:
            raise _not_found(error) from error


register_crud_routes(
    route_name="research-projects",
    model=ResearchProject,
    create_schema=schemas.ResearchProjectCreate,
    update_schema=schemas.ResearchProjectUpdate,
    read_schema=schemas.ResearchProjectRead,
)
register_crud_routes(
    route_name="sources",
    model=Source,
    create_schema=schemas.SourceCreate,
    update_schema=schemas.SourceUpdate,
    read_schema=schemas.SourceRead,
    before_create=_require_payload_project_exists,
)
register_crud_routes(
    route_name="documents",
    model=Document,
    create_schema=schemas.DocumentCreate,
    update_schema=schemas.DocumentUpdate,
    read_schema=schemas.DocumentRead,
    before_create=_require_document_create_scope,
)
register_crud_routes(
    route_name="tool-call-logs",
    model=ToolCallLog,
    create_schema=schemas.ToolCallLogCreate,
    update_schema=schemas.ToolCallLogUpdate,
    read_schema=schemas.ToolCallLogRead,
    before_create=_require_payload_project_exists,
)
register_crud_routes(
    route_name="evidence-items",
    model=EvidenceItem,
    create_schema=schemas.EvidenceItemCreate,
    update_schema=schemas.EvidenceItemUpdate,
    read_schema=schemas.EvidenceItemRead,
    before_create=_require_evidence_item_create_scope,
    before_update=_require_evidence_item_update_scope,
)
register_crud_routes(
    route_name="research-claims",
    model=ResearchClaim,
    create_schema=schemas.ResearchClaimCreate,
    update_schema=schemas.ResearchClaimUpdate,
    read_schema=schemas.ResearchClaimRead,
    before_create=_require_research_claim_create_scope,
    before_update=_require_research_claim_update_scope,
)
register_crud_routes(
    route_name="claim-evidence-edges",
    model=ClaimEvidenceEdge,
    create_schema=schemas.ClaimEvidenceEdgeCreate,
    update_schema=schemas.ClaimEvidenceEdgeUpdate,
    read_schema=schemas.ClaimEvidenceEdgeRead,
    before_create=_require_same_project_edge,
    before_update=_require_edge_update_project_scope,
)
register_crud_routes(
    route_name="research-deltas",
    model=ResearchDelta,
    create_schema=schemas.ResearchDeltaCreate,
    update_schema=schemas.ResearchDeltaUpdate,
    read_schema=schemas.ResearchDeltaRead,
    before_create=_require_research_delta_create_scope,
    before_update=_require_research_delta_update_scope,
)
register_crud_routes(
    route_name="literature-matrix-rows",
    model=LiteratureMatrixRow,
    create_schema=schemas.LiteratureMatrixRowCreate,
    update_schema=schemas.LiteratureMatrixRowUpdate,
    read_schema=schemas.LiteratureMatrixRowRead,
    before_create=_require_literature_matrix_row_create_scope,
    before_update=_require_literature_matrix_row_update_scope,
)
register_crud_routes(
    route_name="method-cards",
    model=MethodCard,
    create_schema=schemas.MethodCardCreate,
    update_schema=schemas.MethodCardUpdate,
    read_schema=schemas.MethodCardRead,
    before_create=_require_method_card_create_scope,
    before_update=_require_method_card_update_scope,
)
register_crud_routes(
    route_name="dataset-cards",
    model=DatasetCard,
    create_schema=schemas.DatasetCardCreate,
    update_schema=schemas.DatasetCardUpdate,
    read_schema=schemas.DatasetCardRead,
    before_create=_require_dataset_card_create_scope,
    before_update=_require_dataset_card_update_scope,
)
register_crud_routes(
    route_name="repro-pack-exports",
    model=ReproPackExport,
    create_schema=schemas.ReproPackExportCreate,
    update_schema=schemas.ReproPackExportUpdate,
    read_schema=schemas.ReproPackExportRead,
    before_create=_require_repro_pack_export_create_scope,
    before_update=_require_repro_pack_export_update_scope,
)
