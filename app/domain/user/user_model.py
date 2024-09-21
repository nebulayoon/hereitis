import uuid

from pydantic import BaseModel, Field
from sqlalchemy import (ARRAY, Boolean, Column, DateTime, ForeignKey, Integer,
                        String, Text)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func, text

from app.core.db.session_maker import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()")
    )
    name = Column(Text)
    email = Column(Text)
    password = Column(Text)
    google_id = Column(Text)
    is_google_id = Column(Boolean)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)


class CreateUserRequestSchema(BaseModel):
    email: str
    password1: str
    password2: str
    name: str


class LoginRequestSchema(BaseModel):
    email: str
    password: str
