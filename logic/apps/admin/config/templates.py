import os
import shutil
from pathlib import Path

from logic.apps.admin.config.variables import Vars, get_var
from logic.apps.modules.services import module_service


def setup_templates():

    template_path = f'{Path.home()}/.hefesto/templates'

    if not os.path.exists(template_path):
        os.makedirs(template_path, exist_ok=True)
