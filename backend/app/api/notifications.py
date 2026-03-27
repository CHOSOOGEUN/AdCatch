from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.models import Notification
from app.schemas.schemas import NotificationResponse

router = APIRouter(prefix="/notifications", tags=["notifications"])


@router.get("/", response_model=list[NotificationResponse])
async def list_notifications(unread_only: bool = False, db: AsyncSession = Depends(get_db)):
    query = select(Notification).order_by(Notification.sent_at.desc())
    if unread_only:
        query = query.where(Notification.read_at.is_(None))
    result = await db.execute(query)
    return result.scalars().all()


@router.patch("/{notification_id}/read", response_model=NotificationResponse)
async def mark_as_read(notification_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Notification).where(Notification.id == notification_id))
    notification = result.scalar_one_or_none()
    if notification and not notification.read_at:
        notification.read_at = datetime.utcnow()
        await db.commit()
        await db.refresh(notification)
    return notification
