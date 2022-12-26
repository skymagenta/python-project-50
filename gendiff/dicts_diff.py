ADDED = 'added'
DELETED = 'deleted'
UNCHANGED = 'unchanged'
NESTED = 'nested'
UPDATED = 'updated'


def build_diff(data1, data2):
    dict1_keys = set(data1.keys())
    dict2_keys = set(data2.keys())
    keys = list(dict1_keys.union(dict2_keys))
    keys.sort()
    diff = []

    for key in keys:
        if key in dict1_keys - dict2_keys:
            diff.append(build_node(key, DELETED, old_value=data1[key]))

        elif key in dict2_keys - dict1_keys:
            diff.append(build_node(key, ADDED, new_value=data2[key]))

        elif data1[key] == data2[key]:
            diff.append(build_node(key, UNCHANGED, old_value=data1[key]))

        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            children_diff = build_diff(data1[key], data2[key])
            diff.append(build_node(key, NESTED, children=children_diff))

        else:
            diff.append(build_node(key, UPDATED,
                        old_value=data1[key], new_value=data2[key]))

    return diff


def build_node(key, node_type, old_value=None, new_value=None, children=None):
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
