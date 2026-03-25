"""
포인트 관련 API 엔드포인트
- 포인트 잔액 조회
- 포인트 내역 조회
- 랭킹 조회
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.point import PointResponse


router = APIRouter()


@router.get("/balance")
async def get_point_balance(
    db: Session = Depends(get_db),
):
    """
    사용자 포인트 잔액 조회

    Returns:
        {
            "user_id": 1,
            "balance": 150,
            "currency": "point"
        }
    """
    # TODO: 포인트 잔액 조회 로직 구현
    return {
        "user_id": 1,
        "balance": 150,
        "currency": "point",
    }


@router.get("/history", response_model=List[PointResponse])
async def get_point_history(
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db),
):
    """
    포인트 내역 조회

    Args:
        skip: 건너뛸 개수
        limit: 조회할 개수

    Returns:
        포인트 내역 목록
    """
    # TODO: 포인트 내역 조회 로직 구현
    return [
        {
            "id": 1,
            "user_id": 1,
            "amount": 30,
            "type": "신고접수",
            "description": "신고 ID #123",
            "created_at": "2024-03-25T10:30:00",
        },
        {
            "id": 2,
            "user_id": 1,
            "amount": 70,
            "type": "불법확정",
            "description": "신고 ID #123 확정",
            "created_at": "2024-03-25T12:00:00",
        },
    ]


@router.get("/ranking")
async def get_ranking(
    limit: int = 10,
    db: Session = Depends(get_db),
):
    """
    포인트 랭킹 조회

    Args:
        limit: 상위 몇 명까지 (기본: 10)

    Returns:
        {
            "ranking": [
                {
                    "rank": 1,
                    "user_id": 5,
                    "nickname": "포인트킹",
                    "balance": 5000,
                    "report_count": 50
                },
                ...
            ]
        }
    """
    # TODO: 랭킹 조회 로직 구현
    return {
        "ranking": [
            {
                "rank": 1,
                "user_id": 5,
                "nickname": "포인트킹",
                "balance": 5000,
                "report_count": 50,
            },
            {
                "rank": 2,
                "user_id": 3,
                "nickname": "적발꾼",
                "balance": 4500,
                "report_count": 45,
            },
        ]
    }
