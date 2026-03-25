"""
인증 관련 API 엔드포인트
- 휴대폰 번호 인증 (SMS)
- 로그인 / 로그아웃
- 토큰 갱신
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional

from app.database import get_db
from app.schemas.user import UserLogin, UserResponse, TokenResponse


router = APIRouter()


@router.post("/send-sms", response_model=dict)
async def send_sms(phone_number: str, db: Session = Depends(get_db)):
    """
    휴대폰 번호로 SMS 인증 코드 전송

    Args:
        phone_number: 010-1234-5678 형식

    Returns:
        {
            "success": true,
            "message": "인증 코드가 전송되었습니다",
            "phone_number": "010-1234-5678"
        }
    """
    # TODO: SMS 발송 로직 구현
    return {
        "success": True,
        "message": "인증 코드가 전송되었습니다",
        "phone_number": phone_number,
    }


@router.post("/verify-sms", response_model=dict)
async def verify_sms(
    phone_number: str,
    code: str,
    db: Session = Depends(get_db),
):
    """
    SMS 인증 코드 검증

    Args:
        phone_number: 010-1234-5678 형식
        code: 6자리 인증 코드

    Returns:
        {
            "success": true,
            "message": "휴대폰 번호가 인증되었습니다"
        }
    """
    # TODO: SMS 코드 검증 로직 구현
    return {
        "success": True,
        "message": "휴대폰 번호가 인증되었습니다",
    }


@router.post("/login", response_model=TokenResponse)
async def login(
    phone_number: str,
    nickname: Optional[str] = None,
    db: Session = Depends(get_db),
):
    """
    사용자 로그인 (휴대폰 번호 기반)

    Args:
        phone_number: 010-1234-5678 형식
        nickname: 처음 로그인 시 닉네임 (선택)

    Returns:
        {
            "access_token": "eyJhbGc...",
            "refresh_token": "eyJhbGc...",
            "token_type": "bearer",
            "user": {...}
        }
    """
    # TODO: 로그인 로직 구현
    return {
        "access_token": "dummy-token",
        "refresh_token": "dummy-refresh-token",
        "token_type": "bearer",
        "user": {
            "id": 1,
            "phone_number": phone_number,
            "nickname": nickname,
            "point_balance": 0,
        },
    }


@router.post("/logout", response_model=dict)
async def logout():
    """
    사용자 로그아웃
    """
    return {"success": True, "message": "로그아웃되었습니다"}


@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(refresh_token: str):
    """
    액세스 토큰 갱신

    Args:
        refresh_token: Refresh 토큰

    Returns:
        새로운 액세스 토큰
    """
    # TODO: 토큰 갱신 로직 구현
    return {
        "access_token": "new-dummy-token",
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }
