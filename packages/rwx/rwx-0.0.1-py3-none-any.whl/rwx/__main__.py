#! /usr/bin/env python3

import os

import fs


if __name__ == '__main__':
    file_path = os.path.realpath(__file__)
    root_path = os.path.dirname(file_path)
    directory_path = os.path.join(root_path, 'tmp')
    file_path = os.path.join(directory_path, 'file')

    fs.wipe(directory_path)
    fs.make_directory(directory_path)
    fs.write(file_path, 'Martine écrit beaucoup.')
    fs.empty_file(file_path)
    fs.write(file_path, 'Martine écrit moins.')
