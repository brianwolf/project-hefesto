from flask import Response, request
from flask_restplus import Resource
from logic.apps.admin.config.rest import api
from logic.apps.admin.config.variables import Vars, get_var
from logic.apps.filesystem.services import filesystem_service

name_space = api.namespace(
    'api/v1/modules', description='Modulos para los pipelines')

# pipeline_model = name_space.model('Pipeline', {})


@name_space.route('/<name>')
@name_space.doc(params={'name': 'Nombre del modulo'})
class Modules(Resource):

    # @name_space.expect(pipeline_model, code=200, validate=False)
    # def post(self):

    #     id, zip_path = exec_pipeline_service.exec(request.json)

    #     return send_file(BytesIO(open(zip_path, 'rb').read()),
    #                      mimetype='application/octet-stream',
    #                      as_attachment=True,
    #                      attachment_filename=ntpath.basename(zip_path))

    @name_space.expect(code=200)
    @name_space.produces(["text/plain"])
    def get(self, name: str):

        path = f'{get_var(Vars.MODULES_RELATIVE_PATH)}/{name}.py'
        content = filesystem_service.get_file_content(path).decode('utf-8')

        return Response(content, mimetype='text/plain', status=201)
