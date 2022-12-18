import pytest
import os

from gendiff.generate_diff import generate_diff


def get_path_to_file(file_name):
    return os.path.join('tests', 'fixtures', file_name)


@pytest.mark.parametrize('file_name1, file_name2, format, expected_file_name', [
    ('file1.json', 'file2.json', 'stylish', 'stylish.txt'),
    ('file1.json', 'file2.json', 'plain', 'plain.txt'),
    ('file1.json', 'file2.json', 'json', 'json.txt'),
    ('file11.json', 'file22.json', 'stylish', 'stylish_nested.txt'),
    ('file11.json', 'file22.json', 'plain', 'plain_nested.txt'),
    ('file11.json', 'file22.json', 'json', 'json_nested.txt'),

    ('file1.yml', 'file2.yml', 'stylish', 'stylish.txt'),
    ('file1.yml', 'file2.yml', 'plain', 'plain.txt'),
    ('file1.yml', 'file2.yml', 'json', 'json.txt'),
    ('file11.yml', 'file22.yml', 'stylish', 'stylish_nested.txt'),
    ('file11.yml', 'file22.yml', 'plain', 'plain_nested.txt'),
    ('file11.yml', 'file22.yml', 'json', 'json_nested.txt'),

    ('file1.yaml', 'file2.yaml', 'stylish', 'stylish.txt'),
    ('file1.yaml', 'file2.yaml', 'plain', 'plain.txt'),
    ('file1.yaml', 'file2.yaml', 'json', 'json.txt'),
    ('file11.yaml', 'file22.yaml', 'stylish', 'stylish_nested.txt'),
    ('file11.yaml', 'file22.yaml', 'plain', 'plain_nested.txt'),
    ('file11.yaml', 'file22.yaml', 'json', 'json_nested.txt'),
])
def test_generate_diff(file_name1, file_name2, format, expected_file_name):
    file_path1 = get_path_to_file(file_name1)
    file_path2 = get_path_to_file(file_name2)
    expected_file_path = get_path_to_file(expected_file_name)
    with open(expected_file_path) as file:
        expected_result = file.read()
        assert expected_result == generate_diff(file_path1, file_path2, format)
