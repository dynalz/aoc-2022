from aoc.utils import get_file_input, LimitedSizeList

text = get_file_input(__file__)
signal_detector_list = LimitedSizeList(4)

for index, char in enumerate(text):
    signal_detector_list.append(char)
    if len(set(signal_detector_list)) == 4:
        print(index + 1)
        break
