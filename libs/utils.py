import os
import importlib
from enum import Enum

def impmod(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def enum2names(enum:Enum):
    return [i.name for i in enum]
