from sqlalchemy.orm.session import Session
from typing import List, Optional, Type, Dict, TypedDict, Union
from src.database.modules.user.entities.user_entity import UserEntity
from src.shared.logger.logger import LOGGER


class UserRepository:
    __session: Session

    def __init__(self, session: Session):
        self.__session = session

    def create(
        self,
        username: str,
        password: str,
        email: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        role: Optional[str] = None,
    ) -> Union[UserEntity, None]:
        try:
            entity = UserEntity(username, password, email, first_name, last_name, role)
            self.__session.add(entity)
            self.__session.commit()
            self.__session.refresh(entity)
            return entity
        except:
            LOGGER.error("error on creating a user")

    def update(
        self,
        id: str,
        username: Optional[str] = None,
        password: Optional[str] = None,
        email: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        role: Optional[str] = None,
    ) -> Union[UserEntity, None]:
        try:
            user = self.get_by_id(id)
            if user is None:
                LOGGER.error(f"no user found with {id}")
                raise ValueError()
            if username:
                user.username = username
            if password:
                user.password = password
            if email:
                user.email = email
            if first_name:
                user.first_name = first_name
            if last_name:
                user.last_name = last_name
            if role:
                user.role = role

            self.__session.commit()
            self.__session.refresh(user)
            return user
        except:
            LOGGER.error("erro no update")

    def delete(self, entity: UserEntity):
        self.__session.delete(entity)
        self.__session.commit()

    def get_all(self) -> List[UserEntity]:
        return self.__session.query(UserEntity).all()

    def get_by_id(self, id: str) -> Union[UserEntity, None]:
        return self.__session.query(UserEntity).get(id)
