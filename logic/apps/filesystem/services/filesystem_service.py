import os
from typing import List


def get_file_content(path: str) -> str:
    with open(path, 'rb') as file:
        return file.read()


def create_file(path: str, content: bytes):
    with open(path, 'w') as file:
        file.write(content)


def name_files_from_path(path: str) -> List[str]:
    result = []
    for _, _, name_files in os.walk(path):
        result += name_files
    return result
