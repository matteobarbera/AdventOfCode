from myutils import run_test


@run_test("day01_test.txt", 24000)
def day01_part1(day_input: str):
    calories = read_input(day_input)
    max_calories = 0
    for elf in calories:
        supplies = sum(elf)
        if supplies > max_calories:
            max_calories = supplies
    return max_calories


@run_test("day01_test.txt", 45000)
def day01_part2(day_input: str):
    calories = read_input(day_input)
    sorted_calories = sorted([sum(elf) for elf in calories], reverse=True)
    return sum(sorted_calories[:3])


def read_input(file: str):
    calories = []
    with open(file) as f:
        elf = []
        for line in f.readlines():
            if line.strip() == "":
                calories.append(elf)
                elf = []
            else:
                elf.append(int(line))
    calories.append(elf)
    return calories


if __name__ == "__main__":
    print("Part 1:\t", day01_part1("day01.txt"))
    print("Part 2:\t", day01_part2("day01.txt"))
