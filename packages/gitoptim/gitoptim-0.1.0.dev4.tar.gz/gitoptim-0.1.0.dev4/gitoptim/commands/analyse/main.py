import typer

from gitoptim.utils import should_callback_execute
from .logs import command as logs

app = typer.Typer(rich_markup_mode="rich")


@app.callback()
def main():
    """
    Analyse code or Gitlab job logs.
    """

    if not should_callback_execute():
        return


app.command(name="logs")(logs)
