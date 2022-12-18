from gendiff.dicts_diff import ADDED, DELETED, UNCHANGED, UPDATED, NESTED

MIDDLE_TEMPLATE = '{}{} {}: {}'
START_TEMPLATE = '{}{} {}: {{'
END_TEMPLATE = '{}  }}'
FINAL_TEMPLATE = '{{\n{}\n}}'

MAX_INDENT = 4
SIGN_INDENT = 2


def get_stylish(diff):
    """
    diff: list of dict
    diff is internal structure of difference between two configuration files
    function render_nodes(diff) return string object: сформированные строки
    эти строки подставляются в шаблон через format
    """
    result = render_nodes(diff)
    return FINAL_TEMPLATE.format(result)


def render_nodes(diff, level=1):  # noqa: C901
    """
    diff: list of dict
    diff is internal structure of difference between two configuration files
    """
    result = []
    indent = get_indent(level)

    for node in diff:
        if node['node_type'] == ADDED:
            result.append(
                create_line(level, '+',
                            node['key'], node['value']['new_value']))
            continue
        if node['node_type'] == DELETED:
            result.append(
                create_line(level, '-', node['key'], node['value']['old_value'])
            )
            continue
        if node['node_type'] == UNCHANGED:
            result.append(
                create_line(level, ' ', node['key'], node['value']['old_value'])
            )
            continue
        if node['node_type'] == UPDATED:
            result.append(
                create_line(level, '-', node['key'], node['value']['old_value'])
            )
            result.append(
                create_line(level, '+', node['key'], node['value']['new_value'])
            )
            continue
        if node['node_type'] == NESTED:
            result.extend([
                START_TEMPLATE.format(indent, ' ', node['key']),  # key: value
                render_nodes(node['children'], level=level + 1),  # dict
                END_TEMPLATE.format(indent)  # ending bracket
            ])

    return '\n'.join(result)


def create_line(level, sign, key, value):
    result = []
    indent = get_indent(level)
    level += 1

    if isinstance(value, dict):
        result.extend([
            START_TEMPLATE.format(indent, sign, key),
            to_str(value, level),
            END_TEMPLATE.format(indent)
        ])
    else:
        result.append(
            MIDDLE_TEMPLATE.format(indent, sign, key, to_str(value))
        )

    return '\n'.join(result)


def to_str(value, level=None):

    if isinstance(value, dict):
        result = []
        for key, dict_value in value.items():
            result.append(create_line(level, ' ', key, dict_value))
        return '\n'.join(result)

    elif isinstance(value, bool):
        return str(value).lower()

    elif value is None:
        return 'null'

    return str(value)


def get_indent(level):
    return ' ' * (MAX_INDENT * level - SIGN_INDENT)
