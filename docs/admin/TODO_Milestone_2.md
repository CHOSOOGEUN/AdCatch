# GateGuard — Milestone 2.0 (Blitz Action) - 실전 연동 및 대시보드

---

## 윤효정 (AI) [High Priority] 🚧
- [ ] YOLOv11 / Supervision 기반 추론 파이프라인 실체화
- [ ] 다중 객체 추적(ByteTrack) 및 ID 유지 테스트 수행
- [ ] 얼굴 블러 비식별화 로직 고도화 및 S3 업로드 연동
- [ ] 추론 결과를 백엔드 `POST /api/events` 로 전송하는 파이프라인 구축

---

## 이지현 (프론트엔드) [High Priority] 🚧
- [ ] 실시간 이벤트 카드 UI 및 WebSocket 알림 연동 테스트
- [ ] 개찰구별 실시간 CCTV 영상 스트리밍 레이아웃 구현
- [ ] 알림 클릭 시 해당 이벤트 영상 클립 팝업 재생 기능 연동
- [ ] ECharts를 활용한 일별/시간별 통계 대시보드 시각화

---

## 김민지 (DB) [Middle Priority] 🚧
- [ ] 실서비스 운영을 위한 시계열 데이터 추가 인덱싱 검수
- [ ] 누적 데이터 증가 시 벤치마킹 테스트 및 성능 최적화 보강
- [ ] PostgreSQL 사용자 권한 분리 및 보안 설정 강화

---

## 이동근 · 최태양 (인프라) [High Priority] 🚧
- [ ] Nginx 설정 최적화 및 HTTPS 정식 도메인 연결 (SSL)
- [ ] Docker Log Rotation 정책 적용 및 리소스 모니터링 구축
- [ ] Celery + Redis 비동기 태스크 큐 안정성 점검 및 모니터링

---

## 조수근 (백엔드) [Middle Priority] 🚧
- [ ] AI 추론 데이터 수신 및 실시간 브로드캐스트 안정성 고도화
- [ ] S3 영상 저장 및 조회 전용 Presigned URL 발급 로직 적용
- [ ] 관리자 행동 로깅 및 대시보드 API 추가 엔드포인트 설계

---

## M2 마일스톤 관리 전략
- [ ] **AI 파이프라인 실시간성 확보**: 0.5초 이내 감지 및 알림 전송 목표.
- [ ] **통합 테스트**: AI -> Backend -> Frontend 로 이어지는 전 과정 시나리오 검증.
- [ ] **문서 관리**: 상세 기술 변경 사항은 `docs/technical/`에 드라이하게 기록.
