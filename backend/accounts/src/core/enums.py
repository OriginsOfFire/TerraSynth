import enum


class CloudTypeEnum(str, enum.Enum):
    AWS = 'AWS'
    AZURE = 'Azure'
    GCP = 'GCP'
