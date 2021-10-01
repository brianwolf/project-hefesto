from flask import Blueprint, Response, jsonify, request
from logic.apps.admin.config.variables import Vars, get_var
from logic.apps.filesystem.services import filesystem_service

blue_print = Blueprint('modules', __name__, url_prefix='/api/v1/modules')


@blue_print.route('/<name>', methods=['POST'])
def post(name: str):

    content = request.get_data().decode('utf8')
    path = f'{get_var(Vars.MODULES_RELATIVE_PATH)}/{name}.py'
    filesystem_service.create_file(path, content)

    return '', 201


@blue_print.route('/<name>', methods=['GET'])
def get(name: str):

    path = f'{get_var(Vars.MODULES_RELATIVE_PATH)}/{name}.py'
    content = filesystem_service.get_file_content(path).decode('utf-8')

    return Response(content, mimetype='text/plain', status=201)


@blue_print.route('/', methods=['GET'])
def list():

    result = [
        nf
        for nf in filesystem_service.name_files_from_path(
            get_var(Vars.MODULES_RELATIVE_PATH))
        if not nf.endswith('.pyc')
    ]

    return jsonify(result), 200


@blue_print.route('/<name>', methods=['DELETE'])
def delete(name: str):

    path = f'{get_var(Vars.MODULES_RELATIVE_PATH)}/{name}.py'
    filesystem_service.delete_file(path)

    return '', 200
