import uuid

from sqlalchemy import UUID, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import relationship


@as_declarative()
class Base:
    """Базовая модель."""

    id = Column(Integer(), primary_key=True, autoincrement=True)

    __name__: str


class CustomUser(Base):

    __tablename__ = "customuser"
    name = Column(String(50), nullable=False)
    token = Column(String(36), unique=True, nullable=False)


class Record(Base):
    __tablename__ = "record"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    path_to_record = Column(String, nullable=False)
    customer_user_id = Column(Integer, ForeignKey(CustomUser.id), nullable=False)
    customer_user = relationship("CustomUser")