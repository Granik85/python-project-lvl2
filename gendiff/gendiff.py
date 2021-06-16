#!/usr/bin/env python
import argparse
import json


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(args)
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


def generate_diff(file_path1, file_path2):
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


if __name__ == '__main__':
    main()
