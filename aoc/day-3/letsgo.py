from string import ascii_letters

from aoc.utils import get_file_input_splitted_by_line

sum_priorities = 0
for line in get_file_input_splitted_by_line(__file__):
    compartment1, compartment2 = set(line[: len(line) // 2]), set(line[len(line) // 2 :])
    for shared_item in compartment1.intersection(compartment2):
        sum_priorities += ascii_letters.index(shared_item) + 1


print(sum_priorities)
