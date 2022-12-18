from dataclasses import dataclass
from typing import Callable
from aoc.utils import get_file_input


@dataclass
class MonkeyLogic:
    index: int
    items: list[int]
    operation: Callable
    test: Callable
    test_result_monkey_map: dict[bool, int]
    inspected_times = 0


monkeys: dict[int, MonkeyLogic] = {}
for index, monkey in enumerate(get_file_input(__file__).split("\n\n")):
    monkey_data = monkey.split("\n")
    index = int(monkey_data[0].split(" ")[1].replace(":", ""))
    items = [int(item) for item in monkey_data[1].split(":")[1].replace(" ", "").split(",")]
    operation = monkey_data[2].split("= ")[1]
    test = f"int(item_worry % {monkey_data[3].split(' ')[-1]}) == 0"
    test_result_monkey_map = {True: int(monkey_data[4].split(" ")[-1]), False: int(monkey_data[5].split(" ")[-1])}

    monkey = MonkeyLogic(index, items, operation, test, test_result_monkey_map)
    monkeys[monkey.index] = monkey

rounds = 20
for _ in range(rounds):
    for monkey_index in sorted(monkeys.keys()):
        monkey = monkeys[monkey_index]
        while monkey.items:
            monkey.inspected_times += 1
            old = monkey.items.pop(0)
            item_worry = eval(monkey.operation)
            item_worry = int(item_worry / 3)
            new_monkey_index = monkey.test_result_monkey_map[eval(monkey.test)]
            monkeys[new_monkey_index].items.append(item_worry)


for monkey in monkeys.values():
    print(f"{monkey.index} => {monkey.inspected_times}")
