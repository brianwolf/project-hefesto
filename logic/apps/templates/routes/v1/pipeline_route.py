import ntpath
from io import BytesIO

from flask import Blueprint, jsonify, request, send_file
from logic.apps.pipeline.services import exec_pipeline_service

blue_print = Blueprint('templates', __name__, url_prefix='/api/v1/templates')


@blue_print.route('/exec', methods=['POST'])
def exec_pipeline():

    id, zip_path = exec_pipeline_service.exec(request.json)

    return send_file(BytesIO(open(zip_path, 'rb').read()),
                     mimetype='application/octet-stream',
                     as_attachment=True,
                     attachment_filename=ntpath.basename(zip_path))
