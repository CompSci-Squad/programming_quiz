from typing import Generic, TypeVar

from sqlalchemy.orm import Session

T = TypeVar('T')

class DefaultRepository(Generic[T]):
    __session: Session
    def create(self, entity: T):
        try:
            self.__session.add(entity)
            self.__session.commit()
