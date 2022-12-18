from aoc.utils import get_file_input_splitted_by_line

RIGHT_ORDER = "right_order"
WRONG_ORDER = "wrong_order"


def is_int(x) -> bool:
    return isinstance(x, int)


def is_list(x) -> bool:
    return isinstance(x, list)


def compare_lists(left_list, right_list):
    while len(left_list) and len(right_list):
        left, right = left_list.pop(0), right_list.pop(0)
        if is_int(left):
            if is_int(right):
                if left < right:
                    return RIGHT_ORDER
                elif left > right:
                    return WRONG_ORDER
            elif comparison := compare_lists([left], right):
                return comparison
        elif is_int(right):
            if comparison := compare_lists(left, [right]):
                return comparison
        elif comparison := compare_lists(left, right):
            return comparison
    if len(left_list) < len(right_list):
        return RIGHT_ORDER
    elif len(left_list) > len(right_list):
        return WRONG_ORDER
    return


list_of_two_position = 1
list_of_six_position = 2  # cuz bigger than two

lines = get_file_input_splitted_by_line(__file__)
while lines:
    line = lines.pop(0)
    if not line:  # empty line
        continue
    if not eval(line):  # empty list
        list_of_two_position += 1
        list_of_six_position += 1
        continue

    if compare_lists(eval(line), [[2]]) == RIGHT_ORDER:
        list_of_two_position += 1
    if compare_lists(eval(line), [[6]]) == RIGHT_ORDER:
        list_of_six_position += 1

print(list_of_two_position * list_of_six_position)
