from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain


def visualize_diff(diff, format='stylish'):
    """
    diff: list of dict
    diff is internal structure of difference between two configuration files
    """
    if format == 'stylish':
        return get_stylish(diff)
    elif format == 'plain':
        return get_plain(diff)
