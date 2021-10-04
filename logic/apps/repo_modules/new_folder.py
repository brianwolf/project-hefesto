import os
from typing import Dict

from logic.apps.repo_modules.commons import sh


def exec(workingdir: str, config: Dict[str, str]):

    path = config.get('path', None)

    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
