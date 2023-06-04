import os
import shutil
from datetime import datetime
from os import walk
from pathlib import Path
from typing import List


def create() -> str:
    now = datetime.now()
    id = f'{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}'
    Path(fullpath(id)).mkdir(parents=True, exist_ok=True)
    return id


def delete(id: str):
    shutil.rmtree(fullpath(id))


def fullpath(id: str) -> str:
    return f'{os.getcwd()}/{id}'


def get(id: str) -> List[str]:
    result = []
    for (dirpath, _, _) in walk(fullpath(id)):
        result.extend(dirpath)

    return result
