import uuid

from app.domain.content.content_model import (CreateContentDTO,
                                              CreateContentRequestSchema)

from .content_repository import ContentAlchemyRepository


class ContentService:
    repository: ContentAlchemyRepository

    def __init__(self, repository):
        self.repository = repository

    async def get_content(self, id: uuid.UUID):
        return await self.repository.get_by_id(id)

    async def get_content_list(self, user_id: uuid.UUID):
        return await self.repository.get_list(user_id)

    async def create_content(self, type: str, user_id: str, data: str):
        content_dto = CreateContentDTO(
            type=type,
            data=data,
            llm_status=False,
            user_id=uuid.UUID(user_id),
            tag=[],
        )
        await self.repository.save(content_dto)
