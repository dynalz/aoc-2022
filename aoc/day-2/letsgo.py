from aoc.utils import get_file_input_splitted_by_line

ROCK = "ROCK"
PAPER = "PAPER"
SCISSORS = "SCISSORS"

ENCRYPTED_PLAYS = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
}

WINNING_GAME = {
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER,
}

PLAY_MOVE_POINTS = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}

WIN = 6
DRAW = 3
LOSE = 0

total_points = 0
for line in get_file_input_splitted_by_line(__file__):
    opponent_play, us_play = [ENCRYPTED_PLAYS.get(play) for play in line.split(" ")]
    if opponent_play == us_play:
        total_points += DRAW
    elif WINNING_GAME[us_play] == opponent_play:
        total_points += WIN
    else:
        total_points += LOSE  # not needed line but just for compreehension
    total_points += PLAY_MOVE_POINTS[us_play]

print(total_points)
