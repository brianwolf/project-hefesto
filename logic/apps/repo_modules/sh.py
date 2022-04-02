from typing import Dict

from logic.apps.repo_modules.commons import sh


def exec(workingdir: str, config: Dict[str, str]):
    cmd = config['cmd']
    sh(f'/bin/sh -c "{cmd}"', echo=False)
