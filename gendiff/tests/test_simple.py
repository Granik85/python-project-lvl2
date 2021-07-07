from ..gendiff import generate_diff


def test_json():
    diff = generate_diff('gendiff/tests/fixtures/test_file1.json',
                         'gendiff/tests/fixtures/test_file2.json')
    assert diff == '{\n    host: "hexlet.io"\n}'


def test_yaml():
    diff = generate_diff('gendiff/tests/fixtures/test_file1.yaml',
                         'gendiff/tests/fixtures/test_file2.yml')
    assert diff == '{\n    host: hexlet.io\n...\n\n}'