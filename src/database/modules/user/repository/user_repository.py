from sqlalchemy.orm.session import Session
from sqlalchemy import select
from typing import List, Dict, Union, Literal
from src.shared.logger.logger import LOGGER

from src.database.modules.user.entities.user_entity import UserEntity
from src.database.modules.user.dtos.create_user_dto import CreateUserDto
from src.database.modules.user.dtos.update_user_dto import UpdateUserDto


class UserRepository:
    __session: Session

    def __init__(self, session: Session):
        self.__session = session

    def create(self, userPayload: CreateUserDto) -> Union[UserEntity, None]:
        try:
            entity = UserEntity(
                email=userPayload["email"],
                password=userPayload["password"],
                name=userPayload["name"],
                ra=userPayload["ra"],
                coins=userPayload["coins"],
                current_level_id=userPayload["current_level_id"],
            )
            self.__session.add(entity)
            self.__session.commit()
            self.__session.refresh(entity)
            return entity
        except Exception:
            LOGGER.error("error on creating a user")
            raise Exception

    def update(self, updateUserDto: UpdateUserDto) -> Union[UserEntity, None]:
        try:
            id = updateUserDto["id"]
            email = updateUserDto["email"]
            password = updateUserDto["password"]
            name = updateUserDto["name"]
            ra = updateUserDto["ra"]
            coins = updateUserDto["coins"]
            current_level_id = updateUserDto["current_level_id"]
            user = self.get_by_id(id)
            if user is None:
                LOGGER.error(f"no user found with {id}")
                raise ValueError()

            if email is not None:
                user.email = email
            if password is not None:
                user.password = password
            if name is not None:
                user.name = name
            if ra is not None:
                user.ra = ra
            if coins is not None:
                user.coins = coins
            if current_level_id is not None:
                user.current_phase_id = current_level_id

            self.__session.commit()
            self.__session.refresh(user)
            return user
        except:
            LOGGER.error("erro no update")

    def delete(self, id: str) -> None:
        try:
            entity = self.get_by_id(id)
            if not entity:
                raise ValueError("entity not found")
            self.__session.delete(entity)
            self.__session.commit()
        except:
            LOGGER.error("erro no delete")

    def get_all(self) -> List[UserEntity]:
        return self.__session.query(UserEntity).all()

    def get_by_id(self, id: str) -> Union[UserEntity, None]:
        return self.__session.query(UserEntity).get(id)

    def find_user(
        self, attribute: Literal["email", "ra"], value: str
    ) -> Union[UserEntity, None]:
        valid_user = 'not found'
        users = self.get_all()
        for user in users:
            if getattr(user, attribute) == value:
                valid_user = user

        if valid_user == 'not found':
            LOGGER.info('user not found')
            return 0
        
        return valid_user


    def add_coin(self, id: str, coins: int) -> Union[UserEntity, None]:
        try:
            user = self.get_by_id(id)
            if user is None:
                LOGGER.error(f"no user found with {id}")
                raise ValueError()

            user.coins = coins

            self.__session.commit()
            self.__session.refresh()
            return user
        except:
            LOGGER.error("erro no update das moedas")
