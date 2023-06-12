from __future__ import annotations
from typing import TYPE_CHECKING

from uuid import uuid4
from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import mapped_column, MappedColumn, relationship
from src.shared.entities.base_entity import Base

if TYPE_CHECKING:
    from src.database.modules.level.entities.level_entity import LevelEntity


class UserEntity(Base):
    __tablename__ = "users"
    __id: MappedColumn[str] = mapped_column(
        String(32), name="id", primary_key=True, default=lambda: uuid4().hex, index=True
    )
    __email: MappedColumn[str] = mapped_column(
        String(50), unique=True, index=True, name="email", nullable=False
    )
    __password: MappedColumn[str] = mapped_column(String(15), name="password", nullable=False)
    __name: MappedColumn[str] = mapped_column(String(50), name="name", nullable=False)
    __ra: MappedColumn[str] = mapped_column(
        String(10), name="ra", index=True, nullable=False, unique=True
    )
    __coins: MappedColumn[int] = mapped_column(
        Integer, name="coins", nullable=False, default=0
    )
    __current_level_id: MappedColumn[int] = mapped_column(
        ForeignKey("level.id"), name="current_level_id"
    )
    level: MappedColumn[LevelEntity] = relationship(back_populates="users")

    def __init__(
        self,
        email: str,
        password: str,
        name: str,
        ra: str,
        coins: int,
        current_level_id: int,
    ) -> None:
        self.email = email
        self.name = name
        self.password = password
        self.ra = ra
        self.coins = coins
        self.__current_level_id = current_level_id

    def __str__(self) -> str:
        return f"UserEntity(id={self.id}, email={self.email}, password={self.password}, name={self.name}, ra={self.ra}, coins={self.coins}, current_level_id={self.current_level_id})"

    # getter/setter methods
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value: str):
        self.__email = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value: str):
        self.__password = value

    @property
    def ra(self):
        return self.__ra

    @ra.setter
    def ra(self, value: str):
        self.__ra = value

    @property
    def coins(self):
        return self.__coins

    @coins.setter
    def coins(self, value):
        self.__coins = value

    @property
    def current_level_id(self):
        return self.__current_level_id

    @current_level_id.setter
    def current_level_id(self, value):
        self.__current_level_id = value
