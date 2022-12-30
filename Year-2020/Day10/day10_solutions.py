def day10_part1():
    with open("day10_input.txt") as f:
        adapters = sorted([int(line) for line in f])
    diffs = [0, 0, 0]
    for i in range(len(adapters) - 1):
        diffs[adapters[i + 1] - adapters[i] - 1] += 1
    diffs[0] += 1
    diffs[2] += 1
    return diffs[0] * diffs[2]


def day10_part2():
    with open("day10_input.txt") as f:
        adapters = sorted([int(line) for line in f])
    adapters.insert(0, 0)
    adapters.append(adapters[-1] + 3)
    arrangements = []
    streak = 0
    for i in range(len(adapters) - 1):
        diff = adapters[i + 1] - adapters[i]
        if diff == 1:
            streak += 1
        else:
            if streak > 1:
                arrangements.append(streak - 1)
            streak = 0
    combs_dict = {1: 2, 2: 4, 3: 7}
    tot = 1
    for n in arrangements:
        tot *= combs_dict[n]
    return tot


if __name__ == "__main__":
    print("=" * 10 + " Part 1 " + "=" * 10)
    print(f"Product of jolt differences: {day10_part1()}")
    print("=" * 10 + " Part 2 " + "=" * 10)
    print(f"Possible arrangements: {day10_part2()}")
