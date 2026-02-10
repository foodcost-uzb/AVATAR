from typing import Optional

from fastapi import APIRouter, Query, UploadFile

from app.heygen_client import heygen
from app.schemas import PhotoGroupCreate

router = APIRouter(prefix="/api/avatars", tags=["avatars"])


@router.get("")
async def list_avatars(name: Optional[str] = Query(None, description="Filter by name (case-insensitive substring)")):
    """List all avatars. Optionally filter by name."""
    data = await heygen.list_avatars()
    if name:
        name_lower = name.lower()
        avatars = data.get("data", {}).get("avatars", [])
        data["data"]["avatars"] = [
            a for a in avatars if name_lower in a.get("avatar_name", "").lower()
        ]
    return data


@router.get("/talking-photos")
async def list_talking_photos():
    """List talking photos from the avatars response."""
    data = await heygen.list_avatars()
    photos = data.get("data", {}).get("talking_photos", [])
    return {"error": None, "data": {"talking_photos": photos}}


@router.get("/{avatar_id}")
async def get_avatar_details(avatar_id: str):
    """Get detailed info about an avatar (includes is_public field)."""
    return await heygen.get_avatar_details(avatar_id)


@router.post("/upload")
async def upload_photo(file: UploadFile):
    """Upload a JPEG/PNG photo and get an image_key back."""
    file_bytes = await file.read()
    content_type = file.content_type or "image/jpeg"
    return await heygen.upload_asset(file_bytes, content_type)


@router.post("/photo-group")
async def create_photo_group(body: PhotoGroupCreate):
    """Create a photo avatar group from an uploaded image_key."""
    return await heygen.create_photo_group(body.name, body.image_key)


@router.post("/photo-group/{group_id}/train")
async def train_photo_avatar(group_id: str):
    """Start training a photo avatar group."""
    return await heygen.train_photo_avatar(group_id)
