from typing import Dict

from logic.apps.repo_modules.commons import sh


def exec(config: Dict[str, str]):

    from_var = config.get('from', None)
    to_var = config.get('to', None)

    sh(f'mv -rf {from_var} {to_var}')
