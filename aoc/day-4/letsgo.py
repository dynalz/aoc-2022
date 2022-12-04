from aoc.utils import get_file_input_splitted_by_line

total_fully_range_contained = 0
for line in get_file_input_splitted_by_line(__file__):
    assignments_sections = [
        set(range(*[int(sections.split("-")[0]), int(sections.split("-")[1]) + 1])) for sections in line.split(",")
    ]
    assignments_interceptions = assignments_sections[0].intersection(assignments_sections[1])
    total_fully_range_contained += int(assignments_interceptions in assignments_sections)

print(total_fully_range_contained)
