import os
import re
import yaml
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
        if re.findall(i, path):
            return True

    return False


def exec(config: Dict[str, str]):

    path_file = config['path']
    key = config['key']
    new_dict = config['new_dict']

    with open(path_file, encoding='ISO-8859-1') as file:
        file_text = str(file.read())
        file_dict = yaml.load(file_text, Loader=yaml.FullLoader)

    aux = file_dict
    for k in list(key.split('.')[:-1]):
        aux = aux[k]

    aux[key.split('.')[-1]] = new_dict

    with open(path_file, 'w', encoding='ISO-8859-1') as file:
        file.write(yaml.dump(file_dict))
