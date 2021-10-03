#!env/bin/python

# ejemplo de uso:
#   ./exec_pipeline.py -p pipeline_ejemplo.json -z /home/brian/Descargas/asd.zip

import argparse
import json
import os

from logic.apps.admin.config.modules import setup_modules
from logic.apps.admin.config.variables import setup_vars
from logic.apps.filesystem.services import (filesystem_service,
                                            workingdir_service)
from logic.apps.pipeline.services import exec_pipeline_service

# VARIABLES
parser = argparse.ArgumentParser()
parser.add_argument('-p', help='Path del pipeline a procesar')
parser.add_argument('-z', help='Path del zip resultado')

args = parser.parse_args()

if not args.p:
    print('El parametro del path del pipeline es requerido')
    exit()

out_path = os.getcwd() if args.z == None else args.z

pipeline_path = args.p


# CODIGO
setup_vars()
setup_modules()

with open(pipeline_path) as json_file:
    pipeline_dict = json.load(json_file)

print(f'Pipeline cargado')
print(f'Ejecutando...')
try:
    id, zip_path = exec_pipeline_service.exec(pipeline_dict)
except Exception as e:
    print(f'Error al procesar pipeline -> {e}')
    exit()

filesystem_service.move_file(zip_path, out_path)

print(f'Zip generado en -> {out_path}')

workingdir_service.delete(id)
