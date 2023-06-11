from uuid import uuid4
from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.ext.declarative import declarative_base

from src.database.modules.level.entities.level_entity import LevelEntity

Base = declarative_base()


class UserEntity(Base):
    __tablename__ = "users"
    __id: Mapped[str] = mapped_column(
        String(32), name="id",primary_key=True, default=lambda: uuid4().hex, index=True
    )
    __email: Mapped[str] = mapped_column(String(50), unique=True, name="email", nullable=False
    )
    __password: Mapped[str] = mapped_column(String(15), name="password",nullable=False)
    __name: Mapped[str] = mapped_column(String(50), name="name",nullable=False)
    __ra: Mapped[str] = mapped_column(String(10), name="ra", nullable=False, unique=True)
    __coins: Mapped[int] = mapped_column(Integer, name="coins", nullable=False, default=0)
    __current_level_id: Mapped[int] = mapped_column(ForeignKey("level.id"), name="current_level_id")
    level: Mapped[LevelEntity] = relationship(back_populates="users")

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
