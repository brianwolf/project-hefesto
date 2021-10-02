#!env/bin/python

import json
import os
import sys

from logic.apps.admin.config.variables import setup_vars
from logic.apps.filesystem.services import (filesystem_service,
                                            workingdir_service)
from logic.apps.pipeline.services import exec_pipeline_service

setup_vars()

if len(sys.argv) < 2:
    print('Es requerido el path del pipeline como parametro')

pipeline_path = sys.argv[1]

with open(pipeline_path) as json_file:
    pipeline_dict = json.load(json_file)

print(f'Pipeline cargado')
print(f'Ejecutando...')
try:
    id, zip_path = exec_pipeline_service.exec(pipeline_dict)
except Exception as e:
    print(f'Error al procesar pipeline -> {e}')
    exit()

zip_name = os.path.basename(zip_path)
filesystem_service.move_file(zip_path, zip_name)

print(f'Zip generado con nombre -> {zip_name}')

workingdir_service.delete(id)
