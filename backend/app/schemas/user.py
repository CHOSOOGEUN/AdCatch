"""
사용자 관련 Pydantic 스키마
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    """기본 사용자 정보"""

    phone_number: str = Field(..., description="휴대폰 번호 (010-1234-5678)")
    nickname: Optional[str] = Field(None, description="사용자 닉네임")


class UserCreate(UserBase):
    """사용자 생성"""

    pass


class UserLogin(BaseModel):
    """로그인 요청"""

    phone_number: str = Field(..., description="휴대폰 번호")
    code: Optional[str] = Field(None, description="SMS 인증 코드")
    nickname: Optional[str] = Field(None, description="처음 로그인 시 닉네임")


class UserResponse(UserBase):
    """사용자 응답"""

    id: int = Field(..., description="사용자 ID")
    point_balance: int = Field(default=0, description="포인트 잔액")
    created_at: datetime = Field(..., description="가입 일시")

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    """토큰 응답"""

    access_token: str = Field(..., description="액세스 토큰")
    refresh_token: str = Field(..., description="리프레시 토큰")
    token_type: str = Field(default="bearer", description="토큰 타입")
    user: Optional[UserResponse] = Field(None, description="사용자 정보")
