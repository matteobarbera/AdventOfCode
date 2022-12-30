import re


def add(a, b):
    return int(a) + int(b)


def multiply(a, b):
    return int(a) * int(b)


def calculate(expression: list):
    while len(expression) > 2:
        if expression[1] == "+":
            expression = [add(expression[0], expression[2])] + expression[3:]
            continue
        if expression[1] == "*":
            expression = [multiply(expression[0], expression[2])] + expression[3:]
            continue
    return expression[0]


def calculate_advanced(expression: str):
    expression = expression.split("*")
    for i in range(len(expression)):
        if "+" in expression[i]:
            expression[i] = sum(map(int, expression[i].split("+")))
    product = 1
    for n in expression:
        product *= int(n)
    return product


def day18_part1():
    with open("day18_input.txt") as f:
        pattern = r"\([\d +*]+\)"
        eval_sum = 0
        for i, line in enumerate(f):
            expression = line.strip()
            while match := re.search(pattern, expression):
                bracket_eval = str(calculate((match[0]).strip("()").split()))
                expression = re.sub(pattern, bracket_eval, expression, count=1)
            if len(expression.split()) > 2:
                eval_sum += calculate(expression.split())
            else:
                eval_sum += expression[0]
        return eval_sum


def day18_part2():
    with open("day18_input.txt") as f:
        pattern = r"\([\d +*]+\)"
        eval_sum = 0
        for i, line in enumerate(f):
            expression = line.strip()
            # Identify inner-most brackets and replace them with
            # integer after evaluating them
            while match := re.search(pattern, expression):
                bracket_eval = str(calculate_advanced((match[0]).strip("()")))
                expression = re.sub(pattern, bracket_eval, expression, count=1)
            # catch edge case where whole expression was between brackets
            if len(expression.split()) > 2:
                eval_sum += calculate_advanced(expression)
            else:
                eval_sum += expression[0]
        return eval_sum


if __name__ == "__main__":
    print("=" * 10 + " Part 1 " + "=" * 10)
    homework_eval = day18_part1()
    print(f"Sum of expressions: {homework_eval}")
    print("=" * 10 + " Part 2 " + "=" * 10)
    homework_eval = day18_part2()
    print(f"Sum of expressions (advanced): {homework_eval}")
