"""Entry point to the example.
Runs the numba jit-accelerated fib function defined in lib.py
"""

import time

from src.lib import fib


def main():
    """Main function"""
    initial = time.perf_counter()

    # run the function a million times to amortize jit compilation time
    # if the jit-accelerated function is only run once, it is much slower
    # than if it had not been accelerated. This is due to the extra compile-step.
    for _ in range(1_000_000):
        fib(limit=1_000_000)

    print(f"Result is {fib(limit=1_000_000)=}")
    print(f"Time taken: {time.perf_counter() - initial}")


if __name__ == "__main__":
    main()
