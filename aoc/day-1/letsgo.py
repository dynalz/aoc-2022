from aoc.utils import get_file_input_splitted_by_line


max_calories = 0
current_calories = 0
for line in get_file_input_splitted_by_line(__file__):
    if not line:
        if current_calories > max_calories:
            max_calories = current_calories
        current_calories = 0
        continue
    current_calories += int(line)

print(max_calories)
