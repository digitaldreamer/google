#!/usr/bin/env python
import os
import sys
import Queue

# add parent directory to path
path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.sep.join(path.split(os.sep)[:-1])
sys.path.append(parent_path)

from data_structures.graph import Graph


class BFSGraph(Graph):
    """
    adds basic Breadth First Search methods to a Graph
    """
    discovered = None
    queue = None
    paths = None
    edge_number = 0

    def __init__(self, *args, **kwargs):
        super(BFSGraph, self).__init__(*args, **kwargs)
        self.discovered = []
        self.paths = []
        self.queue = Queue.Queue()

    def show(self):
        """
        print some BFS processing goodies
        """
        super(BFSGraph, self).show()
        self.traverse('A')
        print 'Edge Number: %s' % self.edge_number

    def traverse(self, start):
        """
        traverses the graph using Breadth First Search

        NOTE: doesn't really search
        """
        def _traverse(x):
            self._preprocess_vertex(x)

            if self.graph.has_key(x):
                for y in self.graph[x]:
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
    """
    {
        'A': ['B', 'E'], 
        'B': ['C', 'D'], 
        'C': ['H'],
        'E': ['F', 'G'],
    }
    """
    graph = BFSGraph({
        'A': ['B', 'E'], 
        'B': ['C', 'D'], 
        'C': ['H'],
        'E': ['F', 'G'],
    })

    graph.show()
