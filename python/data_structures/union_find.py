#!/usr/bin/env python
class UnionFind(object):
    """
    adapted from http://code.activestate.com/recipes/577225-union-find/
    """
    def make_set(self, x):
        x.parent = x
        x.rank = 0
        return x

    def union(self, x, y):
        """
        merge the two sets
        """
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root.rank > y_root.rank:
            y_root.parent = x_root
        elif x_root.rank < y_root.rank:
            x_root.parent = y_root
        elif x_root != y_root: # Unless x and y are already in same set, merge them
            y_root.parent = x_root
            x_root.rank += 1

    def find(self, x):
        """
        find the root of the component
        """
        if x.parent != x:
            x.parent = self.find(x.parent)

        return x.parent

    def same_component(self, x, y):
        """
        check if the two nodes are the members of the same component
        """
        return self.find(x) == self.find(y)


class Node(object):
    label = None
    parent = None
    rank = 0

    def __init__(self, label):
        self.label = label
        self.parent = self

    def __str__(self):
        return self.label


if __name__ == '__main__':
    import itertools

    union = UnionFind()
    components = [Node(ch) for ch in 'abcdefg']

    [union.make_set(node) for node in components]
    sets = [union.find(x) for x in components]

    for s in sets:
        print s.label, s.parent.label, s.rank

    print len(sets)

    union.union(components[0], components[2])
    union.union(components[0], components[1])
    union.union(components[-2], components[-1])
    union.union(components[-3], components[-1])

    for node in components:
        print node.label, node.parent.label, node.rank

    sets = [str(union.find(x)) for x in components]

    print sets
    print len([i for i in itertools.groupby(sets)])
