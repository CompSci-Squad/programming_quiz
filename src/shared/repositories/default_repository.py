from typing import Any, Dict, Generic, Type, TypeVar
from abc import ABC, abstractmethod
from typing_extensions import Unpack
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, declarative_base

from src.shared.logger.logger import LOGGER

Base = declarative_base()

T = TypeVar("T", bound=Base)


class DefaultRepositoryInterface(Generic[T], ABC):

    @abstractmethod
    def create(self, entity: Type[T]) -> None:
        pass
        
    @abstractmethod
    def find_and_delete(self, entity_cls: Type[T], **kwargs: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def find_and_update(
        self, entity_cls: Type[T], filter_by: Dict[str, Any], update_kwargs: Dict[str, Any]
    ):
        pass

