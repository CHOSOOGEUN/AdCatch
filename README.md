# 🚨 SNAP - 스마트 불법광고 적발 및 민원 자동 처리 시스템

> **경기대학교 AI컴퓨터공학부 캡스톤디자인 2024**
>
> 스마트폰으로 불법 광고물을 찍으면 AI가 자동으로 탐지·분류하고, 관할 구청에 민원을 자동 접수하는 시스템입니다.
> 신고 시 지역화폐 포인트 지급 (앱테크 방식)

---

## 📋 프로젝트 개요

| 항목 | 내용 |
|------|------|
| **프로젝트명** | SNAP (미정) |
| **소속** | 경기대학교 AI컴퓨터공학부 캡스톤디자인 |
| **개발 기간** | 2024년 3월 ~ 6월 |
| **최종 발표** | 2024년 6월 13일 (경진대회) |

### 주요 기능
- 📸 **스마트폰 사진 촬영** → 불법 광고물 촬영
- 🤖 **AI 자동 탐지·분류** → YOLOv8 + EfficientNet-B0
- 📍 **자동 민원 접수** → GPS 위치 기반 관할 구청 접수
- 💰 **포인트 지급** → 신고 기본 30P + 확정 시 추가 70P + 완료 보너스 20P

---

## 👥 팀 구성

| 이름 | 학과 | 역할 |
|------|------|------|
| **조수근** | 컴퓨터공학과 | 백엔드팀장 · 백엔드 · AI 연동 보조 |
| 김민지 | 컴퓨터공학과 | 백엔드 |
| 이동근 | 컴퓨터공학과 | 백엔드 |
| 최태양 | 컴퓨터공학과 | 백엔드 |
| 이지현 | 컴퓨터공학과 | 프론트엔드 (사용자 앱) |
| 김유진 | 컴퓨터공학과 | 프론트엔드 (사용자 앱) |
| 양은혜 | 컴퓨터공학과 | 프론트엔드 (관리자 웹) |
| 윤효정 | 인공지능전공 | AI · 프론트엔드 (관리자 웹) |

---

## 🏗️ 서비스 구조

```
┌─────────────────────────────────────────────────────────────┐
│                      사용자 / 관리자                          │
└────────────────────────┬──────────────────────────────────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
    ┌───▼────┐      ┌───▼────┐      ┌──▼──────┐
    │ 사용자앱 │      │관리자웹│      │ AI서버 │
    │(React  │      │(React │      │(PyTorch│
    │Native) │      │.js)   │      │ YOLO)  │
    └───┬────┘      └───┬────┘      └──┬─────┘
        │                │               │
        └────────────────┼───────────────┘
                         │
                    ┌────▼──────────┐
                    │  FastAPI 서버  │
                    │  (Python 3.11) │
                    └────┬───────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
    ┌───▼────┐      ┌───▼────┐      ┌──▼──────┐
    │PostgreSQL│   │Redis/  │      │AWS S3   │
    │ (DB)   │   │Celery  │      │(이미지) │
    └────────┘      └────────┘      └─────────┘
```

### 1️⃣ 사용자 앱 (React Native)
- **플랫폼**: iOS + Android 동시 배포
- **기능**: 촬영 → AI 판별 결과 확인 → 포인트 수령 → 랭킹
- **사용자 플로우**: 단순하게 "찍기 + 포인트 받기"만

### 2️⃣ 관리자 웹 (React.js + Tailwind CSS)
- **대상**: 지자체 담당자 (PC 웹 대시보드)
- **기능**:
  - 지도 시각화 (네이버맵 API)
  - 분류 통계 (Chart.js)
  - AI 결과 검수 및 확정
  - 민원 자동 접수
  - 처리 현황 추적

### 3️⃣ 백엔드 서버 (FastAPI)
- **역할**: 사용자 앱 + 관리자 웹 공통 API 서버
- **AI 처리**: 서버 측 추론 (엣지 컴퓨팅 아님)
- **비동기 처리**: Celery + Redis

---

## 🛠️ 기술 스택

### AI / ML
```
- PyTorch
- YOLOv8 (Ultralytics)       — 불법 광고물 탐지 (바운딩박스)
- EfficientNet-B0             — 업종 분류 (5개 카테고리)
- EasyOCR                      — 텍스트 추출 (전화번호, 업체명)
- OpenCV                       — 전처리 + 얼굴 블러 처리
- 학습 환경: Google Colab Pro (GPU 미확정)
```

### Backend
```
- Python 3.11
- FastAPI                      — 웹 프레임워크
- Celery + Redis               — 비동기 작업 큐
- PostgreSQL                   — 관계형 DB
- SQLAlchemy + Alembic         — ORM + 마이그레이션
- AWS S3                        — 이미지 저장
- 네이버 SENS                   — SMS 인증
- JWT                           — 토큰 인증
```

### Frontend
```
- React Native                 — 사용자 앱 (iOS/Android)
- React.js + Tailwind CSS      — 관리자 웹
- 네이버맵 API                  — 지도 시각화
- Chart.js                      — 통계 차트
```

### Infrastructure
```
- Docker + Docker Compose      — 컨테이너화
- AWS EC2 + Nginx              — 호스팅
- GitHub Actions               — CI/CD 파이프라인
```

---

## 🤖 AI 파이프라인

```
📸 사진 입력
    ↓
🔍 YOLOv8 — 불법 광고물 탐지 (바운딩박스)
    ↓
📊 EfficientNet-B0 — 업종 분류
    (5개 카테고리: 불법금융, 불법도박, 성인, 기타불법, 정상)
    ↓
📝 EasyOCR — 텍스트 추출
    (전화번호, 업체명, URL 등)
    ↓
✅ 결과 반환 (JSON)
    {
      "detected": true,
      "category": "불법금융",
      "confidence": 0.95,
      "bbox": [x1, y1, x2, y2],
      "extracted_text": {
        "phone": "010-1234-5678",
        "company": "대출금융"
      }
    }
```

---

## 💰 포인트 시스템

| 시점 | 지급 포인트 | 설명 |
|------|-----------|------|
| 신고 접수 시 | 기본 30P | 사진 업로드 시 즉시 지급 |
| 불법 확정 시 | 추가 70P | 관리자 검수 후 확정 |
| 민원 처리 완료 시 | 보너스 20P | 구청 처리 완료 |
| **합계** | **최대 120P** | 신고당 최대 120포인트 |

- 관리자가 AI 결과 검수 후 최종 확정
- 초반엔 AI + 사람 검수 병행, 모델 고도화 후 자동화
- 포인트는 지역화폐 바우처·할인권으로만 사용 가능 (현금화 금지)

---

## 🎯 탐지 카테고리

| 카테고리 | 설명 | 예시 |
|---------|------|------|
| **불법 금융** | 대출, 사채 관련 광고 | "즉시 대출 가능 010-1234-5678" |
| **불법 도박** | 스포츠도박, 온라인카지노 광고 | "토토 배팅 사이트 가입" |
| **성인 광고** | 성인 서비스 관련 광고 | 성인 용품 스티커, 전단지 |
| **기타 불법** | 위의 3가지 외 불법 광고 | 위조품 판매, 불법 의약품 |
| **정상 광고** | 일반 상업 광고 | 카페, 음식점, 병원, 학원 |

---

## 📬 민원 처리 흐름

```
┌──────────┐
│사용자 앱  │  ← 찍기 + 포인트 수령 (끝!)
└────┬─────┘
     │
     ▼
┌──────────────────────────────────────┐
│       백엔드 / 관리자 대시보드         │
├──────────────────────────────────────┤
│ 1. AI 자동 판별                       │
│    ↓                                  │
│ 2. 관리자 검수 및 확정                │
│    ↓                                  │
│ 3. 민원 자동 접수 (구청 시스템)       │
│    ↓                                  │
│ 4. 처리 현황 추적 및 완료             │
└──────────────────────────────────────┘
```

**중요**: 민원 자동 접수는 관리자 측에서 처리하며, 사용자는 민원 과정에 개입하지 않습니다.

---

## 🗄️ 데이터베이스 스키마 (초안)

### users
- `id` (PK)
- `phone_number` (UK, 전화번호)
- `nickname` (사용자 이름)
- `point_balance` (누적 포인트)
- `created_at` (가입 일시)

### phone_verifications
- `id` (PK)
- `phone_number` (FK)
- `code` (SMS 인증 코드)
- `expires_at` (만료 시간)
- `is_verified` (검증 여부)

### reports
- `id` (PK)
- `user_id` (FK)
- `image_url` (S3 저장 경로)
- `gps_lat`, `gps_lng` (위치 정보)
- `ai_result` (JSON, AI 판별 결과)
- `confidence` (신뢰도)
- `category` (카테고리)
- `status` (상태: pending, confirmed, rejected)
- `created_at` (신고 일시)

### points
- `id` (PK)
- `user_id` (FK)
- `amount` (포인트 액)
- `type` (신고접수, 불법확정, 완료보너스)
- `description` (설명)
- `created_at` (지급 일시)

### admins
- `id` (PK)
- `email` (로그인 아이디)
- `password` (해시)
- `created_at` (가입 일시)

---

## 📅 개발 일정 (마일스톤)

| 마일스톤 | 기간 | 목표 |
|---------|------|------|
| **M1** | ~3월 30일 | ✅ 환경 세팅 · 데이터 수집 |
| **M2** | ~4월 6일 | 라벨링 완료 · 논문 초록 |
| **M3** | ~4월 17일 | 모델 첫 학습 · API 기본 완성 |
| **M4** | ~5월 1일 | 앱 · AI 연동 완성 |
| **M5** | ~6월 4일 | 전체 완성 · 최종 보고서 |
| **M6** | ~6월 13일 | 🎬 데모 · 경진대회 발표 |

### M1 체크리스트 (현재 진행 중)
- [x] 프로젝트 방향 확정
- [x] 기술 스택 확정
- [x] GitHub 레포 생성
- [x] README 작성
- [ ] 폴더 구조 세팅
- [ ] FastAPI 기본 구조 세팅
- [ ] DB 스키마 확정
- [ ] 데이터 수집 시작
- [ ] Roboflow 세팅

---

## 🚀 빠른 시작 (Quick Start)

### 필수 사항
- Python 3.11+
- PostgreSQL 13+
- Redis
- Node.js 16+ (프론트엔드)

### 백엔드 설치

```bash
# 1. 저장소 클론
git clone <repository-url>
cd snap-backend

# 2. 파이썬 가상환경 생성
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. 의존성 설치
pip install -r requirements.txt

# 4. 환경 변수 설정
cp .env.example .env
# .env 파일 수정 (DB 연결, AWS S3, 네이버 SENS 등)

# 5. DB 마이그레이션
alembic upgrade head

# 6. 개발 서버 실행
uvicorn main:app --reload
# API 문서: http://localhost:8000/docs
```

### 프론트엔드 설치 (사용자 앱)

```bash
cd snap-app
npm install
npm start  # 또는 expo start
```

### 프론트엔드 설치 (관리자 웹)

```bash
cd snap-admin
npm install
npm start
```

---

## 📁 프로젝트 구조

```
snap/
├── backend/                    # FastAPI 백엔드
│   ├── app/
│   │   ├── main.py            # 진입점
│   │   ├── api/               # API 엔드포인트
│   │   │   ├── auth.py        # 인증 (JWT, SMS)
│   │   │   ├── reports.py     # 신고 API
│   │   │   ├── points.py      # 포인트 API
│   │   │   └── admin.py       # 관리자 API
│   │   ├── models/            # SQLAlchemy ORM 모델
│   │   ├── schemas/           # Pydantic 스키마
│   │   ├── services/          # 비즈니스 로직
│   │   ├── ai/                # AI 파이프라인
│   │   └── config.py          # 설정
│   ├── alembic/               # DB 마이그레이션
│   ├── tests/                 # 단위/통합 테스트
│   ├── requirements.txt        # Python 의존성
│   └── Dockerfile
│
├── app/                       # React Native 사용자 앱
│   ├── src/
│   ├── package.json
│   └── app.json
│
├── admin/                     # React.js 관리자 웹
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── tailwind.config.js
│
├── docker-compose.yml         # 로컬 개발 환경
├── README.md                  # 이 파일
└── CLAUDE.md                  # 프로젝트 컨텍스트 (개발팀용)
```

---

## 📖 개발 가이드

### 코드 스타일
- **Python**: PEP 8 (Black으로 포맷)
- **JavaScript**: Prettier + ESLint
- **타입 힌팅**: 모든 함수에 타입 힌팅 필수

### 브랜치 전략
```
main                  # 배포 가능한 코드
├── develop          # 통합 브랜치
│   ├── feature/auth
│   ├── feature/ai-pipeline
│   └── bugfix/login-issue
```

### 커밋 메시지
```
feat(auth): SMS 인증 로직 추가
fix(reports): 이미지 업로드 버그 수정
docs(api): API 문서 업데이트
test(ai): YOLOv8 테스트 케이스 추가
```

### 테스트
```bash
# 백엔드 테스트
pytest tests/

# 커버리지 확인
pytest --cov=app tests/
```

---

## 🔒 법적 고려사항

- ✅ **얼굴 블러 처리**: 개인정보보호를 위해 OpenCV로 자동 처리
- ✅ **위치정보 수집**: 사용자 동의 필수 (앱 권한 요청)
- ✅ **민원 최종 제출**: 관리자가 직접 수행 (자동화 금지)
- ✅ **지역화폐 연동**: 지자체 공식 협약 필요
- ✅ **크롤링**: robots.txt 준수
- ✅ **포인트 정책**: 현금화 금지, 바우처·할인권만 가능

---

## 📞 연락처 & 문의

**백엔드팀장**: 조수근 (josoogen6017@gmail.com)

---

## 📄 라이센스

MIT License - 자세한 내용은 LICENSE 파일 참조

---

**마지막 업데이트**: 2024년 3월 25일
