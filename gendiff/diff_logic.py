import json


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    file1_keys = set(file1.keys())
    file2_keys = set(file2.keys())
    keys = list(file1_keys.union(file2_keys))
    keys.sort()
    diff = {}

    for key in keys:
        if (key in file1_keys) and (key in file2_keys):
            if file1[key] == file2[key]:
                new_key = f"  {key}"
                diff[new_key] = file1[key]
            else:
                new_key1 = f"- {key}"
                new_key2 = f"+ {key}"
                diff[new_key1] = file1[key]
                diff[new_key2] = file2[key]

        elif (key in file1_keys) and (key not in file2_keys):
            new_key = f"- {key}"
            diff[new_key] = file1[key]
        elif (key not in file1_keys) and (key in file2_keys):
            new_key = f"+ {key}"
            diff[new_key] = file2[key]

    diff = json.dumps(diff, indent=2)
    diff = diff.replace('"', '')
    diff = diff.replace(',', '')
    return diff
