def load_forest():
    forest = []
    with open("day3_input.txt") as f:
        for line in f:
            forest.append(line.rstrip())
    return forest


def day3_part1(forest: list, slope: tuple, start: tuple = (0, 0)):
    forest_height = len(forest)
    forest_width = len(forest[0])
    x_incr, y_incr = slope
    x, y = start
    tree_ctr = 0
    while x < forest_height:
        if forest[x][y] == "#":
            tree_ctr += 1
        x += x_incr
        y += y_incr
        y = y % forest_width
    return tree_ctr


def day3_part2(forest: list, slopes: list[tuple], start: tuple = (0, 0)):
    trees_mpl = 1
    for slope in slopes:
        trees_mpl *= day3_part1(forest, slope, start)
    return trees_mpl


if __name__ == "__main__":
    day3_inp = load_forest()
    print("=" * 10 + " Part 1 " + "=" * 10)
    trees_hit = day3_part1(day3_inp, (1, 3))
    print(f"Trees hit: {trees_hit}")
    print("=" * 10 + " Part 2 " + "=" * 10)
    slope_lst = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    trees_decimated = day3_part2(day3_inp, slope_lst)
    print(f"Trees decimated: {trees_decimated}")
