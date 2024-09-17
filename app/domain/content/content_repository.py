import uuid
from sqlalchemy import and_, delete, or_, select, update
from .content_model import Content
from sqlalchemy.ext.asyncio import async_scoped_session
from abc import ABC


class BaseContentRepository(ABC):
    pass


class ContentAlchemyRepository(BaseContentRepository):

    def __init__(self, session: async_scoped_session):
        self.session = session

    async def get_by_id(self, id: uuid.UUID):
        query = select(Content).where(Content.id == id)
        result = await self.session.execute(query)

        return result.scalars().first()
