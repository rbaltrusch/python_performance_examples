"""Library code written in Cython."""

def fib(int limit):
    """Calculates all Fibonnacci numbers up to the specified limit,
    then returns them in a list.
    """
    # declare list of int called numbers
    #Note: this is not a C-array and so does not get as much speed up as it could
    numbers = [0, 1, 1] 

    #populate array
    #numbers[:] = [0, 1, 2] # pre-initialise numbers

    cdef int current = numbers[-1] # declare C-int called current
    while current < limit:
        current = numbers[-2] + numbers[-1]
        numbers.append(current)
    return numbers
