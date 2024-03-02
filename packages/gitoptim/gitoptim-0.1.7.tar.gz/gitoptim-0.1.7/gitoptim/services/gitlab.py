import httpx
from gitoptim.utils import EnvironmentVariables


class GitlabAPI:
    _api_url: str
    _job_token: str
    _job_id: str
    _project_id: str

    def __init__(self):
        self._api_url = EnvironmentVariables().gitlab_api_url
        self._job_token = EnvironmentVariables().job_token
        self._job_id = EnvironmentVariables().job_id
        self._project_id = EnvironmentVariables().project_id

    def _get_headers(self):
        return {
            "JOB-TOKEN": self._job_token
        }

    def get(self, path: str, **kwargs):
        return httpx.get(f"{self._api_url}/{path}", headers=self._get_headers(), **kwargs)

    def get_job_logs(self):
        self.get(f"projects/{self._project_id}/jobs/{self._job_id}/trace").json()
