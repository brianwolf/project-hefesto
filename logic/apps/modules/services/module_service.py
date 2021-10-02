
from datetime import datetime
from pathlib import Path
from typing import List
from uuid import uuid4

from logic.apps.admin.config.variables import Vars, get_var
from logic.apps.filesystem.services import filesystem_service

_MODULES_PATH = f'{Path.home()}/.hefesto/modules'
_DEFAULT_RELATIVE_PATH = f'logic/apps/repo_modules'


def add(name: str, content: str):

    path = f'{get_path()}/{name}.py'
    filesystem_service.create_file(path, content)


def get(name: str) -> str:

    path = f'{get_path()}/{name}.py'
    return filesystem_service.get_file_content(path).decode('utf-8')


def list_all() -> List[str]:

    return [
        nf
        for nf in filesystem_service.name_files_from_path(get_path())
        if not nf.endswith('.pyc')
    ]


def list_default() -> List[str]:

    return [
        nf
        for nf in filesystem_service.name_files_from_path(get_default_path())
        if not nf.endswith('.pyc')
    ]


def delete(name: str):

    path = f'{get_path()}/{name}.py'
    filesystem_service.delete_file(path)


def get_path() -> str:

    global _MODULES_PATH
    return _MODULES_PATH


def get_default_path() -> str:

    global _DEFAULT_RELATIVE_PATH
    return _DEFAULT_RELATIVE_PATH
