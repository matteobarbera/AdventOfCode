from myutils import run_test


def read_input(day_input) -> list[str]:
    rucksacks = []
    with open(day_input) as f:
        for line in f.readlines():
            rucksacks.append(line)
    return rucksacks


def get_priority(char: str):
    unicode = ord(char)
    if unicode < 95:
        return unicode - 64 + 26
    else:
        return unicode - 96


@run_test("day03_test.txt", 157)
def day03_part1(day_input: str):
    rucksacks = read_input(day_input)
    priority_sum = 0
    for rucksack in rucksacks:
        first_compartment = rucksack[:len(rucksack) // 2]
        second_compartment = rucksack[len(rucksack) // 2:]
        for item in first_compartment:
            if item in second_compartment:
                priority_sum += get_priority(item)
                break
    return priority_sum


@run_test("day03_test.txt", 70)
def day03_part2(day_input: str):
    rucksacks = read_input(day_input)
    priority_sum = 0
    for i in range(0, len(rucksacks), 3):
        group = rucksacks[i:i+3]
        for item in group[0]:
            if all([item in rucksack for rucksack in group]):
                priority_sum += get_priority(item)
                break
    return priority_sum


if __name__ == "__main__":
    print("Part 1:\t", day03_part1("day03.txt"))
    print("Part 2:\t", day03_part2("day03.txt"))

