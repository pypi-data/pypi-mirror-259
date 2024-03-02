import gitlab

from gitoptim.utils import EnvironmentVariables


class GitlabAPIFactory:
    @staticmethod
    def with_job_token():
        base_url = EnvironmentVariables().gitlab_server_url.split(":")[0]
        return gitlab.Gitlab(
            base_url,
            job_token=EnvironmentVariables().job_token,
        )
