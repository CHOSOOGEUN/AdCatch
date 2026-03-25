"""
신고 관련 API 엔드포인트
- 이미지 업로드 및 AI 판별
- 신고 목록 조회
- 신고 상세 조회
"""

from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.report import ReportCreate, ReportResponse


router = APIRouter()


@router.post("/upload", response_model=ReportResponse)
async def upload_report(
    file: UploadFile = File(...),
    latitude: float = None,
    longitude: float = None,
    db: Session = Depends(get_db),
):
    """
    이미지 업로드 및 AI 자동 판별

    Args:
        file: 이미지 파일 (JPG, PNG)
        latitude: GPS 위도
        longitude: GPS 경도

    Returns:
        {
            "id": 123,
            "user_id": 1,
            "image_url": "s3://snap-images/...",
            "category": "불법금융",
            "confidence": 0.95,
            "status": "pending",
            "ai_result": {...},
            "created_at": "2024-03-25T10:30:00"
        }
    """
    # TODO: 이미지 업로드 및 AI 판별 로직 구현
    return {
        "id": 1,
        "user_id": 1,
        "image_url": "s3://snap-images/report-001.jpg",
        "category": "불법금융",
        "confidence": 0.95,
        "status": "pending",
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


@router.get("/", response_model=List[ReportResponse])
async def get_reports(
    skip: int = 0,
    limit: int = 10,
    status: str = None,
    db: Session = Depends(get_db),
):
    """
    신고 목록 조회 (사용자별)

    Args:
        skip: 건너뛸 개수
        limit: 조회할 개수
        status: 필터 (pending, confirmed, rejected)

    Returns:
        신고 목록
    """
    # TODO: 신고 목록 조회 로직 구현
    return [
        {
            "id": 1,
            "user_id": 1,
            "image_url": "s3://snap-images/report-001.jpg",
            "category": "불법금융",
            "confidence": 0.95,
            "status": "pending",
            "ai_result": {},
            "created_at": "2024-03-25T10:30:00",
        }
    ]


@router.get("/{report_id}", response_model=ReportResponse)
async def get_report(
    report_id: int,
    db: Session = Depends(get_db),
):
    """
    신고 상세 조회

    Args:
        report_id: 신고 ID

    Returns:
        신고 상세 정보
    """
    # TODO: 신고 상세 조회 로직 구현
    return {
        "id": report_id,
        "user_id": 1,
        "image_url": "s3://snap-images/report-001.jpg",
        "category": "불법금융",
        "confidence": 0.95,
        "status": "pending",
        "ai_result": {},
        "created_at": "2024-03-25T10:30:00",
    }


@router.delete("/{report_id}")
async def delete_report(
    report_id: int,
    db: Session = Depends(get_db),
):
    """
    신고 삭제 (사용자)
    """
    # TODO: 신고 삭제 로직 구현
    return {"success": True, "message": "신고가 삭제되었습니다"}
