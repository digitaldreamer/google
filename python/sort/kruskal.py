#!/usr/bin/env python
import os
import sys

# add parent directory to path
path = os.path.dirname(os.path.abspath(__file__))
project_path = os.sep.join(path.split(os.sep)[:-1])
sys.path.append(project_path)

from data_structures.weighted_graph import WeightedGraph
from data_structures.union_find import UnionFind, Node


class KruskalGraph(WeightedGraph):
    edges = []
    spanning_tree = []
    components = {}
    union = None

    def __init__(self, graph={}, directed=False, *args, **kwargs):
        super(KruskalGraph, self).__init__(graph, directed, *args, **kwargs)
        self.union = UnionFind()

        # find and insert edges
        for vertex, edges in self.graph.items():
            self.components[vertex] = Node(vertex)

            for edge, weight in edges.items():
                self._add_edge(vertex, edge, weight)

        # sort edges
        self.edges = sorted(self.edges, key=lambda edges: edges[2])

    def build(self):
        """
        Build the MST using Kruskal's Algorithm.
        """
        for x, y, weight in self.edges:
            x_root = self.union.find(self.components[x])
            y_root = self.union.find(self.components[y])

            if x_root != y_root:
                self.spanning_tree.append((x, y, weight))
                self.union.union(x_root, y_root)

    def show(self):
        for edge in self.spanning_tree:
            print edge[0], edge[1], edge[2]

    def _add_edge(self, x, y, weight):
        edge = (x, y, weight)
        reverse_edge = (y, x, weight)

        if edge not in self.edges and reverse_edge not in self.edges:
            self.edges.append((x, y, weight))

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

    graph = KruskalGraph(initial)
    graph.build()
    graph.show()
