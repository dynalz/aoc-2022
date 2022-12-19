import sys

# sys.setrecursionlimit(5000)
from collections import defaultdict
from aoc.utils import get_file_input_splitted_by_line


map_rock = defaultdict(set)
map_sand = defaultdict(set)


def build_rock_path(start: str, end: str):
    start_key, start_sub_key = [int(val) for val in start.split(",")]
    end_key, end_sub_key = [int(val) for val in end.split(",")]
    map_rock[start_key].add(start_sub_key)
    map_rock[end_key].add(end_sub_key)
    if start_key != end_key:
        for key in range(start_key, end_key, 1 if start_key < end_key else -1):
            map_rock[key].add(start_sub_key)
    else:
        for key in range(start_sub_key, end_sub_key, 1 if start_sub_key < end_sub_key else -1):
            map_rock[start_key].add(key)


for line in get_file_input_splitted_by_line(__file__):
    start, end = None, None
    rock_path = line.split(" -> ")
    while rock_path:
        start = end
        end = rock_path.pop(0)
        if not start:
            continue
        build_rock_path(start, end)


first_column_key = min(map_rock.keys())
rows = max([max(row) for row in map_rock.values()])
columns = len(map_rock)


def check_if_position_is_free(position: tuple[int, int]) -> bool:
    if position[1] > rows + 2:
        return False  # hit the floor
    return position[1] not in map_rock[position[0]] and position[1] not in map_sand[position[0]]


def get_next_drop_sand_position(current_sand_position: tuple[int, int]):
    bottom_position = (current_sand_position[0], current_sand_position[1] + 1)
    if check_if_position_is_free(bottom_position):
        return bottom_position
    left_diagonal_position = (current_sand_position[0] - 1, current_sand_position[1] + 1)
    if check_if_position_is_free(left_diagonal_position):
        return left_diagonal_position
    right_diagonal_position = (current_sand_position[0] + 1, current_sand_position[1] + 1)
    if check_if_position_is_free(right_diagonal_position):
        return right_diagonal_position
    return False


def drop_sand(current_sand_position: tuple[int, int]):
    if next_position := get_next_drop_sand_position(current_sand_position):
        return drop_sand(next_position)
    map_sand[current_sand_position[0]].add(current_sand_position[1])
    return current_sand_position


def draw_map(till_row=None, highlight_position: tuple[int, int] = None):
    rock_floor = rows + 2
    for row in range(rock_floor + 1):
        line_draw = ""
        for key in range(first_column_key - 95, first_column_key + columns + 95):
            if row == rock_floor:
                line_draw += "#"
            elif highlight_position and highlight_position == (key, row):
                line_draw += "\033[91mX\033[0m"
            elif row == 0 and key == 500:
                line_draw += "+"
            elif row in map_rock[key]:
                line_draw += "#"
            elif row in map_sand[key]:
                line_draw += "o"
            else:
                line_draw += "."
        print(line_draw)
        if till_row and row == till_row:
            break


sand_dropped = 0
while True:
    position = drop_sand((500, 0))
    sand_dropped += 1
    if position == (500, 0):
        draw_map(highlight_position=position)
        break

print(sand_dropped)
