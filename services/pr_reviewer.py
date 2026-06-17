from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()


class PRReviewer:

    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def review_file(self, filename, patch, repo_summary):

        prompt = f"""
        You are a Staff Software Engineer performing a Pull Request review.

        Repository Context:
        {repo_summary}

        File:
        {filename}

        Code Diff:
        {patch}

        Review this code change.

        Analyze:

        1. Correctness
        - Possible bugs
        - Edge cases
        - Logic issues

        2. Maintainability
        - Readability
        - Design concerns
        - Future maintenance risks

        3. Performance
        - Inefficiencies
        - Unnecessary operations

        4. Testing
        - Missing test cases
        - Regression risks

        IMPORTANT:
        - Only mention real concerns visible in the diff.
        - Avoid generic advice.
        - If no issue exists, explicitly say so.
        - Be concise.
        """
        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content