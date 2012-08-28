#!/usr/bin/env python
import Queue


class Graph(object):
    """
    There are many different representations of Graphs, this is based on Guido's graph
    which is an adjacency list

    http://www.python.org/doc/essays/graphs.html

    A -> B
    A -> C
    B -> C
    B -> D
    C -> D
    D -> C
    E -> F
    F -> C

    graph = {
        'A': ['B', 'C'],
        'B': ['C', 'D'],
        'C': ['D'],
        'D': ['C'],
        'E': ['F'],
        'F': ['C']
    }

    or a variation modified to track weight.

    graph = {
        'A': {'B':3, 'C':5},
        'B': {'C':2, 'D':2},
        'C': {'D':1},
        'D': {'C':3},
        'E': {'F':8},
        'F': {'C':2},
    }

    or class based

    class Node(object):
        name = None
        weight = None

        def __init__(name, weight = 0):
            self.name = name
            self.weight = weight

        def __hash__(self):
            return hash((self.name, self.weight))

        def __eq__(self, other):
            return (self.name, self.weight) == (other.name, other.weight)

    A = Node('New York', 10) . . .

    graph = {
        A: [B, C],
        B: [C, D],
        C: [D],
        D: [C],
        E: [F],
        F: [C]
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

    def insert_edge(self, x, y):
        self._insert_edge(x, y)

        if not self.directed:
            self._insert_edge(y, x)

    def _insert_edge(self, x, y):
        try:
            node = self.graph[x]
        except KeyError:
            self.graph[x] = [y]
        else:
            # insert edge if id doesn't exist
            if not y in self.graph[x]:
                node.append(y)

if __name__ == '__main__':
    graph = Graph()
    edges = [
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'C'),
        ('B', 'D'),
        ('C', 'D'),
        ('D', 'C'),
        ('E', 'F'),
        ('F', 'C'),
    ]

    for edge in edges:
        graph.insert_edge(edge[0], edge[1])

    graph.show()
