"""
Rest
----
1.0.0

Dependencias:
* logger
* exception
* reflection

Configura el app de Flask para cargar blueprints dinamicamente, agregar JSON decoders que sigan un estandar, 
agregar handlers para manejo automatico de errores, entre otros.
"""
import logic.libs.reflection.reflection as reflection
from flask import Flask
from flask_restplus import Api
from logic.libs.exception.exception import AppException, UnknownException
from logic.libs.logger.logger import logger
from logic.libs.rest.src.errorHandler import load_generic_error_handler
from logic.libs.rest.src.json import config_encoders
from werkzeug.exceptions import HTTPException


def config_flask_app(app):

    app.config.setdefault('ERROR_INCLUDE_MESSAGE', False)
    load_generic_error_handler(app)
    config_encoders(app)

    return Api(app)
