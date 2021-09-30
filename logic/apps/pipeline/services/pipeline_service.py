import os
import threading
import time
from importlib.util import module_from_spec, spec_from_file_location
from typing import Dict, List, Tuple
from uuid import UUID

from logic.apps.fs.services import fs_service
from logic.apps.pipeline.errors.pipeline_error import PipelineError
from logic.apps.zip.services import zip_service
from logic.libs.exception.exception import AppException
from logic.libs.logger.logger import logger

_pipelines_runned = []
_thread_garbage_active = True


def exec(pipeline: List[Dict[str, any]]) -> Tuple[UUID, str]:

    id = fs_service.create()

    try:
        original_workindir = os.getcwd()
        workindir = fs_service.fullpath(id)
        os.chdir(workindir)

        for stage in pipeline:

            module_name = stage['module']
            module_path = f'{original_workindir}/logic/apps/modules/{module_name}.py'

            spec = spec_from_file_location(module_name, module_path)
            module = module_from_spec(spec)
            spec.loader.exec_module(module)

            module.exec(workindir, stage)

        os.chdir(original_workindir)

    except Exception as e:

        os.chdir(original_workindir)
        fs_service.delete(id)

        msj = str(e)
        raise AppException(PipelineError.EXECUTE_PIPELINE_ERROR, msj, e)

    zip_path = f'{workindir}/project.zip'
    zip_service.create(zip_path, workindir)

    global _pipelines_runned
    _pipelines_runned.append(id)

    return id, zip_path


def garbabge_collector():

    global _pipelines_runned

    for id in _pipelines_runned:
        fs_service.delete(id)
        logger().info(f'Deleted workingdir -> {id}')

    _pipelines_runned = []


def start_garbage_thread():

    global _thread_garbage_active
    _thread_garbage_active = True

    def thread_method():
        global _thread_garbage_active
        while _thread_garbage_active:
            garbabge_collector()
            time.sleep(30)

    thread = threading.Thread(target=thread_method)
    thread.start()


def stop_garbage_thread():
    global _thread_garbage_active
    _thread_garbage_active = False

start_garbage_thread()
