from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from api.core.base import Base


class Email(Base):
    __tablename__ = "emails"

    id_email= Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey("users.id_user"))

    email = Column(String(320), nullable=False)
    is_active = Column(Boolean(), default=True, nullable=False)
    is_email_active = Column(Boolean(), default=False, nullable=False)

    date_validation= Column(DateTime)
    date_insert = Column(DateTime, server_default=func.now())
