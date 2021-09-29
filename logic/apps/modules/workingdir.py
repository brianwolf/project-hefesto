import os
from typing import Dict


def exec(workingdir: str, config: Dict[str, str]) -> str:
    path = config['path']
    os.chdir(f'{workingdir}/{path}')
