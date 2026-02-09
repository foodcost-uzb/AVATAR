from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.heygen_client import heygen
from app.routes import account, avatars, videos, voices


@asynccontextmanager
async def lifespan(app: FastAPI):
    await heygen.start()
    yield
    await heygen.close()


app = FastAPI(
    title="AVATAR — Digital Twin Video API",
    description="Обёртка над HeyGen API для работы с цифровым аватаром",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(account.router)
app.include_router(avatars.router)
app.include_router(voices.router)
app.include_router(videos.router)


@app.get("/health")
async def health():
    return {"status": "ok"}
