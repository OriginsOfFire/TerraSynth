from pydantic import BaseModel


class ConfigurationSchema(BaseModel):
    user_id: int
    name: str
    provider_id: str
    provider_version: str
