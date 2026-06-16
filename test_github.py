from tools.github_tool import GitHubTool

github_tool = GitHubTool()

pr = github_tool.get_pull_request(
    "langchain-ai",
    "langgraph",
    8093
)

print(pr)