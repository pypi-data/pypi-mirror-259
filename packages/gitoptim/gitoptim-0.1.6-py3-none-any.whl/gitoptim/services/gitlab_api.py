import gitlab

from gitoptim.utils import EnvironmentVariables


class GitlabAPIFactory:
    @staticmethod
    def with_job_token():
        base_url = ":".join(EnvironmentVariables().gitlab_server_url.split(":")[:2])
        return gitlab.Gitlab(
            base_url,
            job_token=EnvironmentVariables().job_token,
        )
