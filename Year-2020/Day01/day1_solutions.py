from itertools import permutations
from math import prod

from my_tools import time_decorator


def read_input():
    lst = []
    with open("day1_input.txt")as f:
        for line in f:
            lst.append(int(line))
    return lst


@time_decorator
def sum_to_2020(lst: list, n: int):
    for p in permutations(lst, n):
        if sum(p) == 2020:
            print(tuple(p))
            return prod(p)


@time_decorator
def set_solution(lst: list, n: int):
    nums = set(lst)
    for p in permutations(nums, n - 1):
        if (p_sum := sum(p)) >= 2020:
            continue
        if (m := 2020 - p_sum) in nums:
            return prod([m, *p])


if __name__ == "__main__":
    entries = read_input()
    print("="*10 + " Part 1 " + "="*10)
    day1_part1_solution = sum_to_2020(entries, 2)
    part1_other = set_solution(entries, 2)
    print(f"Product of 2020 sum: {day1_part1_solution}")
    print("=" * 10 + " Part 2 " + "=" * 10)
    day1_part2_solution = sum_to_2020(entries, 3)
    part2_other = set_solution(entries, 3)
    assert day1_part2_solution == part2_other
    print(f"Product of 2020 sum: {day1_part2_solution}")
