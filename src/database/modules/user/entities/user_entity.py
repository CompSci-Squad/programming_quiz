from typing import Optional
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from src.shared.entities.base_entity import BaseEntity


class UserEntity(BaseEntity):
    __tablename__ = "user"
    __email: Mapped[str] = mapped_column(String(18), unique=True, nullable=False)
    __password: Mapped[str] = mapped_column(String(15), nullable=False)
    __name: Mapped[str] = mapped_column(String(255), nullable=False)
    __ra: Mapped[str] = mapped_column(String(10), nullable=False, unique=True)
    __coins: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    __current_phase_id: Mapped[Optional[str]] = mapped_column(ForeignKey("phase.id"))

    def __init__(
        self,
        email: str,
        password: str,
        name: str,
        ra: str,
        coins: int,
        current_phase_id: Optional[str]
    ) -> None:
        self.__email = email
        self.__name = name
        self.__password = password
        self.__ra = ra
        self.__coins = coins
        self.__current_phase_id = current_phase_id

    # getter/setter methods
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
    def email(self, value):
        self.__email = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def ra(self):
        return self.__ra

    @ra.setter
    def ra(self, value):
        self.__ra = value

    @property
    def coins(self):
        return self.__coins

    @coins.setter
    def coins(self, value):
        self.__coins = value
    
    @property
    def current_phase_id(self):
        return self.__current_phase_id
    
    @current_phase_id.setter
    def current_phase_id(self, value):
        self.__current_phase_id = value
