from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI
from fastapi.responses import JSONResponse

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


@app.exception_handler(httpx.HTTPStatusError)
async def heygen_error_handler(request, exc: httpx.HTTPStatusError):
    try:
        detail = exc.response.json()
    except Exception:
        detail = exc.response.text
    return JSONResponse(
        status_code=exc.response.status_code,
        content={"error": "heygen_api_error", "detail": detail},
    )


@app.get("/health")
async def health():
    return {"status": "ok"}
