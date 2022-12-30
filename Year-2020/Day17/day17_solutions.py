from itertools import product


def cube_will_activate(active_cubes: set, cube: tuple):
    x, y, z = cube
    active_neighbors = 0
    for c in product(*[range(x - 1, x + 2), range(y - 1, y + 2), range(z - 1, z + 2)]):
        if active_neighbors > 3:
            return False
        if c in active_cubes:
            active_neighbors += 1
    else:
        if active_neighbors == 3:
            return True
    return False


def cycle_pocket_dimension(active_cubes: set):
    deactivate_cubes = set()
    activate_cubes = set()
    for c in active_cubes:
        x, y, z = c
        active_neighbors = 0
        for n in product(*[range(x - 1, x + 2), range(y - 1, y + 2), range(z - 1, z + 2)]):
            if n in active_cubes:
                active_neighbors += 1
            else:
                if cube_will_activate(active_cubes, n):
                    activate_cubes.add(n)
        else:
            if not 3 <= active_neighbors < 5:
                deactivate_cubes.add(c)
    return (active_cubes - deactivate_cubes) | activate_cubes


def hypercube_will_activate(active_cubes: set, cube: tuple):
    x, y, z, w = cube
    active_neighbors = 0
    for c in product(*[range(x - 1, x + 2), range(y - 1, y + 2), range(z - 1, z + 2), range(w - 1, w + 2)]):
        if active_neighbors > 3:
            return False
        if c in active_cubes:
            active_neighbors += 1
    else:
        if active_neighbors == 3:
            return True
    return False


def cycle_hypercube_dimension(active_cubes: set):
    deactivate_cubes = set()
    activate_cubes = set()
    for c in active_cubes:
        x, y, z, w = c
        active_neighbors = 0
        for n in product(*[range(x - 1, x + 2), range(y - 1, y + 2), range(z - 1, z + 2), range(w - 1, w + 2)]):
            if n in active_cubes:
                active_neighbors += 1
            else:
                if hypercube_will_activate(active_cubes, n):
                    activate_cubes.add(n)
        else:
            if not 3 <= active_neighbors < 5:
                deactivate_cubes.add(c)
    return (active_cubes - deactivate_cubes) | activate_cubes


def initialize_pocket_dimension():
    active_cubes = set()
    with open("day17_input.txt") as f:
        x = 0
        for line in f:
            y = 0
            for character in line:
                if character == "#":
                    active_cubes.add((x, y, 0))
                y += 1
            x += 1
    return active_cubes


def initialize_hypercube_dimension():
    active_cubes = set()
    with open("day17_input.txt") as f:
        x = 0
        for line in f:
            y = 0
            for character in line:
                if character == "#":
                    active_cubes.add((x, y, 0, 0))
                y += 1
            x += 1
    return active_cubes


def day17_part1():
    active_cubes = initialize_pocket_dimension()
    for i in range(6):
        active_cubes = cycle_pocket_dimension(active_cubes)
    return len(active_cubes)


def day17_part2():
    active_cubes = initialize_hypercube_dimension()
    for i in range(6):
        active_cubes = cycle_hypercube_dimension(active_cubes)
    return len(active_cubes)


if __name__ == "__main__":
    print("=" * 10 + " Part 1 " + "=" * 10)
    print(f"Active cubes after 6 cycles: {day17_part1()}")
    print("=" * 10 + " Part 3" + "=" * 10)
    print(f"Active hypercubes after 6 cycles: {day17_part2()}")
