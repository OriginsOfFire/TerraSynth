from sqlalchemy import Column, Enum, ForeignKey
from sqlalchemy.orm import relationship, mapped_column

from src.core.enums import CloudTypeEnum
from src.models.base_model import BaseModel


class Configuration(BaseModel):
    __tablename__ = 'configurations'

    cloud_type = Column('cloud_type', Enum(CloudTypeEnum), nullable=False)

    user_id = mapped_column(ForeignKey('users.id'))
    user = relationship('User', back_populates='configurations', lazy='joined')
    provider_id = mapped_column(ForeignKey('providers.id'))
    provider = relationship('Provider', back_populates='configurations', lazy='joined')