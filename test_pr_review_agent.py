from agents.pr_review_agent import PRReviewAgent

agent = PRReviewAgent()

reviews = agent.review_pr(
    "langchain-ai",
    "langgraph",
    8091
)

for review in reviews:

    print("\n")
    print("=" * 80)

    print(review["file"])

    print("=" * 80)

    print(review["review"])