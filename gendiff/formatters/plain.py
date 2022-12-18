from gendiff.dicts_diff import ADDED, DELETED, UPDATED, NESTED

TEMPLATE_ADDED = "Property '{}' was added with value: {}"
TEMPLATE_DELETED = "Property '{}' was removed"
TEMPLATE_UPDATED = "Property '{}' was updated. From {} to {}"
TEMPLATE_PATH = "{}.{}"


def get_plain(diff, activate=''):  # noqa: C901
    diff.sort(key=lambda node: node['key'])
    result = []

    for node in diff:
        if not activate:
            path = node['key']
        else:
            path = TEMPLATE_PATH.format(activate, node['key'])

        if node['node_type'] == ADDED:
            result.append(TEMPLATE_ADDED.format(
                path,
                to_str(node['value']['new_value'])
            ))

        elif node['node_type'] == DELETED:
            result.append(TEMPLATE_DELETED.format(path))

        elif node['node_type'] == UPDATED:
            result.append(TEMPLATE_UPDATED.format(
                path,
                to_str(node['value']['old_value']),
                to_str(node['value']['new_value'])
            ))

        elif node['node_type'] == NESTED:
            result.append(get_plain(node['children'], activate=path))

    return '\n'.join(result)


def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, int):
        return str(value)
    elif isinstance(value, dict):
        return '[complex value]'
    else:
        return f"'{value}'"
