from ..fpcli_settings import config_folder
import importlib.util

def get_settings():
    # Dynamically import settings
    settings_path = f"{config_folder}.settings"
    spec = importlib.util.find_spec(settings_path)
    if spec is None:
        raise ImportError(f"Settings module not found in {config_folder}")

    settings = importlib.import_module(settings_path)
    return settings.settings