def remove(n, digit):
    """Try to remove all the digits in number N that are equal to DIGIT
       and return the remaining number.

    >>> remove(234, 3)
    24
    >>> remove(983478824, 8)
    934724
    """
    kept, digits = 0, 0
    while n > 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept += last * pow(10, digits)
            digits += 1
    return kept
