import numpy as np


def encode_seats() -> np.ndarray:
    with open("day11_input.txt") as f:
        seats = []
        for row, line in enumerate(f):
            for seat in line.rstrip("\n"):
                if seat == "L":
                    seats.append(0)
                else:
                    seats.append(2)
        seats = np.asarray(seats).reshape(row + 1, len(seats) // (row + 1))
    return seats


def check_neighbours(seats: np.ndarray, x: int, y: int) -> int:
    """Returns number of occupied neighbour seats"""
    occupied_ctr = 0
    for i in [x - 1, x, x + 1]:
        for j in [y - 1, y, y + 1]:
            if i < 0 or j < 0:
                continue
            try:
                if seats[i, j] == 1 and (i, j) != (x, y):
                    occupied_ctr += 1
            except IndexError:
                pass
    return occupied_ctr


def check_neighbours2(seats: np.ndarray, x: int, y: int) -> int:
    """Returns number of occupied neighbour seats"""
    occupied_ctr = 0
    m, n = seats.shape
    d_row = y - x
    d_inv_row = n - 1 - (y + x)
    d = seats.diagonal(d_row)
    d_inv = np.fliplr(seats).diagonal(d_inv_row)
    slices = [seats[x, :y][::-1], seats[x, y+1:], seats[:x, y][::-1], seats[x+1:, y]]
    if d_row > 0:
        slices += [d[:x][::-1], d[x+1:]]
    else:
        slices += [d[:y][::-1], d[y+1:]]
    if x + y <= n - 1:
        slices += [d_inv[:x][::-1], d_inv[x+1:]]
    else:
        slices += [d_inv[:n-1-y][::-1], d_inv[n-y:]]
    for s in slices:
        try:
            if s[s != 2][0] == 1:
                occupied_ctr += 1
        except IndexError:
            pass
    return occupied_ctr


def print_seats(seats: np.ndarray):
    d = {0: "L", 1: "#", 2: "."}
    for row in seats:
        s = ""
        for seat in row:
            s += d[seat]
        print(s)


def day11_part1():
    seats = encode_seats()
    new_seats = seats[:, :]
    while True:
        seats = new_seats.copy()
        for i in range(seats.shape[0]):
            for j in range(seats.shape[1]):
                if seats[i, j] == 0:
                    if check_neighbours(seats, i, j) == 0:
                        new_seats[i, j] = 1
                elif seats[i, j] == 1:
                    if check_neighbours(seats, i, j) > 3:
                        new_seats[i, j] = 0
        if np.array_equal(seats, new_seats):
            break
    return new_seats[new_seats == 1].size


def day11_part2():
    seats = encode_seats()
    new_seats = seats[:, :]
    while True:
        seats = new_seats.copy()
        for i in range(seats.shape[0]):
            for j in range(seats.shape[1]):
                if seats[i, j] == 0:
                    if check_neighbours2(seats, i, j) == 0:
                        new_seats[i, j] = 1
                elif seats[i, j] == 1:
                    if check_neighbours2(seats, i, j) > 4:
                        new_seats[i, j] = 0
        if np.array_equal(seats, new_seats):
            break
    return new_seats[new_seats == 1].size


if __name__ == "__main__":
    print("=" * 10 + " Part 1 " + "=" * 10)
    print(f"Occupied seats: {day11_part1()}")
    print("=" * 10 + " Part 2 " + "=" * 10)
    print(f"Occupied seats: {day11_part2()}")
