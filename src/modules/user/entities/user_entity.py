from dataclasses import dataclass
from sqlalchemy import Column, String, Text

from src.shared.entities.base_entity import BaseEntity


@dataclass
class UserEntity(BaseEntity):
    __tablename__ = "user"

    username = Column(String(255), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    role = Column(String(255))
