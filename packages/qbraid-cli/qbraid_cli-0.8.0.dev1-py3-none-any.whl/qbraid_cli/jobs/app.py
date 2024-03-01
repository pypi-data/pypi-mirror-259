"""
Module defining commands in the 'qbraid jobs' namespace.

"""

import sys
from typing import Callable, Dict, Optional, Tuple

import typer
from rich.console import Console

from qbraid_cli.handlers import handle_error, run_progress_task, validate_item

app = typer.Typer(help="Manage qBraid quantum jobs.")

QJOB_LIBS = ["braket"]


def validate_library(value: str) -> str:
    """Validate quantum jobs library."""
    return validate_item(value, QJOB_LIBS, "Library")


def get_state(library: Optional[str] = None) -> Dict[str, Tuple[bool, bool]]:
    """Get the state of qBraid Quantum Jobs for the specified library."""
    from qbraid.api.system import qbraid_jobs_state

    state_values = {}

    if library:
        libraries_to_check = [library]
    else:
        libraries_to_check = QJOB_LIBS

    for lib in libraries_to_check:
        state_values[lib] = qbraid_jobs_state(lib)

    return state_values


def run_progress_get_state(library: Optional[str] = None) -> Dict[str, Tuple[bool, bool]]:
    """Run get state function with rich progress UI."""
    return run_progress_task(
        get_state,
        library,
        description="Collecting package metadata...",
        error_message=f"Failed to collect {library} package metadata.",
    )


def handle_jobs_state(
    library: str,
    action: str,  # 'enable' or 'disable'
    action_callback: Callable[[], None],
) -> None:
    """Handle the common logic for enabling or disabling qBraid Quantum Jobs."""
    state_values: Dict[str, Tuple[bool, bool]] = run_progress_get_state(library)
    installed, enabled = state_values[library]

    if not installed:
        handle_error(message=f"{library} not installed.")
    if (enabled and action == "enable") or (not enabled and action == "disable"):
        action_color = "green" if enabled else "red"
        console = Console()
        console.print(
            f"\nqBraid quantum jobs already [bold {action_color}]{action}d[/bold {action_color}] "
            f"for [magenta]{library}[/magenta]."
        )
        console.print(
            "To check the state of all quantum jobs libraries in this environment, "
            "use: `[bold]qbraid jobs state[/bold]`"
        )
        raise typer.Exit()

    action_callback()  # Perform the specific enable/disable action


@app.command(name="enable")
def jobs_enable(
    library: str = typer.Argument(
        ..., help="Software library with quantum jobs support.", callback=validate_library
    )
) -> None:
    """Enable qBraid Quantum Jobs."""

    def enable_action():
        if library == "braket":
            from .toggle_braket import enable_braket

            enable_braket()
        else:
            raise RuntimeError(f"Unsupported device library: '{library}'.")

    handle_jobs_state(library, "enable", enable_action)


@app.command(name="disable")
def jobs_disable(
    library: str = typer.Argument(
        ..., help="Software library with quantum jobs support.", callback=validate_library
    )
) -> None:
    """Disable qBraid Quantum Jobs."""

    def disable_action():
        if library == "braket":
            from .toggle_braket import disable_braket

            disable_braket()
        else:
            raise RuntimeError(f"Unsupported device library: '{library}'.")

    handle_jobs_state(library, "disable", disable_action)


@app.command(name="state")
def jobs_state(
    library: str = typer.Argument(
        default=None,
        help="Optional: Specify a software library with quantum jobs support to check its status.",
        callback=validate_library,
    )
) -> None:
    """Display the state of qBraid Quantum Jobs for the current environment."""
    state_values: Dict[str, Tuple[bool, bool]] = run_progress_get_state(library)
    state_values = dict(sorted(state_values.items()))

    console = Console()
    header_1, header_2 = "Library", "State"
    max_lib_length = max((len(lib) for lib in state_values.keys()), default=len(header_1))
    padding = max_lib_length + 9

    console.print(f"Executable: {sys.executable}")
    console.print(f"\n{header_1:<{padding}}{header_2}", style="bold")

    for lib, (installed, enabled) in state_values.items():
        state_str = (
            "[green]enabled"
            if enabled and installed
            else "[red]disabled" if installed else "[grey70]unavailable"
        )
        console.print(f"{lib:<{padding-1}}", state_str, end="\n")


@app.command(name="list")
def jobs_list(
    limit: int = typer.Option(
        10, "--limit", "-l", help="Limit the maximum number of results returned"
    )
) -> None:
    """List qBraid Quantum Jobs."""

    def import_jobs() -> Tuple[Callable, Exception]:
        from qbraid import get_jobs
        from qbraid.exceptions import QbraidError

        return get_jobs, QbraidError

    result: Tuple[Callable, Exception] = run_progress_task(import_jobs)
    get_jobs, QbraidError = result

    try:
        get_jobs(filters={"numResults": limit})
    except QbraidError:
        handle_error(message="Failed to fetch quantum jobs.")


if __name__ == "__main__":
    app()
