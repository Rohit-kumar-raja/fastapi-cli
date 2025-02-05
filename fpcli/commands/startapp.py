import os
from pathlib import Path
from click import Option, option
import typer

from ..function.startproject import create_file
from ..content.startproject import   get_helper_utilities_content,  get_urls_contant, get_welcome_controller_contant
from ..function.makeapp import makeapp_with_folder
from .basic import app
from ..fpcli_settings import app_folder

def create_folder_structure(base_dir: str):
    """Creates the folder and file structure."""
    folders = [
    ]

    files = {
        f"{base_dir}/__init__.py": "# Configuration file",
        f"{base_dir}/urls.py": "# all routes file\n"+get_urls_contant(),
        f"{base_dir}/utils.py": "# Utility functions \n\n"+get_helper_utilities_content(),
        f"{base_dir}/views.py": "#Welcome View  "+get_welcome_controller_contant(),
        f"{base_dir}/schemas.py": "",
        f"{base_dir}/test.py": "",
        f"{base_dir}/models.py": "",

    }

    # Create folders
    for folder in folders:
        os.makedirs(f"{base_dir}/{folder}", exist_ok=True)

    # Create files
    for file, content in files.items():
        create_file(file, content)
    
@app.command("startapp")
def startapp(name: str, f:bool=typer.Option(False, help="if you passs the --f then you will get the structure into with folder")):
    """Create a new APP Structure. --f to Create APP with Folder structure"""
    base_dir = Path(f"{app_folder}/{name}").resolve()
    if f:
        makeapp_with_folder(base_dir)
    else:
        create_folder_structure(str(base_dir))
        typer.echo(f"App '{name}' created successfully at {base_dir}!")

