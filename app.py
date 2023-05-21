#!/usr/local/bin/python

import argparse
import logging
import os
import ssl
import sys
from sys import exit
from typing import Dict
from urllib.request import urlopen

import yaml

from logic.apps.filesystem import service as filesystem_service
from logic.apps.filesystem import workingdir_service
from logic.apps.pipeline import service as pipline_service


VERSION = '1.3.0'

if sys.argv[1] in ['--version', '-v']:
    print(VERSION)
    exit(0)

# ----------------------------------------
# VARIABLES
# ----------------------------------------

parser = argparse.ArgumentParser()

parser.add_argument('pipeline_file', help='Yaml pipeline path or url')
parser.add_argument('-p', help='params -p K1=V1,K2=V2', required=False)
parser.add_argument('-f', help='file params', required=False)
parser.add_argument('-o', help='folder output', required=False)

args = parser.parse_args()

yaml_path = args.pipeline_file
params_str = args.p if args.p else None
params_path = args.f if args.f else None
out_path = args.o if args.o else os.getcwd()


# ----------------------------------------
# FUNCTIONS
# ----------------------------------------

def _get_content(yaml_path: str):

    if yaml_path.startswith('http'):
        context = ssl._create_unverified_context()
        f = urlopen(yaml_path, context=context)
        return f.read().decode("utf-8")

    with open(yaml_path) as f:
        return f.read()


def _get_dict(yaml_path: str) -> Dict[str, any]:
    return yaml.load(_get_content(yaml_path), Loader=yaml.FullLoader)


def _get_params_dict() -> Dict[str, any]:
    params_dict = {}

    if params_str:
        for kv in params_str.split(','):
            k = kv.split('=')[0]
            v = kv.split('=')[1]
            params_dict[k] = v

    if params_path:
        params_dict.update(_get_dict(params_path))

    return params_dict


def _get_full_path(path: str) -> str:
    if not path.startswith('/') and not path.startswith('http'):
        return f'{os.getcwd()}/{path}'
    return path


# ----------------------------------------
# SCRIPT
# ----------------------------------------

# para que funcione al estar compilado
yaml_path = _get_full_path(yaml_path)
out_path = _get_full_path(out_path)
params_path = _get_full_path(params_path)
if hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)

try:
    params_dict = _get_params_dict()
    yaml_str = _get_content(yaml_path)

    id = pipline_service.exec(yaml_str, params_dict)

except Exception as e:
    logging.exception(e)
    exit(1)

filesystem_service.move_file(workingdir_service.fullpath(id), out_path)
