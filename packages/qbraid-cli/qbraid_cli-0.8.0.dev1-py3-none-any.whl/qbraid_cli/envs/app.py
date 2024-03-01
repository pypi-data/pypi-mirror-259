"""
Module defining commands in the 'qbraid envs' namespace.

"""

import json
import keyword
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import typer
from rich.console import Console

from qbraid_cli.handlers import QbraidException, run_progress_task

app = typer.Typer(help="Manage qBraid environments.")


def is_valid_env_name(env_name: str) -> bool:  # pylint: disable=too-many-return-statements
    """
    Validates a Python virtual environment name against best practices.

    This function checks if the given environment name is valid based on certain
    criteria, including length, use of special characters, reserved names, and
    operating system-specific restrictions.

    Args:
        env_name (str): The name of the Python virtual environment to validate.

    Returns:
        bool: True if the name is valid, False otherwise.

    Raises:
        ValueError: If the environment name is not a string or is empty.
    """
    # Basic checks for empty names or purely whitespace names
    if not env_name or env_name.isspace():
        return False

    # Check for invalid characters, including shell metacharacters and spaces
    if re.search(r'[<>:"/\\|?*\s&;()$[\]#~!{}]', env_name):
        return False

    if env_name.startswith("tmp"):
        return False

    # Reserved names for Windows (example list, can be expanded)
    reserved_names = [
        "CON",
        "PRN",
        "AUX",
        "NUL",
        "COM1",
        "COM2",
        "COM3",
        "COM4",
        "COM5",
        "COM6",
        "COM7",
        "COM8",
        "COM9",
        "LPT1",
        "LPT2",
        "LPT3",
        "LPT4",
        "LPT5",
        "LPT6",
        "LPT7",
        "LPT8",
        "LPT9",
    ]
    if env_name.upper() in reserved_names:
        return False

    if len(env_name) > 20:
        return False

    # Check against Python reserved words
    if keyword.iskeyword(env_name):
        return False

    # Check if it starts with a number, which is not a good practice
    if env_name[0].isdigit():
        return False

    return True


def validate_env_name(value: str) -> str:
    """Validate environment name."""
    if not is_valid_env_name(value):
        raise typer.BadParameter(
            f"Invalid environment name '{value}'. " "Please use a valid Python environment name."
        )
    return value


def installed_envs_data() -> Tuple[Dict[str, Path], Dict[str, str]]:
    """Gather paths and aliases for all installed qBraid environments."""
    from qbraid.api.system import get_qbraid_envs_paths, is_valid_slug

    installed = {}
    aliases = {}

    qbraid_env_paths: List[Path] = get_qbraid_envs_paths()

    for env_path in qbraid_env_paths:
        for entry in env_path.iterdir():
            if entry.is_dir() and is_valid_slug(entry.name):
                installed[entry.name] = entry

                if entry.name == "qbraid_000000":
                    aliases["default"] = entry.name
                    continue

                state_json_path = entry / "state.json"
                if state_json_path.exists():
                    try:
                        with open(state_json_path, "r", encoding="utf-8") as f:
                            data = json.load(f)
                        aliases[data.get("name", entry.name[:-7])] = entry.name
                    # pylint: disable-next=broad-exception-caught
                    except (json.JSONDecodeError, Exception):
                        aliases[entry.name[:-7]] = entry.name
                else:
                    aliases[entry.name[:-7]] = entry.name

    return installed, aliases


def request_delete_env(slug: str) -> str:
    """Send request to delete environment given slug."""
    from qbraid.api import QbraidSession, RequestsApiError

    session = QbraidSession()

    try:
        session.delete(f"/environments/{slug}")
    except RequestsApiError as err:
        raise QbraidException("Delete environment request failed") from err


@app.command(name="create")
def envs_create(  # pylint: disable=too-many-statements
    name: str = typer.Option(
        ..., "--name", "-n", help="Name of the environment to create", callback=validate_env_name
    ),
    description: Optional[str] = typer.Option(
        None, "--description", "-d", help="Short description of the environment"
    ),
) -> None:
    """Create a new qBraid environment."""
    from .create import create_qbraid_env_assets, create_venv

    def request_new_env(req_body: Dict[str, str]) -> Dict[str, Any]:
        """Send request to create new environment and return the slug."""
        from qbraid.api import QbraidSession, RequestsApiError

        session = QbraidSession()

        try:
            env_data = session.post("/environments/create", json=req_body).json()
        except RequestsApiError as err:
            raise QbraidException("Create environment request failed") from err

        if env_data is None or len(env_data) == 0 or env_data.get("slug") is None:
            raise QbraidException(
                "Create environment request responsed with invalid environment data"
            )

        return env_data

    def gather_local_data() -> Tuple[Path, str]:
        """Gather environment data and return the slug."""
        from qbraid.api.system import get_qbraid_envs_paths

        env_path = get_qbraid_envs_paths()[0]

        result = subprocess.run(
            [sys.executable, "--version"],
            capture_output=True,
            text=True,
            check=True,
        )

        python_version = result.stdout or result.stderr

        return env_path, python_version

    req_body = {
        "name": name,
        "description": description or "",
        "tags": "",  # comma separated list of tags
        "code": "",  # newline separated list of packages
        "visibility": "private",
        "kernelName": "",
        "prompt": "",
        "origin": "CLI",
    }

    environment = run_progress_task(
        request_new_env,
        req_body,
        description="Validating request...",
        error_message="Failed to create qBraid environment",
    )

    env_path, python_version = run_progress_task(
        gather_local_data,
        description="Solving environment...",
        error_message="Failed to create qBraid environment",
    )

    slug = environment.get("slug")
    display_name = environment.get("displayName")
    prompt = environment.get("prompt")
    description = environment.get("description")
    tags = environment.get("tags")
    kernel_name = environment.get("kernelName")

    slug_path = env_path / slug
    description = "None" if description == "" else description

    typer.echo("\n\n## qBraid Metadata ##\n")
    typer.echo(f"  name: {display_name}")
    typer.echo(f"  description: {description}")
    typer.echo(f"  tags: {tags}")
    typer.echo(f"  slug: {slug}")
    typer.echo(f"  shellPrompt: {prompt}")
    typer.echo(f"  kernelName: {kernel_name}")

    typer.echo("\n\n## Environment Plan ##\n")
    typer.echo(f"  location: {slug_path}")
    typer.echo(f"  version: {python_version}\n")

    user_confirmation = typer.confirm("Proceed", default=True)
    typer.echo("")
    if not user_confirmation:
        request_delete_env(slug)
        typer.echo("qBraidSystemExit: Exiting.")
        raise typer.Exit()

    run_progress_task(
        create_qbraid_env_assets,
        slug,
        prompt,
        kernel_name,
        slug_path,
        description="Generating qBraid assets...",
        error_message="Failed to create qBraid environment",
    )

    run_progress_task(
        create_venv,
        slug_path,
        prompt,
        description="Creating virtual environment...",
        error_message="Failed to create qBraid environment",
    )

    console = Console()
    console.print(
        f"\n[bold green]Successfully created qBraid environment: "
        f"[/bold green][bold magenta]{name}[/bold magenta]\n"
    )
    typer.echo("# To activate this environment, use")
    typer.echo("#")
    typer.echo(f"#     $ qbraid envs activate {name}")
    typer.echo("#")
    typer.echo("# To deactivate an active environment, use")
    typer.echo("#")
    typer.echo("#     $ deactivate")


@app.command(name="remove")
def envs_remove(
    name: str = typer.Option(..., "-n", "--name", help="Name of the environment to remove")
) -> None:
    """Delete a qBraid environment."""

    def gather_local_data(env_name: str) -> Tuple[Path, str]:
        """Get environment path and slug from name (alias)."""
        installed, aliases = installed_envs_data()
        for alias, slug in aliases.items():
            if alias == env_name:
                path = installed[slug]

                return path, slug

        raise QbraidException(f"Environment '{name}' not found.")

    slug_path, slug = gather_local_data(name)

    confirmation_message = (
        f"⚠️  Warning: You are about to delete the environment '{name}' "
        f"located at '{slug_path}'.\n"
        "This will remove all local packages and permanently delete all "
        "of its associated qBraid environment metadata.\n"
        "This operation CANNOT be undone.\n\n"
        "Are you sure you want to continue?"
    )

    # Ask for user confirmation
    if typer.confirm(confirmation_message, abort=True):
        typer.echo("")
        run_progress_task(
            request_delete_env,
            slug,
            description="Deleting remote environment data...",
            error_message="Failed to delete qBraid environment",
        )

        run_progress_task(
            shutil.rmtree,
            slug_path,
            description="Deleting local environment...",
            error_message="Failed to delete qBraid environment",
        )
        typer.echo(f"\nEnvironment '{name}' successfully removed.")
        # console = Console()
        # console.print(
        #     f"\n[bold green]Successfully deleted qBraid environment: "
        #     f"[/bold green][bold magenta]{name}[/bold magenta]\n"
        # )


@app.command(name="list")
def envs_list():
    """List installed qBraid environments."""
    installed, aliases = installed_envs_data()

    if len(installed) == 0:
        print("No qBraid environments installed.")
        print("\nUse 'qbraid envs create' to create a new environment.")
        return

    alias_path_pairs = [(alias, installed[slug_name]) for alias, slug_name in aliases.items()]

    sorted_alias_path_pairs = sorted(
        alias_path_pairs,
        key=lambda x: (x[0] != "default", str(x[1]).startswith(str(Path.home())), x[0]),
    )

    current_env_path = Path(sys.executable).parent.parent.parent

    max_alias_length = (
        max(len(alias) for alias, _ in sorted_alias_path_pairs) if sorted_alias_path_pairs else 0
    )
    max_path_length = (
        max(len(str(path)) for _, path in sorted_alias_path_pairs) if sorted_alias_path_pairs else 0
    )

    print("# qbraid environments:")
    print("#")
    print("")
    for alias, path in sorted_alias_path_pairs:
        mark = "*  " if path == current_env_path else "   "
        print(f"{alias.ljust(max_alias_length + 7)}{mark}{str(path).ljust(max_path_length)}")


@app.command(name="activate")
def envs_activate(
    name: str = typer.Argument(..., help="Name of the environment. Values from 'qbraid envs list'.")
):
    """Activate qBraid environment.

    NOTE: Currently only works on qBraid Lab platform, and select few other OS types.
    """
    installed, aliases = installed_envs_data()
    if name in aliases:
        venv_path: Path = installed[aliases[name]] / "pyenv"
    elif name in installed:
        venv_path: Path = installed[name] / "pyenv"
    else:
        raise typer.BadParameter(f"Environment '{name}' not found.")

    from .activate import activate_pyvenv

    activate_pyvenv(venv_path)


if __name__ == "__main__":
    app()
