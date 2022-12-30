def day2_part1():
    valid_pwd = 0
    with open("day2_input.txt") as f:
        for line in f:
            rng, letter, pwd = line.split(' ')
            l_cnt = pwd.count(letter[0])
            rng_l, rng_m = [int(n) for n in rng.split('-')]
            if l_cnt < rng_l or l_cnt > rng_m:
                continue
            else:
                valid_pwd += 1
    return valid_pwd


def day2_part2():
    valid_pwd = 0
    with open("day2_input.txt") as f:
        for line in f:
            idx, letter, pwd = line.split(' ')
            idx_l, idx_u = [int(n) - 1 for n in idx.split('-')]
            if (pwd[idx_l] == letter[0]) is (pwd[idx_u] == letter[0]):
                continue
            else:
                valid_pwd += 1
    return valid_pwd


if __name__ == "__main__":
    print("=" * 10 + " Part 1 " + "=" * 10)
    v_pwd = day2_part1()
    print(f"Number of valid passwords (old policy): {v_pwd}")
    print("=" * 10 + " Part 2 " + "=" * 10)
    v_pwd = day2_part2()
    print(f"Number of valid passwords (new policy): {v_pwd}")
