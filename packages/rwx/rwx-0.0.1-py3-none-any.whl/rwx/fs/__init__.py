import os
import shutil

import ps

CHARSET = 'UTF-8'


def create_image(file_path: str, size_bytes: int):
    ps.run(
        ('qemu-img', 'create'),
        ('-f', 'qcow2'),
        (file_path, size_bytes),
    )


def empty_file(path: str):
    write(path, str())


def get_mount_uuid(path: str):
    return ps.run_line(
        ('findmnt',),
        ('--noheadings',),
        ('--output', 'UUID'),
        (path,),
    )


def get_path_mount(path: str):
    return ps.run_line(
        ('stat',),
        ('--format', '%m'),
        (path,),
    )


def get_path_uuid(path: str):
    return get_mount_uuid(get_path_mount(path))


def make_directory(path: str):
    os.makedirs(path, exist_ok=True)


def read_file(file_path: str):
    with open(file_path, 'br') as file_object:
        return file_object.read()


def read_file_lines(file_path: str, charset=CHARSET):
    return read_file_text(file_path).split(os.linesep)


def read_file_text(file_path: str, charset=CHARSET):
    return read_file(file_path).decode(charset)


def wipe(path: str):
    try:
        shutil.rmtree(path)
    except NotADirectoryError:
        os.remove(path)
    except FileNotFoundError:
        pass


def write(file_path: str, text: str, charset=CHARSET):
    with open(file_path, 'bw') as file_object:
        file_object.write(text.encode(charset))
