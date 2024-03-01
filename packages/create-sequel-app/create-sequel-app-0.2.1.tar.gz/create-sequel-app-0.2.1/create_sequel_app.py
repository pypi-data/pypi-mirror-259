import subprocess
import os
import click
import shutil
from pathlib import Path


# Assuming the CLI is run from the repository root
TEMPLATE_DIR = Path(__file__).parent.parent / "template_project"

# Use TEMPLATE_DIR as the source for copying files


@click.command()
@click.option(
    "--name", prompt="Enter the name for the project", help="The name of the project."
)
@click.option(
    "--git/--no-git",
    default=True,
    prompt="Would you like to initialize a Git repository?",
    help="Initialize a Git repository.",
)
@click.option(
    "--package-manager",
    type=click.Choice(["pipenv", "pip", "none"], case_sensitive=False),
    prompt="Select the package manager to use",
)
def create_project(name, git, package_manager):
    """Creates a new project with the given name and optionally initializes a Git repository."""
    # Create project directory
    target_dir = os.path.join(os.getcwd(), name)
    try:
        shutil.copytree(TEMPLATE_DIR, target_dir)
        click.echo(f"Project {name} created successfully.")
    except Exception as e:
        click.echo(f"Error creating project: {e}")
        return

    # Navigate into project directory
    os.chdir(name)

    # Optionally initialize a Git repository
    if git:
        try:
            subprocess.run(["git", "init", "--initial-branch=main"], check=True)
            click.echo("Initialized a Git repository.")
        except Exception as e:
            click.echo(f"Error initializing Git repository: {e}")

    # Setup the selected package manager
    if package_manager == "pipenv":
        subprocess.run(["pipenv", "install"], check=True)
        click.echo("Initialized project with pipenv. Run 'pipenv shell' to activate.")
    elif package_manager == "pip":
        # Create a requirements.txt file or install initial packages as needed
        with open("requirements.txt", "w") as f:
            f.write("# Add your project dependencies here")
        click.echo("Initialized project with pip. Created requirements.txt.")
    else:
        click.echo("No package manager selected.")


if __name__ == "__main__":
    create_project()
