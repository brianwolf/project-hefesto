import os
from typing import Dict


def exec(workingdir: str, config: Dict[str, str]):

    path = config.get('path', '.')
    output = config.get('output')

    os.system(f'zip -r {output} {path}')
