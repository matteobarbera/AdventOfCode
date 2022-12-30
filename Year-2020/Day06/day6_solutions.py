def day6_part1():
    with open("day6_input.txt") as f:
        answer_sum = 0
        answers = ''
        for line in f:
            if not (l := line.rstrip()):
                answer_sum += len(set(answers))
                answers = ''
            else:
                answers += l
        answer_sum += len(set(answers))
    return answer_sum


def day6_part2():
    with open("day6_input.txt") as f:
        answer_sum = 0
        answers_reset = set(chr(i) for i in range(ord('a'), ord('z') + 1))
        answers = answers_reset.copy()
        for line in f:
            if not (l := line.rstrip()):
                answer_sum += len(answers)
                answers = answers_reset.copy()
            else:
                answers.intersection_update(set(l))
        answer_sum += len(set(answers))
    return answer_sum


if __name__ == "__main__":
    print("=" * 10 + " Part 1 " + "=" * 10)
    print(f"Sum of answers: {day6_part1()}")
    print("=" * 10 + " Part 2 " + "=" * 10)
    print(f"Sum of answers: {day6_part2()}")
