import typer

from gitoptim import commands
from gitoptim.utils.cli import console, should_callback_execute
from gitoptim.utils.tag import EndTag, StartTag

app = typer.Typer(rich_markup_mode="rich")
app.add_typer(commands.analyse.app, name="analyse")


# pylint: disable=unused-argument
def teardown(*args, **kwargs):
    console.print(EndTag())


@app.callback(result_callback=teardown)
def main():
    """
    Gitoptim SDK
    """

    if not should_callback_execute():
        return

    console.print(StartTag())


app.command(name="memlab")(commands.memlab)
app.command(name="tag")(commands.tag)
