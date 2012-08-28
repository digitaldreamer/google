#!/usr/bin/env python
import os
import sys
import Queue

# add parent directory to path
path = os.path.dirname(os.path.abspath(__file__))
project_path = os.sep.join(path.split(os.sep)[:-1])
sys.path.append(project_path)

from data_structures.graph import Graph


class BFSGraph(Graph):
    """
    adds basic Breadth First Search methods to a Graph
    """
    discovered = None
    queue = None
    edge_number = 0

    def __init__(self, mode='bfs', *args, **kwargs):
        super(BFSGraph, self).__init__(*args, **kwargs)
        self.reset()

    def reset(self):
        self.discovered = []
        self.edge_number = 0
        self.queue = Queue.Queue()

    def show(self, start):
        """
        print some BFS processing goodies
        """
        self.reset()

        super(BFSGraph, self).show()
        self.traverse(start)
        print 'Edge Number: %s' % self.edge_number

    def find_path(self, start, finish):
        """
        finds the shortest path between start and finish
        """
        def _find_path(x, path):
            for y in self.graph.get(x, []):
                if y not in self.discovered:
                    self.discovered.append(y)
                    new_path = list(path) + [y]
                    self.queue.put(new_path)

        self.reset()

        # push first node into queue
        if not self.graph.has_key(start):
            return None

        self.discovered.append(start)
        self.queue.put([start])

        while not self.queue.empty():
            path = self.queue.get()
            node = path[-1]

            if node == finish:
                return path

            _find_path(node, path)

        # no path was found
        return None

    def traverse(self, start):
        """
        traverses the graph using BFS depending on Queue type

        NOTE: doesn't really search
        """
        def _traverse(x):
            self._preprocess_vertex(x)

            for y in self.graph.get(x, []):
                if y not in self.discovered:
                    self.discovered.append(y)
                    self._process_edge(x, y)
                    self.queue.put(y)

            self._postprocess_vertex(x)

        # push first node into queue
        if not self.graph.has_key(start):
            return None

        self.discovered.append(start)
        self.queue.put(start)

        while not self.queue.empty():
            node = self.queue.get()
            _traverse(node)

    def _preprocess_vertex(self, node):
        print 'Preprocess: %s' % node

    def _postprocess_vertex(self, node):
        pass

    def _process_edge(self, x, y):
        self.edge_number += 1


if __name__ == '__main__':
    initial_graph = {
        'A': ['B', 'C'], 
        'B': ['D', 'E'], 
        'C': ['F', 'G'],
        'E': ['H'],
    }

    graph = BFSGraph()

    for node, edges in initial_graph.items():
        for edge in edges:
            graph.insert_edge(node, edge)

    graph.show('A')
    print 'Find Path (H, F): ', graph.find_path('H', 'F')
