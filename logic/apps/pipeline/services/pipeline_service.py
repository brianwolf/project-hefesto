import os
from importlib.util import module_from_spec, spec_from_file_location
from typing import Dict, List, Tuple
from uuid import UUID

from logic.apps.fs.services import fs_service
from logic.apps.pipeline.errors.pipeline_error import PipelineError
from logic.apps.zip.services import zip_service
from logic.libs.exception.exception import AppException


def exec(pipeline: List[Dict[str, any]]) -> Tuple[UUID, str]:

    id = fs_service.create()

    try:
        for stage in pipeline:

            module_name = stage['module']
            module_path = f'logic/apps/modules/{module_name}.py'

            spec = spec_from_file_location(module_name, module_path)
            module = module_from_spec(spec)
            spec.loader.exec_module(module)

            original_workindir = os.getcwd()
            workindir = fs_service.fullpath(id)

            os.chdir(workindir)
            module.exec(workindir, stage)
            os.chdir(original_workindir)

    except Exception as e:
        fs_service.delete(id)
        msj = str(e)
        raise AppException(PipelineError.EXECUTE_PIPELINE_ERROR, msj, e)

    zip_path = f'{workindir}/project.zip'
    zip_service.create(zip_path, workindir)

    return id, zip_path
