from src.core.managers.base_manager import CRUDManager
from src.models import Configuration


class ConfigurationManager(CRUDManager):
    table = Configuration
