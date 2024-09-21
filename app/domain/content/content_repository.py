import uuid
from abc import ABC
from typing import List

from sqlalchemy import and_, delete, or_, select, update
from sqlalchemy.ext.asyncio import async_scoped_session

from .content_model import (Content, CreateContentDTO,
                            CreateContentRequestSchema)


class BaseContentRepository(ABC):
    pass


class ContentAlchemyRepository(BaseContentRepository):

    def __init__(self, session: async_scoped_session):
        self.session = session

    async def get_by_id(self, id: uuid.UUID):
        query = select(Content).where(Content.id == id)
        result = await self.session.execute(query)

        return result.scalars().first()

    async def get_list(self, user_id: uuid.UUID):
        query = (
            select(Content)
            .where(Content.user_id == user_id)
            .order_by(Content.created_at.desc())
        )
        result = await self.session.execute(query)

        return result.scalars().all()

    async def get_queued_list(self):
        query = (
            select(Content)
            .where(and_(Content.type == "text"))
            .order_by(Content.created_at.desc())
        )
        result = await self.session.execute(query)

        return result.scalars().all()

    async def update_tags(self, content_id: uuid.UUID, tags: List):
        query = update(Content).where(Content.id == content_id).values(tag=tags)
        await self.session.execute(query)

    async def save(self, content_dto: CreateContentDTO):
        content = Content(
            type=content_dto.type,
            data=content_dto.data,
            llm_status=content_dto.llm_status,
            user_id=content_dto.user_id,
            tag=content_dto.tag,
        )

        await self.session.add(content)
