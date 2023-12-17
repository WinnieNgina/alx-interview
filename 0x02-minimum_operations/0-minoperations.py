#!/usr/bin/python3
"""calculates the fewest number of operations needed to
result in exactly n H characters in the file."""


def minOperations(n):
    """
    n represents the characters we are aiming
    if its less than two we return 0 since no need for operation
    """
    if n < 2:
        return 0
    f = 2
    result = 0
    while n > 1:
        if n % f == 0:
            n = n / f
            result += f
        else:
            f += 1
    return result
