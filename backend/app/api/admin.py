"""
관리자 API 엔드포인트
- 신고 검수 및 확정
- 통계 조회
- 민원 접수
- 처리 현황 추적
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db


router = APIRouter()


@router.get("/reports/pending", response_model=List[dict])
async def get_pending_reports(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    """
    검수 대기 중인 신고 목록 조회

    Args:
        skip: 건너뛸 개수
        limit: 조회할 개수

    Returns:
        대기 중인 신고 목록
    """
    # TODO: 대기 중인 신고 조회 로직 구현
    return [
        {
            "id": 1,
            "user_id": 1,
            "image_url": "s3://snap-images/report-001.jpg",
            "category": "불법금융",
            "confidence": 0.95,
            "ai_result": {
                "detected": True,
                "bbox": [10, 20, 100, 150],
                "extracted_text": {
                    "phone": "010-1234-5678",
                    "company": "대출금융",
                },
            },
            "created_at": "2024-03-25T10:30:00",
        }
    ]


@router.post("/reports/{report_id}/confirm")
async def confirm_report(
    report_id: int,
    is_illegal: bool,
    comment: str = None,
    db: Session = Depends(get_db),
):
    """
    신고 확정 (불법/정상)

    Args:
        report_id: 신고 ID
        is_illegal: 불법 여부
        comment: 관리자 코멘트

    Returns:
        {
            "success": true,
            "report_id": 1,
            "status": "confirmed",
            "points_awarded": 100
        }
    """
    # TODO: 신고 확정 로직 구현
    return {
        "success": True,
        "report_id": report_id,
        "status": "confirmed",
        "points_awarded": 100 if is_illegal else 0,
    }


@router.post("/reports/{report_id}/submit-complaint")
async def submit_complaint(
    report_id: int,
    gu_code: str,  # 구청 코드
    db: Session = Depends(get_db),
):
    """
    민원 자동 접수

    Args:
        report_id: 신고 ID
        gu_code: 관할 구청 코드 (예: 11110 = 강남구)

    Returns:
        {
            "success": true,
            "complaint_id": "C20240325001",
            "status": "submitted"
        }
    """
    # TODO: 민원 자동 접수 로직 구현
    return {
        "success": True,
        "complaint_id": f"C{report_id}",
        "status": "submitted",
    }


@router.get("/statistics")
async def get_statistics(
    start_date: str = None,
    end_date: str = None,
    db: Session = Depends(get_db),
):
    """
    통계 조회

    Args:
        start_date: YYYY-MM-DD
        end_date: YYYY-MM-DD

    Returns:
        {
            "total_reports": 150,
            "illegal_count": 120,
            "confirmed_count": 145,
            "category_breakdown": {
                "불법금융": 50,
                "불법도박": 40,
                "성인": 20,
                "기타": 10
            },
            "avg_confidence": 0.92
        }
    """
    # TODO: 통계 조회 로직 구현
    return {
        "total_reports": 150,
        "illegal_count": 120,
        "confirmed_count": 145,
        "category_breakdown": {
            "불법금융": 50,
            "불법도박": 40,
            "성인": 20,
            "기타": 10,
        },
        "avg_confidence": 0.92,
    }


@router.get("/map-data")
async def get_map_data(
    db: Session = Depends(get_db),
):
    """
    지도 시각화용 데이터

    Returns:
        {
            "markers": [
                {
                    "id": 1,
                    "lat": 37.4979,
                    "lng": 127.0276,
                    "category": "불법금융",
                    "status": "confirmed"
                },
                ...
            ]
        }
    """
    # TODO: 지도 데이터 조회 로직 구현
    return {
        "markers": [
            {
                "id": 1,
                "lat": 37.4979,
                "lng": 127.0276,
                "category": "불법금융",
                "status": "confirmed",
            }
        ]
    }


@router.get("/dashboard")
async def get_dashboard(
    db: Session = Depends(get_db),
):
    """
    관리자 대시보드 종합 정보

    Returns:
        {
            "pending_count": 5,
            "today_reports": 12,
            "this_month_illegal": 45,
            "recent_reports": [...],
            "status_breakdown": {...}
        }
    """
    # TODO: 대시보드 데이터 조회 로직 구현
    return {
        "pending_count": 5,
        "today_reports": 12,
        "this_month_illegal": 45,
        "recent_reports": [],
        "status_breakdown": {
            "pending": 5,
            "confirmed": 45,
            "rejected": 3,
        },
    }
