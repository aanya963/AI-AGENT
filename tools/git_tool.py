from git import Repo
# Comes from GitPython.
# Instead of running: git clone ... : python wil do
from pathlib import Path


class GitTool:

    @staticmethod
    def clone_repository(repo_url: str) -> str:

        repo_name = repo_url.split("/")[-1]

        clone_path = Path("repos") / repo_name

        if clone_path.exists():
            return str(clone_path)

        Repo.clone_from(repo_url, clone_path)

        return str(clone_path)