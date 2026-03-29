"""Enable TimescaleDB and create hypertable for events

Revision ID: b5521f8a3c10
Revises: a4437e459dcf
Create Date: 2026-03-28 17:00:00.000000

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "b5521f8a3c10"
down_revision: Union[str, None] = "a4437e459dcf"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1) TimescaleDB 확장 활성화
    op.execute("CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;")

    # 2) notifications FK 임시 제거 (events PK 변경을 위해)
    op.execute("ALTER TABLE notifications DROP CONSTRAINT notifications_event_id_fkey;")

    # 3) PK를 복합키(id, timestamp)로 변경 — 하이퍼테이블은 파티셔닝 컬럼이 PK에 포함되어야 함
    op.execute("ALTER TABLE events DROP CONSTRAINT events_pkey;")
    op.execute("ALTER TABLE events ADD PRIMARY KEY (id, timestamp);")

    # 4) events 테이블을 하이퍼테이블로 변환 (timestamp 컬럼 기준, 7일 단위 청크)
    op.execute(
        "SELECT create_hypertable('events', 'timestamp', "
        "chunk_time_interval => INTERVAL '7 days', "
        "migrate_data => true, "
        "if_not_exists => true);"
    )

    # 5) 하이퍼테이블은 파티셔닝 컬럼 없이 UNIQUE 인덱스를 지원하지 않으므로
    #    notifications → events FK는 복원하지 않음 (TimescaleDB 제약사항)
    #    대신 event_id에 일반 인덱스를 생성하여 조회 성능 확보
    op.execute("CREATE INDEX IF NOT EXISTS ix_notifications_event_id ON notifications (event_id);")


def downgrade() -> None:
    # 하이퍼테이블 → 일반 테이블 복원은 불가하므로 PK만 원복
    op.execute("ALTER TABLE events DROP CONSTRAINT events_pkey;")
    op.execute("ALTER TABLE events ADD PRIMARY KEY (id);")
    op.execute("DROP EXTENSION IF EXISTS timescaledb CASCADE;")
