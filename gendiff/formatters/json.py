import json
from gendiff.dicts_diff import ADDED, DELETED, UNCHANGED, UPDATED, NESTED


def get_json(diff):
    """
    diff: list of dict
    diff is internal structure of difference between two configuration files
    """
    return json.dumps(render_nodes(diff), indent=4)


def render_nodes(diff):

    diff.sort(key=lambda node: node['key'])
    result = {}

    for node in diff:
        if node['node_type'] in (DELETED, UNCHANGED):
            result[node['key']] = {'value': node['value']['old_value']}

        elif node['node_type'] == ADDED:
            result[node['key']] = {'value': node['value']['new_value']}

        elif node['node_type'] == UPDATED:
            result[node['key']] = {
                'value': {
                    'old_value': node['value']['old_value'],
                    'new_value': node['value']['new_value']}}
        elif node['node_type'] == NESTED:
            result[node['key']] = {'value': render_nodes(node['children'])}

        result[node['key']]['node_type'] = node['node_type']

    return result
