from aoc.utils import get_file_input_splitted_by_line

X, sprite_position = 1, 0
drawing = []


def increment_signal():
    global sprite_position, X
    sprite_position += 1
    if sprite_position % 40 in [X, X - 1, X + 1]:
        drawing.append("#")
    else:
        drawing.append(".")


for index, line in enumerate(get_file_input_splitted_by_line(__file__)):
    increment_signal()
    if line == "noop":
        continue
    _, value = line.split(" ")
    increment_signal()
    X += int(value)

for index, char in enumerate(drawing):
    if index % 40 == 0:
        print()
    print(char, end="")
