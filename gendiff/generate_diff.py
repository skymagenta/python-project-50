from gendiff.formatters.visualize_diff import visualize_diff
from gendiff.diff_logic import get_dict, get_diff


def generate_diff(filepath1, filepath2, format='stylish'):
    return visualize_diff(get_diff(*get_dict(filepath1, filepath2)), format)
