from ..gendiff import generate_diff


def test_simple1():
    diff = generate_diff('gendiff/tests/fixtures/test_file1.json',
                         'gendiff/tests/fixtures/test_file2.json')
    assert diff == '{\n    host: "hexlet.io"\n}'
