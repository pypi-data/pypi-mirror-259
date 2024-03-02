import typer

from gitoptim.utils import is_help_option_present

from .logs import command as logs

app = typer.Typer(rich_markup_mode="rich")


@app.callback()
def main():
    """
    Analyse code or Gitlab job logs.
    """

    if is_help_option_present():
        return


app.command(name="logs")(logs)
