#!/usr/bin/env python
import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
project_path = os.sep.join(path.split(os.sep)[:-1])
sys.path.append(project_path)

from data_structures.graph import Graph


class DFSGraph(Graph):
    """
    Adds basic Depth First Search methods to Graph

    Conceptually DFS is just BFS but using a stack instead of a queue,
    but here I use recursion to eliminate the need for a stack
    """
    discovered = None
    edge_number = 0
    time = 0
    entry_times = None
    exit_times = None

    def __init__(self, *args, **kwargs):
        super(DFSGraph, self).__init__(*args, **kwargs)
        self.reset()

    def show(self, start):
        """
        lets print some stuff
        """
        super(DFSGraph, self).show()
        self.reset()
        self.traverse(start)
        print 'Edge Number: %s' % self.edge_number
        print 'Entry Times: ', self.entry_times
        print 'Exit Times: ', self.exit_times

    def traverse(self, x):
        """
        discover all nodes using DFS
        """
        if not self.graph.has_key(x):
            return

        self.discovered.append(x)
        self._preprocess_vertex(x)

        for y in self.graph[x]:
            if y not in self.discovered:
                self.discovered.append(y)
                self._process_edge(x, y)
                self.traverse(y)

        self._postprocess_vertex(x)
                    
    def reset(self):
        self.discovered = []
        self.edge_number = 0
        self.time = 0
        self.exit_times = {}
        self.entry_times = {}

    def _preprocess_vertex(self, node):
        print 'Preprocess: %s' % node
        self.time += 1
        self.entry_times[node] = self.time

    def _postprocess_vertex(self, node):
        self.exit_times[node] = self.time
        self.time += 1

    def _process_edge(self, x, y):
        self.edge_number += 1


if __name__ == '__main__':
    initial_graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'E': ['H'],
    }

    graph = DFSGraph()

    for node, edges in initial_graph.items():
        for edge in edges:
            graph.insert_edge(node, edge)

    graph.show('A')
