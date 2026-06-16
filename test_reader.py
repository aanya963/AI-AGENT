from tools.repo_reader import RepoReader

structure = RepoReader.get_repository_structure(
    "repos/langgraph"
)

for item in structure:
    print(item)