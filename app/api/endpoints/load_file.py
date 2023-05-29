from pathlib import Path

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.db import get_session
from app.models.models import CustomUser, Record
from app.service.convert_from_wav_to_mp3 import convert
from app.service.save_file_in_local_storage import save_in_local_storage
from app.validation.check_when_save_file import check_file

router = APIRouter()


@router.post('/load_file')
def load_file(
        id: int = Form(...),
        token: str = Form(...),
        record: UploadFile = File(...),
        session: Session = Depends(get_session)
) -> dict:
    file_location = f"files/{record.filename}"
    if not session.query(CustomUser).where(
            CustomUser.id == id, CustomUser.token == token).count():
        raise HTTPException(
            status_code=404,
            detail='Такого пользователя не существует или у него нет доступа'
        )
    check_file(record)
    save_in_local_storage(record, file_location)
    dst = convert(record)
    path_in_root = Path(__file__).resolve().parent.parent
    path_in_file = Path(path_in_root, dst)
    create_record = Record(path_to_record=str(path_in_file), customer_user_id=id)
    try:
        session.add(create_record)
        session.commit()
        session.refresh(create_record)
    except Exception:
        session.rollback()
    url = (f'http://'
           f'{settings.localhost}:{settings.local_port}/'
           f'record?id={create_record.id}&user={id}')
    return {'url_for_for_load_file': url}
