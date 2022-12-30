from my_tools import time_decorator


def day15_part1():
    nums = [2, 20, 0, 4, 1, 17]

    last_spoken = nums[-1]
    for i in range(2020 - len(nums)):
        try:
            idx = (list(reversed(nums)).index(last_spoken, 1))
        except ValueError:
            idx = None
        if idx is None:
            next_spoken = 0
        else:
            next_spoken = idx
        nums.append(next_spoken)
        last_spoken = next_spoken
    return last_spoken


@time_decorator
def da15_part2():
    nums = [2, 20, 0, 4, 1, 17]

    ctr = len(nums)
    spoken = dict(zip(nums, list(range(1, len(nums[:-1]) + 1))))

    last_spoken = nums[-1]
    for i in range(ctr, 30000000):
        if last_spoken in spoken.keys():
            spoken_this_turn = i - spoken[last_spoken]
        else:
            spoken_this_turn = 0
        spoken[last_spoken] = i
        last_spoken = spoken_this_turn
    return last_spoken


if __name__ == "__main__":
    print("=" * 10 + " Part 1 " + "=" * 10)
    print(f"2020th number: {day15_part1()}")
    print("=" * 10 + " Part 2 " + "=" * 10)
    print(f"30000000th number: {da15_part2()}")
