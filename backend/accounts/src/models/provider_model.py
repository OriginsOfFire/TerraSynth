from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.models.base_model import BaseModel


class Provider(BaseModel):
    __tablename__ = 'providers'

    name = Column(String(64), unique=True, nullable=False)
    provider_name = Column(String(64), nullable=False)
    configurations = relationship('Configuration', back_populates='provider')