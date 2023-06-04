import os
import shutil
from typing import Dict, List


def walk_path(folder_path: str) -> List[str]:
    result = []
    for (dirpath, dirs, files) in os.walk(folder_path):

        for dir in dirs:
            result.append(f'{dirpath}/{dir}')

        for file in files:
            result.append(f'{dirpath}/{file}')

    return result


def is_a_ignored_path(path: str, ignore: List[str]) -> bool:

    for i in ignore:
        if i + '/' in path:
            return True

    return False


def exec(config: Dict[str, str]):

    words = config.get('words')
    regex = config.get('regex')
    ignore = config.get('ignore', [])

    if words:
        for old, new in words.items():

            paths = walk_path(os.getcwd())
            for a_path in list(paths):

                if is_a_ignored_path(a_path, ignore):
                    continue

                basename = os.path.basename(a_path)
                if old in basename:
                    shutil.move(a_path, a_path.replace(old, new))
