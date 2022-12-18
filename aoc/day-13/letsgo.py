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


packet = 0
sum_packets = 0

lines = get_file_input_splitted_by_line(__file__)
while lines:
    packet += 1
    left, right = eval(lines.pop(0)), eval(lines.pop(0))
    if lines:
        lines.pop(0)

    if compare_lists(left, right) == RIGHT_ORDER:
        sum_packets += packet

print(sum_packets)
