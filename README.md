# AVATAR

Digital Twin Video Avatar — FastAPI wrapper over [HeyGen API](https://docs.heygen.com/) for creating and managing video avatars.

## Features

- List available avatars and voices
- Upload photos to create photo avatars
- Generate videos with avatar + voice + text
- Check video generation status
- Check remaining HeyGen credits

## Quick Start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # add your HEYGEN_API_KEY
uvicorn app.main:app --reload --port 8000
```

Open http://localhost:8000/docs for Swagger UI.

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Health check |
| GET | `/api/quota` | Remaining HeyGen credits |
| GET | `/api/avatars` | List all avatars |
| GET | `/api/voices` | List available voices |
| POST | `/api/avatars/upload` | Upload photo (JPEG/PNG) |
| POST | `/api/avatars/photo-group` | Create photo avatar group |
| POST | `/api/avatars/photo-group/{group_id}/train` | Train photo avatar |
| POST | `/api/videos/generate` | Generate video |
| GET | `/api/videos/{video_id}/status` | Video generation status |

## Example: Generate a Video

```bash
# 1. Find an avatar_id
curl http://localhost:8000/api/avatars

# 2. Find a voice_id
curl http://localhost:8000/api/voices

# 3. Generate video
curl -X POST http://localhost:8000/api/videos/generate \
  -H "Content-Type: application/json" \
  -d '{
    "avatar_id": "YOUR_AVATAR_ID",
    "voice": {
      "voice_id": "YOUR_VOICE_ID",
      "input_text": "Hello! I am your digital twin."
    }
  }'

# 4. Check status (use video_id from step 3)
curl http://localhost:8000/api/videos/VIDEO_ID/status
```

## Note on Digital Twin

A full Digital Twin (from 2+ min video) must be created via the HeyGen web interface at `app.heygen.com`. The API can create Photo Avatars (from photos) and generate videos with any existing avatar, including Digital Twins created on the website.
