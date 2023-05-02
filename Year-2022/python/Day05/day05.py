from collections import deque
from typing import List

from myutils import run_test


def read_input(day_input, n_stacks):
    stacks = [[] for _ in range(n_stacks)]
    instructions = []
    with open(day_input) as f:
        instructions_reached = False
        for line in f:
            if not instructions_reached:
                if line[1] == '1':
                    next(f)
                    instructions_reached = True
                else:
                    for i in range(n_stacks):
                        try:
                            stacks[i].append(line[1 + i * 4])
                        except IndexError:
                            stacks[i].append(" ")
            else:
                linesplit = line.split()
                instructions.append(list(map(int, [linesplit[1], linesplit[3], linesplit[5]])))
    return stacks, instructions


def build_stacks(s):
    stacks = [deque() for _ in range(len(s))]
    for i, stack in enumerate(s):
        for item in reversed(stack):
            if item != " ":
                stacks[i].append(item)
    return stacks


def move_crate(stacks: List[deque], instruction: List[int]):
    n, start, end = instruction
    for i in range(n):
        stacks[end - 1].append(stacks[start - 1].pop())


def move_crate_v2(stacks: List[deque], instruction: List[int]):
    n, start, end = instruction
    stack = []
    for _ in range(n):
        stack.append(stacks[start - 1].pop())
    stacks[end - 1].extend(reversed(stack))


@run_test("day05_test.txt", "CMZ")
def day05_part1(day_input: str):
    if 'test' in day_input:
        n_stacks = 3
    else:
        n_stacks = 9
    stacks, instructions = read_input(day_input, n_stacks)
    stacks = build_stacks(stacks)
    for instruction in instructions:
        move_crate(stacks, instruction)
    message = ""
    for stack in stacks:
        message += stack.pop()
    return message


@run_test("day05_test.txt", "MCD")
def day05_part2(day_input: str):
    if 'test' in day_input:
        n_stacks = 3
    else:
        n_stacks = 9
    stacks, instructions = read_input(day_input, n_stacks)
    stacks = build_stacks(stacks)
    for instruction in instructions:
        move_crate_v2(stacks, instruction)
    message = ""
    for stack in stacks:
        message += stack.pop()
    return message


if __name__ == "__main__":
    print("Part 1:\t", day05_part1("day05.txt"))
    print("Part 2:\t", day05_part2("day05.txt"))

