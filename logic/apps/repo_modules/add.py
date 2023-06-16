from typing import Dict

from logic.apps.repo_modules.commons import sh


def exec(config: Dict[str, str]):
    to_var = config.get("to", ".")

    sh(f"mkdir -p ./{to_var}")
    sh(f"cp -rf ../ {to_var}")
