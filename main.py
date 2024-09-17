from fastapi import FastAPI
import uvicorn
from app.init_router import router
from app.core.config.config import config, Settings
from app.core.db.session_maker import init_db
import asyncio
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    if config.API_MODE == "development":
        print(config)
        from app.domain import Content, User

        await init_db()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router)


@app.get("/")
async def test():
    print(Settings().DB_URL)
    return {"hello": "world"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
