import re


def day4_part1():
    with open("day4_input.txt") as f:
        valid_passports = 0
        passport_fields = []
        for line in f:
            passport_fields += re.findall(r"\w{3}(?=:)", line)
            if not line.strip():
                if len(passport_fields) == 8:
                    valid_passports += 1
                elif len(passport_fields) == 7 and 'cid' not in passport_fields:
                    valid_passports += 1
                passport_fields = []
                continue
        if len(passport_fields) == 8:
            valid_passports += 1
        elif len(passport_fields) == 7 and 'cid' not in passport_fields:
            valid_passports += 1
        return valid_passports


fields = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hcl': lambda x: re.fullmatch(r"#[\da-z]{6}", x),
    'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    'pid': lambda x: re.fullmatch(r'^\d{9}', x),
    'hgt': lambda x: (x.endswith('cm') and 150 <= int(x[:-2]) <= 193) or
                     (x.endswith('in') and 59 <= int(x[:-2]) <= 76)
}


def is_passport_valid(passport):
    try:
        if len(passport.keys()) >= 7:
            if all([check(passport[field]) for field, check in fields.items()]):
                return True
    except KeyError:
        return False
    return False


def day4_part2():
    with open("day4_input.txt") as f:
        valid_passports = 0
        passport = {}
        for line in f:
            for match in re.findall(r"\w{3}:[^ \n]*", line):
                key, val = match.split(":")
                passport[key] = val
            if not line.strip():
                if is_passport_valid(passport):
                    valid_passports += 1
                passport = {}
        if is_passport_valid(passport):
            valid_passports += 1
        return valid_passports


if __name__ == "__main__":
    print("=" * 10 + " Part 1 " + "=" * 10)
    print(f"Number of valid passports: {day4_part1()}")
    print("=" * 10 + " Part 2 " + "=" * 10)
    print(f"Number of valid passports: {day4_part2()}")
