from gendiff.formatters.render_diff import apply_diff
from gendiff.content_loader import get_content
from gendiff.dicts_diff import build_diff


def generate_diff(filepath1, filepath2, format='stylish'):
    dict1 = get_content(filepath1)
    dict2 = get_content(filepath2)
    return apply_diff(build_diff(dict1, dict2), format)
