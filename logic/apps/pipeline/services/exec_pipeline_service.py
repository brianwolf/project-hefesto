import os
from importlib.util import module_from_spec, spec_from_file_location
from typing import Dict, List, Tuple
from uuid import UUID

from logic.apps.filesystem.services import workingdir_service
from logic.apps.modules.services import module_service
from logic.apps.pipeline.errors.pipeline_error import PipelineError
from logic.apps.zip.services import zip_service
from logic.libs.exception.exception import AppException


def exec(pipeline: List[Dict[str, any]], zip_name: str = 'project.zip') -> Tuple[UUID, str]:

    id = workingdir_service.create()

    try:
        original_workindir = os.getcwd()
        workindir = workingdir_service.fullpath(id)
        os.chdir(workindir)

        for stage in pipeline:

            module_name = stage['module']
            module_path = f'{original_workindir}/{module_service.get_path()}/{module_name}.py'

            spec = spec_from_file_location(module_name, module_path)
            module = module_from_spec(spec)
            spec.loader.exec_module(module)

            module.exec(workindir, stage)

        os.chdir(original_workindir)

    except Exception as e:

        os.chdir(original_workindir)
        workingdir_service.delete(id)

        msj = str(e)
        raise AppException(PipelineError.EXECUTE_PIPELINE_ERROR, msj, e)

    zip_path = os.path.join(workindir, zip_name)
    zip_service.create(zip_path, workindir)

    return id, zip_path
