from gendiff.gendiff import generate_diff


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


def test_json_step6():
    diff = generate_diff('gendiff/tests/fixtures/step6_1.json',
                         'gendiff/tests/fixtures/step6_2.json')
    assert diff == '{\n' \
                   '    common: {\n' \
                   '      + follow: false\n' \
                   '        setting1: Value 1\n' \
                   '      - setting2: 200\n' \
                   '      - setting3: true\n' \
                   '      + setting3: null\n' \
                   '      + setting4: blah blah\n' \
                   '      + setting5: {\n' \
                   '            key5: value5\n' \
                   '        }\n' \
                   '        setting6: {\n' \
                   '            doge: {\n' \
                   '              - wow:\n' \
                   '              + wow: so much\n' \
                   '            }\n' \
                   '            key: value\n' \
                   '          + ops: vops\n' \
                   '        }\n    }\n' \
                   '    group1: {\n' \
                   '      - baz: bas\n' \
                   '      + baz: bars\n' \
                   '        foo: bar\n' \
                   '      - nest: {\n' \
                   '            key: value\n' \
                   '        }\n' \
                   '      + nest: str\n' \
                   '    }\n' \
                   '  - group2: {\n' \
                   '        abc: 12345\n' \
                   '        deep: {\n' \
                   '            id: 45\n' \
                   '        }\n' \
                   '    }\n' \
                   '  + group3: {\n' \
                   '        deep: {\n' \
                   '            id: {\n' \
                   '                number: 45\n' \
                   '            }\n' \
                   '        }\n' \
                   '        fee: 100500\n' \
                   '    }\n' \
                   '}'
