from typing import Dict

from logic.apps.modules.commons import sh_out


def exec(workingdir: str, config=Dict[str, str]) -> str:
    cmd = config['cmd']
    return sh_out(f'/bin/sh -c "{cmd}"')
