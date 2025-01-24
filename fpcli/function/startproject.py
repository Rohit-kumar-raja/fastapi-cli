import os
def create_file(path: str, content: str = ""):
    """Creates a file with the given content."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as file:
        file.write(content)



def create_and_activate_env(project_path:str):
    os.chdir(path=project_path)
    os.system("python3 -m venv .venv")
    os.system(". .venv/bin/activate")