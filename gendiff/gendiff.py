#!/usr/bin/env python
import argparse

from gendiff.parsing import check_file_type, file_load, diff
from gendiff.formatters.format_diff import format_diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    file_type = check_file_type(file_path1)

    dict_minus = file_load(open(file_path1), file_type)
    dict_plus = file_load(open(file_path2), file_type)
    list_diff = diff(dict_minus, dict_plus)
    return format_diff(list_diff, format_name)


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish', help='set format of output')
    args = parser.parse_args()
    # print(args)
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
