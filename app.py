#!/usr/local/bin/python

import argparse
import logging
import os
import ssl
import sys
from functools import reduce
from sys import exit
from typing import Dict
from urllib.request import urlopen

import yaml

from logic.apps.filesystem import service as filesystem_service
from logic.apps.filesystem import workingdir_service
from logic.apps.pipeline import service as pipline_service

VERSION = "0.1.0"

if len(sys.argv) == 2 and sys.argv[1] in ["--version", "-v"]:
    print(VERSION)
    exit(0)

# ----------------------------------------
# VARIABLES
# ----------------------------------------

parser = argparse.ArgumentParser()

parser.add_argument(
    "-i", help="pipeline yaml path or url (default hefesto.yaml)", required=False)
parser.add_argument("-o", help="folder output", required=False)
parser.add_argument("-p", help="params -p K1=V1,K2=V2", required=False)
parser.add_argument(
    "-f", help="params yaml path (default config.yaml)", required=False)

args = parser.parse_args()

in_path = args.i if args.i else "hefesto.yaml"
out_path = args.o if args.o else None
params_str = args.p if args.p else None
params_path = args.f if args.f else "config.yaml"


# ----------------------------------------
# FUNCTIONS
# ----------------------------------------


def _get_content(yaml_path: str):
    if yaml_path.startswith("http"):
        context = ssl._create_unverified_context()
        f = urlopen(yaml_path, context=context)
        return f.read().decode("utf-8")

    yaml_path = _get_full_path(yaml_path)

    if os.path.exists(yaml_path):
        with open(yaml_path) as f:
            return f.read()

    return ""


def _get_dict(yaml_path: str) -> Dict[str, any]:
    content = _get_content(yaml_path)
    if not content:
        return {}
    return yaml.load(content, Loader=yaml.FullLoader)


def _get_params_dict() -> Dict[str, any]:
    final_dict = {}

    params_dict = {}
    if params_str:
        for kv in params_str.split(","):
            k = kv.split("=")[0]
            v = kv.split("=")[1]
            params_dict[k] = v

    config_dict = {}
    if params_path:
        config_dict = _get_dict(params_path)
        config_dict.update(params_dict)

    final_dict.update(config_dict)
    final_dict.update(params_dict)
    return final_dict


def _dot_to_json(params: dict[str, str]) -> dict[str, object]:
    output = {}
    for key, value in params.items():
        path = key.split('.')
        if path[0] == 'json':
            path = path[1:]
        target = reduce(lambda d, k: d.setdefault(k, {}), path[:-1], output)
        target[path[-1]] = value
    return output


def _get_full_path(path: str) -> str:
    if path and not path.startswith("http") and not path.startswith("/"):
        return f"{os.getcwd()}/{path}"
    return path


# ----------------------------------------
# SCRIPT
# ----------------------------------------

if not os.path.exists(in_path):
    print(f"Pipeline file with path {in_path} not exist")
    exit(1)

try:
    yaml_str = _get_content(in_path)
    params_dict = _dot_to_json(_get_params_dict())

    id = pipline_service.exec(yaml_str, params_dict)

except Exception as e:
    logging.exception(e)
    exit(1)

if out_path:
    filesystem_service.move_file(workingdir_service.fullpath(id), out_path)
