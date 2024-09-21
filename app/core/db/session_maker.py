import asyncio
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (AsyncSession, async_scoped_session,
                                    create_async_engine)
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config.config import config

engine = create_async_engine(config.DB_URL, echo=True)

async_session_factory = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)
async_session = async_scoped_session(
    async_session_factory, scopefunc=asyncio.current_task
)
Base = declarative_base()


async def init_db():
    print("init db called")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Dependency
async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
