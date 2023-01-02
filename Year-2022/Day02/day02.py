from myutils import run_test
from data_structures import CircularDLList


def map_move(move: str):
    if move == "A" or move == "X":
        return "R"
    elif move == "B" or move == "Y":
        return "P"
    elif move == "C" or move == "Z":
        return "S"
    else:
        raise ValueError("Invalid move")


class RockPaperScissors:

    moves = CircularDLList("RPS")
    move_value = {"R": 1, "P": 2, "S": 3}

    @classmethod
    def round_outcome(cls, move_1, move_2):
        if move_1 == move_2:
            return 3
        elif move_2 == cls.moves[move_1].next.data:
            return 6
        else:
            return 0

    @classmethod
    def round_score(cls, move_1, move_2):
        return cls.move_value[move_2] + cls.round_outcome(move_1, move_2)

    @classmethod
    def fix_round(cls, move_1, outcome):
        score = 0
        if outcome == "X":  # loss
            my_move = cls.moves[move_1].previous.data
        elif outcome == "Y":  # draw
            score += 3
            my_move = move_1
        else:  # win
            score += 6
            my_move = cls.moves[move_1].next.data
        score += cls.move_value[my_move]
        return score


def read_input(text_file):
    rounds = []
    with open(text_file) as f:
        for line in f.readlines():
            rounds.append(line.split())
    return rounds


@run_test("day02_test.txt", 15)
def day02_part1(day_input: str):
    rounds = read_input(day_input)
    score = 0
    for r in rounds:
        score += RockPaperScissors.round_score(map_move(r[0]), map_move(r[1]))
    return score


@run_test("day02_test.txt", 12)
def day02_part2(day_input: str):
    rounds = read_input(day_input)
    score = 0
    for r in rounds:
        score += RockPaperScissors.fix_round(map_move(r[0]), r[1])
    return score


if __name__ == "__main__":
    print("Part 1:\t", day02_part1("day02.txt"))
    print("Part 2:\t", day02_part2("day02.txt"))
