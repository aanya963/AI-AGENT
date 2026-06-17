from tools.github_tool import GitHubTool
from services.pr_reviewer import PRReviewer


class PRReviewAgent:

    def __init__(self):

        self.github_tool = GitHubTool()
        self.reviewer = PRReviewer()

    def review_pr(
        self,
        owner,
        repo,
        pr_number
    ):

        files = self.github_tool.get_pr_files(
            owner,
            repo,
            pr_number
        )

        reviews = []

        for file in files:

            print(
                f"Reviewing {file['filename']}..."
            )

            review = self.reviewer.review_file(
                file["filename"],
                file["patch"],
            )

            reviews.append(
                {
                    "file": file["filename"],
                    "review": review
                }
            )

        return reviews