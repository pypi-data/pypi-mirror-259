import datetime
import os
from enum import Enum
from pathlib import Path

import typer
from click import ClickException
from rich.console import Console
from rich.text import Text

from vanity_ssh_keygen.__version__ import version_callback
from vanity_ssh_keygen.keygen import find_concurrently

app = typer.Typer()
console = Console()
err_console = Console(stderr=True)


class Error(ClickException):
    def __init__(self, message: str, exit_code=1) -> None:
        super().__init__(message)
        self.exit_code = exit_code


class KeyTypes(str, Enum):
    ED25519 = "ED25519"


def highlight_last_characters(text, x, color):
    styled_text = Text()
    styled_text.append(text[:-x], style="")
    styled_text.append(text[-x:], style=color)
    return styled_text


@app.command()
def main(  # noqa: PLR0913
    vanity_string: str = typer.Argument(help="The vanity string that should be in the SSH public key"),
    key_type: KeyTypes = typer.Option(
        KeyTypes.ED25519.value, help="The type of SSH key to generate"
    ),  # Just for reference...
    processes: int = typer.Option(4, help="The number of processes to use in the search"),
    case_insensitive: bool = typer.Option(
        True, "--case-insensitive/--case-sensitive", help="Case sensitivity of vanity string"
    ),
    path: Path = typer.Option(None, help="Path to write keys to"),
    comment: str = typer.Option("", help="Comment for public key"),
    print: bool = typer.Option(True, "--print/--no-print", help="Print the keys to stdout"),
    _: bool = typer.Option(None, "-v", "--version", callback=version_callback, is_eager=True),
):
    if not print and not path:
        raise Error("Must allow printing to stdout or specifying a file")

    if path:
        if os.path.exists(path) or os.path.exists(f"{path}.pub"):
            raise Error(f"Path '{path}' already exists. Cannot overwrite existing keys.")

    start = datetime.datetime.utcnow()
    result = find_concurrently(
        suffix=vanity_string.encode("utf-8"),
        num_processes=processes,
        case_insensitive=case_insensitive,
    )
    end = datetime.datetime.utcnow()
    duration_seconds = (end - start).seconds

    if result:
        public_key, private_key = result

        console.print(
            f"[green bold]Vanity keys generated in {datetime.timedelta(seconds=duration_seconds)}[/green bold]"
        )

        if path:
            console.print(f"[green bold]Written to file '{path}'[/green bold]")
            with os.fdopen(os.open(path, os.O_WRONLY | os.O_CREAT, 0o600), "x") as f:
                f.write(private_key.decode())
            with os.fdopen(os.open(f"{path}.pub", os.O_WRONLY | os.O_CREAT, 0o600), "x") as f:
                f.write(f"{public_key.decode()} {comment}")

        if print:
            console.print("")
            console.print("[green]Public key:[/green]")
            console.print(
                highlight_last_characters(public_key.decode(), len(vanity_string), "red bold") + f" {comment}"
            )
            console.print("")
            console.print("[green]Private key:[/green]")
            console.print(private_key.decode(), highlight=False)


if __name__ == "__main__":
    app()
