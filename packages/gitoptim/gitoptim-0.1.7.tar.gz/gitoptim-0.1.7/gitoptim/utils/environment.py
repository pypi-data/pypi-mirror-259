import os
from typing import Optional, Self, Type

import rich
import typer


class EnvironmentVariables:
    _INSTANCE: Self = None
    _project_id: Optional[str] = None
    _job_id: Optional[str] = None
    _job_token: Optional[str] = None
    _gitlab_api_url: Optional[str] = None
    _gitlab_server_url: Optional[str] = None

    def __new__(cls):
        if cls._INSTANCE is None:
            cls._INSTANCE = super().__new__(cls)
        return cls._INSTANCE

    def _load_variable(self, name: str, cast_type: Type = str):
        if hasattr(self, name) and getattr(self, name) is not None:
            return getattr(self, name)

        value = os.environ.get(name)
        if value is None:
            rich.print(f"[bold red]Environment variable {name} not found[/bold red]")
            raise typer.Exit(code=1)
        return cast_type(value)

    @property
    def project_id(self) -> str:
        self._project_id = self._load_variable("CI_PROJECT_ID")
        return self._project_id

    @project_id.setter
    def project_id(self, value: str):
        self._project_id = value

    @property
    def job_id(self) -> str:
        self._job_id = self._load_variable("CI_JOB_ID")
        return self._job_id

    @job_id.setter
    def job_id(self, value: str):
        self._job_id = value

    @property
    def job_token(self) -> str:
        self._job_token = self._load_variable("CI_JOB_TOKEN")
        return self._job_token

    @job_token.setter
    def job_token(self, value: str):
        self._job_token = value

    @property
    def gitlab_api_url(self) -> str:
        self._gitlab_api_url = self._load_variable("CI_API_V4_URL")
        return self._gitlab_api_url

    @gitlab_api_url.setter
    def gitlab_api_url(self, value: str):
        self._gitlab_api_url = value

    @property
    def gitlab_server_url(self) -> str:
        self._gitlab_server_url = self._load_variable("CI_SERVER_URL")
        return self._gitlab_server_url

    @gitlab_server_url.setter
    def gitlab_server_url(self, value: str):
        self._gitlab_server_url = value
