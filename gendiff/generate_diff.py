from gendiff.formatters.render_diff import visualize_diff
from gendiff.dicts_diff import get_dict, build_diff


def generate_diff(filepath1, filepath2, format='stylish'):
    return visualize_diff(build_diff(*get_dict(filepath1, filepath2)), format)
