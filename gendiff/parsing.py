import json
import yaml


def generate_diff(file_path1, file_path2):
    file_type = check_file_type(file_path1)

    str_result = '{\n'
    json_minus = file_load(open(file_path1), file_type)
    json_plus = file_load(open(file_path2), file_type)
    print(type(json_minus))
    keys = set(json_plus)
    keys.update(set(json_minus))
    for item in sorted(keys):
        if json_minus.get(item) is None:
            str_result += '  + ' + item + \
                          ': ' + dump_result(json_plus.get(item), file_type) + '\n'
        elif json_plus.get(item) is None:
            str_result += '  - ' + item + \
                          ': ' + dump_result(json_minus.get(item), file_type) + '\n'
        elif json_minus.get(item) != json_plus.get(item):
            str_result += '  - ' + item + \
                          ': ' + dump_result(json_minus.get(item), file_type) + '\n'
            str_result += '  + ' + item + \
                          ': ' + dump_result(json_plus.get(item), file_type) + '\n'
        else:
            str_result += '    ' + item + \
                          ': ' + dump_result(json_plus.get(item), file_type) + '\n'
    str_result += '}'
    return str_result


def file_load(file_path, file_type):
    if file_type == 'json':
        return json.load(file_path)
    return yaml.full_load(file_path)


def dump_result(item, file_type='yaml'):
    if file_type == 'json':
        return json.dumps(item)
    return yaml.dump(item)


def check_file_type(file_path: str):
    if file_path.endswith('json'):
        return 'json'
    if file_path.endswith('yaml') or file_path.endswith('yml'):
        return 'yaml'
