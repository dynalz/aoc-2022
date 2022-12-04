from aoc.utils import get_file_input_splitted_by_line

ROCK = "ROCK"
PAPER = "PAPER"
SCISSORS = "SCISSORS"

ENCRYPTED_PLAYS = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
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
    opponent_play, us_play = line.split(" ")
    opponent_play = ENCRYPTED_PLAYS[opponent_play]
    if us_play == "X":  # we need to lose
        total_points += LOSE
        total_points += PLAY_MOVE_POINTS[WINNING_GAME[opponent_play]]
    elif us_play == "Y":  # we need to draw
        total_points += DRAW
        total_points += PLAY_MOVE_POINTS[opponent_play]
    elif us_play == "Z":  # we need to win
        total_points += WIN
        for win_play, lose_play in WINNING_GAME.items():
            if lose_play == opponent_play:
                total_points += PLAY_MOVE_POINTS[win_play]


print(total_points)
