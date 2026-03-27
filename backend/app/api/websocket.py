import json
from typing import Any

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter(tags=["websocket"])


class ConnectionManager:
    def __init__(self):
        self._connections: list[WebSocket] = []

    async def connect(self, ws: WebSocket):
        await ws.accept()
        self._connections.append(ws)

    def disconnect(self, ws: WebSocket):
        self._connections.remove(ws)

    async def broadcast(self, data: dict[str, Any]):
        message = json.dumps(data, ensure_ascii=False, default=str)
        for ws in list(self._connections):
            try:
                await ws.send_text(message)
            except Exception:
                self._connections.remove(ws)


manager = ConnectionManager()


@router.websocket("/ws/events")
async def websocket_events(ws: WebSocket):
    await manager.connect(ws)
    try:
        while True:
            await ws.receive_text()  # keep-alive ping 수신
    except WebSocketDisconnect:
        manager.disconnect(ws)
