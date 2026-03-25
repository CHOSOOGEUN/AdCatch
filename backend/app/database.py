"""
데이터베이스 연결 및 설정
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator

from app.config import settings

# SQLAlchemy 엔진 생성
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    pool_pre_ping=True,  # 연결 테스트
)

# 세션 팩토리
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# 선언적 기본 클래스
Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    """
    데이터베이스 세션 의존성

    FastAPI 경로 함수에서 사용:
    @router.get("/")
    async def get_data(db: Session = Depends(get_db)):
        # db 사용
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
