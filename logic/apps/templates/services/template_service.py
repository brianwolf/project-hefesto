
from datetime import datetime
from pathlib import Path
from typing import List
from uuid import uuid4

from logic.apps.admin.config.variables import Vars, get_var
from logic.apps.filesystem.services import filesystem_service

_TEMPLATES_PATH = f'{Path.home()}/.hefesto/templates'


def add(name: str, content: str):

    path = f'{get_path()}/{name}.txt'
    filesystem_service.create_file(path, content)


def get(name: str) -> str:

    path = f'{get_path()}/{name}.txt'
    return filesystem_service.get_file_content(path).decode('utf-8')


def list_all() -> List[str]:

    return filesystem_service.name_files_from_path(get_path())


def delete(name: str):

    path = f'{get_path()}/{name}.txt'
    filesystem_service.delete_file(path)


def get_path() -> str:

    global _TEMPLATES_PATH
    return _TEMPLATES_PATH
