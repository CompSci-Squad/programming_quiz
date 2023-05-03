import uuid
from sqlalchemy import Column, DateTime, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

from src.database.connect import engine
from src.shared.database_types.uuid import UUID
Base = declarative_base()


class User(Base):
    """User account."""

    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    bio = Column(Text)
    avatar_url = Column(Text)
    role = Column(String(255))
    

    def __repr__(self):
        return "<User %r>" % self.username


Base.metadata.create_all(engine)
