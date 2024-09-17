from app.core.db.session_maker import Base
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Boolean,
    ARRAY,
    Text,
    DateTime,
)
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(Text)
    email = Column(Text)
    password = Column(Text)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)
