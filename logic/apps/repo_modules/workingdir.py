import os
from typing import Dict


def exec(config: Dict[str, str]):
    path = config['path']
    os.chdir(path)
