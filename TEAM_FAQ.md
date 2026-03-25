# 🤔 SNAP 프로젝트 팀원 협업 가이드

> **조수근(백엔드팀장) 제공 | 2026년 3월 25일**

---

## 🔄 변경사항 (최신)

### 팀 역할 변경
- **기존**: 조수근이 모든 초기 세팅 후 팀원들에게 설명
- **변경**: **각 팀원이 자신의 분야에서 직접 담당**, 조수근은 **전분야 총괄+보조** 역할
- **효과**: 더 효율적인 병렬 개발, 빠른 의사결정

### 기술 결정 사항
- ✅ **서버 언어**: Python FastAPI (고정)
  - 최태양: Node.js 제안 → Python이 더 효율적 (AI 연동, 기술 스택 통일)
- ✅ **AI 연동**: 안전하게 분리된 인터페이스 사용 (분리만 돼 있다면 추가 조심 없음)
- ✅ **브랜칭 전략**: GitHub Flow (간단하고 효율적)
- ⏳ **탐지 카테고리 #1**: 회의 후 결정 필요

---

## 🌳 GitHub Flow 브랜칭 전략

> "체계적이고 복잡할수록 꼬인다" → GitHub Flow 선택!

### 브랜치 구조

```
main (배포 가능한 상태)
  ↓
feature/담당자-기능명 (기능 개발)
  ↓
PR (Pull Request)
  ↓
코드 리뷰 & Merge
  ↓
Release Tag (매 마일스톤마다)
```

### 브랜치 규칙

**Feature 브랜치 명명**
```
feature/담당자-기능명

예시:
- feature/최태양-auth
- feature/김민지-user-model
- feature/윤효정-yolo-detector
- feature/이지현-login-screen
```

**Main 브랜치**
- 언제든 배포 가능한 상태 유지
- 직접 commit 금지 (항상 PR 통해서만 merge)

### PR (Pull Request) 프로세스

**1️⃣ PR 올리기**
```bash
# feature 브랜치에서 작업
git checkout -b feature/담당자-기능명

# 커밋
git add .
git commit -m "기능 설명" (간단하게!)

# 푸시
git push origin feature/담당자-기능명

# GitHub에서 PR 생성 (main으로)
```

**2️⃣ 코드 리뷰 담당자**
- **일반 (백엔드/AI/DB/인프라)**: 조수근이 검토
- **프론트엔드**: 이지현님 + 조수근이 검토

**3️⃣ Review 후 Merge**
- Approve 받으면 "Squash and merge" 또는 "Rebase and merge"
- main으로 병합 후 feature 브랜치 삭제

### Commit 메시지

**간단하게!** (Conventional Commits 사용 금지)

```
✅ 좋은 예:
- "SMS 인증 로직 추가"
- "User ORM 모델 작성"
- "네이버맵 API 연동"
- "인증 토큰 검증 로직"

❌ 피해야 할 것:
- "fix(auth): add sms verification logic" (복잡)
- "update" (너무 애매함)
- "asdf" (뭐하는 건지 모름)
```

### Release & Tagging

**매 마일스톤마다**
```bash
# Tag 생성
git tag -a v0.1.0 -m "M1 - 환경 세팅 · 데이터 수집"
git push origin v0.1.0

Tag 규칙:
v0.1.0 (M1)
v0.2.0 (M2)
v0.3.0 (M3)
v0.4.0 (M4)
v0.5.0 (M5)
v1.0.0 (M6 - 경진대회)
```

### 실제 워크플로우

```
🔄 일반적인 진행 순서:

1. feature 브랜치 생성
   ↓
2. 작업 완료 (여러 commit 가능)
   ↓
3. PR 올리기
   ↓
4. 코드 리뷰 (담당자가 검토)
   ↓
5. 수정 요청받으면 반영 (추가 commit)
   ↓
6. Approve 받으면 Merge
   ↓
7. feature 브랜치 삭제
   ↓
8. 다음 기능 작업...
```

---

## 🚀 Claude Cowork를 통한 협업 방식

### 1️⃣ CLAUDE.md 읽기 (필수!)
**모든 팀원이 시작 전에 읽어야 할 것**

```
/Scrab/CLAUDE.md
├── 프로젝트 개요
├── 팀 구성 및 역할
├── 기술 스택
├── 개발 일정
└── 현재 상태
```

### 2️⃣ Claude 도구 활용 방법

#### **MCP (Model Context Protocol) 연결**
- 각자의 도구 연결 (Slack, GitHub, Google Drive 등)
- `search_mcp_registry` → 필요한 도구 찾기
- `suggest_connectors` → 연결 설정

#### **Claude Code에서**
```
1. Scrab 폴더 선택 (작업 폴더)
2. CLAUDE.md 읽기 (맥락)
3. 자기 역할의 파일 수정/작성
4. 변경사항 git에 커밋 (또는 공유)
```

#### **Claude Cowork에서**
```
1. "니가 할 수 있는 게 뭐야?" 물어보기
2. 파일 생성/수정 작업 자동화
3. 코드 실행 및 테스트
4. 문서 생성 (Word, Excel, PDF)
5. 자동화 작업 스케줄링
```

### 3️⃣ 협업 플로우

```
🔄 일반적인 협업 순서

1. CLAUDE.md 읽기
   ↓
2. 자신의 분야 작업 시작
   ↓
3. "어떻게 해?" 질문 → 이 문서 또는 조수근에게
   ↓
4. 파일 수정 후 GitHub에 푸시 (feature 브랜치)
   ↓
5. PR 올리기
   ↓
6. 조수근(또는 담당자)이 코드 리뷰
   ↓
7. Merge 후 마일스톤 진행
```

---

## 📋 목차

- [🔧 최태양 (서버)](#최태양-서버)
- [🤖 윤효정 (AI)](#윤효정-ai)
- [📖 일반 팀원들](#일반-팀원들)

---

## ⚠️ 중요한 규칙

### "이 문서에서만 확인 후 진행해!" 사항들

1. **조수근(팀장)에게 먼저 물어볼 것**
   - 기술적 의사결정 (언어, 라이브러리, 방식 변경)
   - 다른 팀과의 연동 (API 스펙, 인터페이스)
   - 미결정된 요구사항 (탐지 카테고리, 포인트 등)

2. **절대 건드리면 안 될 것**
   - ❌ 코드를 만들기 전에 먼저 물어보지 않기
   - ❌ 큰 결정을 독단적으로 내리지 않기
   - ❌ 다른 팀의 영역 임의로 건들기

3. **협업할 때**
   - ✅ 자신의 분야는 자유롭게
   - ✅ 모르는 건 빨리 물어보기
   - ✅ 진행 상황 공유하기

---

## 🔧 최태양 (서버)

> FastAPI 서버 세팅 및 백엔드 API 구현 담당
> **M1**: ~3월 30일 | **M3**: API 기본 완성

### 시작하기

**이미 준비된 것들** ✅
```
backend/
├── main.py          (FastAPI 앱, 라우터 등록 완료)
├── config.py        (환경 설정)
├── database.py      (DB 연결)
├── api/             (4개 라우터 스켈레톤)
│   ├── auth.py
│   ├── reports.py
│   ├── points.py
│   └── admin.py
├── schemas/         (Pydantic 스키마)
├── requirements.txt (Python 패키지)
└── .env.example    (환경 변수 템플릿)
```

### 필요한 작업
1. **로컬 개발 환경 세팅**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   cp .env.example .env
   ```

2. **FastAPI 실행**
   ```bash
   uvicorn app.main:app --reload
   # http://localhost:8000/docs (Swagger UI)
   ```

3. **각 라우터 함수 구현** (auth, reports, points, admin)
   - 지금은 스켈레톤 코드 (TODO 주석)
   - 실제 로직 채우기

4. **김민지와 협력**
   - ORM 모델 완성 후 import
   - DB 스키마 연동

---

## 🤖 윤효정 (AI)

> AI 모델 학습 및 파이프라인 백엔드 통합 담당
> **M2**: 라벨링 완료 | **M3**: 모델 학습 시작

### ⚠️ 중요: "건들면 안 되는 것들" (필독!)

**이 부분들은 조수근이 정의했으니 변경하지 말 것:**

```
❌ 절대 건드리면 안 됨:

1. AI 출력 JSON 스키마
   {
     "detected": bool,
     "category": str,
     "confidence": float,
     "bbox": [x1, y1, x2, y2],
     "extracted_text": {
       "phone": str,
       "company": str
     }
   }
   → 이 구조는 백엔드 API와 연결되어 있음!

2. 모델 입력 전처리
   - 이미지 크기 리사이징 규칙
   - 정규화 방식
   - 채널 순서 (RGB 고정)

3. 탐지 카테고리 (아직 미결정)
   - 현재: 1번 미정 → 조수근이 결정할 때까지 4개만 진행
   - 임의로 바꾸면 분류 모델 재학습 필요!

4. Roboflow 데이터셋
   - 데이터 수집/라벨링만 담당
   - 무단으로 삭제/수정 금지

✅ 자유롭게 할 수 있는 것:
- 모델 학습 및 최적화
- 성능 테스트
- Colab 환경 세팅
- 전처리 알고리즘 개선
```

### 파이프라인 구조

```
사진 입력 (JPG/PNG)
  ↓
[1] 전처리 (OpenCV)
  - 리사이징
  - 정규화
  - 얼굴 블러 처리
  ↓
[2] YOLOv8 탐지
  - 바운딩박스 추출
  ↓
[3] EfficientNet-B0 분류
  - 5개 카테고리 중 선택
  ↓
[4] EasyOCR 텍스트 추출
  - 전화번호, 업체명
  ↓
JSON 응답 (위 스키마 준수)
```

---

## 📖 일반 팀원들

### 🗄️ 김민지 (DB)

> 데이터베이스 스키마 및 ORM 모델 담당
> **M1**: ~3월 30일

#### DB 테이블 (5개)

| 테이블 | 용도 |
|--------|------|
| **users** | 사용자 정보 (phone_number, nickname, point_balance) |
| **phone_verifications** | SMS 인증 코드 (code, expires_at, is_verified) |
| **reports** | 신고 정보 (image_url, gps_lat/lng, ai_result, category, status) |
| **points** | 포인트 내역 (amount, type, description) |
| **admins** | 관리자 계정 (email, password) |

#### 해야 할 것
- SQLAlchemy ORM 모델 작성 (app/models/)
- 테이블 관계 정의 (1-to-Many)
- 최태양과 함께 API 스키마 확인

---

### 🏗️ 이동근 (인프라)

> Docker, AWS, CI/CD 담당
> **M1**: 로컬 개발 환경 | **M5**: 배포 환경

#### 지금 할 것

```bash
# Docker Compose 테스트
cd backend
docker-compose up -d

# 확인
docker-compose ps
docker logs snap-backend
```

**포함된 서비스**:
- PostgreSQL (DB)
- Redis (캐시 + 메시지 브로커)
- FastAPI (백엔드)
- Celery Worker (비동기 작업)
- Celery Beat (스케줄러)

---

### 📱 이지현 / 김유진 / 양은혜 (프론트엔드)

> React Native (사용자 앱) + React.js (관리자 웹)
> **M3**: 기본 화면 | **M4**: AI 연동 완성

#### API 확인하기

```
백엔드 시작 후:
http://localhost:8000/docs

4개 영역:
- /api/v1/auth      (로그인, SMS)
- /api/v1/reports   (신고 업로드)
- /api/v1/points    (포인트, 랭킹)
- /api/v1/admin     (관리자)
```

#### 앱 기능
- **사용자 앱**: 촬영 → 결과 확인 → 포인트 수령
- **관리자 웹**: 지도 시각화 → 신고 검수 → 민원 접수

---

## ✅ M1 체크리스트

**~3월 30일까지**

```
백엔드
- [x] 폴더 구조 ✅
- [x] FastAPI 기본 설정 ✅
- [x] API 라우터 스켈레톤 ✅
- [ ] ORM 모델 (김민지)
- [ ] 라우터 함수 구현 (최태양)

인프라
- [x] Docker/Compose ✅
- [ ] 로컬 테스트 실행 (이동근)

AI
- [ ] Roboflow 프로젝트 (윤효정)
- [ ] 초기 데이터 수집

프론트
- [ ] 프로젝트 초기화 (이지현팀)
- [ ] API 연동 계획
```

**마지막 업데이트**: 2026년 3월 25일 14:30
**다음 회의**: TBD
