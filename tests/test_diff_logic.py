# from gendiff.diff_logic import generate_diff
# from gendiff.formatter import get_stylish
from gendiff.diff_logic import get_dict, get_diff
from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain


def test_get_stylish_json():
    with open('tests/fixtures/expected1.txt') as file:
        expected_result_1 = file.read()
    with open('tests/fixtures/expected2.txt') as file:
        expected_result_2 = file.read()
    with open('tests/fixtures/expected3.txt') as file:
        expected_result_3 = file.read()
    
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file2.json'
    file_path3 = 'tests/fixtures/file11.json'
    file_path4 = 'tests/fixtures/file22.json'
    result_1 = get_stylish(get_diff(*get_dict(file_path1, file_path2)))
    result_2 = get_stylish(get_diff(*get_dict(file_path3, file_path4)))
    result_3 = get_plain(get_diff(*get_dict(file_path3, file_path4)))
    assert result_1 == expected_result_1
    assert result_2 == expected_result_2
    assert result_3 == expected_result_3


def test_get_stylish_yaml():
    with open('tests/fixtures/expected1.txt') as file:
        expected_result_1 = file.read()
    with open('tests/fixtures/expected2.txt') as file:
        expected_result_2 = file.read()
    with open('tests/fixtures/expected3.txt') as file:
        expected_result_3 = file.read()
    
    file_path1 = 'tests/fixtures/file1.yml'
    file_path2 = 'tests/fixtures/file2.yml'
    file_path3 = 'tests/fixtures/file11.yml'
    file_path4 = 'tests/fixtures/file22.yml'
    result_1 = get_stylish(get_diff(*get_dict(file_path1, file_path2)))
    result_2 = get_stylish(get_diff(*get_dict(file_path3, file_path4)))
    result_3 = get_plain(get_diff(*get_dict(file_path3, file_path4)))
    assert result_1 == expected_result_1
    assert result_2 == expected_result_2
    assert result_3 == expected_result_3
