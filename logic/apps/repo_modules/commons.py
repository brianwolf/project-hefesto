import os
import subprocess
from typing import Dict


def sh(cmd: str) -> int:
    print(cmd)
    print(sh_out(cmd))


def sh_out(cmd: str) -> str:
    return subprocess.getoutput(cmd)


def sh_full(cmd: str) -> Dict[int, str]:
    return subprocess.getstatusoutput(cmd)


def var(env_var: str, default_value: str = None) -> str:
    return os.getenv(env_var, default_value)


def var_exists(env_var: str) -> bool:
    return env_var in os.environ
