from aoc.utils import get_file_input_splitted_by_line

X, current_signal, sum_signals = 1, 0, 0
cycle_signal_capture = {20, 60, 100, 140, 180, 220}


def increment_signal():
    global X, sum_signals, current_signal
    current_signal += 1
    if current_signal in cycle_signal_capture:
        sum_signals += current_signal * X


for index, line in enumerate(get_file_input_splitted_by_line(__file__)):
    increment_signal()
    if line == "noop":
        continue
    _, value = line.split(" ")
    increment_signal()
    X += int(value)

print(f"Total size: {sum_signals}")
