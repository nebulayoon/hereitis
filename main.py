from fastapi import FastAPI
import uvicorn
from app.api import router
from app.core.config.config import config, Settings


app = FastAPI()

app.include_router(router)


@app.get("/")
async def test():
    print(Settings().DB_URL)
    return {"hello": "world"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
