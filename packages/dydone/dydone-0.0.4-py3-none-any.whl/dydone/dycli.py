import os

def warn(string: str) -> str:
    return f"\033[1m\033[31m{string}\033[0m"

def info(string: str) -> str:
    return f"\033[1m\033[32m{string}\033[0m"

def indent(lines: str) -> str:
    return os.linesep.join(map(lambda line: f"\t{line}", lines.splitlines()))

def dilemma(info: str, choices: tuple[str, str] = ("yes", "no")) -> bool:
    command = None
    positive, negative = choices
    print(info, end=os.linesep if info.endswith(os.linesep) else os.linesep*2)
    while command not in choices:
        command = input(warn(f"[{positive}/{negative}]: "))
    return command == positive
