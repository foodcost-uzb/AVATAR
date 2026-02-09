from typing import Optional

from pydantic import BaseModel


# --- Video generation ---

class VoiceInput(BaseModel):
    voice_id: str
    input_text: str
    speed: float = 1.0


class VideoGenerateRequest(BaseModel):
    avatar_id: str
    voice: VoiceInput
    dimension: Optional[dict] = None  # {"width": 1280, "height": 720}
    background: Optional[dict] = None


# --- Photo avatar ---

class PhotoGroupCreate(BaseModel):
    name: str
    image_key: str


class PhotoGroupTrain(BaseModel):
    group_id: str
