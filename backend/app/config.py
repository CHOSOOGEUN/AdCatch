"""
애플리케이션 설정
"""

from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """애플리케이션 전역 설정"""

    # 환경
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    SECRET_KEY: str = "your-secret-key-change-in-production"

    # 데이터베이스
    DATABASE_URL: str = "postgresql://postgres:password@localhost:5432/snap_db"

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    # AWS S3
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""
    AWS_REGION: str = "ap-northeast-2"
    S3_BUCKET_NAME: str = "snap-images"

    # Naver SENS (SMS)
    NAVER_SENS_SERVICE_ID: str = ""
    NAVER_SENS_ACCESS_KEY: str = ""
    NAVER_SENS_SECRET_KEY: str = ""
    NAVER_SENS_PHONE_NUMBER: str = ""

    # JWT
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    ALGORITHM: str = "HS256"

    # AI 모델
    MODEL_YOLO_PATH: str = "models/yolov8n.pt"
    MODEL_CLASSIFIER_PATH: str = "models/efficientnet_b0.pth"
    OCR_LANGUAGES: str = "ko,en"

    # 관리자
    ADMIN_EMAIL: str = "admin@example.com"
    ADMIN_PASSWORD: str = "admin-password"

    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:3001",
        "http://localhost:8081",
    ]

    # Celery
    CELERY_BROKER_URL: str = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/2"

    class Config:
        env_file = ".env"
        case_sensitive = True


# 전역 설정 인스턴스
settings = Settings()
