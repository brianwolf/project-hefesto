import os
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


def exec(workingdir: str, config: Dict[str, str]):

    words = config.get('words')
    regex = config.get('regex')
    ignore = config.get('ignore', [])

    if words:
        paths = walk_path(workingdir)

        for old, new in words.items():
            for path in paths:

                if is_a_ignored_path(path, ignore):
                    continue

                basename = os.path.basename(path)
                if old in basename:
                    os.rename(path, path.replace(old, new))
                    paths = walk_path(workingdir)
