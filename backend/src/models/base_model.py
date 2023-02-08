from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.sql.functions import now, current_timestamp

from src.core.db.db import Base


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, index=True, primary_key=True)
    created_at = Column(DateTime, server_default=now())
    updated_at = Column(DateTime, server_default=now(), onupdate=current_timestamp())
