from typing import Optional
from sqlalchemy import Column, String, Text

from src.shared.entities.base_entity import BaseEntity


class UserEntity(BaseEntity):
    __tablename__ = "user"

    username = Column(String(255), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    role = Column(String(255))

    def __init__(
        self,
        username: str,
        password: str,
        email: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        role: Optional[str] = None,
    ) -> None:
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
