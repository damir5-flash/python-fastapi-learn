from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Request, Form
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from api import router
from core.config import settings
from core.models.db_helper import db_helper
from core.models.user import User


@asynccontextmanager
async def lifespan(apps: FastAPI):
    # start-up

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

templates = Jinja2Templates(directory="fastapi-app/templates")
app.mount("/static", StaticFiles(directory="fastapi-app/static"), name="static")


if __name__ == "__main__":
    print(f"Starting server at {settings.run.host}:{settings.run.port}")
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True
    )


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Главная страница"})


