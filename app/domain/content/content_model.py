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
from sqlalchemy.sql import func


class Content(Base):
    __tablename__ = "contents"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type = Column(String)
    data = Column(Text)
    llm_status = Column(Boolean)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    # user_id = Column(UUID(as_uuid=True))
    tag = Column(ARRAY(String))
    google_id = Column(Text)
    is_google_id = Column(Boolean)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)
