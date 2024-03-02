import gitlab

from gitoptim.utils import EnvironmentVariables


class GitlabAPIFactory:
    @staticmethod
    def with_job_token():
        return gitlab.Gitlab(
            EnvironmentVariables().gitlab_api_url,
            job_token=EnvironmentVariables().job_token,
        )
