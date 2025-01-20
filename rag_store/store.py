import os
from pinecone import Pinecone


pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
assistant = pc.assistant.Assistant(
    assistant_name="projectretriver",
)


def store_projects(file_paths: list) -> None:
    """given a list of file paths stores the projects for later reference

    :param file_paths: list of file paths to store
    """
    for file_path in file_paths:
        response = assistant.upload_file(file_path=file_path, timeout=None)


file_paths = [
    "rag_store/old_projects/project1.txt",
    "rag_store/old_projects/project2.txt",
]
store_projects(file_paths)
