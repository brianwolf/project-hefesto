import os
import shutil
from pathlib import Path

from logic.apps.admin.config.variables import Vars, get_var
from logic.apps.modules.services import module_service


def setup_modules():

    names_modules = module_service.list_default()

    default_path = module_service.get_default_path()
    modules_path = f'{Path.home()}/.hefesto/modules'

    if not os.path.exists(modules_path):
        os.makedirs(modules_path, exist_ok=True)

    for name in names_modules:
        shutil.copy(f'{default_path}/{name}.py', f'{modules_path}/{name}.py')
