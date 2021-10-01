from flask import Blueprint, Response, request
from logic.apps.admin.config.variables import Vars, get_var
from logic.apps.filesystem.services import filesystem_service

blue_print = Blueprint('modules', __name__, url_prefix='/api/v1/modules')


@blue_print.route('/<name>', methods=['POST'])
def post(name: str):

    content = request.get_data()
    path = f'{get_var(Vars.MODULES_RELATIVE_PATH)}/{name}.py'
    filesystem_service.create_file(path, content)

    return '', 201


@blue_print.route('/<name>', methods=['GET'])
def get(name: str):

    path = f'{get_var(Vars.MODULES_RELATIVE_PATH)}/{name}.py'
    content = filesystem_service.get_file_content(path).decode('utf-8')

    return Response(content, mimetype='text/plain', status=201)
