from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()


class PRReviewer:

    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def review_file(
        self,
        filename,
        patch
    ):

        prompt = f"""
You are a Senior Software Engineer.

Review this code change.

File:
{filename}

Diff:
{patch}

Provide:

1. Summary
2. Potential Bugs
3. Performance Concerns
4. Security Concerns
5. Final Recommendation
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