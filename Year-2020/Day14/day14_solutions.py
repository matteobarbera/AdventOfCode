from itertools import product


def process_line():
    with open("day14_input.txt") as f:
        for line in f:
            no_whitespace = "".join(line.split())
            comm, val = no_whitespace.split("=")
            yield comm, val


def apply_bitmask(mask, num):
    binary = "{:b}".format(int(num))  # convert to binary without 0b
    binary = [*binary.zfill(36)]  # pad to match bitmask length
    for i, bit in enumerate(mask):
        if bit != "X":
            binary[i] = bit
    return int("".join(binary), 2)


def apply_bitmask_v2(mask, address):
    binary_address = "{:b}".format(int(address))  # convert to binary without 0b
    binary_address = [*binary_address.zfill(36)]  # pad to match bitmask length
    for i, m_bit in enumerate(mask):
        if m_bit != "0":  # override 1 and X
            binary_address[i] = m_bit
    floating_bits = binary_address.count("X")
    floating_address = "".join(binary_address).replace("X", "{}")  # prepare for format
    # Loop over all possible combinations of floating bits
    for bits in product(range(2), repeat=floating_bits):
        new_address = floating_address.format(*bits)
        yield int(new_address, 2)


def day14_part1():
    initialization_values = {}
    mask = None
    for c, v in process_line():
        if c == "mask":
            mask = v
        else:
            address = c[4:-1]
            initialization_values[address] = apply_bitmask(mask, v)
    sum = 0
    for val in initialization_values.values():
        sum += val
    return sum


def day14_part2():
    initialization_values = {}
    mask = None
    for c, v in process_line():
        if c == "mask":
            mask = v
        else:
            address = c[4:-1]
            for addr in apply_bitmask_v2(mask, address):
                initialization_values[addr] = int(v)
    sum = 0
    for val in initialization_values.values():
        sum += val
    return sum


if __name__ == "__main__":
    print("=" * 10 + " Part 1 " + "=" * 10)
    print(f"Sum of initialization values: {day14_part1()}")
    print("=" * 10 + " Part 2 " + "=" * 10)
    print(f"Sum of initialization values: {day14_part2()}")
