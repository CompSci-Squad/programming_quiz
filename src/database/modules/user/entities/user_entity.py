from sqlalchemy import Column, String, Integer

from src.shared.entities.base_entity import BaseEntity


class UserEntity(BaseEntity):
    __tablename__ = "user"
    email = Column(String(18), unique=True, nullable=False)
    password = Column(String(15), nullable=False)
    name = Column(String(255), nullable=False)
    ra = Column(String(10), nullable=False, unique=True)
    coins = Column(Integer, nullable=False, default=0)

    def __init__(
        self,
        email: str,
        password: str,
        name: str,
        ra: str,
        coins: int,
    ) -> None:
        self.email = email
        self.password = password
        self.name = name
        self.ra = ra
        self.coins = coins
