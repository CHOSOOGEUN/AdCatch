"""
포인트 관련 Pydantic 스키마
"""

from pydantic import BaseModel, Field
from datetime import datetime


class PointBase(BaseModel):
    """기본 포인트 정보"""

    amount: int = Field(..., description="포인트 액")
    type: str = Field(
        ...,
        description="포인트 타입 (신고접수, 불법확정, 완료보너스)",
    )


class PointCreate(PointBase):
    """포인트 생성"""

    user_id: int = Field(..., description="사용자 ID")
    description: str = Field(..., description="설명")


class PointResponse(PointBase):
    """포인트 응답"""

    id: int = Field(..., description="포인트 내역 ID")
    user_id: int = Field(..., description="사용자 ID")
    description: str = Field(..., description="설명")
    created_at: datetime = Field(..., description="지급 일시")

    class Config:
        from_attributes = True
