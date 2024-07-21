import uvicorn
from fastapi import FastAPI
from api import router
from core.config import settings

app = FastAPI()
app.include_router(
    router,
    prefix=settings.api.prefix,
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app" ,
        host=settings.run.host,
        port=settings.run.port,
        reload=True)


@app.get("/")
async def root():
    return {"message": "Hello World"}



