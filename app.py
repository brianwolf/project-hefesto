#!/usr/local/bin/python

import sys
import os
import argparse
import logging
from typing import Dict

import yaml

from logic.apps.admin.config.variables import setup_vars
from logic.apps.filesystem.services import (filesystem_service,
                                            workingdir_service)
from logic.apps.pipeline.services import exec_pipeline_service
from logic.apps.templates.services import exec_template_service

# VARIABLES
# ----------------------------------------
parser = argparse.ArgumentParser()

parser.add_argument('yaml', help='Path del yaml del pipeline/template')
parser.add_argument(
    '-p', help='Parametros del template. Formato: -p KEY1=VALUE1,KEY2=VALUE2')
parser.add_argument('-o', help='Path del zip resultado')

args = parser.parse_args()

yaml_path = args.yaml
out_path = args.o if args.o else 'project.zip'
params_str = args.p if args.p else ''


# FUNCIONES
# ----------------------------------------

def _get_dict(yaml_path: str) -> Dict[str, any]:
    with open(yaml_path) as f:
        return yaml.load(f.read(), Loader=yaml.FullLoader)


def _get_params_dict(params_str) -> Dict[str, any]:
    params_dict = {}

    for kv in params_str.split(','):
        k = kv.split('=')[0]
        v = kv.split('=')[1]
        params_dict[k] = v

    return params_dict


# SCRIPT
# ----------------------------------------
yaml_path = f'{os.getcwd()}/{yaml_path}' if not yaml_path.startswith('/') else yaml_path
out_path = f'{os.getcwd()}/{out_path}' if not out_path.startswith('/') else out_path
os.chdir(sys._MEIPASS)

setup_vars()

print(f'Yaml cargado')
print(f'Ejecutando...')

try:
    if params_str:
        params_dict = _get_params_dict(params_str)

        with open(yaml_path) as f:
            yaml_str = f.read()

        id, zip_path = exec_template_service.exec(
            yaml_str, params_dict, out_path)

    else:
        yaml_dict = _get_dict(yaml_path)

        id, zip_path = exec_pipeline_service.exec(yaml_dict, out_path)

except Exception as e:
    logging.exception(e)
    print(f'Error al procesar')
    exit(1)

filesystem_service.move_file(zip_path, out_path)

print(f'Zip generado en -> {out_path}')

workingdir_service.delete(id)
