import typer

from gitoptim.utils import should_callback_execute
from .logs import command as logs

app = typer.Typer(rich_markup_mode="rich")


@app.callback()
def main(ctx: typer.Context):
    """
    Analyse code or Gitlab job logs.
    """

    if not should_callback_execute(ctx.invoked_subcommand):
        return


app.command(name="logs")(logs)
