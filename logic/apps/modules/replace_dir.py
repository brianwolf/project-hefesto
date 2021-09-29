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


def exec(workingdir: str, config: Dict[str, str]):

    words = config.get('words')
    regex = config.get('regex')

    paths = walk_path(workingdir)

    if words:
        for old, new in words.items():
            for path in paths:
                if path.endswith(old):
                    os.rename(path, path.replace(old, new))
                    paths = walk_path(workingdir)
