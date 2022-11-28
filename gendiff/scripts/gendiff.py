#!/usr/bin/env python

from gendiff.arg_parser import parse_arguments
from gendiff.formatter import get_stylish
from gendiff.diff_logic import get_dict, get_diff


def main(stylish='stylish'):
    args = parse_arguments()
    if stylish == 'stylish':
        print(get_stylish(get_diff(*get_dict(args.first_file, args.second_file))))


if __name__ == '__main__':
    main()
