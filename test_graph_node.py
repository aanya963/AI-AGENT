from graphs.pr_review_graph import (
    fetch_pr_node
)

state = {
    "owner": "langchain-ai",
    "repo": "langgraph",
    "pr_number": 8091,
    "files": [],
    "reviews": [],
    "final_report": ""
}

result = fetch_pr_node(state)

print(
    len(result["files"])
)