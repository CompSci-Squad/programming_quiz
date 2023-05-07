from sqlalchemy.orm.session import Session
from typing import List, Type
from src.shared.repositories.default_repository import DefaultRepositoryInterface
from src.modules.user.entities.user_entity import UserEntity

class UserRepository:
    __session: Session
    def __init__(self, session: Session):
        self.__session = session

    def create(self, user: UserEntity) -> UserEntity:
        self.__session.add(user)
        self.__session.commit()
        return user

    def update(self, user: UserEntity) -> UserEntity:
        self.__session.commit()
        return user

    def delete(self, user: UserEntity) -> None:
        self.__session.delete(user)
        self.__session.commit()

    def get_all(self) -> List[UserEntity]:
        return self.__session.query(UserEntity).all()


