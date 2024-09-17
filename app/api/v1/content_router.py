import uuid
from fastapi import APIRouter, Depends

from app.core.db.session_maker import get_db_session
from app.domain.content.content_repository import ContentAlchemyRepository
from app.domain.content.content_service import ContentService
from sqlalchemy.ext.asyncio import async_scoped_session


content_router = APIRouter()


@content_router.get("/test")
async def test(session: async_scoped_session = Depends(get_db_session)):
    repository = ContentAlchemyRepository(session)
    content_service: ContentService = ContentService(repository)
    return await content_service.get_content(
        uuid.UUID("fc483563-bad5-468c-9929-1f55f5b73a0f")
    )
