'''
Author: RonaldSun a297131009@qq.com
Date: 2022-05-09 15:31:54
LastEditors: RonaldSun a297131009@qq.com
LastEditTime: 2022-10-11 21:46:32
'''
import argparse
from pathlib import Path


def merge_files(input_files, output_file):
    output = Path(output_file)
    if not output.parent.exists():
        output.parent.mkdir(parents=True, exist_ok=True)
    with open(str(output_file), 'w') as outfile:
        for file in input_files:
            file = str(file)
            with open(file) as infile:
                data = infile.read()
                outfile.write(data)
                if len(data) > 0 and data[-1] != '\n':
                    outfile.write("\n")


def merge_folder():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_folder", nargs='+',
                        help='<Required> folder to merge', required=True)
    parser.add_argument(
        "-o", "--output_folder", help='<Required> output folder', required=True)

    parser.add_argument("-k", "--key", required=False,
                        help='key worlds to choose files to merge')

    args = parser.parse_args()
    file_dict = {}
    total_file_name_set = set()
    for folder in args.input_folder:
        file_name_set = set()
        file_folder = Path(folder)
        files = []
        if args.key is None:
            files = [file for file in file_folder.rglob('*')]
        else:
            files = [file
                     for file in file_folder.rglob('*' + args.key + '*')]
        for file in files:
            file_relative_path = str(file).split(folder)[1]
            file_name_set.add(file_relative_path)
            total_file_name_set.add(file_relative_path)
        file_dict[folder] = file_name_set
    for file_name in total_file_name_set:
        merge_file_list = []
        for folder, file_name_set in file_dict.items():
            if file_name in file_name_set:
                merge_file_list.append(Path(folder) / Path(file_name).name)
        output_file = Path(args.output_folder) / Path(file_name).name
        if len(merge_file_list) > 0:
            merge_files(merge_file_list, output_file)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_files", nargs='+',
                        help='<Required> files to merge', required=True)
    parser.add_argument(
        "-o", "--output_file", help='<Required> output file', required=True)
    args = parser.parse_args()
    merge_files(args.input_files, args.output_file)


if __name__ == '__main__':
    merge_folder()
