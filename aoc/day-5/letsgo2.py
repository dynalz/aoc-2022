from aoc.utils import get_file_input_splitted_by_line

state = {}
state_lines = []


def build_state():
    columns = state_lines.pop()
    column_to_index = {}
    for index, column in enumerate(columns):
        if column == " ":
            continue
        column_to_index[index] = column
        state[column] = []
    state_lines.reverse()
    for line in state_lines:
        for index, char in enumerate(line):
            if char in "[] ":
                continue
            column = column_to_index[index]
            state[column].append(char)


def move_crates(how_many: int, from_crate: str, to_crate: str):
    crates_to_move = [state[from_crate].pop() for _ in range(how_many)]
    crates_to_move.reverse()
    state[to_crate].extend(crates_to_move)


for line in get_file_input_splitted_by_line(__file__):
    if line == "":
        build_state()
        continue
    if not state:
        state_lines.append(line)
        continue
    move_parsed = line.split(" ")
    move_crates(int(move_parsed[1]), move_parsed[3], move_parsed[5])

print("".join([queue[-1] for queue in state.values()]))
