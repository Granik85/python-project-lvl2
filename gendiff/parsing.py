import json
import yaml


def generate_diff(file_path1, file_path2):
    file_type = check_file_type(file_path1)

    str_result = '{\n'
    dict_minus = file_load(open(file_path1), file_type)
    dict_plus = file_load(open(file_path2), file_type)
    keys = set(dict_plus)
    keys.update(set(dict_minus))
    for item in sorted(keys):
        if dict_minus.get(item) is None:
            str_result += '  + ' + item + \
                          ': ' + dump_r(dict_plus.get(item), file_type) + '\n'
        elif dict_plus.get(item) is None:
            str_result += '  - ' + item + \
                          ': ' + dump_r(dict_minus.get(item), file_type) + '\n'
        elif dict_minus.get(item) != dict_plus.get(item):
            str_result += '  - ' + item + \
                          ': ' + dump_r(dict_minus.get(item), file_type) + '\n'
            str_result += '  + ' + item + \
                          ': ' + dump_r(dict_plus.get(item), file_type) + '\n'
        else:
            str_result += '    ' + item + \
                          ': ' + dump_r(dict_plus.get(item), file_type) + '\n'
    str_result += '}'
    return str_result


def file_load(file_path, file_type):
    if file_type == 'json':
        return json.load(file_path)
    return yaml.full_load(file_path)


def dump_r(item, file_type='yaml'):
    if file_type == 'json':
        return json.dumps(item)
    return yaml.dump(item).replace('\n...\n', '')


def check_file_type(file_path: str):
    if file_path.endswith('json'):
        return 'json'
    if file_path.endswith('yaml') or file_path.endswith('yml'):
        return 'yaml'
