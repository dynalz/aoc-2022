from dataclasses import dataclass
from aoc.utils import get_file_input_splitted_by_line


@dataclass
class Position:
    x: int
    y: int

    def __str__(self) -> str:
        return f"{self.x},{self.y}"

    def __iter__(self):
        yield self.x
        yield self.y

    def play_down(self):
        self.y -= 1

    def play_up(self):
        self.y += 1

    def play_left(self):
        self.x -= 1

    def play_right(self):
        self.x += 1


@dataclass
class State:
    visited_set: set
    head_position: Position
    tail_position: Position

    def does_tail_need_to_move(self) -> bool:
        return (
            abs(self.head_position.x - self.tail_position.x) > 1 or abs(self.head_position.y - self.tail_position.y) > 1
        )

    def move_tail(self):
        if self.head_position.x == self.tail_position.x:
            if self.head_position.y > self.tail_position.y:
                return self.tail_position.play_up()
            return self.tail_position.play_down()
        elif self.head_position.y == self.tail_position.y:
            if self.head_position.x > self.tail_position.x:
                return self.tail_position.play_right()
            return self.tail_position.play_left()
        else:  # diagonals
            if self.head_position.x > self.tail_position.x:
                self.tail_position.play_right()
            else:
                self.tail_position.play_left()
            if self.head_position.y > self.tail_position.y:
                self.tail_position.play_up()
            else:
                self.tail_position.play_down()

    def add_tail_visited(self):
        self.visited_set.add((tuple(state.tail_position)))


state = State(set(), Position(0, 0), Position(0, 0))
state.add_tail_visited()

play_to_callback = {
    "D": state.head_position.play_down,
    "U": state.head_position.play_up,
    "L": state.head_position.play_left,
    "R": state.head_position.play_right,
}
for line in get_file_input_splitted_by_line(__file__):
    play, moves = line.split(" ")
    move_head_callback = play_to_callback[play]
    for _ in range(int(moves)):
        move_head_callback()
        if state.does_tail_need_to_move():
            state.move_tail()
            state.add_tail_visited()

print(len(state.visited_set))
