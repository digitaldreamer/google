#!/usr/bin/env python
class WeightedGraph(object):
    """
    graph = {
        'A': {'B':3, 'C':5},
        'B': {'C':2, 'D':2},
        'C': {'D':1},
        'D': {'C':3},
        'E': {'F':8},
        'F': {'C':2},
    }
    """
    graph = {}
    directed = False

    def __init__(self, graph={}, directed=False, *args, **kwargs):
        self.directed = directed
        self.graph = graph

    def show(self):
        for node, edges in self.graph.items():
            print node, edges

    def insert_edge(self, x, y, weight):
        self._insert_edge(x, y, weight)

        if not self.directed:
            self._insert_edge(y, x, weight)

    def _insert_edge(self, x, y, weight):
        try:
            node = self.graph[x]
        except KeyError:
            self.graph[x] = {y: weight}
        else:
            # insert edge if id doesn't exist
            node[y] = weight


if __name__ == '__main__':
    initial = {
        'A': {'B': 5, 'C': 7, 'D': 12},
        'B': {'A': 5, 'C': 9, 'E': 7},
        'C': {'A': 7, 'B': 9, 'D': 4, 'E': 4, 'F': 3},
        'D': {'A': 12, 'C': 4, 'F': 7},
        'E': {'B': 7, 'C': 4, 'F': 2, 'G': 5},
        'F': {'C': 3,'D': 7,'E': 2,'G': 2},
        'G': {'E': 5, 'F': 2},
    }

    graph = WeightedGraph(initial)
    graph.show()
