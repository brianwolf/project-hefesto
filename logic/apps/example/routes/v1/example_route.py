from flask import request
from flask_restplus import Resource, fields
from logic.apps.admin.config.rest import api
from logic.apps.example.errors.example_error import ExampleError
from logic.apps.example.routes.v1.dtos import example_dto
from logic.apps.example.services import example_service
from logic.libs.exception.exception import AppException

name_space = api.namespace('api/v1/examples', description='Ejemplos')


example_model = name_space.model('Example', {
    'string': fields.String,
    'integer': fields.Integer,
    'date_time': fields.DateTime,
    'double': fields.Float,
    'uuid': fields.String(required=False)
})


@name_space.route('')
class Examples(Resource):

    def get(self):
        result = example_service.get_example()
        return example_dto.example_to_json(result)

    @name_space.expect(example_model, code=201, validate=True)
    def post(self):
        m = example_dto.json_to_example(request.json)
        m = example_service.add(m)
        return example_dto.example_to_json(m), 201


@name_space.route('/all')
class ExamplesAll(Resource):

    def get(self):
        result = example_service.get_all()
        return [example_dto.example_to_json(o) for o in result]


@name_space.route('/errors/unknow')
class ErrorUnknow(Resource):

    def get(self):
        boom = 1 / 0
        return '', 200


@name_space.route('/errors/business')
class ErrorBusiness(Resource):

    def get(self):
        try:
            1 / 0

        except Exception as e:
            raise AppException(
                code=ExampleError.EXAMPLE_RANDOM_ERROR,
                msj='BOOM...!!!',
                exception=e
            )

        return '', 200
