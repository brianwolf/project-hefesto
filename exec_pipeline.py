#!/usr/local/bin/python

# ejemplo de uso:
#   python exec_pipeline.py -p example/pipeline_ejemplo.yaml -z example/asd.zip

import argparse
import json
import logging
import os
from typing import Dict

import yaml

from logic.apps.admin.config.modules import setup_modules
from logic.apps.admin.config.variables import setup_vars
from logic.apps.filesystem.services import (filesystem_service,
                                            workingdir_service)
from logic.apps.pipeline.services import exec_pipeline_service

# VARIABLES
# ----------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument('-p', help='Path del pipeline a procesar')
parser.add_argument('-z', help='Path del zip resultado')

args = parser.parse_args()

if not args.p:
    print('El parametro del path del pipeline es requerido')
    exit()

out_path = os.getcwd() if args.z == None else args.z

pipeline_path = args.p


# FUNCIONES
# ----------------------------------------
def _get_dict(pipeline_str: str) -> Dict[str, any]:
    return yaml.load(pipeline_str, Loader=yaml.FullLoader) if _is_yaml(pipeline_str) else json.loads(pipeline_str)


def _is_yaml(yaml_str: str) -> bool:
    try:
        yaml.load(yaml_str, Loader=yaml.FullLoader)
        return True

    except Exception as _:
        return False


# SCRIPT
# ----------------------------------------
setup_vars()
setup_modules()

with open(pipeline_path) as file:
    pipeline_dict = _get_dict(file.read())

print(f'Pipeline cargado')
print(f'Ejecutando...')
try:
    id, zip_path = exec_pipeline_service.exec(pipeline_dict)
except Exception as e:
    logging.exception(e)
    print(f'Error al procesar pipeline -> {e}')
    exit()

filesystem_service.move_file(zip_path, out_path)

print(f'Zip generado en -> {out_path}')

workingdir_service.delete(id)
