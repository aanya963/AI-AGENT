from utils.url_parser import parse_pr_url

owner, repo, pr = parse_pr_url(
    "https://github.com/langchain-ai/langgraph/pull/8093"
)

print(owner)
print(repo)
print(pr)