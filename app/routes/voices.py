from fastapi import APIRouter

from app.heygen_client import heygen

router = APIRouter(prefix="/api", tags=["voices"])


@router.get("/voices")
async def list_voices():
    return await heygen.list_voices()
