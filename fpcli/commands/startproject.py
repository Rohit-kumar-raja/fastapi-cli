import os
from pathlib import Path
import typer
from .basic import app


def create_file(path: str, content: str = ""):
    """Creates a file with the given content."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as file:
        file.write(content)

def create_folder_structure(base_dir: str):
    """Creates the folder and file structure."""
    folders = [
        "app/commands",
        "app/helpers",
        "app/http/v1/controllers",
        "app/http/v1/responses",
        "app/http/v1/validators",
        "app/middleware",
        "app/models",
        "app/services",
        "config",
        "database/migrations",
        "database/seeders",
        "routes",
        "storage/cli/commands",
        "storage/cli/content",
        "storage/cli/function",
        "storage/logs",
        "tests"
    ]

    files = {
        f"{base_dir}/app/commands/__init__.py": "",
        f"{base_dir}/app/config.py": "# Configuration file",
        f"{base_dir}/app/helpers/__init__.py": "",
        f"{base_dir}/app/helpers/utils.py": "# Utility functions",
        f"{base_dir}/app/http/v1/controllers/__init__.py": "",
        f"{base_dir}/app/http/v1/responses/__init__.py": "",
        f"{base_dir}/app/http/v1/validators/__init__.py": "",
        f"{base_dir}/app/middleware/__init__.py": "",
        f"{base_dir}/app/models/__init__.py": "",
        f"{base_dir}/app/services/__init__.py": "",
        f"{base_dir}/config/__init__.py": "",
        f"{base_dir}/config/database.py": "# Database Configuration",
        f"{base_dir}/config/logging.py": "# Logging Configuration",
        f"{base_dir}/config/settings.py": "# Settings Configuration",
        f"{base_dir}/database/__init__.py": "",
        f"{base_dir}/database/migrations/__init__.py": "",
        f"{base_dir}/database/migrations/migration_file.py": "# Migration File",
        f"{base_dir}/database/run_seeders.py": "# Run Seeders",
        f"{base_dir}/database/seeders/__init__.py": "",
        f"{base_dir}/routes/api.py": "# API Routes",
        f"{base_dir}/routes/channel.py": "# Channel Routes",
        f"{base_dir}/routes/console.py": "# Console Routes",
        f"{base_dir}/server.py": "# Entry point",
        f"{base_dir}/storage/logs/app.log": "",
        f"{base_dir}/storage/logs/error.log": "",
        f"{base_dir}/tests/__init__.py": "",
        f"{base_dir}/README.md": "# Project Readme",
        f"{base_dir}/Dockerfile": "# Dockerfile",
        f"{base_dir}/docker-compose.yml": "# Docker Compose Configuration",
        f"{base_dir}/pyproject.toml": "# pyproject.toml",
        f"{base_dir}/Guidelines.md": "# Guidelines",
    }

    # Create folders
    for folder in folders:
        os.makedirs(f"{base_dir}/{folder}", exist_ok=True)

    # Create files
    for file, content in files.items():
        create_file(file, content)
    
@app.command()
def startproject(name: str):
    """Create a new project structure."""
    base_dir = Path(name).resolve()
    os.makedirs(base_dir, exist_ok=True)
    create_folder_structure(str(base_dir))
    typer.echo(f"Project '{name}' created successfully at {base_dir}!")

