import os
from typing import Dict

from logic.apps.repo_modules.commons import sh


def exec(config: Dict[str, str]):

    path = config.get('path')
    content = config.get('content')

    folder_path = os.path.dirname(path)

    if not os.path.exists(folder_path) and folder_path != '':
        os.makedirs(folder_path, exist_ok=True)

    with open(path, 'w') as file:
        file.write(str(content))
