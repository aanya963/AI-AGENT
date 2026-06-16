# services/architecture_analyzer.py

from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


class ArchitectureAnalyzer:

    @staticmethod
    def analyze(
        scan_result,
        readme_content,
        code_samples
    ):

        prompt = f"""
        You are a Staff Software Engineer.

        Analyze this repository.

        Repository Metadata:
        {scan_result}

        README:
        {readme_content}

        Source Code Samples:
        {code_samples}

        Generate:

        1. Project Purpose
        2. Tech Stack
        3. High-Level Architecture
        4. Main Components
        5. Design Patterns Used
        6. Potential Challenges
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content