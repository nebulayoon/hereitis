import uuid
from .content_repository import ContentAlchemyRepository


class ContentService:
    repository: ContentAlchemyRepository

    def __init__(self, repository):
        self.repository = repository

    async def get_content(self, id: uuid.UUID):
        return await self.repository.get_by_id(id)
