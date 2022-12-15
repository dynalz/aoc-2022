from aoc.utils import get_file_input_splitted_by_line

map = [[int(char) for char in line] for line in get_file_input_splitted_by_line(__file__)]
row_sizes = len(map)
column_sizes = len(map[0])


def is_visible_from_top(tree_size: int, row_index: int, column_index: int) -> bool:
    if row_index == 0:
        return True
    while row_index:
        row_index -= 1
        if map[row_index][column_index] >= tree_size:
            return False
    return True


def is_visible_from_bottom(tree_size: int, row_index: int, column_index: int) -> bool:
    if row_index == row_sizes:
        return True
    while row_index != row_sizes - 1:
        row_index += 1
        if map[row_index][column_index] >= tree_size:
            return False
    return True


def is_visible_from_right(tree_size: int, row_index: int, column_index: int) -> bool:
    if column_index == column_sizes:
        return True
    while column_index != column_sizes - 1:
        column_index += 1
        if map[row_index][column_index] >= tree_size:
            return False
    return True


def is_visible_from_left(tree_size: int, row_index: int, column_index: int) -> bool:
    if column_index == 0:
        return True
    while column_index:
        column_index -= 1
        if map[row_index][column_index] >= tree_size:
            return False
    return True


# speed ups? No.
visible_trees = 0
for row_index, row in enumerate(map):
    for column_index, tree_size in enumerate(row):
        if is_visible_from_top(tree_size, row_index, column_index):
            visible_trees += 1
        elif is_visible_from_bottom(tree_size, row_index, column_index):
            visible_trees += 1
        elif is_visible_from_right(tree_size, row_index, column_index):
            visible_trees += 1
        elif is_visible_from_left(tree_size, row_index, column_index):
            visible_trees += 1


print(visible_trees)
