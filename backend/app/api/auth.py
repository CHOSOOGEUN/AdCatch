from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import create_access_token, verify_password
from app.database import get_db
from app.models.models import Admin
from app.schemas.schemas import AdminLogin, TokenResponse

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=TokenResponse)
async def login(body: AdminLogin, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Admin).where(Admin.email == body.email))
    admin = result.scalar_one_or_none()

    if not admin or not verify_password(body.password, admin.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="이메일 또는 비밀번호가 올바르지 않습니다.")

    token = create_access_token({"sub": str(admin.id), "email": admin.email})
    return TokenResponse(access_token=token)
