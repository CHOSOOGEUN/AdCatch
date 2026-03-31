# GateGuard (게이트가드) - AI 기반 지하철 무임승차 자동 감지 시스템

지하철 개찰구 CCTV 영상을 실시간 분석하여 무임승차(뒤따라 들어가기, 점프, 비상문 이용 등)를 감지하고, 즉각적인 알림을 제공하는 통합 보안 관제 시스템입니다.

---

## 🏗️ 텍스트 기반 시스템 구조

### 관리자 대시보드 (React.js)
- 실시간 CCTV 영상 스트리밍 및 무임승차 감지 알림
- 이벤트 로그 기록 및 통계 현황 (ECharts 연동)

### 백엔드 서버 (FastAPI)
- JWT 기반 RBAC 지원 및 실시간 알림 전용 WebSocket 엔진
- 시계열 최적화 (TimescaleDB) 및 비동기 작업 처리 (Celery + Redis)

### 알림 모바일 앱 (React Native)
- 무임승차 감지 시 모바일 푸시 알림 전송

---

## 🛠️ 기술 스택 (Technology Stack)

- **Backend**: Python 3.11, FastAPI, SQLAlchemy, Alembic, PostgreSQL(TimescaleDB), Redis, Celery
- **AI/ML**: PyTorch, YOLOv11 (Ultralytics), ByteTrack, Supervision, OpenCV
- **Frontend**: React.js, Vite, TypeScript, Tailwind CSS, Shadcn UI
- **Infrastructure**: AWS (EC2, S3), GitHub Actions (CI/CD), Docker, Nginx

---

## 📊 현재 개발 진행 상황 (Status)

| 마일스톤 | 구분 | 상태 (2026-03-31) | 비고 |
| :--- | :--- | :--- | :--- |
| **Milestone 1.0** | 인프라 & 데이터베이스 기초 | **완료 (100%)** | AWS 배포 및 코어 DB 연동 완료 |
| **Milestone 2.0** | AI 연동 & 대시보드 구현 | **진행 중 (0%)** | YOLO 파이프라인 통합 착수 |

---

## 📂 프로젝트 문서 구조 (Documentation)

- **`docs/admin/`**: 마일스톤 관리 및 주간 보고서
- **`docs/technical/`**: API 가이드 및 시스템 최적화 보고서

---

## 🏁 라이선스 (License)

Copyright © 2026 GateGuard. All rights reserved.
