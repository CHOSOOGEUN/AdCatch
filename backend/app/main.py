"""
SNAP 프로젝트 - 백엔드 메인 애플리케이션
불법 광고물 탐지 및 민원 자동 처리 시스템
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.config import settings
from app.api import auth, reports, points, admin
from app.database import Base, engine


# 애플리케이션 시작/종료 이벤트
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 시작 시 실행
    print("🚀 SNAP 백엔드 서버 시작")
    yield
    # 종료 시 실행
    print("🛑 SNAP 백엔드 서버 종료")


# FastAPI 앱 초기화
app = FastAPI(
    title="SNAP API",
    description="스마트 불법광고 적발 및 민원 자동 처리 시스템",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB 테이블 생성 (개발용, 프로덕션은 Alembic 사용)
Base.metadata.create_all(bind=engine)

# API 라우터 등록
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(reports.router, prefix="/api/v1/reports", tags=["Reports"])
app.include_router(points.router, prefix="/api/v1/points", tags=["Points"])
app.include_router(admin.router, prefix="/api/v1/admin", tags=["Admin"])


# 헬스 체크 엔드포인트
@app.get("/health")
async def health_check():
    """서버 상태 확인"""
    return {
        "status": "healthy",
        "service": "SNAP Backend",
        "version": "0.1.0",
    }


# 루트 엔드포인트
@app.get("/")
async def root():
    """API 정보"""
    return {
        "name": "SNAP API",
        "description": "불법 광고물 탐지 및 민원 자동 처리 시스템",
        "docs": "/docs",
        "redoc": "/redoc",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
    )
