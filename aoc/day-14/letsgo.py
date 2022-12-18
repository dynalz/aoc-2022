from collections import defaultdict
from aoc.utils import get_file_input_splitted_by_line

map = defaultdict(set)


def build_rock_path(start: str, end: str):
    start_key, start_sub_key = [int(val) for val in start.split(",")]
    end_key, end_sub_key = [int(val) for val in end.split(",")]
    map[start_key].add(start_sub_key)
    map[end_key].add(end_sub_key)
    if start_key != end_key:
        for key in range(start_key, end_key, 1 if start_key < end_key else -1):
            map[key].add(start_sub_key)
    else:
        for key in range(start_sub_key, end_sub_key, 1 if start_sub_key < end_sub_key else -1):
            map[start_key].add(key)


for line in get_file_input_splitted_by_line(__file__):
    start, end = None, None
    rock_path = line.split(" -> ")
    while rock_path:
        start = end
        end = rock_path.pop(0)
        if not start:
            continue
        build_rock_path(start, end)


first_column_key = min(map.keys())
columns = len(map)

rows = max([max(row) for row in map.values()])


for row in range(rows + 1):
    line_draw = ""
    for key in range(first_column_key, first_column_key + columns):
        if row == 0 and key == 500:
            line_draw += "+"
        elif row in map[key]:
            line_draw += "#"
        else:
            line_draw += "."
    print(line_draw)


# print(map)
