import subprocess

import txt


def get_tuples_args(tuples) -> list[str]:
    args: list[str] = []
    for item in tuples:
        if type(item) is tuple:
            args.extend(item)
        else:
            args.append(item)
    return args


def run(*tuples) -> subprocess.CompletedProcess:
    return subprocess.run(get_tuples_args(tuples), capture_output=False)


def run_line(*tuples, charset: str = txt.CHARSET) -> str:
    lines = run_lines(*get_tuples_args(tuples), charset=charset)
    return lines[0]


def run_lines(*tuples, charset: str = txt.CHARSET) -> list[str]:
    process = subprocess.run(get_tuples_args(tuples), capture_output=True)
    string = process.stdout.decode(charset)
    return string.rstrip().splitlines()
