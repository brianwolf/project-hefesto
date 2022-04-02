from typing import Dict

from logic.apps.repo_modules.commons import sh


def exec(workingdir: str, config: Dict[str, str]):

    url = config['url'].replace('https://', '')
    username = config.get('user', None)
    password = config.get('pass', None)
    branch = config.get('branch', None)

    cmd = "git clone https://"

    if username and password:
        cmd += f"{username}:{password}@"

    cmd += url

    if branch:
        cmd += f' -b {branch}'

    sh(cmd, echo=False)
