from typing import Dict

from logic.apps.repo_modules.commons import sh


def exec(config: Dict[str, str]):

    path = config.get('path', None)
    sh(f'rm -rf {path}')
