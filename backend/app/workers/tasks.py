import boto3
from botocore.exceptions import ClientError

from app.core.config import settings
from app.workers.celery_app import celery_app


@celery_app.task(bind=True, max_retries=3, default_retry_delay=10)
def upload_clip_task(self, event_id: int, local_path: str):
    """무임승차 영상 클립을 S3에 업로드합니다."""
    try:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION,
        )
        s3_key = f"clips/event_{event_id}.mp4"
        s3.upload_file(local_path, settings.AWS_S3_BUCKET, s3_key)
        return {"event_id": event_id, "s3_key": s3_key}
    except (ClientError, FileNotFoundError) as exc:
        raise self.retry(exc=exc)
