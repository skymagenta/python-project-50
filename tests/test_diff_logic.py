from gendiff.diff_logic import generate_diff


def test_generate_diff():
    with open('tests/fixtures/expected.txt') as file:
        expected_result = file.read()
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file2.json'
    result = generate_diff(file_path1, file_path2)
    assert result == expected_result


def test_generate_diff_yaml():
    with open('tests/fixtures/expected.txt') as file:
        expected_result = file.read()
    file_path1 = 'tests/fixtures/file1.yml'
    file_path2 = 'tests/fixtures/file2.yml'
    result = generate_diff(file_path1, file_path2)
    assert result == expected_result
