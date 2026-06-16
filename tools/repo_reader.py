# from pathlib import Path


# class RepoReader:

#     @staticmethod
#     def get_repository_structure(repo_path: str):

#         repo = Path(repo_path)

#         structure = []

#         for item in repo.iterdir():

#             if item.name.startswith("."):
#                 continue

#             structure.append({
#                 "name": item.name,
#                 "type": "folder" if item.is_dir() else "file"
#             })

#         return structure