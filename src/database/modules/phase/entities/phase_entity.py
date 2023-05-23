from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, mapped_column

from src.shared.entities.base_entity import BaseEntity


class PhaseEntity(BaseEntity):
    __tablename__ = "phase"
    name: Mapped[str] = mapped_column(String(30), nullable=False)

    def __init__(
        self,
        name: str,
    ) -> None:
        self.name = name
        