import ntpath
from io import BytesIO

from flask import Blueprint, Response, jsonify, request, send_file
from logic.apps.admin.config.variables import Vars, get_var
from logic.apps.templates.services import (exec_template_service,
                                           template_service)

blue_print = Blueprint('templates', __name__, url_prefix='/api/v1/templates')


@blue_print.route('/<name>', methods=['POST'])
def post(name: str):
    content = request.get_data().decode('utf8')
    template_service.add(name, content)
    return '', 201


@blue_print.route('/<name>', methods=['GET'])
def get(name: str):
    content = template_service.get(name)
    return Response(content, mimetype='text/plain', status=201)


@blue_print.route('/', methods=['GET'])
def list_all():
    return jsonify(template_service.list_all()), 200


@blue_print.route('/<name>', methods=['DELETE'])
def delete(name: str):
    template_service.delete(name)
    return '', 200


@blue_print.route('/<name>/exec', methods=['POST'])
def exec_template(name: str):

    params = request.json

    id, zip_path = exec_template_service.exec_from_name(name, params)

    return send_file(BytesIO(open(zip_path, 'rb').read()),
                     mimetype='application/octet-stream',
                     as_attachment=True,
                     attachment_filename=ntpath.basename(zip_path))
