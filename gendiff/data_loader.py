from os import path
import json
import yaml
from yaml import Loader


def get_file_extension(file_path):
    _, extension = path.splitext(file_path)
    return extension.lower()


def get_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content, get_file_extension(file_path)


def load_content(content, content_format):
    """
    content_format is file extension
    """
    if content_format == '.json':
        return load_json(content)
    elif content_format in ('.yml', '.yaml'):
        return load_yaml(content)
    else:
        raise ValueError('Extension {} is not supported'.format(content_format))


def load_json(file_path):
    data = json.loads(file_path)
    return data


def load_yaml(file_path):
    """
    convert yaml document to dict
    """
    data = yaml.load(file_path, Loader=Loader)
    return data
