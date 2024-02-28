import os


class Project:

    def __init__(self, root_path: str):
        self.root = root_path


def from_root_file(file_path: str):
    project_file = os.path.realpath(file_path)
    project_root = os.path.dirname(project_file)
    return Project(project_root)
