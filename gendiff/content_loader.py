from os import path
import json
import yaml
from yaml import Loader


def get_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    _, extension = path.splitext(file_path)
    return content, extension.lower()


def parse_content(content, content_format):
    """
    content_format is file extension
    """
    if content_format == '.json':
        return json.loads(content)
    elif content_format in ('.yml', '.yaml'):
        return yaml.load(content, Loader=Loader)
    raise ValueError('Extension {} is not supported'.format(content_format))
