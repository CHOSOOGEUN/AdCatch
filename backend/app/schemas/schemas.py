from datetime import datetime

from pydantic import BaseModel, EmailStr


# ── Auth ──────────────────────────────────────────────────────────────────────

class AdminLogin(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ── Camera ────────────────────────────────────────────────────────────────────

class CameraCreate(BaseModel):
    location: str
    station_name: str


class CameraResponse(BaseModel):
    id: int
    location: str
    station_name: str
    is_active: bool

    model_config = {"from_attributes": True}


# ── Event ─────────────────────────────────────────────────────────────────────

class EventCreate(BaseModel):
    camera_id: int
    clip_url: str | None = None
    track_id: int | None = None
    confidence: float | None = None


class EventResponse(BaseModel):
    id: int
    camera_id: int
    timestamp: datetime
    clip_url: str | None
    track_id: int | None
    confidence: float | None
    status: str

    model_config = {"from_attributes": True}


class EventStatusUpdate(BaseModel):
    status: str  # confirmed | dismissed


# ── Notification ──────────────────────────────────────────────────────────────

class NotificationResponse(BaseModel):
    id: int
    event_id: int
    sent_at: datetime
    read_at: datetime | None

    model_config = {"from_attributes": True}
