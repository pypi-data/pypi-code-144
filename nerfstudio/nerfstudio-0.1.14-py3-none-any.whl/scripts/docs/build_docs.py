#!/usr/bin/env python
"""Simple yaml debugger"""
import subprocess
import sys

import tyro
from rich.console import Console
from rich.style import Style

CONSOLE = Console(width=120)

LOCAL_TESTS = ["Run license checks", "Run Black", "Python Pylint", "Test with pytest"]


def run_command(command: str) -> None:
    """Run a command kill actions if it fails

    Args:
        command: command to run
    """
    ret_code = subprocess.call(command, shell=True)
    if ret_code != 0:
        CONSOLE.print(f"[bold red]Error: `{command}` failed. Exiting...")
        sys.exit(1)


def main(clean_cache: bool = False):
    """Run the github actions locally.

    Args:
        clean_cache: whether to clean the cache before building docs.
    """

    CONSOLE.print("[green]Adding notebook documentation metadata")
    run_command("python scripts/docs/add_nb_tags.py")

    # Add checks for building documentation
    CONSOLE.print("[green]Building Documentation")
    if clean_cache:
        run_command("cd docs/; make clean; make html SPHINXOPTS='-W;'")
    else:
        run_command("cd docs/; make html SPHINXOPTS='-W;'")

    CONSOLE.line()
    CONSOLE.rule(characters="=", style=Style(color="green"))
    CONSOLE.print("[bold green]Done")
    CONSOLE.rule(characters="=", style=Style(color="green"))


if __name__ == "__main__":
    tyro.extras.set_accent_color("bright_yellow")
    tyro.cli(main)
