import ntpath
import os
from io import BytesIO

from flask import jsonify, send_file
from flask_restplus import Resource
from logic.apps.admin.config.rest import api
from logic.apps.admin.config.variables import Vars
from logic.libs.logger.logger import logger
from logic.libs.variables.variables import all_vars, get_var

name_space = api.namespace('/', description='Administracion de la aplicacion')


@name_space.route("/vars")
class Variables(Resource):

    def get(self):
        return jsonify(all_vars())


@name_space.route("/alive")
class Index(Resource):

    def get(self):
        version = get_var(Vars.VERSION)
        logger().info(f'Version: {version}')
        return jsonify(version=version)


@name_space.route("/postman")
class Postman(Resource):

    def get(self):
        postman_files = sorted([
            f for f in os.listdir(os.getcwd())
            if str(f).endswith('.postman_collection.json')
        ], reverse=True)

        collection_dir = next(iter(postman_files), None)

        return send_file(BytesIO(open(collection_dir, 'rb').read()),
                         mimetype='application/octet-stream',
                         as_attachment=True,
                         attachment_filename=ntpath.basename(collection_dir))
