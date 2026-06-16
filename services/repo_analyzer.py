from groq import Groq
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


class RepoAnalyzer:

    @staticmethod
    def analyze_repository(scan_result, readme_content):

        prompt = f"""
        You are a senior software architect.

        Analyze this repository.

        Repository Metadata:
        {scan_result}

        README:
        {readme_content}

        Provide:

        1. Project Purpose
        2. Tech Stack
        3. Architecture Overview
        4. Key Components
        5. Difficulty Level
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