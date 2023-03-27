from sqlalchemy import Column, String, Boolean, CheckConstraint
from sqlalchemy.orm import relationship

from src.models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    email = Column(String(128), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    full_name = Column(String(64), nullable=False)
    configurations = relationship('Configuration', back_populates='user')

    def __str__(self):
        return self.email
