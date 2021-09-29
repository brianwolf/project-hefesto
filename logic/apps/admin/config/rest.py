from flask import Flask
from logic.libs.reflection import reflection
from logic.libs.rest import rest

api = None


def setup_rest(app: Flask) -> Flask:

    global api
    api = rest.config_flask_app(app)

    reflection.load_modules_by_regex_path('logic/apps/*/routes')
