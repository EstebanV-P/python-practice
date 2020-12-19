def unsigned_div_alg(a, b):
    """Calculates div_alg if the dividend (a) and divisor (b) give a positive answer
    inputs (a, b) ---> outputs (q, r)"""
    q, r = 0, 0
    r = a - (b * q)

    while r >= b:
        # Increase the quotient to meet (r < b).
        q += 1
        r = a - (b * q)
    return q, r


def signed_div_alg(a, b):
    """Calculates div_alg if either a<0 or b<0"""
    q, r = 0, 0
    a = -abs(a)
    b = abs(b)
    r = a - (b * q)

    while r < 0:
        # Decreases quotient to meet (r >= 0).
        q -= 1
        r = a - (b * q)  # This quantity becomes greater.
    return q, r


def div_alg(a, b):
    """Takes two numbers; dividend and divisor (a, b), and uses the
    division algorithm to calculate the quotient and remainder (q, r)."""

    if b == 0:
        return "Zero Division Error"

    if ((a < 0) and (b < 0)) or ((a > 0) and (b > 0)):
        a = abs(a)
        b = abs(b)
        if b > a:
            # a = 0b + a
            q = 0
            r = a
            return q, r
        return unsigned_div_alg(a, b)

    elif (a < 0) or (b < 0):
        # Remember we're taking (a, b) --> (-abs(a), abs(b))
        # Then, -abs(a) = (abs(b))*q + r.
        return signed_div_alg(a, b)
