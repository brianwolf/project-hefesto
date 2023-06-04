import os
from typing import Dict, List


def files_on_path(folder_path: str) -> List[str]:
    result = []
    for (dirpath, _, files) in os.walk(folder_path):

        for file in files:
            path = f'{dirpath}/{file}'

            if os.path.isfile(path):
                result.append(path)

    return result


def is_a_ignored_path(path: str, ignore: List[str]) -> bool:

    for i in ignore:

        i_path = i if i.endswith('/') else i + '/'
        if i_path in path:
            return True

    return False


def exec(config: Dict[str, str]):

    words = config.get('words')
    ignore = config.get('ignore', [])

    files_paths = files_on_path(".")

    if words:
        for file_path in files_paths:

            if is_a_ignored_path(file_path, ignore):
                continue

            with open(file_path, encoding='ISO-8859-1') as file:
                file_text = str(file.read())

            for old, new in words.items():
                file_text = file_text.replace(old, new)

            with open(file_path, 'w') as file:
                file.write(file_text)
