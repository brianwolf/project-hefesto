#!/usr/local/bin/python

# ejemplos de uso:
#   ./exec_template.py -t example/template_ejemplo.json -z asd.zip -p example/parametros_ejemplo.json

#   Para este es necesario que se halla cargado en template antes con nombre ejemplo
#   ./exec_template.py -n ejemplo -z asd.zip -p example/parametros_ejemplo.json

import argparse
import json
import os

from logic.apps.admin.config.modules import setup_modules
from logic.apps.admin.config.variables import setup_vars
from logic.apps.filesystem.services import (filesystem_service,
                                            workingdir_service)
from logic.apps.templates.services import exec_template_service

# VARIABLES
parser = argparse.ArgumentParser()
parser.add_argument('-n', help='Nombre del template')
parser.add_argument('-z', help='Path del zip resultado')
parser.add_argument('-t', help='Path del template para usar')
parser.add_argument('-p', help='Path del json de parametros del template')

args = parser.parse_args()

if not args.p:
    print('El parametro del json de los parametros del template es requerido')
    exit()

if not args.n and not args.t:
    print('Es requerido alguno de los parametros de nombre o template')
    exit()

out_path = 'project.zip' if args.z == None else args.z

name = args.n
with open(args.t, 'r') as file:
    in_path = file.read()
with open(args.p) as json_file:
    params_dict = json.load(json_file)


# CODIGO
setup_vars()
setup_modules()

print(f'Ejecutando...')
try:
    if in_path:
        id, zip_path = exec_template_service.exec(
            in_path, params_dict, out_path)
    else:
        id, zip_path = exec_template_service.exec_from_name(name, params_dict)

except Exception as e:
    print(f'Error al procesar pipeline -> {e}')
    exit()


filesystem_service.move_file(zip_path, out_path)
print(f'Zip generado en -> {out_path}')

workingdir_service.delete(id)
