# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

AVATAR — Digital Twin Video Avatar wrapper over HeyGen API. Python/FastAPI stateless service.
Repository hosted at https://github.com/foodcost-uzb/AVATAR.

## Repository Structure

```
AVATAR/
├── app/
│   ├── main.py              # FastAPI app with lifespan
│   ├── config.py             # Settings from .env (pydantic-settings)
│   ├── heygen_client.py      # Async HTTP client for HeyGen API
│   ├── schemas.py            # Pydantic request/response models
│   └── routes/
│       ├── account.py        # GET /api/quota
│       ├── avatars.py        # Avatars: list, upload, photo-group, train
│       ├── voices.py         # GET /api/voices
│       └── videos.py         # Video generation + status
├── .env                      # HEYGEN_API_KEY (gitignored)
├── .env.example
├── requirements.txt
├── README.md
└── CLAUDE.md
```

## Development

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then fill in HEYGEN_API_KEY
uvicorn app.main:app --reload --port 8000
```

Swagger UI: http://localhost:8000/docs

## Key Design Decisions

- **No database** — HeyGen stores all state; this service is a stateless wrapper
- **Upload: raw bytes** — HeyGen expects raw bytes with Content-Type, not multipart. Our route accepts multipart from clients but forwards raw bytes
- **Polling over webhooks** — simpler for local dev; webhook support can be added later

## Git

- Main branch: `main`
- Remote: `origin` → https://github.com/foodcost-uzb/AVATAR.git
