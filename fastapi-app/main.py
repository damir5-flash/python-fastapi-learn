from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from api import router
from core.config import settings
from core.models import Base
from core.models.db_helper import db_helper



@asynccontextmanager
async def lifespan(apps: FastAPI):
    # start-up
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # shut-down
    db_helper.despose()

app = FastAPI(
    lifespan=lifespan,
)
app.include_router(
    router,
    prefix=settings.api.prefix,
)
if __name__ == "__main__":
    print(f"Starting server at {settings.run.host}:{settings.run.port}")
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True
    )


@app.get("/")
async def root():
    return {"message": "Hello World"}



