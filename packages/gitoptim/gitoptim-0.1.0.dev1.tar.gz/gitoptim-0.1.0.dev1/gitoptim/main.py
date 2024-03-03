import typer

from gitoptim import commands
from gitoptim.utils import EndTag, StartTag, should_callback_execute, console

app = typer.Typer(rich_markup_mode="rich")
app.add_typer(commands.analyse.app, name="analyse")


# pylint: disable=unused-argument
def teardown(*args, **kwargs):
    console.print(EndTag())


@app.callback(result_callback=teardown)
def main(ctx: typer.Context):
    """
    Gitoptim SDK
    """

    if not should_callback_execute(ctx.invoked_subcommand):
        return

    console.print(StartTag())


app.command(name="memlab")(commands.memlab)
app.command(name="tag")(commands.tag)
