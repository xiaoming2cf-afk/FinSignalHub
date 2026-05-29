from __future__ import annotations

from typing import Any, Generic, TypeVar

from sqlalchemy import select
from sqlalchemy.orm import Session

from finsignalhub_api.db.base import Base


ModelT = TypeVar("ModelT", bound=Base)


class NotFoundError(LookupError):
    def __init__(self, model_name: str, item_id: str) -> None:
        super().__init__(f"{model_name} {item_id} was not found")
        self.model_name = model_name
        self.item_id = item_id


class CrudService(Generic[ModelT]):
    def __init__(self, model: type[ModelT]) -> None:
        self.model = model

    def create(self, session: Session, data: dict[str, Any]) -> ModelT:
        item = self.model(**self._normalize(data))
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

    def list(self, session: Session, limit: int = 100, offset: int = 0) -> list[ModelT]:
        statement = select(self.model).offset(offset).limit(limit)
        return list(session.scalars(statement))

    def get(self, session: Session, item_id: str) -> ModelT:
        item = session.get(self.model, item_id)
        if item is None:
            raise NotFoundError(self.model.__name__, item_id)
        return item

    def update(self, session: Session, item_id: str, data: dict[str, Any]) -> ModelT:
        item = self.get(session, item_id)
        for key, value in self._normalize(data).items():
            setattr(item, key, value)
        session.commit()
        session.refresh(item)
        return item

    def delete(self, session: Session, item_id: str) -> None:
        item = self.get(session, item_id)
        session.delete(item)
        session.commit()

    def _normalize(self, data: dict[str, Any]) -> dict[str, Any]:
        normalized: dict[str, Any] = {}
        for key, value in data.items():
            normalized[key] = getattr(value, "value", value)
        return normalized
