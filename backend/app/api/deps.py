from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import decode_access_token
from app.database import get_db
from app.models.models import Admin

# OAuth2 스키마 설정 (로그인 경로 필수 지정)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


async def get_current_admin(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
) -> Admin:
    """
    [최적화 v2] 헤더에서 토큰을 추출하고, 만료 여부 및 실제 계정 존재 여부를 통합 검증합니다.
    """
    try:
        # 1. security.py의 통합 검증 로직 사용
        payload = decode_access_token(token)
        admin_id: str = payload.get("sub")
        if not admin_id:
            raise ValueError("ID 정보가 없는 토큰입니다.")
    except ValueError as e:
        # 비즈니스 로직(security.py)의 에러를 401 Unauthorized로 변환
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 2. DB 검증 및 캐싱
    result = await db.execute(select(Admin).where(Admin.id == int(admin_id)))
    admin = result.scalar_one_or_none()
    
    if not admin:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="계정을 찾을 수 없습니다."
        )

    return admin
