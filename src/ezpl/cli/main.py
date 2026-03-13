# ///////////////////////////////////////////////////////////////
# EZPL - CLI Main Entry Point
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Main CLI entry point for Ezpl logging framework.

This module provides the command-line interface for managing Ezpl
configuration, viewing logs, and performing various operations.
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Standard library imports
import click

# Third-party imports
from rich.panel import Panel
from rich.text import Text

# Local imports
from ..version import __version__
from ._console import console
from .commands import config, info, logs, version

# ///////////////////////////////////////////////////////////////
# CLI GROUP
# ///////////////////////////////////////////////////////////////


@click.group(
    name="ezpl",
    invoke_without_command=True,
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click.version_option(
    version=__version__,
    prog_name="Ezpl CLI",
    message="%(prog)s version %(version)s",
)
@click.pass_context
def cli(ctx: click.Context) -> None:
    """
    🚀 Ezpl CLI - Modern Python Logging Framework

    Command-line interface for managing Ezpl logging configuration,
    viewing logs, and performing various operations.

    Use 'ezpl <command> --help' for more information on a specific command.
    """
    # If no subcommand is invoked, display the welcome screen and help
    if ctx.invoked_subcommand is None:
        _display_welcome()
        click.echo(ctx.get_help())


def _display_welcome() -> None:
    """Display welcome message with Rich."""
    try:
        welcome_text = Text()
        welcome_text.append("🚀 ", style="bold bright_green")
        welcome_text.append("Ezpl CLI", style="bold bright_blue")
        welcome_text.append(" - Modern Python Logging Framework", style="dim white")

        panel = Panel(
            welcome_text,
            title="[bold bright_blue]Welcome[/bold bright_blue]",
            border_style="bright_blue",
            padding=(1, 2),
        )
        console.print(panel)
    except (OSError, RuntimeError, ValueError):
        # Fallback if Rich is not available
        click.echo("🚀 Ezpl CLI - Modern Python Logging Framework")


# ///////////////////////////////////////////////////////////////
# COMMAND GROUPS
# ///////////////////////////////////////////////////////////////


# Logs group
cli.add_command(logs.logs_group)

# Config group
cli.add_command(config.config_group)

# Version command
cli.add_command(version.version_command)

# Info command
cli.add_command(info.info_command)


# ///////////////////////////////////////////////////////////////
# MAIN ENTRY POINT
# ///////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////


def main() -> None:
    """
    Main entry point for the CLI.

    This function is called when the CLI is invoked from the command line.
    """
    try:
        cli()
    except click.ClickException as e:
        e.show()
        raise SystemExit(e.exit_code) from e
    except KeyboardInterrupt as e:
        console.print("\n[yellow]Interrupted by user[/yellow]")
        raise SystemExit(1) from e
    except (OSError, RuntimeError, ValueError) as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise SystemExit(1) from e


if __name__ == "__main__":
    main()
