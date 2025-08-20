# Data abstraction of TREE

def tree(label, branches=[]):
    """A constructor for TREE."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)


def label(tree):
    """A selector for TREE."""
    return tree[0]


def branches(tree):
    """A selector for TREE."""
    return tree[1:]


def is_tree(tree):
    """Judge whether the input is an instance of TREE."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    """Judge whether the given tree is a leaf."""
    return not branches(tree)


def count_leaves(tree):
    """Return the number of leaves of the given tree."""
    assert is_tree(tree), 'the given value must be a tree'
    if is_leaf(tree):
        return 1
    else:
        return sum([count_leaves(branch) for branch in branches(tree)])


def print_tree(tree, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> new_tree = tree(3,
    ...                 [tree(6,   
    ...                       [tree(9),
    ...                        tree(4)]),
    ...                  tree(4),
    ...                  tree(7, 
    ...                       [tree(9,
    ...                             [tree(8)]),
    ...                        tree(0)])])
    >>> print_tree(new_tree)
    3
      6
        9
        4
      4
      7
        9
          8
        0
    """
    print('  ' * indent + str(label(tree)))
    for branch in branches(tree):
        print_tree(branch, indent + 1)