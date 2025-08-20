def Hanoi(n, start, end, aid):
    """Print the solution for the N-order Hanoi question. The
    START is the index of the peg which the disc(s) are at 
    in the beginning, the END is the index of the peg which
    you want to move the disc(s) to, and the AID is the index 
    of the aided peg.

    >>> Hanoi(1, 1, 2, 3)
    1 -> 2
    >>> Hanoi(2, 1, 2, 3)
    1 -> 3
    1 -> 2
    3 -> 2
    >>> Hanoi(3, 1, 2, 3)
    1 -> 2
    1 -> 3
    2 -> 3
    1 -> 2
    3 -> 1
    3 -> 2
    1 -> 2
    >>> Hanoi(4, 1, 2, 3)
    1 -> 3
    1 -> 2
    3 -> 2
    1 -> 3
    2 -> 1
    2 -> 3
    1 -> 3
    1 -> 2
    3 -> 2
    3 -> 1
    2 -> 1
    3 -> 2
    1 -> 3
    1 -> 2
    3 -> 2
    """
    if n == 1:
        print(start, "->", end)
    else:
        Hanoi(n - 1, start, aid, end)
        print(start, "->", end)
        Hanoi(n - 1, aid, end, start)
    