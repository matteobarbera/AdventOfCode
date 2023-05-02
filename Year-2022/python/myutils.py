from functools import wraps


def run_test(test_input: str, correct_solution: [int, None]):

    def decorator(func):

        @wraps(func)
        def wrapper(txt_input: str):
            if correct_solution is not None:
                solution = func(test_input)
                if solution != correct_solution:
                    print()
                    print("Test failed!")
                    print("Output: ", solution)
                    print("Solution: ", correct_solution)
                    print()

            return func(txt_input)

        return wrapper

    return decorator
