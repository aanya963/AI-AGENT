from graphs.pr_review_graph import app

result = app.invoke(
    {
        "owner": "langchain-ai",
        "repo": "langgraph",
        "pr_number": 8091,
        "repo_summary": "",
        "files": [],
        "reviews": [],
        "final_report": ""
    }
)

print("\n")
print("=" * 80)

print(result["final_report"])