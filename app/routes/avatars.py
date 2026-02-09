from fastapi import APIRouter, UploadFile

from app.heygen_client import heygen
from app.schemas import PhotoGroupCreate

router = APIRouter(prefix="/api/avatars", tags=["avatars"])


@router.get("")
async def list_avatars():
    return await heygen.list_avatars()


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
