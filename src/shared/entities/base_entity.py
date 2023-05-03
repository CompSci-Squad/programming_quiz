from dataclasses import dataclass
from typing import Any, Dict
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
import uuid


Base = declarative_base()


@dataclass
class BaseEntity(Base):
    __abstract__ = True

    id = Column(String(32), primary_key=True, default=lambda: uuid.uuid4().hex)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
