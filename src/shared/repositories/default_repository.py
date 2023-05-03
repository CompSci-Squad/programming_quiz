from typing import Generic, TypeVar
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.shared.logger.logger import LOGGER

T = TypeVar("T")


class DefaultRepository(Generic[T]):
    __session: Session

    def __init__(self, session: Session):
        self.__session = session

    def create(self, entity: T) -> None:
        try:
            self.__session.add(entity)
            self.__session.commit()
        except IntegrityError as e:
            LOGGER.error(f"unexpected error when commiting entity {entity}, error: {e}")

    def find_and_delete(self, id: str) -> None:
        try:
            self.__session.expire
