import os


def get_file_input(path: str) -> str:
    path = os.path.abspath(os.path.dirname(path))
    with open(f"{path}{os.sep}input.txt", "r") as f:
        text = f.read()
    return text


def get_file_input_splitted_by_line(path: str) -> list[str]:
    return get_file_input(path).split("\n")


class LimitedSizeList(object):
    __slots__ = ("list", "next")

    def __init__(self, list_limit):
        self.next = 0
        self.list = [None] * list_limit

    def __iter__(self):
        return iter(self.get_list())

    def append(self, item):
        self.list[self.next % len(self.list)] = item
        self.next += 1

    def get_list(self) -> list:
        if self.next < len(self.list):
            return self.list[: self.next]
        split = self.next % len(self.list)
        return self.list[split:] + self.list[:split]
