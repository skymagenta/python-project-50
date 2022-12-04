#!/usr/bin/env python
from gendiff.arg_parser import parse_arguments
from gendiff.generate_diff import generate_diff


def main():
    args = parse_arguments()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
