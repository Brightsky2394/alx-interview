#!/usr/bin/python3
"""
calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    returns an integer
    """

    operation_count = 0
    allowed_operation = 2
    if not isinstance(n, int) or n <= 1:
        return operation_count
    while n > 1:
        if n % allowed_operation == 0:
            operation_count += allowed_operation
            n /= allowed_operation
        else:
            allowed_operation += 1
    return operation_count
