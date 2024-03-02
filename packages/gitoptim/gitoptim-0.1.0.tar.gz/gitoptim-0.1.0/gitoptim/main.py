import rich
import typer

from gitoptim import commands
from gitoptim.utils import (EndTag, EnvironmentVariables, StartTag,
                            is_help_option_present)

app = typer.Typer(rich_markup_mode="rich")
app.add_typer(commands.analyse.app, name="analyse")


# pylint: disable=unused-argument
def teardown(*args, **kwargs):
    rich.print(EndTag())


@app.callback(result_callback=teardown)
def main():
    """
    Gitoptim SDK
    """

    if is_help_option_present():
        return

    rich.print(StartTag())
    rich.print(EnvironmentVariables().job_id)
    rich.print(EnvironmentVariables().job_token)


app.command(name="memlab")(commands.memlab)
app.command(name="tag")(commands.tag)
