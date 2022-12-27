from os import path
import json
import yaml


def get_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    _, extension = path.splitext(file_path)
    return parse_content(content, extension[1:])


def parse_content(content, content_format):
    """
    content_format is file extension
    """
    if content_format == 'json':
        return json.loads(content)
    elif content_format in ('yml', 'yaml'):
        return yaml.safe_load(content)
    raise ValueError('Extension {} is not supported'.format(content_format))
