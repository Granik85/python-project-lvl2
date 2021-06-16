from gendiff.gendiff import generate_diff


def test_simple1():
    diff = generate_diff('gendiff/tests/test_file1.json',
                         'gendiff/tests/test_file2.json')
    assert diff == '{\n    host: "hexlet.io"\n}'
