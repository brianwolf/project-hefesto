import os
from typing import List
from zipfile import Path, ZipFile

from logic.apps.admin.config.variables import Vars, get_var


def create(zip_path: str, file_paths: str):

    paths = walk_path(file_paths)
    
    with ZipFile(zip_path, 'w') as zip:
        for file in paths:
            zip.write(file)


def walk_path(folder_path: str) -> List[str]:
    result = []
    for (dirpath, dirs, files) in os.walk(folder_path):

        for dir in dirs:
            result.append(f'{dirpath}/{dir}')

        for file in files:
            result.append(f'{dirpath}/{file}')

    return result
