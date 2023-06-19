from src.models.provider_model import Provider

from src.core.managers.base_manager import CRUDManager


class ProviderManager(CRUDManager):
    table = Provider
