from os import path
import json
import yaml
from yaml import Loader


def load_data(file_path):
    _, extension = path.splitext(file_path)
    if extension == '.json':
        data = load_json(file_path)
    elif extension in ('.yml', '.yaml'):
        data = load_yaml(file_path)
    return data, extension


def load_json(file_path):
    data = json.load(open(file_path))
    return data


def load_yaml(file_path):
    data = yaml.load(open(file_path), Loader=Loader)
    return data
