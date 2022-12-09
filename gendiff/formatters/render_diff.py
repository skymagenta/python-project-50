from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain
from gendiff.formatters.json import get_json


def visualize_diff(diff, format):
    """
    diff: list of dict
    diff is internal structure of difference between two configuration files
    """
    if format == 'stylish':
        return get_stylish(diff)
    elif format == 'plain':
        return get_plain(diff)
    elif format == 'json':
        return get_json(diff)
    else:
        raise ValueError(
            'Format is not supported, use stylish, plain or json format')
