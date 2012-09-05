#!/usr/bin/env python
import os
import sys

# add parent directory to path
path = os.path.dirname(os.path.abspath(__file__))
project_path = os.sep.join(path.split(os.sep)[:-1])
sys.path.append(project_path)

from data_structures.weighted_graph import WeightedGraph


class DijkstraGraph(WeightedGraph):
    distance = {} # Final distances dict
    parent = {} # parent dict
    start = None

    def __init__(self, graph={}, directed=False, *args, **kwargs):
        super(DijkstraGraph, self).__init__(graph, directed, *args, **kwargs)

    def build(self, start):
        """
        Dijkstra's algorithm Python implementation.

        builds the shortest path tree for every node in the graph given the start
        """
        self.distance = {} # Final distances dict
        self.parent = {} # Predecessor dict
        self.start = start
        known = [start]

        # Fill the dicts with default values
        for node in self.graph.keys():
            self.distance[node] = float("inf") # Vertices are unreachable
            self.parent[node] = None # Vertices have no predecessors

        self.distance[start] = 0 # The start vertex needs no move

        unseen_nodes = self.graph.keys() # All nodes are unseen
        unseen_nodes.remove(start) # except for the start

        while unseen_nodes:
            shortest = None
            parent = None
            node = None

            for x in known:
                # Select the node with the lowest value in a newly discovered vertex
                for y, weight in (self.graph[x]).items():
                    if y in known:
                        pass
                    elif not node:
                        shortest = weight
                        node = y
                        parent = x
                    elif self.distance[x] + weight < self.distance[x] + shortest:
                        shortest = weight
                        node = y
                        parent = x

            # Remove the selected node from unseen_nodes
            if node:
                self.parent[node] = parent
                self.distance[node] = self.distance[x] + shortest
                unseen_nodes.remove(node)
                known.append(node)

    def find_path(self, end):
        """
        returns the path from the start to the end
        """
        path = []
        node = end

        if not self.start:
            return path

        # While we are not arrived at the beginning
        while not (node == self.start):
            if path.count(node) == 0:
                path.insert(0, node) # Insert the parent of the current node
                node = self.parent[node] # The current node becomes its parent
            else:
                break

        path.insert(0, self.start) # Finally, insert the start vertex
        return path


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

    graph = DijkstraGraph(initial)
    graph.build('A')
    path = graph.find_path('G')
    print path
