import json
import yaml


def generate_diff(file_path1, file_path2):
    type_comparison = check_file_type(file_path1)
    if type_comparison == 'json':
        str_result = '{\n'
        json_minus = json.load(open(file_path1))
        json_plus = json.load(open(file_path2))
        print(type(json_minus))
        keys = set(json_plus)
        keys.update(set(json_minus))
        for item in sorted(keys):
            if json_minus.get(item) is None:
                str_result += '  + ' + item + \
                              ': ' + json.dumps(json_plus.get(item)) + '\n'
            elif json_plus.get(item) is None:
                str_result += '  - ' + item + \
                              ': ' + json.dumps(json_minus.get(item)) + '\n'
            elif json_minus.get(item) != json_plus.get(item):
                str_result += '  - ' + item + \
                              ': ' + json.dumps(json_minus.get(item)) + '\n'
                str_result += '  + ' + item + \
                              ': ' + json.dumps(json_plus.get(item)) + '\n'
            else:
                str_result += '    ' + item + \
                              ': ' + json.dumps(json_plus.get(item)) + '\n'
        str_result += '}'
        return str_result
    elif type_comparison == 'yaml':
        pass


def json_load(file_path):
    pass


def yaml_load(file_path):
    pass


def dump_result(item, file_type='yaml'):
    if file_type == 'json':
        return json.dumps(item)
    return yaml.dump(item)


def check_file_type(file_path: str):
    if file_path.endswith('json'):
        return 'json'
    if file_path.endswith('yaml') or file_path.endswith('yml'):
        return 'yaml'
