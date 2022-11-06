from gendiff.diff_logic import generate_diff


def test_generate_diff():
    with open('tests/fixtures/expected_result_1.txt') as file:
        expected_result = file.read()
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file2.json'
    result = generate_diff(file_path1, file_path2)
    assert result == expected_result
