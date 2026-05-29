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


def register_crud_routes(
    *,
    route_name: str,
    model: type,
    create_schema: type,
    update_schema: type,
    read_schema: type,
) -> None:
    service = CrudService(model)
    prefix = f"/{route_name}"

    @router.post(prefix, response_model=read_schema, status_code=status.HTTP_201_CREATED)
    def create_item(payload: create_schema, session: Session = Depends(get_db_session)) -> Any:  # type: ignore[valid-type]
        return service.create(session, payload.model_dump(exclude_unset=True))

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
            return service.update(session, item_id, payload.model_dump(exclude_unset=True))
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
)
register_crud_routes(
    route_name="documents",
    model=Document,
    create_schema=schemas.DocumentCreate,
    update_schema=schemas.DocumentUpdate,
    read_schema=schemas.DocumentRead,
)
register_crud_routes(
    route_name="tool-call-logs",
    model=ToolCallLog,
    create_schema=schemas.ToolCallLogCreate,
    update_schema=schemas.ToolCallLogUpdate,
    read_schema=schemas.ToolCallLogRead,
)
register_crud_routes(
    route_name="evidence-items",
    model=EvidenceItem,
    create_schema=schemas.EvidenceItemCreate,
    update_schema=schemas.EvidenceItemUpdate,
    read_schema=schemas.EvidenceItemRead,
)
register_crud_routes(
    route_name="research-claims",
    model=ResearchClaim,
    create_schema=schemas.ResearchClaimCreate,
    update_schema=schemas.ResearchClaimUpdate,
    read_schema=schemas.ResearchClaimRead,
)
register_crud_routes(
    route_name="claim-evidence-edges",
    model=ClaimEvidenceEdge,
    create_schema=schemas.ClaimEvidenceEdgeCreate,
    update_schema=schemas.ClaimEvidenceEdgeUpdate,
    read_schema=schemas.ClaimEvidenceEdgeRead,
)
register_crud_routes(
    route_name="research-deltas",
    model=ResearchDelta,
    create_schema=schemas.ResearchDeltaCreate,
    update_schema=schemas.ResearchDeltaUpdate,
    read_schema=schemas.ResearchDeltaRead,
)
register_crud_routes(
    route_name="literature-matrix-rows",
    model=LiteratureMatrixRow,
    create_schema=schemas.LiteratureMatrixRowCreate,
    update_schema=schemas.LiteratureMatrixRowUpdate,
    read_schema=schemas.LiteratureMatrixRowRead,
)
register_crud_routes(
    route_name="method-cards",
    model=MethodCard,
    create_schema=schemas.MethodCardCreate,
    update_schema=schemas.MethodCardUpdate,
    read_schema=schemas.MethodCardRead,
)
register_crud_routes(
    route_name="dataset-cards",
    model=DatasetCard,
    create_schema=schemas.DatasetCardCreate,
    update_schema=schemas.DatasetCardUpdate,
    read_schema=schemas.DatasetCardRead,
)
register_crud_routes(
    route_name="repro-pack-exports",
    model=ReproPackExport,
    create_schema=schemas.ReproPackExportCreate,
    update_schema=schemas.ReproPackExportUpdate,
    read_schema=schemas.ReproPackExportRead,
)
