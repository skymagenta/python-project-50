from unittest import result
from gendiff.diff_logic import generate_diff


def test_gendiff():
    with open('tests/fixtures/expected_value_1.txt') as file:
        expected_result = file.read()
    file_path1 = 'gendiff/scripts/file1.json'
    file_path2 = 'gendiff/scripts/file2.json'
    result = generate_diff(file_path1, file_path2)
    assert result == expected_result
