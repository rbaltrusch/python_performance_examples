"""Library code accelerated using the numba jit compiler using the @numba.jit decorator."""

from typing import List

import numba  # type: ignore


@numba.jit  # type: ignore
def fib(limit: int) -> List[int]:
    """Calculates all Fibonnacci numbers up to the specified limit,
    then returns them in a list.
    """
    numbers: List[int] = [0, 1, 1]

    current: int = numbers[-1]
    while current < limit:
        current = numbers[-2] + numbers[-1]
        numbers.append(current)
    return numbers
