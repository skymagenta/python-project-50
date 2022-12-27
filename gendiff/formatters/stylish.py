ADDED = 'added'
DELETED = 'deleted'
UNCHANGED = 'unchanged'
UPDATED = 'updated'

MIDDLE_TEMPLATE = '{indent}{sign} {key}: {value}'
START_TEMPLATE = '{indent}{sign} {key}: {{'
END_TEMPLATE = '{indent}  }}'
FINAL_TEMPLATE = '{{\n{result}\n}}'

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
    return FINAL_TEMPLATE.format(result=result)


def render_nodes(diff, level=1):
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
        result.extend([
            START_TEMPLATE.format(indent=indent, sign=' ', key=node['key']),
            render_nodes(node['children'], level=level + 1),  # dict
            END_TEMPLATE.format(indent=indent)
        ])

    return '\n'.join(result)


def create_line(level, sign, key, value):
    result = []
    indent = get_indent(level)
    level += 1

    if isinstance(value, dict):
        result.extend([
            START_TEMPLATE.format(indent=indent, sign=sign, key=key),
            to_str(value, level),
            END_TEMPLATE.format(indent=indent)
        ])
    else:
        result.append(
            MIDDLE_TEMPLATE.format(
                indent=indent, sign=sign, key=key, value=to_str(value))
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
