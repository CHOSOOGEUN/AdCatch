/**
 * @file Header.tsx
 * @description 대시보드 헤더 컴포넌트
 *
 * ## 기능
 * - 현재 경로 기반 페이지 타이틀 자동 표시
 * - AppContext의 wsConnected 상태에 따라 실시간 모니터링 뱃지 on(초록)/off(회색) 전환
 * - 톱니바퀴 아이콘 클릭 시 /settings 이동
 *
 * ## 주의사항
 * - 프로필 아바타는 하드코딩 ("관"), API 사용자 정보 연동 미구현
 *
 * ## TODO
 * - [ ] 프로필 아바타 → API 사용자 정보로 교체
 */

import { Settings } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import { useLocation, useNavigate } from "react-router-dom";
import { useAppContext } from "@/contexts/AppContext";

const pageTitles: Record<string, string> = {
  "/dashboard": "대시보드",
  "/stats": "통계 리포트",
  "/events": "전체 발생내역",
  "/settings": "설정",
};

export default function Header() {
  const { pathname } = useLocation();
  const navigate = useNavigate();
  const { wsConnected } = useAppContext();
  const title = pageTitles[pathname] ?? "대시보드";

  return (
    <header className="h-20 bg-white border-b border-gray-100 flex items-center justify-between px-8">
      {/* 페이지 타이틀 */}
      <h1 className="text-xl font-bold text-gray-900">{title}</h1>

      {/* 우측 영역 */}
      <div className="flex items-center gap-4">
        {/* 실시간 모니터링 뱃지 */}
        {wsConnected ? (
          <Badge className="bg-green-50 text-green-600 border border-green-200 font-medium gap-2 px-5 py-4 text-sm">
            <span className="w-2 h-2 rounded-full bg-green-500 animate-pulse inline-block" />
            실시간 모니터링 중
          </Badge>
        ) : (
          <Badge className="bg-gray-50 text-gray-400 border border-gray-200 font-medium gap-2 px-5 py-4 text-sm">
            <span className="w-2 h-2 rounded-full bg-gray-400 inline-block" />
            연결 끊김
          </Badge>
        )}

        {/* 설정 아이콘 */}
        <button
          onClick={() => navigate("/settings")}
          className="w-10 h-10 flex items-center justify-center rounded-xl hover:bg-gray-100 transition"
        >
          <Settings className="w-5 h-5 text-gray-500" />
        </button>

        {/* 프로필 아바타 */}
        <Avatar className="w-10 h-10">
          <AvatarFallback className="bg-[#4B73F7] text-white text-sm font-bold">
            관
          </AvatarFallback>
        </Avatar>
      </div>
    </header>
  );
}
