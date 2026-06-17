from tools.github_tool import GitHubTool
from services.pr_reviewer import PRReviewer

github_tool = GitHubTool()
reviewer = PRReviewer()

files = github_tool.get_pr_files(
    "langchain-ai",
    "langgraph",
    8091
)

first_file = files[0]

review = reviewer.review_file(
    first_file["filename"],
    first_file["patch"],
)

print(review)