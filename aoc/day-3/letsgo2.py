from string import ascii_letters

from aoc.utils import get_file_input_splitted_by_line


lines = []
sum_priorities = 0
for line in get_file_input_splitted_by_line(__file__):
    lines.append(set(line))
    if len(lines) != 3:
        continue
    intersection: set = lines[0]
    for line in lines[1:]:
        intersection = intersection.intersection(line)

    shared_item = intersection.pop()
    sum_priorities += ascii_letters.index(shared_item) + 1
    lines = []


print(sum_priorities)
