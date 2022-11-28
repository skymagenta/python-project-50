import json
import yaml
from gendiff.data_loader import load_data

ADDED = 'added'
DELETED = 'deleted'
UNCHANGED = 'unchanged'
NESTED = 'nested'
UPDATED = 'updated'


def get_dict(file_path1, file_path2):
    dict1, extension = load_data(file_path1)
    dict2, extension = load_data(file_path2)
    return dict1, dict2


def get_diff(dict1, dict2):
    dict1_keys = set(dict1.keys())
    dict2_keys = set(dict2.keys())
    keys = list(dict1_keys.union(dict2_keys))
    keys.sort()
    diff = []
    
    for key in keys:
        if (key in dict1_keys) and (key not in dict2_keys):
            diff.append(get_node(key, DELETED, old_value=dict1[key]))

        elif (key not in dict1_keys) and (key in dict2_keys):
            diff.append(get_node(key, ADDED, new_value=dict2[key]))

        elif dict1[key] == dict2[key]:
            diff.append(get_node(key, UNCHANGED, old_value=dict1[key]))

        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            children_diff = get_diff(dict1[key], dict2[key])
            diff.append(get_node(key, NESTED, children=children_diff))

        else:
            diff.append(get_node(key, UPDATED, old_value=dict1[key], new_value=dict2[key]))

    return diff


def get_node(key, node_type, old_value=None, new_value=None, children=None):
    node = {
        'key': key,
        'node_type': node_type,
        'value': {
            'old_value': old_value,
            'new_value': new_value
        }
    }
    if children is not None:
        node['children'] = children
    
    return node
