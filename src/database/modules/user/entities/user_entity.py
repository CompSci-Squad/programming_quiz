from typing import Optional
from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped

from src.shared.entities.base_entity import BaseEntity


class UserEntity(BaseEntity):
    __tablename__ = "user"
    email: Mapped[str] = mapped_column(String(18), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(15), nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    ra: Mapped[str] = mapped_column(String(10), nullable=False, unique=True)
    coins: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    # __current_phase_id: Mapped[Optional[str]] = mapped_column(ForeignKey("phase.id"))

    def __init__(
        self,
        email: str,
        password: str,
        name: str,
        ra: str,
        coins: int,
    ) -> None:
        self.email = email
        self.name = name
        self.password = password
        self.ra = ra
        self.coins = coins
        # self.__current_phase_id = current_phase_id

    """ # getter/setter methods
    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.name = value

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, value: str):
        self.email = value

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, value: str):
        self.password = value

    @property
    def ra(self):
        return self.ra

    @ra.setter
    def ra(self, value: str):
        self.ra = value

    @property
    def coins(self):
        return self.coins

    @coins.setter
    def coins(self, value):
        self.coins = value """
