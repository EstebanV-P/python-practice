import math


def prim(n):
    """Enters a natural number and returns it's primality"""
    if n == 1:
        return False

    lim = math.floor(math.sqrt(n))
    # Check up to the root of the number.

    if n > 2 and n % 2 == 0:
        # Discards even numbers starting at 3.
        return False
    else:
        # Discards if the number has whole divisors.
        for k in range(3, lim + 1, 2):
            if n % k == 0:
                return False

    # Every other case returns True (2, 5...).
    return True
