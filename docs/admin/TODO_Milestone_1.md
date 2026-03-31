# GateGuard — Milestone 1.0 (Foundation) - 화요일(4/1)까지 목표

---

## 조수근 (백엔드) [Milestone v1.0 완료]
- [x] `backend/.env` 작성 후 `docker-compose up -d` → 서버 정상 실행 확인 (2026-03-27)
- [x] FastAPI /docs 엔드포인트 동작 확인
- [x] Alembic 세팅 → `alembic upgrade head` 테이블 생성 (2026-03-27)
- [x] `get_current_admin` 의존성 작성 → JWT 인증 적용 (2026-03-27)
- [x] WebSocket 실시간 통신 브로드캐스트 로직 구현 (2026-03-27)
- [x] 백엔드 코어 인프라 통합 완료 및 master 병합 (2026-03-27)

---

## 김민지 (DB) [Milestone v1.0 완료]
- [x] TimescaleDB 하이퍼테이블 변환 및 인력 최적화 (2026-03-31)
- [x] Alembic `env.py` 비동기 엔진 연동 (2026-03-27)
- [x] `seed.py` 작성 → 초기 관리자 및 카메라 데이터 주입 (2026-03-31)
- [x] 통합 시나리오 테스트 (Swagger 기반) 완료 (2026-03-31)

---

## 이동근 · 최태양 (인프라) [완료]
- [x] AWS EC2 (Ubuntu 24.04 LTS) 생성 및 보안 그룹 설정 (2026-03-28)
- [x] Docker / Docker Compose 운영 환경 구축
- [x] GitHub Actions CI/CD 파이프라인 구축 및 자동 배포 연동 (2026-03-28)
- [x] AWS S3 버킷 생성 및 IAM 권한 연동 (2026-03-30)
- [x] [M2 이관] Nginx 리버스 프록시 및 SSL 공식 적용
- [x] [M2 이관] Docker Log Rotation 설정

---

## 이지현 · 김유진 · 양은혜 (프론트엔드) [완료]
- [x] React + TypeScript + Shadcn UI 초기 환경 구축 (2026-03-30)
- [x] API 통신을 위한 Axios 인스턴스 및 라우팅 설정 (2026-03-30)
- [x] 로그인 페이지 및 토큰 관리 로직 구현 (2026-03-30)
- [x] 대시보드 기본 레이아웃 구성 (2026-03-30)

---

## 윤효정 (AI) [M2 이관]
- [ ] [M2 이관] YOLOv11 / Supervision 기반 추론 파이프라인 구축
- [ ] [M2 이관] 다중 객체 추적(ByteTrack) 및 ID 유지 테스트
- [ ] [M2 이관] 비식별화(얼굴 블러) 처리 로직 구현
- [ ] [M2 이관] Line Crossing 기반 무임승차 감지 구역 설정

> **사유**: 테스트 데이터 확보 및 M2 통합 단계 집중을 위한 일정 조정 (2026-03-31)

---

## 브랜치 최신 상태
```
master (Target)
├── feature/조수근-backend-complete-v1  (Merged)
├── feature/김민지-db-setup (Merged)
├── feature/이동근-infra-cicd (Merged)
├── feature/이지현-dashboard-ui (Merged)
└── feature/윤효정-yolo-pipeline (M2 Target)
```
