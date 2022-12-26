from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain
from gendiff.formatters.json import get_json


def apply_diff(diff, format):
    """
    diff: list of dict
    diff is internal structure of difference between two configuration files
    """
    if format == 'stylish':
        return get_stylish(diff)
    if format == 'plain':
        return get_plain(diff)
    if format == 'json':
        return get_json(diff)
    raise ValueError(
        'Format is not supported, use stylish, plain or json format')
