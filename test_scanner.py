from tools.repo_scanner import RepoScanner

result = RepoScanner.scan_repository(
    "repos/langgraph"
)

print(result)