from math import log
from random import randint
import time

def leading_digits_log(n: int, digits: int = 2) -> int:
    """Return the first `d` leading digits of integer `n` using log base 10."""
    magnitude = int(log(n) / log(10)) + 1
    return n // 10 ** (magnitude - digits)

def leading_digits_loop(n: int, digits: int = 2) -> int:
    """Return the first `d` leading digits of integer `n` using a loop."""
    while n > 10 ** digits:
        n //= 10
    return n

def leading_digits_str(n: int, digits: int = 2) -> int:
    """Return the first two leading digits of a number using string casting."""
    return str(n)[:digits]

def leading_digits(n: int, digits: int = 2, method: str = "log") -> int:
    """
    Return the first `d` leading digits of integer `n`
    using method `method`: 'log', 'loop' or 'string'.
    """
    if not isinstance(n, int):
        print(f"Input '{n}' is not an integer.")
        return
    n = abs(n)
    if n < 10 ** (digits - 1):
        print(f"Input {n} has strictly less than {digits} digits.")
        return
    functions = {
        "log": leading_digits_log,
        "loop": leading_digits_loop,
        "string": leading_digits_str
    }
    return functions[method](n=n, digits=digits)

def time_leading_digits(
        method: str,
        sample_size: int = 10 ** 6,
        max_value: int = 10 ** 200,
        digits: int = 2
    ) -> int:
    """
    Display the time taken to compute the first `d` digits of `sample_size` integers.
    The integers are randomly generated and have a value between 10 ** `digits` and `max_value`
    """
    start_time = time.time()
    for _ in range(sample_size):
        n = randint(10 ** digits, max_value)
        leading_digits(n=n, digits=digits, method=method)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Method {method} - Elapsed time = {elapsed_time} seconds.")
    return

def main() -> None:
    methods = ("log", "loop", "string")
    for method in methods:
            time_leading_digits(method=method)

if __name__ == "__main__":
    main()