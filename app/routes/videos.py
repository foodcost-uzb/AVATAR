from fastapi import APIRouter

from app.heygen_client import heygen
from app.schemas import VideoGenerateRequest

router = APIRouter(prefix="/api/videos", tags=["videos"])


@router.post("/generate")
async def generate_video(body: VideoGenerateRequest):
    """Generate a video with an avatar speaking the given text."""
    payload = {
        "video_inputs": [
            {
                "character": {
                    "type": "avatar",
                    "avatar_id": body.avatar_id,
                    "avatar_style": "normal",
                },
                "voice": {
                    "type": "text",
                    "voice_id": body.voice.voice_id,
                    "input_text": body.voice.input_text,
                    "speed": body.voice.speed,
                },
            }
        ],
    }
    if body.dimension:
        payload["dimension"] = body.dimension
    if body.background:
        payload["video_inputs"][0]["background"] = body.background
    return await heygen.generate_video(payload)


@router.get("/{video_id}/status")
async def get_video_status(video_id: str):
    return await heygen.get_video_status(video_id)
