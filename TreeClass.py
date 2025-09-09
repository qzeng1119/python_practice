"""Class of Tree."""

class Tree:
    my_flag = False # Used in __str__, set my_flag to True to use the amazing __str__ created by myself
    def __init__(self, label, branches=[]):
        self.label = label
        for b in branches:
            assert isinstance(b, Tree), 'Each branch must be a tree'
        self.branches = list(branches)
    
    def __repr__(self):
        if not self.branches:
            return 'Tree({0})'.format(self.label)
        return 'Tree({0}, {1})'.format(self.label, repr(self.branches))
    
    def __str__(self):
        if not Tree.my_flag:
            return '\n'.join(self.indented())
        else:
            return '\n'.join(self.my_indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines

    def is_leaf(self):
        return not self.branches

    # This is figured out by myself!!!
    def my_indented(self):
        """A function used by __str__ to return a string expression of a tree, 
        which is both user-friendly(easy to read) and developer-friendly(vaild 
        in Python syntax).

        >>> Tree.my_flag = True
        >>> my_tree = Tree(4, [Tree(7, [Tree(4), Tree(3)]), Tree(5), Tree(4, [Tree(9)])])
        >>> print(my_tree)
        Tree(4,
             [Tree(7,
                   [Tree(4),
                    Tree(3)]),
              Tree(5),
              Tree(4,
                   [Tree(9)])])
        """
        if self.is_leaf():
            return ['Tree({0})'.format(self.label)]
        lines = ['Tree({0},'.format(self.label)]
        for b in self.branches:
            indented_branch = b.my_indented()
            lines.extend([' '*6 + line for line in indented_branch])
            lines[-1] += ','
        lines[1] = lines[1][:5] + '[' + lines[1][6:]
        lines[-1] = lines[-1][:-1] + '])'
        return lines