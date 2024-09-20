from typing import List, Optional
from pydantic import BaseModel
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
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import func, text


class Content(Base):
    __tablename__ = "contents"

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()")
    )
    type = Column(String)
    data = Column(Text)
    llm_status = Column(Boolean)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    tag = Column(ARRAY(String))
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)


class CreateContentRequestSchema(BaseModel):
    data: str


class CreateContentDTO(BaseModel):
    type: str
    data: str
    llm_status: bool
    user_id: uuid.UUID
    tag: Optional[List[str]]
