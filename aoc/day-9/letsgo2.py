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
    head: Position
    tail: list[Position]

    def get_head_and_tail_from_index(self, index: int) -> tuple[Position, Position]:
        if index == 0:
            return self.head, self.tail[index]
        return self.tail[index - 1], self.tail[index]

    def does_tail_need_to_move(self, head: Position, tail: Position) -> bool:
        return abs(head.x - tail.x) > 1 or abs(head.y - tail.y) > 1

    def move_tail(self, index=0):
        try:
            head, tail = self.get_head_and_tail_from_index(index)
        except:
            return  # reach end of tail

        if self.does_tail_need_to_move(head, tail):
            if head.x == tail.x:
                tail.play_up() if head.y > tail.y else tail.play_down()
            elif head.y == tail.y:
                tail.play_right() if head.x > tail.x else tail.play_left()
            else:  # diagonals
                if head.x > tail.x:
                    tail.play_right()
                else:
                    tail.play_left()
                if head.y > tail.y:
                    tail.play_up()
                else:
                    tail.play_down()
        self.move_tail(index + 1)

    def add_tail_visited(self):
        self.visited_set.add((tuple(state.tail[-1])))


state = State(set(), Position(0, 0), [Position(0, 0) for _ in range(9)])
state.add_tail_visited()

play_to_callback = {
    "D": state.head.play_down,
    "U": state.head.play_up,
    "L": state.head.play_left,
    "R": state.head.play_right,
}
for line in get_file_input_splitted_by_line(__file__):
    play, moves = line.split(" ")
    move_head_callback = play_to_callback[play]
    for _ in range(int(moves)):
        move_head_callback()
        state.move_tail()
        state.add_tail_visited()

print(len(state.visited_set))
