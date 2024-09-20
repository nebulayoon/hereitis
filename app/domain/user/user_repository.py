import uuid

from sqlalchemy import and_, delete, or_, select, update
from .user_model import User
from sqlalchemy.ext.asyncio import async_scoped_session
from abc import ABC


class BaseUserRepository(ABC):
    pass


class UserAlchemyRepository(BaseUserRepository):
    def __init__(self, session: async_scoped_session):
        self.session = session

    async def get_by_id(self, id: uuid.UUID):
        query = select(User).where(User.id == id)
        result = await self.session.execute(query)

        return result.scalars().first()

    async def get_by_email(self, email: str):
        query = select(User).where(User.email == email)
        result = await self.session.execute(query)

        return result.scalars().first()

    async def save(self, name: str, email: str, password: str):
        user = User(name=name, email=email, password=password)
        await self.session.add(user)
