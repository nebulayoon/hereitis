import os
import uuid
from fastapi import APIRouter, Depends, File, Path, UploadFile

from app.core.db.session_maker import get_db_session
from app.domain.auth.auth_depends import auth_depends
from app.domain.content.content_model import CreateContentRequestSchema
from app.domain.content.content_repository import ContentAlchemyRepository
from app.domain.content.content_service import ContentService
from sqlalchemy.ext.asyncio import async_scoped_session
from app.core.config.config import config


content_router = APIRouter()


@content_router.get("/list")
async def get_content_list(
    session: async_scoped_session = Depends(get_db_session),
    user_id: str = Depends(auth_depends),
):
    repository = ContentAlchemyRepository(session)
    content_service: ContentService = ContentService(repository)

    return await content_service.get_content_list(uuid.UUID(user_id))


@content_router.get("/{content_id}")
async def get_content(
    content_id: str = Path(...), session: async_scoped_session = Depends(get_db_session)
):
    repository = ContentAlchemyRepository(session)
    content_service: ContentService = ContentService(repository)

    return await content_service.get_content(uuid.UUID(content_id))


@content_router.post("/text")
async def create_text_content(
    data: CreateContentRequestSchema,
    session: async_scoped_session = Depends(get_db_session),
    user_id: str = Depends(auth_depends),
):
    repository = ContentAlchemyRepository(session)
    content_service: ContentService = ContentService(repository)

    return await content_service.create_content("text", user_id, data.data)


@content_router.post("/file")
async def create_file_content(
    file: UploadFile = File(...),
    session: async_scoped_session = Depends(get_db_session),
    user_id: str = Depends(auth_depends),
):
    repository = ContentAlchemyRepository(session)
    content_service: ContentService = ContentService(repository)

    file_extension = os.path.splitext(file.filename)[1]
    unique_filename = f"{uuid.uuid4()}{file_extension}"
    file_location = f"{config.UPLOAD_DIR}/{unique_filename}"

    with open(file_location, "wb") as f:
        f.write(await file.read())

    return await content_service.create_content("text", user_id, file_location)
