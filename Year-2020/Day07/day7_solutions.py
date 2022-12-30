import re
from collections import namedtuple, defaultdict


def make_bag_tree():
    bag_tree = {}
    bag_tree_inv = defaultdict(list)
    Vals = namedtuple('Vals', ['num', 'name'])
    with open("day7_input.txt") as f:
        for line in f:
            key = re.match(r"^[a-z]+ [a-z]*", line)[0]
            vals_str = re.findall(r"\d [a-z]+ [a-z]*", line)
            vals = []
            if len(vals_str) == 0:
                vals.append(Vals(num=0, name=''))
            else:
                for val in vals_str:
                    num = int(val[0])
                    bag = val[2:]
                    vals.append(Vals(num=num, name=bag))
                    bag_tree_inv[bag].append(key)
            bag_tree[key] = vals
    return bag_tree, bag_tree_inv


def day7_part1():
    _, bag_tree_inv = make_bag_tree()
    shiny_first_holders = bag_tree_inv['shiny gold']
    ex_bags = set()

    def count_bags(bags: list):
        if len(bags) == 0:
            return
        else:
            for b in bags:
                if b not in ex_bags:
                    ex_bags.add(b)
                    count_bags(bag_tree_inv[b])

    for bag in shiny_first_holders:
        ex_bags.add(bag)
        count_bags(bag_tree_inv[bag])
    return len(ex_bags)


def day7_part2():
    bag_tree, _ = make_bag_tree()

    def count_bags(*args):
        bag = args[0]
        if len(args) == 1:
            if bag.num == 0:
                return 0
            else:
                return bag.num * (1 + count_bags(*bag_tree[bag.name]))
        else:
            return bag.num * (1 + count_bags(*bag_tree[bag.name])) + count_bags(*args[1:])

    return count_bags(*bag_tree['shiny gold'])


if __name__ == "__main__":
    print("=" * 10 + " Part 1 " + "=" * 10)
    print(f"Bags that can contain mine: {day7_part1()}")
    print("=" * 10 + " Part 2 " + "=" * 10)
    print(f"Individual bags: {day7_part2()}")
