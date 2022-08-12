"""Entry point to the example.
Runs the fib function defined in lib.pyx using cython.
"""

import time

from src.lib import fib


def main():
    """Main function"""
    initial = time.perf_counter()
    for _ in range(1_000_000):
        fib(1_000_000)
    print(f"Result is {fib(1_000_000)=}")
    print(f"Time taken: {time.perf_counter() - initial}")


if __name__ == "__main__":
    main()
