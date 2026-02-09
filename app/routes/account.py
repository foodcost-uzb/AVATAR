from fastapi import APIRouter

from app.heygen_client import heygen

router = APIRouter(prefix="/api", tags=["account"])


@router.get("/quota")
async def get_quota():
    return await heygen.get_remaining_quota()
