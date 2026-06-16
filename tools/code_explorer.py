from pathlib import Path

class CodeExplorer:

    @staticmethod
    def find_python_files(repo_path: str):

        repo = Path(repo_path)

        python_files = []

        for file in repo.rglob("*.py"):

            if ".venv" in str(file):
                continue

            python_files.append(str(file))

        return {
            "total_python_files": len(python_files),
            "python_files": python_files[:20]
        }

    @staticmethod
    def get_code_samples(repo_path: str):

        repo = Path(repo_path)

        samples = []

        for file in repo.rglob("*.py"):

            try:
                content = file.read_text(
                    encoding="utf-8",
                    errors="ignore"
                )[:2000]

                samples.append({
                    "file": str(file),
                    "content": content
                })

            except Exception:
                pass

            if len(samples) >= 5:
                break

        return samples