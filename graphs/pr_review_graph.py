from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from tools.github_tool import GitHubTool
from services.pr_reviewer import PRReviewer
from services.review_aggregator import ReviewAggregator
from agents.repository_agent import RepositoryAgent
aggregator = ReviewAggregator()
repo_agent = RepositoryAgent()

class PRReviewState(TypedDict):

    owner: str
    repo: str
    pr_number: int

    repo_summary: str

    files: list
    reviews: list

    final_report: str


github_tool = GitHubTool()
reviewer = PRReviewer()


def fetch_pr_node(state):

    files = github_tool.get_pr_files(
        state["owner"],
        state["repo"],
        state["pr_number"]
    )

    print(f"Fetched {len(files)} files")

    state["files"] = files

    return state


def review_files_node(state):

    reviews = []

    for file in state["files"]:

        print(f"Reviewing {file['filename']}")

        review = reviewer.review_file(
            file["filename"],
            file["patch"],
            state["repo_summary"]
        )

        reviews.append({
            "file": file["filename"],
            "review": review
        })

    state["reviews"] = reviews

    return state

def repository_analysis_node(state):

    print("Analyzing Repository...")

    repo_url = (
        f"https://github.com/"
        f"{state['owner']}/"
        f"{state['repo']}.git"
    )

    analysis = repo_agent.analyze(
        repo_url
    )

    state["repo_summary"] = analysis

    return state


def aggregate_node(state):

    report = aggregator.aggregate_reviews(
        state["reviews"]
    )

    state["final_report"] = report

    return state


graph = StateGraph(PRReviewState)

graph.add_node(
    "repository_analysis",
    repository_analysis_node
)

graph.add_node(
    "fetch_pr",
    fetch_pr_node
)

graph.add_node(
    "review_files",
    review_files_node
)

graph.add_node(
    "aggregate",
    aggregate_node
)

graph.add_edge(
    START,
    "repository_analysis"
)

graph.add_edge(
    "repository_analysis",
    "fetch_pr"
)

graph.add_edge(
    "fetch_pr",
    "review_files"
)

graph.add_edge(
    "review_files",
    "aggregate"
)

graph.add_edge(
    "aggregate",
    END
)

app = graph.compile()