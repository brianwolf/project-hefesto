"""
SQLiteAlchemy
---------
1.0.0

Utiliza sqlAlchemy para establecer una uncia conexion con un sqlite local, es para uso simple sin tanta configuracion
"""
from logic.libs.sqliteAlchemy.src import config
from logic.libs.sqliteAlchemy.src.sqlAlchemyMethods import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker


def setup(url: str, echo: bool = False):
    """
    Configura la util, se debe usar antes de usar cualquier otro metodo

    - url -> es para la conexion, se lo pasa al metodo create_engine() de sqlAlchemy
    - echo -> si esta en True loguea todo los comandos ejecutados en sqlite con INFO
    """
    config.URL = url
    config.ECHO = echo


def make_session() -> Session:
    """
    Crea una nueva session para conectarse a la BD
    """
    if not config.ENGINE:
        create_engine()

    return sessionmaker(config.ENGINE)()


def get_engine() -> Engine:
    """
    Devuelve el engine creado
    """
    return config.ENGINE
