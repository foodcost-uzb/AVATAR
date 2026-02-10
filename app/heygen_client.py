from typing import Optional

import httpx

from app.config import settings

API_BASE = "https://api.heygen.com"
UPLOAD_BASE = "https://upload.heygen.com"


class HeyGenClient:
    """Async wrapper around HeyGen REST API."""

    def __init__(self) -> None:
        self._client: Optional[httpx.AsyncClient] = None

    async def start(self) -> None:
        self._client = httpx.AsyncClient(
            headers={"X-Api-Key": settings.heygen_api_key},
            timeout=120.0,
        )

    async def close(self) -> None:
        if self._client:
            await self._client.aclose()

    @property
    def client(self) -> httpx.AsyncClient:
        assert self._client is not None, "Call start() first"
        return self._client

    # ------ Account ------

    async def get_remaining_quota(self) -> dict:
        resp = await self.client.get(f"{API_BASE}/v2/user/remaining_quota")
        resp.raise_for_status()
        return resp.json()

    # ------ Avatars ------

    async def list_avatars(self) -> dict:
        resp = await self.client.get(f"{API_BASE}/v2/avatars")
        resp.raise_for_status()
        return resp.json()

    async def get_avatar_details(self, avatar_id: str) -> dict:
        resp = await self.client.get(f"{API_BASE}/v2/avatar/{avatar_id}/details")
        resp.raise_for_status()
        return resp.json()

    # ------ Voices ------

    async def list_voices(self) -> dict:
        resp = await self.client.get(f"{API_BASE}/v2/voices")
        resp.raise_for_status()
        return resp.json()

    # ------ Upload ------

    async def upload_asset(self, file_bytes: bytes, content_type: str) -> dict:
        """Upload raw bytes to HeyGen (not multipart)."""
        resp = await self.client.post(
            f"{UPLOAD_BASE}/v1/asset",
            content=file_bytes,
            headers={"Content-Type": content_type},
        )
        resp.raise_for_status()
        return resp.json()

    # ------ Photo Avatar ------

    async def create_photo_group(self, name: str, image_key: str) -> dict:
        resp = await self.client.post(
            f"{API_BASE}/v2/photo_avatar/avatar_group/create",
            json={"name": name, "image_key": image_key},
        )
        resp.raise_for_status()
        return resp.json()

    async def train_photo_avatar(self, group_id: str) -> dict:
        resp = await self.client.post(
            f"{API_BASE}/v2/photo_avatar/train",
            json={"group_id": group_id},
        )
        resp.raise_for_status()
        return resp.json()

    # ------ Video ------

    async def generate_video(self, payload: dict) -> dict:
        resp = await self.client.post(
            f"{API_BASE}/v2/video/generate",
            json=payload,
        )
        resp.raise_for_status()
        return resp.json()

    async def get_video_status(self, video_id: str) -> dict:
        resp = await self.client.get(
            f"{API_BASE}/v1/video_status.get",
            params={"video_id": video_id},
        )
        resp.raise_for_status()
        return resp.json()


heygen = HeyGenClient()
