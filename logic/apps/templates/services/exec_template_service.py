import json
from typing import Dict, List, Tuple
from uuid import UUID

import yaml
from jinja2 import Template
from logic.apps.pipeline.services import exec_pipeline_service
from logic.apps.templates.errors.template_error import TemplateError
from logic.apps.templates.services import template_service
from logic.libs.exception.exception import AppException


def exec(template_str: str, params: Dict[str, any], template_name: str = 'project.zip') -> Tuple[UUID, str]:

    try:
        print(f'Ejecutando template {template_name} con variables -> {params}')

        template = Template(template_str)
        pipeline_str = template.render(params)

        print(f'\n')
        print(f'Pipeline generado ->')
        print(f'{pipeline_str}\n')

    except Exception as e:

        msj = 'Error al procesar template'
        raise AppException(TemplateError.EXECUTE_TEMPLATE_ERROR, msj, e)

    id, zip_path = exec_pipeline_service.exec(
        _get_dict(pipeline_str), template_name)

    return id, zip_path


def exec_from_name(template_name: str, params: Dict[str, any]) -> Tuple[UUID, str]:

    template_str = template_service.get(template_name)
    return exec(template_str, params, template_name)


def _get_dict(pipeline_str: str) -> Dict[str, any]:
    return yaml.load(pipeline_str, Loader=yaml.FullLoader) if _is_yaml(pipeline_str) else json.loads(pipeline_str)


def _is_yaml(yaml_str: str) -> bool:
    try:
        yaml.load(yaml_str, Loader=yaml.FullLoader)
        return True

    except Exception as _:
        return False
