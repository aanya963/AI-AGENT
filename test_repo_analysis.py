from tools.repo_scanner import RepoScanner
from tools.readme_reader import ReadmeReader
from services.repo_analyzer import RepoAnalyzer

repo_path = "repos/langgraph"

scan_result = RepoScanner.scan_repository(repo_path)

readme = ReadmeReader.read(repo_path)

analysis = RepoAnalyzer.analyze_repository(
    scan_result,
    readme
)

print(analysis)