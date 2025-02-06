from .basic import app
import subprocess

@app.command("shell")
def shell():
    """Open an interactive Python shell"""
    # Setup any context or objects you need available in the shell
    subprocess.run(['python'])


