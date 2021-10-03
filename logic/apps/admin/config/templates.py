import os
from pathlib import Path


def setup_templates():

    template_path = f'{Path.home()}/.hefesto/templates'

    if not os.path.exists(template_path):
        os.makedirs(template_path, exist_ok=True)
