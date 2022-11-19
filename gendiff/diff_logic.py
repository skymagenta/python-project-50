import json
import yaml
from gendiff.data_loader import load_data


def generate_diff(file_path1, file_path2):
    data1, extension = load_data(file_path1)
    data2, extension = load_data(file_path2)
    if extension == '.json':
        return generate_diff_json(data1, data2)
    elif extension in ('.yml', '.yaml'):
        return generate_diff_yaml(data1, data2)


def generate_diff_json(dict1, dict2): # noqa: C901
    dict1_keys = set(dict1.keys())
    dict2_keys = set(dict2.keys())
    keys = list(dict1_keys.union(dict2_keys))
    keys.sort()
    diff = {}

    for key in keys:
        if (key in dict1_keys) and (key in dict2_keys):
            if dict1[key] == dict2[key]:
                new_key = f"  {key}"
                diff[new_key] = dict1[key]
            else:
                new_key1 = f"- {key}"
                new_key2 = f"+ {key}"
                diff[new_key1] = dict1[key]
                diff[new_key2] = dict2[key]

        elif (key in dict1_keys) and (key not in dict2_keys):
            new_key = f"- {key}"
            diff[new_key] = dict1[key]
        elif (key not in dict1_keys) and (key in dict2_keys):
            new_key = f"+ {key}"
            diff[new_key] = dict2[key]

    diff = json.dumps(diff, indent=2)
    diff = diff.replace('"', '')
    diff = diff.replace(',', '')
    return diff


def generate_diff_yaml(dict1, dict2): # noqa: C901
    dict1_keys = set(dict1.keys())
    dict2_keys = set(dict2.keys())
    keys = list(dict1_keys.union(dict2_keys))
    keys.sort()
    diff = {}

    for key in keys:
        if (key in dict1_keys) and (key in dict2_keys):
            if dict1[key] == dict2[key]:
                new_key = f"  {key}"
                diff[new_key] = dict1[key]
            else:
                new_key1 = f"- {key}"
                new_key2 = f"+ {key}"
                diff[new_key1] = dict1[key]
                diff[new_key2] = dict2[key]

        elif (key in dict1_keys) and (key not in dict2_keys):
            new_key = f"- {key}"
            diff[new_key] = dict1[key]
        elif (key not in dict1_keys) and (key in dict2_keys):
            new_key = f"+ {key}"
            diff[new_key] = dict2[key]

    diff = yaml.dump(diff, indent=2, sort_keys=False)
    diff = diff.replace('"', '')
    diff = diff.replace("'", '')
    diff_list = diff.split(sep='\n')
    changed_diff_list = change_list_items(diff_list)
    diff = '\n'.join(changed_diff_list)
    diff = '{\n' + diff + '\n}'
    return diff


def change_list_items(items):
    result = []
    for item in items:
        if item:
            new_item = '  ' + item
            result.append(new_item)
    return result
