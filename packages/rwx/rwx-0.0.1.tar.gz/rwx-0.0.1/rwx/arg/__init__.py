import sys


def split() -> tuple[str, list[str]]:
    command, *arguments = sys.argv
    return command, arguments
