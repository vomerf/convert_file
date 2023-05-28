from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.core.db import get_session
from app.models.models import Record

router = APIRouter()


@router.get('/record/')
def upload_record(
    id: str,
    user: int,
    session: Session = Depends(get_session)
) -> FileResponse:
    record = session.query(Record).where(
        Record.id == id, Record.customer_user_id == user).scalar()
    return FileResponse(
        path=record.path_to_record,
        filename='лучшая-музычка.mp3',
        media_type='multipart/form-data'
    )
