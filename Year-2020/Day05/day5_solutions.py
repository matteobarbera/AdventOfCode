from math import ceil
from my_tools import time_decorator


def seat_bisection(l, u, code):
    _l = l
    _u = u
    key_lower = ("F", "L")
    for c in code:
        if c in key_lower:
            m = int(0.5 * (_l + _u))
            _u = m
        else:
            m = ceil(0.5 * (_l + _u))
            _l = m
    return m


def find_seat(code):
    row_code = code[:7]
    col_code = code[7:]
    row = seat_bisection(0, 127, row_code)
    col = seat_bisection(0, 7, col_code)
    return row, col


def day5_part1():
    with open("day5_input.txt") as f:
        highest_id = 0
        for line in f:
            row, col = find_seat(line.rstrip())
            if (seat_id := row * 8 + col) > highest_id:
                highest_id = seat_id
    return highest_id


@time_decorator
def day5_part2():
    with open("day5_input.txt") as f:
        max_id = 127 * 8 + 8
        ids = []
        for line in f:
            row, col = find_seat(line.rstrip())
            seat_id = row * 8 + col
            ids.append(seat_id)
        missing_ids = set(range(max_id)) - set(ids)
        for seat in missing_ids:
            if seat - 1 in ids and seat + 1 in ids:
                return seat


@time_decorator
def binary_solution():
    # Solution by u/ViliamPucik
    with open("day5_input.txt") as f:
        rule = str.maketrans("FBLR", "0101")
        ids = set(int(s.translate(rule), 2) for s in f)
        lo = min(ids)
        hi = max(ids)
        print(hi, next(i for i in range(lo + 1, hi) if i not in ids))
        # Equivalent to this:
        # for i in range(lo + 1, hi):
        #     if i not in ids:
        #         print(hi, i)


if __name__ == "__main__":
    print("=" * 10 + " Part 1 " + "=" * 10)
    print(f"Highest seat ID: {day5_part1()}")
    print("=" * 10 + " Part 2 " + "=" * 10)
    print(f"My seat: {day5_part2()}")
    binary_solution()
