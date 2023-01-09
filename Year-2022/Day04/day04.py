from myutils import run_test


def read_input(day_input):
    assignments = []
    with open(day_input) as f:
        for line in f.readlines():
            assignments.append(list(map(int, line.replace("-", ",").split(sep=","))))
    return assignments


def create_bit(a: int, b: int):
    bitstring = "0" * (a - 1) + "1" * (b - a + 1)
    num = int(bitstring[::-1], 2)
    return num


@run_test("day04_test.txt", 2)
def day04_part1(day_input: str):
    assignments = read_input(day_input)
    overlapping = 0
    for assignment in assignments:
        elf_1 = create_bit(assignment[0], assignment[1])
        elf_2 = create_bit(assignment[2], assignment[3])
        overlap = elf_1 | elf_2
        if overlap == elf_1 or overlap == elf_2:
            overlapping += 1
    return overlapping


@run_test("day04_test.txt", 4)
def day04_part2(day_input: str):
    assignments = read_input(day_input)
    overlapping = 0
    for assignment in assignments:
        elf_1 = create_bit(assignment[0], assignment[1])
        elf_2 = create_bit(assignment[2], assignment[3])
        overlap = elf_1 & elf_2
        if overlap != 0:
            overlapping += 1
    return overlapping


if __name__ == "__main__":
    print("Part 1:\t", day04_part1("day04.txt"))
    print("Part 2:\t", day04_part2("day04.txt"))

