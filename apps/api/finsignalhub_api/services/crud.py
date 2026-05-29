from __future__ import annotations

from typing import Any, Generic, TypeVar

from sqlalchemy import inspect, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from finsignalhub_api.db.base import Base


ModelT = TypeVar("ModelT", bound=Base)


class NotFoundError(LookupError):
    def __init__(self, model_name: str, item_id: str) -> None:
        super().__init__(f"{model_name} {item_id} was not found")
        self.model_name = model_name
        self.item_id = item_id


class DeleteBlockedError(RuntimeError):
    def __init__(self, model_name: str, item_id: str) -> None:
        super().__init__(f"{model_name} {item_id} cannot be deleted while referenced")
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
        return self.update_existing(session, item, data)

    def update_existing(self, session: Session, item: ModelT, data: dict[str, Any]) -> ModelT:
        for key, value in self._normalize(data).items():
            setattr(item, key, value)
        session.commit()
        session.refresh(item)
        return item

    def delete(self, session: Session, item_id: str) -> None:
        item = self.get(session, item_id)
        if self._has_dependents(session, item):
            raise DeleteBlockedError(self.model.__name__, item_id)
        session.delete(item)
        try:
            session.commit()
        except IntegrityError as error:
            session.rollback()
            raise DeleteBlockedError(self.model.__name__, item_id) from error

    def _has_dependents(self, session: Session, item: ModelT) -> bool:
        mapper = inspect(self.model)
        for relation in mapper.relationships:
            if relation.direction.name != "ONETOMANY":
                continue

            criteria = []
            for local_column, remote_column in relation.local_remote_pairs:
                value = getattr(item, local_column.key)
                if value is None:
                    criteria = []
                    break
                criteria.append(remote_column == value)
            if not criteria:
                continue

            related_model = relation.mapper.class_
            statement = select(related_model).where(*criteria).limit(1)
            if session.scalars(statement).first() is not None:
                return True
        return False

    def _normalize(self, data: dict[str, Any]) -> dict[str, Any]:
        normalized: dict[str, Any] = {}
        for key, value in data.items():
            normalized[key] = getattr(value, "value", value)
        return normalized
