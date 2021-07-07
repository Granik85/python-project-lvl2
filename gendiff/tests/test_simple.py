from ..gendiff import generate_diff


def test_json():
    diff = generate_diff('gendiff/tests/fixtures/test_file1.json',
                         'gendiff/tests/fixtures/test_file2.json')
    assert diff == '{\n    host: "hexlet.io"\n}'


def test_yaml():
    diff = generate_diff('gendiff/tests/fixtures/test_file0.yaml',
                         'gendiff/tests/fixtures/test_file1.yaml')
    assert diff == '{\n' \
                   '  - follow: false\n' \
                   '    host: hexlet.io\n' \
                   '  - proxy: 123.234.53.22\n' \
                   '  - timeout: 50\n' \
                   '  + timeout: 20\n' \
                   '  + verbose: true\n' \
                   '}'
