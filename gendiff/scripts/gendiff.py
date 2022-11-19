#!/usr/bin/env python
# import argparse
from gendiff.diff_logic import generate_diff
from gendiff.arg_parser import parse_arguments

# parser = argparse.ArgumentParser(
#     description='Compares two configuration files and shows a difference.')
# parser.add_argument('first_file')
# parser.add_argument('second_file')
# parser.add_argument('-f', '--format', help='set format of output')
# args = parser.parse_args()


def main():
    args = parse_arguments()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
