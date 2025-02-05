import os
from pathlib import Path
import typer

from fpcli.commands.startapp_with_folder import startapp_with_folder_structure

from ..function.startproject import create_file
from ..content.startproject import   get_helper_utilities_content,  get_urls_contant, get_welcome_controller_contant
from .basic import app

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
def startapp(name: str, f:bool=typer.Option(False,help="if you pass the --f then you can create the App with folder structure")):
    """Create a new app structure."""
    if f:
        startapp_with_folder_structure(name=name)
    else:
        base_dir = Path(name).resolve()
        os.makedirs(base_dir, exist_ok=True)
        create_folder_structure(str(base_dir))
        typer.echo(f"App '{name}' created successfully at {base_dir}!")

