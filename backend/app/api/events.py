from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.websocket import manager
from app.database import get_db
from app.models.models import Event, Notification
from app.schemas.schemas import EventCreate, EventResponse, EventStatusUpdate
from app.workers.tasks import upload_clip_task

router = APIRouter(prefix="/events", tags=["events"])


@router.get("/", response_model=list[EventResponse])
async def list_events(
    camera_id: int | None = None,
    status: str | None = None,
    limit: int = 50,
    db: AsyncSession = Depends(get_db),
):
    query = select(Event).order_by(Event.timestamp.desc()).limit(limit)
    if camera_id:
        query = query.where(Event.camera_id == camera_id)
    if status:
        query = query.where(Event.status == status)
    result = await db.execute(query)
    return result.scalars().all()


@router.post("/", response_model=EventResponse, status_code=201)
async def create_event(
    body: EventCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    무임승차 이벤트 등록 (AI 서버용)
    """
    event = Event(**body.model_dump())
    db.add(event)
    await db.flush()

    # 알림 레코드 생성
    notification = Notification(event_id=event.id)
    db.add(notification)

    await db.commit()
    await db.refresh(event)

    # 📡 [실시간 전송] 모든 연결된 웹소켓 클라이언트에게 이벤트 브로드캐스트
    await manager.broadcast({
        "type": "NEW_EVENT",
        "data": EventResponse.model_validate(event).model_dump()
    })

    # 비동기 S3 업로드 태스크
    if event.clip_url:
        upload_clip_task.delay(event.id, event.clip_url)

    return event


@router.patch("/{event_id}/status", response_model=EventResponse)
async def update_event_status(
    event_id: int,
    body: EventStatusUpdate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Event).where(Event.id == event_id))
    event = result.scalar_one_or_none()
    if not event:
        raise HTTPException(status_code=404, detail="이벤트를 찾을 수 없습니다.")
    event.status = body.status
    await db.commit()
    await db.refresh(event)
    return event
