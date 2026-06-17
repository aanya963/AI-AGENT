import os


class CacheService:

    CACHE_FOLDER = "cache"

    @classmethod
    def get_cache_path(cls, owner, repo):
        return f"{cls.CACHE_FOLDER}/{owner}_{repo}.txt"

    @classmethod
    def exists(cls, owner, repo):
        return os.path.exists(
            cls.get_cache_path(owner, repo)
        )

    @classmethod
    def load(cls, owner, repo):
        with open(
            cls.get_cache_path(owner, repo),
            "r"
        ) as f:
            return f.read()

    @classmethod
    def save(
        cls,
        owner,
        repo,
        content
    ):
        with open(
            cls.get_cache_path(owner, repo),
            "w"
        ) as f:
            f.write(content)