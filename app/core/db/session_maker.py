from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config.config import config
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

engine = create_async_engine(config.DB_URL, echo=True)

async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


async def init_db():
    print("init db called")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Dependency
async def get_db():
    db = async_session()
    try:
        yield db
    finally:
        await db.close()
