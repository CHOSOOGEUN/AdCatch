"""
신고 관련 Pydantic 스키마
"""

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime


class AIResult(BaseModel):
    """AI 판별 결과"""

    detected: bool = Field(..., description="불법 광고물 탐지 여부")
    bbox: Optional[list] = Field(None, description="바운딩 박스 [x1, y1, x2, y2]")
    extracted_text: Optional[Dict[str, Any]] = Field(None, description="추출된 텍스트")


class ReportBase(BaseModel):
    """기본 신고 정보"""

    category: Optional[str] = Field(None, description="카테고리")
    latitude: Optional[float] = Field(None, description="GPS 위도")
    longitude: Optional[float] = Field(None, description="GPS 경도")


class ReportCreate(ReportBase):
    """신고 생성"""

    pass


class ReportResponse(ReportBase):
    """신고 응답"""

    id: int = Field(..., description="신고 ID")
    user_id: int = Field(..., description="사용자 ID")
    image_url: str = Field(..., description="S3 이미지 URL")
    confidence: float = Field(..., description="AI 신뢰도 (0.0~1.0)")
    status: str = Field(
        ...,
        description="상태 (pending: 대기, confirmed: 확정, rejected: 거절)",
    )
    ai_result: Optional[Dict[str, Any]] = Field(None, description="AI 판별 결과")
    created_at: datetime = Field(..., description="신고 일시")

    class Config:
        from_attributes = True
