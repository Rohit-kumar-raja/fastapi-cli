import os
from pathlib import Path
import typer

from .startproject import create_file
from ..content.startproject import   get_helper_utilities_content,  get_urls_contant, get_welcome_controller_contant
from ..fpcli_settings import app_folder

def makeapp_with_folder(base_dir: str):
    """Creates the folder and file structure."""
    folders = [
        "utils",
        "views",
        "test",
        "schemas",
        "models",
        "services",
      
    ]

    files = {
        f"{base_dir}/urls.py": "# all routes file\n"+get_urls_contant(),
        f"{base_dir}/utils/__init__.py": "# Utility functions \n\n"+get_helper_utilities_content(),
        f"{base_dir}/views/welcome_views.py": "#Welcome Controller  "+get_welcome_controller_contant(),
        f"{base_dir}/models/__init__.py": "",
        f"{base_dir}/test/__init__.py": "",
        f"{base_dir}/services/__init__.py": "",

    }

    # Create folders
    for folder in folders:
        os.makedirs(f"{base_dir}/{folder}", exist_ok=True)

    # Create files
    for file, content in files.items():
        create_file(file, content)
    
   

