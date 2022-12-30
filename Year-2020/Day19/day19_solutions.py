import re


def parse_rules():
    rules = {}
    with open("day19_input.txt") as f:
        for line in f:
            if line.strip() == "":
                break
            key, val = line.strip().split(": ")
            rules[key] = val
    return rules


def parse_messages():
    with open("day19_input.txt") as f:
        line = next(f).strip()
        while line != "":
            line = next(f).strip()
        for line in f:
            yield line.strip()


def rule8(pattern, rules, rules_dict):
    pattern += "("
    subrules = rules.split("|")[0].split()
    pattern = crete_regex_pattern(pattern, subrules[0], rules_dict)
    pattern += ")+"
    return pattern


def rule11(pattern, rules, rules_dict):
    r = "("
    subrules = rules.split("|")[0].split()
    r42 = crete_regex_pattern(r, subrules[0], rules_dict)
    r31 = crete_regex_pattern(r, subrules[1], rules_dict)
    for hack in range(1, 40):
        r += f"{r42})" + "{" + f"{hack}" + "}" + f"{r31})" + "{" + f"{hack}" + "}|"
    r = r[:-1]
    r += ")"
    pattern += r
    return pattern


def crete_regex_pattern(pattern, rules, rules_dict, key_id=None):
    for key in rules.split():
        if rules_dict[key] == '"a"':
            pattern += "a"
        elif rules_dict[key] == '"b"':
            pattern += "b"
        elif "|" in rules_dict[key]:
            pattern += "("
            subrules = rules_dict[key].split("|")
            for sr in subrules:
                pattern = crete_regex_pattern(pattern, sr, rules_dict, key)
                pattern += "|"
            pattern = pattern[:-1]
            pattern += ")"
        else:
            pattern = crete_regex_pattern(pattern, rules_dict[key], rules_dict, key)
    return pattern


def day19_part1():
    rules = parse_rules()
    rule0_regex = crete_regex_pattern(r"^", rules["0"], rules) + "$"

    valid_msgs = 0
    for m in parse_messages():
        if re.search(re.compile(rule0_regex), m) is not None:
            valid_msgs += 1
    return valid_msgs


def day19_part2():
    # Hack from reddit
    rules = parse_rules()
    rules["8"] = "42 | 42 8"
    rules["11"] = "42 31 | 42 11 31"
    pattern = r"^"
    pattern = rule8(pattern, rules["8"], rules)
    rule0_regex = rule11(pattern, rules["11"], rules)
    rule0_regex += "$"
    valid_msgs = 0
    for m in parse_messages():
        if re.search(rule0_regex, m) is not None:
            valid_msgs += 1
    return valid_msgs


if __name__ == "__main__":
    print("=" * 10 + " Part 1 " + "=" * 10)
    print(f"Valid messages: {day19_part1()}")
    print("=" * 10 + " Part 2 " + "=" * 10)
    print(f"Valid messages: {day19_part2()}")
