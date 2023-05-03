from typing import Any, Dict, Generic, Type, TypeVar
from sqlalchemy import Table
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.shared.logger.logger import LOGGER

T = TypeVar("T", bound=Table)


class DefaultRepository(Generic[T]):
    __session: Session
    __entity: Type[T]
    def __init__(self, session: Session, entity: Type[T]):
        self.__entity = entity
        self.__session = session

    def create(self) -> None:
        try:
            self.__session.add(self.__entity)
            self.__session.commit()
        except IntegrityError as e:
            LOGGER.error(f"unexpected error when commiting entity {self.__entity}, error: {e}")
            raise e

    def find_and_delete(self, entity_cls: Type[T], **kwargs: Dict[str, Any]) -> None:
        try:
            entity = self.__session.query(entity_cls).filter_by(**kwargs).first()
            if entity:
                self.__session.delete(entity)
                self.__session.commit()
            else:
                LOGGER.info(f"not able to find entity with {kwargs}")
        except IntegrityError as e:
            LOGGER.error(f"unexpected error when commiting entity, error: {e}")
            raise e

    def find_and_update(
        self, entity_cls: Type[T], filter_by: Dict[str, Any], update_kwargs: Dict[str, Any]
    ):
        try:
            entity = self.__session.query(entity_cls).filter_by(**filter_by).first()
            if entity:
                # Update the entity with the given values
                for key, value in update_kwargs.items():
                    setattr(entity, key, value)
                self.__session.commit()
        except IntegrityError as e:
            LOGGER.error(f"unexpected error when commiting entity, error: {e}")
            raise e
