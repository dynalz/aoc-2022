from aoc.utils import get_file_input_splitted_by_line

current_folder = None
FOLDER = "folder"
folder_structure = {}
folder_size_map = {}


for index, line in enumerate(get_file_input_splitted_by_line(__file__)):
    if "$ ls" in line:
        continue
    elif "$ cd" in line:
        upcoming_folder = line.split(" ")[-1]
        if upcoming_folder == "..":
            current_folder = current_folder[: current_folder[:-1].rindex("/") + 1]
            continue
        if current_folder:
            folder_structure[current_folder][upcoming_folder] = FOLDER
            current_folder = f"{current_folder}{upcoming_folder}/"
        else:  # first folder we find
            current_folder = upcoming_folder
        if current_folder not in folder_structure:
            folder_structure[current_folder] = {}
    else:
        line_splitted = line.split(" ")
        if line_splitted[0] == "dir":
            folder_structure[current_folder][line_splitted[1]] = FOLDER
        else:
            folder_structure[current_folder][line_splitted[1]] = int(line_splitted[0])


def calculate_folder_size(folder: str):
    if folder in folder_size_map:
        return folder_size_map[folder]

    total_size = 0
    for item, value in folder_structure[folder].items():
        if value == FOLDER:
            total_size += calculate_folder_size(f"{folder}{item}/")
        else:
            total_size += value
    folder_size_map[folder] = total_size
    return total_size


for folder in folder_structure.keys():
    calculate_folder_size(folder)

sum_sizes = sum(size for _, size in folder_size_map.items() if size <= 100000)

print(f"Total size: {sum_sizes}")
