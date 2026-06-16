from tools.git_tool import GitTool

repo_path = GitTool.clone_repository(
    "https://github.com/langchain-ai/langgraph"
)

print(repo_path)