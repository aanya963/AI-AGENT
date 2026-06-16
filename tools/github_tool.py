from github import Github
from dotenv import load_dotenv
import os

load_dotenv()


class GitHubTool:

    def __init__(self):
        self.github = Github(
            os.getenv("GITHUB_TOKEN")
        )

    def get_pull_request(self, owner, repo, pr_number):

        repository = self.github.get_repo(
            f"{owner}/{repo}"
        )

        pr = repository.get_pull(pr_number)

        return {
            "title": pr.title,
            "body": pr.body,
            "state": pr.state,
            "author": pr.user.login
        }