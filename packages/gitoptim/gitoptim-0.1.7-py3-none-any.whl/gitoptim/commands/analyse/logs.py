from typing import Annotated

import rich
import typer

from gitoptim.services.gitlab import GitlabAPI


def command(
        after_last_tag: Annotated[
            bool, typer.Option("--after_last_tag",
                               help="Include only the logs that appear after the last execution of `gitoptim tag`. "
                                    "Includes all logs if `gitoptim tag` was never used.")] = False,
        analyse_logs_trigger_id: Annotated[
            int, typer.Option(help="Needs to be provided if not set in environment variables.")] = None,
):
    """
    Analyze logs from the current job.

    Includes only the logs that appear before execution of this command.
    """

    rich.print(after_last_tag)
    rich.print(analyse_logs_trigger_id)

    rich.print("Running job logs analysis...")

    gitlab_api = GitlabAPI()
    rich
