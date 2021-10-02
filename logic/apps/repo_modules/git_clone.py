from typing import Dict

from logic.apps.repo_modules.commons import sh


def exec(workingdir: str, config: Dict[str, str]):

    url = config['url'].replace('https://', '')
    username = config.get('user', None)
    password = config.get('pass', None)

    if not username:
        sh(f'git clone https://{url}')
        return

    sh(f'git clone https://{username}:{password}@{url}', echo=False)
