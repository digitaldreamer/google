#!/usr/bin/env python
import os
import sys

# add parent directory to path
path = os.path.dirname(os.path.abspath(__file__))
project_path = os.sep.join(path.split(os.sep)[:-1])
sys.path.append(project_path)

from data_structures.weighted_graph import WeightedGraph


class PrimGraph(WeightedGraph):
    connected = []
    unconnected = []
    spanning_tree = []

    def __init__(self, graph={}, directed=False, *args, **kwargs):
        super(PrimGraph, self).__init__(graph, directed, *args, **kwargs)

        for node, edges in self.graph.items():
            try:
                self.unconnected.index(node)
            except ValueError:
                self.unconnected.append(node)

            for key in edges.keys():
                try:
                    self.unconnected.index(key)
                except ValueError:
                    self.unconnected.append(key)

    def build(self, start):
        """
        Build the MST using Prim's Algorithm.

        The implementation is crude.

        Efficiencies could/should be made to not force a need to read the connected graph on each iteration.
        """
        self.connected = [start]
        self.spanning_tree = []
        self.unconnected.pop(self.unconnected.index(start))

        while self.unconnected:
            lowest_cost = {
                'parent': None,
                'node': None,
                'weight': -1,
            }

            # for each vertex we have in the tree check the edges
            # of the unconnected nodes and pick the smallest weight
            for vertex in self.connected:
                edges = self.graph[vertex]

                for node, weight in edges.items():
                    if node not in self.connected:
                        if not lowest_cost['node'] or weight < lowest_cost['weight']:
                            lowest_cost['parent'] = vertex
                            lowest_cost['node'] = node
                            lowest_cost['weight'] = weight

            # insert the node
            self.spanning_tree.append((lowest_cost['parent'], lowest_cost['node'], lowest_cost['weight']))
            self.connected.append(lowest_cost['node'])
            self.unconnected.pop(self.unconnected.index(lowest_cost['node']))

    def show(self):
        for edge in self.spanning_tree:
            print edge[0], edge[1], edge[2]


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

    graph = PrimGraph(initial)
    graph.build('A')
    graph.show()
