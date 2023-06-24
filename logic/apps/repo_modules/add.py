import os
import re
from typing import Dict

from logic.apps.repo_modules.commons import sh


def files_on_path(folder_path: str) -> list[str]:
    result = []
    for dirpath, _, files in os.walk(folder_path):
        for file in files:
            path = f"{dirpath}/{file}"

            if os.path.isfile(path):
                result.append(path)

    return result


def is_a_ignored_path(path: str, ignore: list[str]) -> bool:
    for i in ignore:
        if re.findall(i, path):
            return True

    return False


def exec(config: Dict[str, str]):

    paths = config.get("paths", [""])
    ignore = config.get("ignore", [])

    for path in paths:

        path = "../" + path

        for pf in files_on_path(path):
            if is_a_ignored_path(pf, ignore):
                continue

            mkdir_to = os.path.dirname(pf).replace("../", "")
            pf_to = pf.replace("//", "/").replace("../", "")

            sh(f"mkdir -p {mkdir_to}")
            sh(f"cp {pf} {pf_to}")
