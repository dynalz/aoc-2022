import sys

sys.setrecursionlimit(5000)

import string
import contextlib
from dataclasses import dataclass, field
from aoc.utils import get_file_input_splitted_by_line


@dataclass
class Path:
    path: list = field(default_factory=list)
    visited_locations: set = field(default_factory=set)


GOAL, START = "E", "a"
start_positions = []

map: list[list] = []
solutions: list[Path] = []
shortest_visited_locations: dict[tuple[int], int] = {}
location_allowed_to_visit_map = {
    letter: set(string.ascii_lowercase[: index + 2]) for index, letter in enumerate(string.ascii_lowercase)
}
location_allowed_to_visit_map["y"].add("E")
location_allowed_to_visit_map["z"].add("E")
location_allowed_to_visit_map[START] = location_allowed_to_visit_map["a"]


for row, line in enumerate(get_file_input_splitted_by_line(__file__)):
    map.append(list(line))
    if START in line:
        start_positions.append((row, line.index(START)))

LONGEST_PATH = len(map) * len(map[0])


def get_possible_next_position(position: tuple[int]) -> list[tuple]:
    current_position_height = map[position[0]][position[1]]
    positions_to_test, possible_positions = [], []
    positions_to_test.extend(
        (
            (position[0] - 1, position[1]),
            (position[0] + 1, position[1]),
            (position[0], position[1] - 1),
            (position[0], position[1] + 1),
        )
    )
    for new_position in positions_to_test:
        with contextlib.suppress(Exception):  # prevents from testing off limit positions
            if new_position[0] < 0 or new_position[1] < 0:  # negative indexes work on python so no exception is thrown
                continue
            if map[new_position[0]][new_position[1]] in [START, "S"]:
                continue  # if next position is a then we could have started here
            if map[new_position[0]][new_position[1]] in location_allowed_to_visit_map[current_position_height]:
                possible_positions.append(new_position)
                continue
    return possible_positions


def find_solutions(current_position: tuple, path: Path):
    if map[current_position[0]][current_position[1]] == GOAL:
        solutions.append(path)
        return
    next_positions = get_possible_next_position(current_position)
    for next_position in next_positions:
        if next_position in path.visited_locations:
            continue
        steps_to_reach_next_position = len(path.path) + 1
        if steps_to_reach_next_position >= shortest_visited_locations.get(next_position, LONGEST_PATH):
            continue
        shortest_visited_locations[next_position] = steps_to_reach_next_position
        find_solutions(
            next_position,
            Path(path=list(path.path) + [next_position], visited_locations=path.visited_locations | {next_position}),
        )


for start_position in start_positions:
    find_solutions(start_position, Path())

best_solution = min([len(solution.path) for solution in solutions])
print(f"Solution: {best_solution}")
