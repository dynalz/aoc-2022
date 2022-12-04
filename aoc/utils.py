import os

def get_file_input(path: str) -> str:
    path = os.path.abspath(os.path.dirname(path))
    with open(f"{path}{os.sep}input.txt", "r") as f:
        text = f.read()
    return text

def get_file_input_splitted_by_line(path: str) -> list[str]:
    return get_file_input(path).split("\n")

    