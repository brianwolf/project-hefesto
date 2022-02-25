from typing import Dict

from repo_modules.commons import sh


def exec(workingdir: str, config: Dict[str, str]):

    path = config.get('path', None)
    sh(f'rm -rf {path}')
