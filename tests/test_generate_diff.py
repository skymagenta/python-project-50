import pytest

from gendiff.generate_diff import generate_diff

JSON1 = 'tests/fixtures/file1.json'
JSON2 = 'tests/fixtures/file2.json'
JSON1_NESTED = 'tests/fixtures/file11.json'
JSON2_NESTED = 'tests/fixtures/file22.json'
YML1 = 'tests/fixtures/file1.yml'
YML2 = 'tests/fixtures/file2.yml'
YML1_NESTED = 'tests/fixtures/file11.yml'
YML2_NESTED = 'tests/fixtures/file22.yml'
YAML1 = 'tests/fixtures/file1.yaml'
YAML2 = 'tests/fixtures/file2.yaml'
YAML1_NESTED = 'tests/fixtures/file11.yaml'
YAML2_NESTED = 'tests/fixtures/file22.yaml'

EXPECTED_STYLISH = 'tests/fixtures/stylish.txt'
EXPECTED_STYLISH_NESTED = 'tests/fixtures/stylish_nested.txt'
EXPECTED_PLAIN = 'tests/fixtures/plain.txt'
EXPECTED_PLAIN_NESTED = 'tests/fixtures/plain_nested.txt'
EXPECTED_JSON = 'tests/fixtures/json.txt'
EXPECTED_JSON_NESTED = 'tests/fixtures/json_nested.txt'


@pytest.mark.parametrize('file_path1, file_path2, format, expexted_file_path', [
    (JSON1, JSON2, 'stylish', EXPECTED_STYLISH),
    (JSON1, JSON2, 'plain', EXPECTED_PLAIN),
    (JSON1, JSON2, 'json', EXPECTED_JSON),
    (JSON1_NESTED, JSON2_NESTED, 'stylish', EXPECTED_STYLISH_NESTED),
    (JSON1_NESTED, JSON2_NESTED, 'plain', EXPECTED_PLAIN_NESTED),
    (JSON1_NESTED, JSON2_NESTED, 'json', EXPECTED_JSON_NESTED),

    (YML1, YML2, 'stylish', EXPECTED_STYLISH),
    (YML1, YML2, 'plain', EXPECTED_PLAIN),
    (YML1, YML2, 'json', EXPECTED_JSON),
    (YML1_NESTED, YML2_NESTED, 'stylish', EXPECTED_STYLISH_NESTED),
    (YML1_NESTED, YML2_NESTED, 'plain', EXPECTED_PLAIN_NESTED),
    (YML1_NESTED, YML2_NESTED, 'json', EXPECTED_JSON_NESTED),

    (YAML1, YAML2, 'stylish', EXPECTED_STYLISH),
    (YAML1, YAML2, 'plain', EXPECTED_PLAIN),
    (YAML1, YAML2, 'json', EXPECTED_JSON),
    (YAML1_NESTED, YAML2_NESTED, 'stylish', EXPECTED_STYLISH_NESTED),
    (YAML1_NESTED, YAML2_NESTED, 'plain', EXPECTED_PLAIN_NESTED),
    (YAML1_NESTED, YAML2_NESTED, 'json', EXPECTED_JSON_NESTED)
])

def test_generate_diff(file_path1, file_path2, format, expexted_file_path):
    with open(expexted_file_path) as file:
        expected_result = file.read()
    assert expected_result == generate_diff(file_path1, file_path2, format)
