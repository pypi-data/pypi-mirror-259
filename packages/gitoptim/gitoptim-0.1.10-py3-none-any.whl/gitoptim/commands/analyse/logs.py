from typing import Annotated

import httpx
import rich
import typer

from gitoptim.schemas.workflows import AnalyseLogsSchema
from gitoptim.services.gitlab import GitlabAPI
from gitoptim.utils import SectionTag, StartTag

PROMPT_TEMPLATE = (
    "{input}\n\nAbove are displayed logs from Gitlab CI/CD job. Analyze them. If there are no errors and warning "
    "don't do anything. If there are any errors or warning summarize them. If you know how to fix some "
    "errors/warnings or fix is described in the logs include it in your answer.")


def extract_relevant_logs(logs: str, after_last_tag: bool):
    start_tag_index = logs.find(str(StartTag()))
    if start_tag_index == -1:
        rich.print("[red]Cannot find current command's location in the logs[/red]")
        raise typer.Exit(code=1)

    logs_before_command = logs[:start_tag_index]

    if after_last_tag:
        section_tag_index = logs_before_command.rfind(str(SectionTag()))
        if section_tag_index == -1:
            return logs_before_command
        return logs_before_command[section_tag_index + len(str(SectionTag())):]

    return logs_before_command


def run_workflow_task(logs: str):
    headers = {'Authorization': "Basic MjkzOllyV1NZd0NQZEotQTJNYXRpNUFZc25xWDJsVGxoSlE0"}
    timeout = httpx.Timeout(None, connect=None, read=None, write=None)

    data = AnalyseLogsSchema(input=PROMPT_TEMPLATE.format(input=logs))

    r = httpx.post(
        "https://autumn8functions.default.aws.autumn8.ai/inference/4373e4e3-2502-4f28-b96a-125c2bc6faeb%2B293"
        "%2Bq5k6v6egxqi65gt1ojg9%2Bg5-2xlarge%2Bmar",
        json=data.model_dump(), headers=headers, timeout=timeout)

    print(r.json())


def command(
        after_last_tag: Annotated[
            bool, typer.Option("--after-last-tag",
                               help="Include only the logs that appear after the last execution of `gitoptim tag`. "
                                    "Includes all logs if `gitoptim tag` was never used.")] = False,
        # analyse_logs_trigger_id: Annotated[
        #     int, typer.Option(help="Needs to be provided if not set in environment variables.")] = None,
):
    """
    Analyze logs from the current job.

    Includes only the logs that appear before execution of this command.
    """

    print("Running job logs analysis...")
    gitlab_api = GitlabAPI()

    print("Fetching logs...")
    relevant_logs = extract_relevant_logs(gitlab_api.get_job_logs(), after_last_tag)

    print("Starting logs analysis...")
    run_workflow_task(relevant_logs)

    print("Logs analysis started. See [url] for more details.")
