import sys
from pathlib import Path

import click

from starwhale.utils import console, get_current_shell
from starwhale.utils.fs import ensure_dir
from starwhale.utils.cli import AliasedGroup

_SUPPORT_SHELLS = {
    "bash": ("~/.bashrc", 'eval "$(_{prog_u}_COMPLETE=bash_source {prog})"'),
    "zsh": ("~/.zshrc", 'eval "$(_{prog_u}_COMPLETE=zsh_source {prog})"'),
    "fish": (
        "~/.config/fish/completions/{prog}.fish",
        "eval (env _{prog_u}_COMPLETE=fish_source {prog})",
    ),
}


@click.group(
    "completion", cls=AliasedGroup, help="Shell completion for Starwhale command-line"
)
def completion_cmd() -> None:
    pass


@completion_cmd.command("show", help="Show shell completion code")
@click.argument("shell", required=False, type=click.Choice(_SUPPORT_SHELLS.keys()))
def show(shell: str) -> None:
    _inject_code(shell, stdout=True)


@completion_cmd.command(
    "install", help="Install shell completion script in the current shell"
)
@click.argument("shell", required=False, type=click.Choice(_SUPPORT_SHELLS.keys()))
def completion(shell: str) -> None:
    _inject_code(shell)


def _inject_code(shell: str = "", stdout: bool = False) -> None:
    prog: str = click.get_current_context().find_root().info_name  # type: ignore
    shell = shell or get_current_shell()

    if shell not in _SUPPORT_SHELLS:
        console.print(f":crying_face: no support {shell} completion")
        sys.exit(1)

    _path, code = _SUPPORT_SHELLS[shell]
    path = Path(_path.format(prog=prog)).expanduser().absolute()
    code = code.format(prog_u=prog.upper(), prog=prog)

    if stdout:
        console.print(code)
    else:
        ensure_dir(path.parent)

        mode = "a" if path.exists() else "w"
        with path.open(mode=mode) as f:
            f.write(f"\n#Generated by Starwhale for {prog} completion\n")
            f.write(code + "\n")

        console.print(f":clap: {prog} {shell} completion installed in {path}")
        console.print(
            f":beer: run [bold magenta]exec {shell}[/] command to activate shell completion"
        )
