"""
Tips about recursion: 
The key of using recursion to solve problem is
splitting it into several similiar subproblems
and figuring out the base case.
"""


"""
The problem:
The number of partitions of a positive interger N, using
parts up to size M, is the number of ways in which N can
be expressed as the sum of positive integer parts up to 
M in increasing order.
"""
way = 0
# here are two different ways to split the problem

if way:
    # the first way: this is my way
    def count_partitions(n, m, least = 1):
        if n == 0:
            return 1
        elif n < least:
            return 0
        total, i = 0, least
        while i <= min(n, m):
            total += count_partitions(n - i, m, i)
            i += 1
        return total
else:
    # the second way: this is Professor John DeNero's way from cs61a
    def count_partitions(n, m):
        if m == 1 or n == 1 or n == 0:
            return 1
        elif n < 0:
            return 0
        else:
            with_m = count_partitions(n - m, m)
            without_m = count_partitions(n, m - 1)
            return with_m + without_m
