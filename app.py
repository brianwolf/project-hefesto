#!/usr/local/bin/python

import argparse
import logging
import os
import sys
from sys import exit
from typing import Dict
from urllib.request import urlopen

import yaml

from logic.apps.filesystem.services import (filesystem_service,
                                            workingdir_service)
from logic.apps.pipeline.services import exec_pipeline_service
from logic.apps.templates.services import exec_template_service

# VARIABLES
# ----------------------------------------
VERSION = '1.2.0'

if sys.argv[1] in ['--version', '-v']:
    print(VERSION)
    exit(0)

parser = argparse.ArgumentParser()

parser.add_argument('yaml', help='Yaml path to pipeline or template')
parser.add_argument(
    '-p', help='Template params. Format: -p KEY1=VALUE1,KEY2=VALUE2', required=False)
parser.add_argument('-o', help='Zip output',
                    required=False, default='project.zip')

args = parser.parse_args()

yaml_path = args.yaml
out_path = args.o if args.o else 'project.zip'
params_str = args.p if args.p else ''


# FUNCIONES
# ----------------------------------------

def _get_content(yaml_path: str):

    if yaml_path.startswith('http'):
        f = urlopen(yaml_path)
        return f.read().decode("utf-8")

    with open(yaml_path) as f:
        return f.read().decode("utf-8")


def _get_dict(yaml_path: str) -> Dict[str, any]:
    return yaml.load(_get_content(yaml_path), Loader=yaml.FullLoader)


def _get_params_dict(params_str) -> Dict[str, any]:
    params_dict = {}

    for kv in params_str.split(','):
        k = kv.split('=')[0]
        v = kv.split('=')[1]
        params_dict[k] = v

    return params_dict


def _get_full_path(path: str) -> str:
    if not path.startswith('/') and not path.startswith('http'):
        return f'{os.getcwd()}/{path}'
    return path


# SCRIPT
# ----------------------------------------

# para que funcione al estar compilado
yaml_path = _get_full_path(yaml_path)
out_path = _get_full_path(out_path)
if hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)


print(f'Running')

try:
    if params_str:
        params_dict = _get_params_dict(params_str)

        yaml_str = _get_content(yaml_path)

        id, zip_path = exec_template_service.exec(
            yaml_str, params_dict, out_path)

    else:
        yaml_dict = _get_dict(yaml_path)
        id, zip_path = exec_pipeline_service.exec(yaml_dict, out_path)

except Exception as e:
    logging.exception(e)
    print(f'Error on process')
    exit(1)

filesystem_service.move_file(zip_path, out_path)
workingdir_service.delete(id)

print(f'Success')
