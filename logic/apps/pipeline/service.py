import os
from importlib.util import module_from_spec, spec_from_file_location
from uuid import UUID

import yaml
from jinja2 import Template

from logic.apps.filesystem import workingdir_service
from logic.apps.modules import service as module_service
from logic.apps.pipeline.error import PipelineErrors
from logic.libs.exception.exception import AppException


def exec(pipeline_str: str, params: dict[str, any] = {}) -> str:

    id = workingdir_service.create()

    pipeline_str = Template(pipeline_str).render(params)
    pipeline = _get_pipeline_dict(pipeline_str)

    print(pipeline_str)

    try:
        original_workindir = os.getcwd()

        workindir = workingdir_service.fullpath(id)
        os.chdir(workindir)

        for stage in pipeline:

            module_name = stage['module']
            module_path = f'{original_workindir}/{module_service.get_path()}/{module_name}.py'

            if not os.path.exists(module_path):
                msj = f'Module with name as {module_name} not exist'
                raise AppException(PipelineErrors.MODULE_NOT_EXISTS_ERROR, msj)

            spec = spec_from_file_location(module_name, module_path)
            module = module_from_spec(spec)
            spec.loader.exec_module(module)

            module.exec(workindir, stage)

        os.chdir(original_workindir)

    except Exception as e:
        os.chdir(original_workindir)
        workingdir_service.delete(id)
        raise e

    return id


def _get_pipeline_dict(pipeline_str: str) -> dict[str, any]:
    return yaml.load(pipeline_str, Loader=yaml.FullLoader)
