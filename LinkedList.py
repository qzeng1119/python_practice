"""Class of Linked List."""

class Link:
    empty = ()
    def __init__(self, first, rest=empty):  # 'rest=Link.empty' will lead to error
        assert rest == Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    # >>> print(Link.__repr__(other)) # OTHER is not a instance of Link
    # >>> None
    def __repr__(self):              
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_repr)
        # You also need to call 'repr' on self.first, namely using 'repr(self.first)' instead of 'self.first' in line 17

    def __str__(self):
        # if not(self.rest):
        #     return str(self.first)
        # return '{0} -> {1}'.format(self.first, self.rest)
        #
        # The version above can't work well when <somelink>.first is also an instance of Link
        # >>> print(Link(1, Link(Link(2))))
        # 1 -> 2  # It is not what we want!
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest # 'self' is like a name bound to the object, the change of the binding of 'self' wouldn't affect the object itself 
        return string + str(self.first) + '>'
        # >>> print(Link(1, Link(Link(2))))
        # <1, <2>>
def range_link(start, end):
    """Return a Link containing consecutive integers from START to END.

    >>> range_link(3, 6)
    Link(3, Link(4, Link(5)))
    """
    if start >= end:
        return Link.empty
    return Link(start, range_link(start+1, end))

def map_link(f, s):
    """Return a Link that contains f(x) for each x in Link s.

    >>> square = lambda x: x*x
    >>> map_link(square, range_link(3, 6))
    Link(9, Link(16, Link(25)))
    """
    if s is Link.empty:
        return s
    return Link(f(s.first), map_link(f, s.rest))
    
def filter_link(f, s):
    """Return a Link that contains only the elements x of Link s for which f(x) is a true value.

    >>> odd = lambda x: x%2 == 1
    >>> filter_link(odd, range_link(1, 6))
    Link(1, Link(3, Link(5)))
    """
    if s is Link.empty:
        return s
    filtered_rest = filter_link(f, s.rest)
    if f(s.first):
        return Link(s.first, filtered_rest)
    return filtered_rest

def add(s, v):
    """Add v to a Link s which is in increasing order with no repeats, returning modified s.
    
    >>> add((), 4)
    Link(4)
    >>> add(Link(1, Link(7)), 7)
    Link(1, Link(7))
    >>> add(Link(2, Link(3)), 1)
    Link(1, Link(2, Link(3)))
    >>> add(Link(1, Link(2)), 3)
    Link(1, Link(2, Link(3)))
    >>> add(Link(1, Link(3)), 2)
    Link(1, Link(2, Link(3)))
    """
    if s is Link.empty:
        return Link(v)
    elif v < s.first:
        return Link(v, s)
    elif s.first < v:
        return Link(s.first, add(s.rest, v))
    return s # v == s.first