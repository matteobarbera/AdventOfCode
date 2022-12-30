from collections import OrderedDict


def day9_part1():
    with open("day9_input.txt") as f:
        nums = []
        for line in f:
            nums.append(int(line))
    buffer = OrderedDict()
    for i in range(p):
        buffer[nums[i]] = None
    for n in nums[p:]:
        for k in buffer.keys():
            if n - k in buffer.keys():
                break
        else:
            return n, nums
        buffer.popitem(last=False)
        buffer[n] = None


def day9_part2():
    impostor, nums = day9_part1()
    n = [nums[0]]
    start = 0
    end = 0
    for i in range(len(nums)):
        while (n_sum := sum(n)) <= impostor:
            if n_sum == impostor:
                return min(n) + max(n)
            end += 1
            n.append(nums[end])
        n.pop(0)
        start += 1
        while sum(n) > impostor:
            n.pop()
            end -= 1


if __name__ == "__main__":
    p = 25
    print("=" * 10 + " Part 1 " + "=" * 10)
    print(f"First impostor: {day9_part1()[0]}")
    print("=" * 10 + " Part 2 " + "=" * 10)
    print(f"Encryption weakness: {day9_part2()}")
