from aoc.utils import get_file_input_splitted_by_line

map = [[int(char) for char in line] for line in get_file_input_splitted_by_line(__file__)]
row_sizes = len(map)
column_sizes = len(map[0])


def score_from_top(tree_size: int, row_index: int, column_index: int) -> int:
    viewing_trees = 0
    while row_index:
        row_index -= 1
        viewing_trees += 1
        if map[row_index][column_index] >= tree_size:
            break
    return viewing_trees


def score_from_bottom(tree_size: int, row_index: int, column_index: int) -> int:
    viewing_trees = 0
    while row_index != row_sizes - 1:
        row_index += 1
        viewing_trees += 1
        if map[row_index][column_index] >= tree_size:
            break
    return viewing_trees


def score_from_right(tree_size: int, row_index: int, column_index: int) -> int:
    viewing_trees = 0
    while column_index != column_sizes - 1:
        column_index += 1
        viewing_trees += 1
        if map[row_index][column_index] >= tree_size:
            break
    return viewing_trees


def score_from_left(tree_size: int, row_index: int, column_index: int) -> int:
    viewing_trees = 0
    while column_index:
        column_index -= 1
        viewing_trees += 1
        if map[row_index][column_index] >= tree_size:
            break
    return viewing_trees


# speed ups? No.
max_score = 0
for row_index, row in enumerate(map):
    for column_index, tree_size in enumerate(row):
        args = [tree_size, row_index, column_index]
        scenic_score = (
            score_from_top(*args) * score_from_bottom(*args) * score_from_left(*args) * score_from_right(*args)
        )
        if scenic_score > max_score:
            max_score = scenic_score

print(max_score)
