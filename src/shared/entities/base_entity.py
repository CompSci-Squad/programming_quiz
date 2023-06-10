from sqlalchemy import String, DateTime
from sqlalchemy.orm import declarative_base, mapped_column, Mapped
from sqlalchemy.sql import func
import uuid


Base = declarative_base()

class BaseEntity(Base):
    __abstract__ = True

    __id: Mapped[str] = mapped_column(String(32), primary_key=True, default=lambda: uuid.uuid4().hex, index=True)
    __created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    __updated_at: Mapped[DateTime] = mapped_column(DateTime, onupdate=func.now())

    @property
    def id(self):
        return self.__id
    

