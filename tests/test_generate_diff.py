import pytest

from gendiff.generate_diff import generate_diff


def get_path_to_file(file_name):
    return 'tests/fixtures/' + file_name


@pytest.mark.parametrize('file_path1, file_path2, format, expected_file_path', [
    (get_path_to_file('file1.json'), get_path_to_file('file2.json'), 'stylish', get_path_to_file('stylish.txt')),
    (get_path_to_file('file1.json'), get_path_to_file('file2.json'), 'plain', get_path_to_file('plain.txt')),
    (get_path_to_file('file1.json'), get_path_to_file('file2.json'), 'json', get_path_to_file('json.txt')),
    (get_path_to_file('file11.json'), get_path_to_file('file22.json'), 'stylish', get_path_to_file('stylish_nested.txt')),
    (get_path_to_file('file11.json'), get_path_to_file('file22.json'), 'plain', get_path_to_file('plain_nested.txt')),
    (get_path_to_file('file11.json'), get_path_to_file('file22.json'), 'json', get_path_to_file('json_nested.txt')),

    (get_path_to_file('file1.yml'), get_path_to_file('file2.yml'), 'stylish', get_path_to_file('stylish.txt')),
    (get_path_to_file('file1.yml'), get_path_to_file('file2.yml'), 'plain', get_path_to_file('plain.txt')),
    (get_path_to_file('file1.yml'), get_path_to_file('file2.yml'), 'json', get_path_to_file('json.txt')),
    (get_path_to_file('file11.yml'), get_path_to_file('file22.yml'), 'stylish', get_path_to_file('stylish_nested.txt')),
    (get_path_to_file('file11.yml'), get_path_to_file('file22.yml'), 'plain', get_path_to_file('plain_nested.txt')),
    (get_path_to_file('file11.yml'), get_path_to_file('file22.yml'), 'json', get_path_to_file('json_nested.txt')),

    (get_path_to_file('file1.yaml'), get_path_to_file('file2.yaml'), 'stylish', get_path_to_file('stylish.txt')),
    (get_path_to_file('file1.yaml'), get_path_to_file('file2.yaml'), 'plain', get_path_to_file('plain.txt')),
    (get_path_to_file('file1.yaml'), get_path_to_file('file2.yaml'), 'json', get_path_to_file('json.txt')),
    (get_path_to_file('file11.yaml'), get_path_to_file('file22.yaml'), 'stylish', get_path_to_file('stylish_nested.txt')),
    (get_path_to_file('file11.yaml'), get_path_to_file('file22.yaml'), 'plain', get_path_to_file('plain_nested.txt')),
    (get_path_to_file('file11.yaml'), get_path_to_file('file22.yaml'), 'json', get_path_to_file('json_nested.txt')),
])
def test_generate_diff(file_path1, file_path2, format, expected_file_path):
    with open(expected_file_path) as file:
        expected_result = file.read()
        assert expected_result == generate_diff(file_path1, file_path2, format)
