import ntpath
from io import BytesIO
from typing import Dict

from flask import jsonify, request, send_file
from flask_restplus import Resource
from logic.apps.admin.config.rest import api
from logic.apps.pipeline.services import exec_pipeline_service

name_space = api.namespace('api/v1/pipelines', description='Pipelines')

pipeline_model = name_space.model('Pipeline', {})


@name_space.route('')
class Examples(Resource):

    @name_space.expect(pipeline_model, code=200, validate=False)
    def post(self):

        id, zip_path = exec_pipeline_service.exec(request.json)

        return send_file(BytesIO(open(zip_path, 'rb').read()),
                         mimetype='application/octet-stream',
                         as_attachment=True,
                         attachment_filename=ntpath.basename(zip_path))
