import typer
import subprocess

def choose_database():
    """
    Choose a database to use for your project.
    """
    DATABASES = ["SQLite", "PostgreSQL", "MySQL", "MongoDB"]

    typer.echo(typer.style("Please select a database from the list below:",typer.colors.WHITE,blink=True,bg=typer.colors.BLUE, bold=True))
    for idx, db in enumerate(DATABASES, start=1):
        typer.echo(typer.style(f"{idx}. {db}",bold=True))
    
    choice = typer.prompt("Enter the number of your choice", type=int)

    if 1 <= choice <= len(DATABASES):
        selected_db = DATABASES[choice - 1]
        typer.echo(f"You have selected: {selected_db}")
    else:
        typer.echo("Invalid choice. Please run the command again and choose a valid option.")
    


def dependency_management():
    """
    Choose between uv, poetry, or None, and install the selected one.
    """
    typer.echo("Select a dependency manager to install:")
    typer.echo("1. uv")
    typer.echo("2. poetry")
    typer.echo("3. None (Do not install any manager)")
    
    choice = typer.prompt("Enter the number of your choice", type=int)

    if choice == 1:
        typer.echo("You selected uv.")
        try:
            typer.echo("Installing uv...")
            subprocess.run(["pip", "install", "uv"], check=True)
            subprocess.run(['uv','init'])
            subprocess.run(['uv','add', 'fastapi', 'uvicorn', 'fpcli', 'alembic'])
            typer.echo("uv installed successfully.")
        except subprocess.CalledProcessError:
            typer.echo("Failed to install uv. Please check your pip installation.")
    elif choice == 2:
        typer.echo("You selected poetry.")
        try:
            typer.echo("Installing poetry...")
            subprocess.run(["pip", "install", "poetry"], check=True)
            subprocess.run(['poetry','init'])
            subprocess.run(['poetry','install', 'fastapi', 'uvicorn', 'fpcli', 'alembic'])

            typer.echo("poetry installed successfully.")
        except subprocess.CalledProcessError:
            typer.echo("Failed to install poetry. Please check your pip installation.")
    elif choice == 3:
        typer.echo("You selected None. No dependency manager will be installed.")
    else:
        typer.echo("Invalid choice. Please run the command again and select a valid option.")
        raise typer.Exit()


