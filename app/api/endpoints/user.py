import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db import get_session
from app.models.models import CustomUser
from app.schemas import UserCreate

router = APIRouter()


@router.post('/user/')
def create_user(
    user: UserCreate,
    session: Session = Depends(get_session)

):
    token = str(uuid.uuid4())
    user = CustomUser(**user.dict(), token=token)
    try:
        session.add(user)
        session.commit()
        session.refresh(user)
    except Exception:
        session.rollback()
    return {'id': user.id, 'token': token}
