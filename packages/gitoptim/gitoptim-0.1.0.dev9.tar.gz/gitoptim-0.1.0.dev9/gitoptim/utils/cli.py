import sys
from rich.console import Console

SUBCOMMAND_NAMES = ["analyse"]


def should_callback_execute():
    return "--help" not in sys.argv and sys.argv[-1] not in SUBCOMMAND_NAMES


console = Console()
error_console = Console(stderr=True, style="bold red")
