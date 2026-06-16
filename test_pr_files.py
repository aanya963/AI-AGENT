from tools.github_tool import GitHubTool

# github_tool = GitHubTool()

# files = github_tool.get_pr_files(
#     "langchain-ai",
#     "langgraph",
#     8091
# )

# print(files[0])


github_tool = GitHubTool()

files = github_tool.get_pr_files(
    "langchain-ai",
    "langgraph",
    8091
)

print(f"\nTotal files: {len(files)}\n")

for file in files:
    print("=" * 50)
    print(file["filename"])
    print("Changes:", file["changes"])