from gendiff.diff_logic import ADDED, DELETED, UNCHANGED, UPDATED, NESTED

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
    diff.sort(key=lambda node: node['key'])
    result = []
    indent = get_indent(level)

    for node in diff:
        if node['node_type'] == ADDED:
            result.append(
                create_line(level, '+',
                            node['key'], node['value']['new_value']))
        elif node['node_type'] == DELETED:
            result.append(
                create_line(level, '-', node['key'], node['value']['old_value'])
            )
        elif node['node_type'] == UNCHANGED:
            result.append(
                create_line(level, ' ', node['key'], node['value']['old_value'])
            )
        elif node['node_type'] == UPDATED:
            result.append(
                create_line(level, '-', node['key'], node['value']['old_value'])
            )
            result.append(
                create_line(level, '+', node['key'], node['value']['new_value'])
            )
        elif node['node_type'] == NESTED:
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
            formate_dict_value(value, level),
            END_TEMPLATE.format(indent)
        ])
    else:
        result.append(
            MIDDLE_TEMPLATE.format(indent, sign, key, get_valid_value(value))
        )

    return '\n'.join(result)


def formate_dict_value(dict_value, level):
    result = []
    for key, value in dict_value.items():
        result.append(create_line(level, ' ', key, value))
    return '\n'.join(result)


def get_valid_value(value):
    if isinstance(value, bool):
        valid_value = str(value).lower()
    elif value is None:
        valid_value = 'null'
    else:
        valid_value = str(value)
    return valid_value


def get_indent(level):
    return ' ' * (MAX_INDENT * level - SIGN_INDENT)
