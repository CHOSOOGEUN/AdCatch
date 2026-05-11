#!/bin/bash
# GateGuard 테스트 데이터 주입 스크립트
# 사용법: bash scripts/test_data.sh

BASE_URL="http://localhost:8001"
EMPLOYEE_ID="${1:-admin001}"
PASSWORD="${2:-admin1234}"

echo "======================================"
echo " GateGuard 테스트 데이터 주입"
echo "======================================"

# 1. 로그인 → 토큰 획득
echo ""
echo "[1/4] 로그인 중..."
TOKEN=$(curl -s -X POST "$BASE_URL/api/auth/login" \
  -H "Content-Type: application/json" \
  -d "{\"employee_id\": \"$EMPLOYEE_ID\", \"password\": \"$PASSWORD\"}" \
  | python3 -c "import sys, json; print(json.load(sys.stdin)['access_token'])" 2>/dev/null)

if [ -z "$TOKEN" ]; then
  echo "❌ 로그인 실패. 사원번호/비밀번호를 확인하세요."
  echo "   사용법: bash scripts/test_data.sh <사원번호> <비밀번호>"
  exit 1
fi
echo "✅ 로그인 성공"

AUTH="Authorization: Bearer $TOKEN"

# 2. 카메라 3개 등록
echo ""
echo "[2/4] 카메라 등록 중..."

CAM1=$(curl -s -X POST "$BASE_URL/api/cameras/" \
  -H "Content-Type: application/json" \
  -H "$AUTH" \
  -d '{"location": "1번 게이트", "station_name": "수원역"}')
CAM1_ID=$(echo $CAM1 | python3 -c "import sys,json; print(json.load(sys.stdin)['id'])" 2>/dev/null)

CAM2=$(curl -s -X POST "$BASE_URL/api/cameras/" \
  -H "Content-Type: application/json" \
  -H "$AUTH" \
  -d '{"location": "2번 게이트", "station_name": "수원역"}')
CAM2_ID=$(echo $CAM2 | python3 -c "import sys,json; print(json.load(sys.stdin)['id'])" 2>/dev/null)

CAM3=$(curl -s -X POST "$BASE_URL/api/cameras/" \
  -H "Content-Type: application/json" \
  -H "$AUTH" \
  -d '{"location": "1번 게이트", "station_name": "경기대역"}')
CAM3_ID=$(echo $CAM3 | python3 -c "import sys,json; print(json.load(sys.stdin)['id'])" 2>/dev/null)

echo "✅ 카메라 등록 완료: ID $CAM1_ID (수원역 1번), ID $CAM2_ID (수원역 2번), ID $CAM3_ID (경기대역 1번)"

# 3. 이벤트 10개 전송 (AI 엔드포인트 — 토큰 불필요)
echo ""
echo "[3/4] 무임승차 이벤트 전송 중..."

TYPES=("tailgating" "jumping" "emergency_door" "unknown")
CAMS=($CAM1_ID $CAM2_ID $CAM3_ID)
COUNT=0

for i in {1..10}; do
  TYPE=${TYPES[$((RANDOM % 4))]}
  CAM=${CAMS[$((RANDOM % 3))]}
  CONF=$(python3 -c "import random; print(round(random.uniform(0.65, 0.99), 2))")

  RES=$(curl -s -X POST "$BASE_URL/api/events/" \
    -H "Content-Type: application/json" \
    -d "{\"camera_id\": $CAM, \"confidence\": $CONF, \"event_type\": \"$TYPE\", \"track_id\": $i}")

  ID=$(echo $RES | python3 -c "import sys,json; print(json.load(sys.stdin).get('id','?'))" 2>/dev/null)
  echo "  → 이벤트 #$ID | 카메라 $CAM | 유형: $TYPE | 신뢰도: $CONF"
  COUNT=$((COUNT+1))
  sleep 0.3
done

echo "✅ 이벤트 $COUNT건 전송 완료"

# 4. 결과 확인
echo ""
echo "[4/4] 현재 DB 상태 확인..."
STATS=$(curl -s -X GET "$BASE_URL/api/events/stats" -H "$AUTH")
echo "  통계: $STATS"

echo ""
echo "======================================"
echo " 완료! 대시보드에서 데이터를 확인하세요."
echo " → http://localhost:5173/dashboard"
echo "======================================"
