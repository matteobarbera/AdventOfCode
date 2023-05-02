dirname="Day$1"
mkdir "$dirname"
touch "$dirname/day$1.py"
cat <<EOF >"$dirname/day$1.py"
from myutils import run_test


@run_test("day$1_test.txt", None)
def day$1_part1(day_input: str):
    pass


@run_test("day$1_test.txt", None)
def day$1_part2(day_input: str):
    pass


if __name__ == "__main__":
    print("Part 1:\t", day$1_part1("day$1.txt"))
    print("Part 2:\t", day$1_part2("day$1.txt"))

EOF
touch "$dirname/day$1.txt"
touch "$dirname/day$1_test.txt"