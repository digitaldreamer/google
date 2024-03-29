######
GOOGLE
######


=============================
Coding: C++,  Java or Python.
=============================

You will be expected to write some code in at least some of your interviews. You will be expected to know a fair amount of detail about your favorite programming language. 


==============================================================
Big-O notations: "the run time characteristic of an algorithm"
==============================================================

determine if an algorithm is appropriate for a problem of a given size:
    f(n) = O(g(n)) < c * g(n)

sum of two functions is dominated by the larger one

|    O(f(n)) + O(g(n)) -> O(max(f(n),g(n))
|    n^3 + n^2 = O(n^3)

ignore constant multipliers:
    O(c*f(n)) -> O(f(n))

fastest -> slowest

* 1		constant, no dependence on n: (adding or printing)
* log(n)		logarithmic, grow slowly: (binary search)
* n		linear, look at each item once: (getting biggest item, averaging)
* n * lg(n)	superlinear, grow a little faster than linear: (quicksort, mergesort)
* n^2		quadratic, look at all the pairs, good till around 10,000: (insortion sort, selection sort)
* 2^n		exponential, look at all subsets, quickly becomes useless
* n!		factorial, generate all permutations, almost useless

logarithm
=========

| logarithms are an inverse exponential function:
| b^x = y => x = log b (y)

* exponential functions grow fast therefor logarithms grow slowly
* show up when things are repeatedly halved or doubled
* O(log n) algorithms are fast enough to work on data sets of almost any size

* binary logarithm (base 2): lg x
* natrual logarithm (base e): ln x
* comon logarithm (base 10): log x
* the base has no impact on growth rate

| logarithms cut any function down to size: the growth rate of the log of any polynomial is O(lg n) because:
| log a (n^b) = b * log a (n)

log a (xy) = log a (x) + log a (y)

convert one base to another:
log a (b) = log c (b) / log c (a)

binary tree
-----------

`Binary Trees`_

bits
----

* there are two bit patterns (1 or 0) of length 1
* we need 2^lenght = numbers, or lenght = log 2 (numbers)

fast exponentiation
-------------------

compute a^n::

    notice: n = n/2 + n/2
    a^n = (a^(n/2))^2 if n is even
    a^n = a * (a^(n/2))^2 if n is odd
    we can halve the amount of multiplications O(lg n)

http://www.topcoder.com/tc?module=Static&d1=tutorials&d2=alg_index


===============
Data Structures
===============

| When dealing with large data sets only linear or near linear O(n log(n)) are likely to be fast enough.
| Selecting the right data structure is often the key to getting the time complexity down to this point

2 types of data structures

* contiguously allocated
    * single slabs of memory
    * arrays, matrices, heaps, hash tables

* linked data
    * distinct chuncks of memory bound together by pointers
    * lists, trees, graphs


Arrays
======

contigously-allocated data structure

Good

    * constant time access given the index: can access the element directly for a given index
    * space efficiency: no need for meta data like pointer links
    * memory locality: the data is next to each other in memory

Bad

    * hard to adjust their size: can waste space allocating too much memory to compensate
    * if need to adjust the size of the array it's good to double or halve the size on each step


Linked Lists
============

linked data structure

Good

    * overflow can never occure unless if totally out of memory
    * easier and faster to insert/delete

Bad

    * require extra space to hold the pointer
    * cannot efficiently randomly access items
    * harder to cache because the data lacks memory locality: might not be clustered together


Containers
==========

storage and retrieval of data independant of content

| can be implemented with either arrays or linked lists,
| the key is whether the upper bound on the size of container is known in advance,
| in which case an array would be more efficient.


Stacks
------

* LIFO - last in first out
* simple to implement
* good for batch jobs or when order doesn't matter

functions

* push - insert item at the top of stack
* pop - retrieve and remove item on top of stack


Queues
------

* FIFO - first in first out
* fair way to control waiting times: minimizes the maximum time spent waiting (the average time will be the same regardless of LIFO or FIFO)
* harder to implemnent than stacks so typically used when order is important, otherwise use a stack

functions

* put - insert item at the back of queue
* get - retrieve and remove item at the front of queue


Priority Queues
---------------

* allows inserting, retrieving, and deleting by weighted importance
* new elements can be inserted at arbitrary intervals
* better to insert in place rather than resort entire data set

functions

* insert - insert element into queue
* min/max - retrieve min/max element in queue
* delete_min / delete_max - delete min/max element in queue


Dictionaries
============

| a set of n records, each identified by one or more key fields
| permits access to data items by content: stick and item in a dictionary so you can find it when needed

* can be built with unsorted/unsorted (double) linked lists, sorted/unsorted arrays, hash tables, binary tree, B-tree, skip lists

operations

* search(D, k): if exists, return a pointer to the element in dictionary (D) whose key value is the key (k)
* insert(D, x): add data item (x) to the set in dictionary (D)
* delete(D, x): remove the data item (x) from the dictionary (D)
* max(D), min(D): retrieve the largest/smallest key from the dictionary (D) (priority queue)
* predecessor(D, k), successor(D, k): retrieve the item from dictionary (D) whose key (k) is immediately before/after k in the sort order

Costs

=========== ============== ============ =========== ================== ========= ================
operation   unsorted array sorted array unsorted ll double unsorted ll sorted ll double sorted ll
=========== ============== ============ =========== ================== ========= ================
search      O(n)           O(log n)     O(n)        O(n)               O(n)      O(n)
insert      O(1)           O(n)         O(1)        O(1)               O(n)      O(n)
delete      O(1)*          O(n)         O(n)        O(1)               O(n)      O(1)
max         O(n)           O(1)         O(n)        O(n)               O(1)      O(1)
min         O(n)           O(1)         O(n)        O(n)               O(1)      O(1)
predecessor O(n)           O(1)         O(n)        O(n)               O(n)      O(1)
successor   O(n)           O(1)         O(n)        O(n)               O(1)      O(1)
=========== ============== ============ =========== ================== ========= ================

\* to delete an item in unsorted array leaves a hole, you can move every element after the deltion up a level for O(n), or you can cheat and replace the hole with the last element for O(1)
| can maintain a pointer to the end of a double ll


Hash Tables
-----------

| Arguably the single most important data structure known to mankind.
| You absolutely should know how they work.
| Be able to implement one using only arrays in your favorite language, in about the space of one interview.

* very effective way to maintain a dictionary, and often the best data structure to maintain a dictionary
* exploit constant time lookup of an index in an array
* a hash function mathematically maps keys to integers which is used to index the array
* ideally the hash values will be uniformly distributed
* the main idea of hashing is to represent a large object with a single number that can then be manipulated in constant time
* optimizing hash table performance is surprisingly complicated for such a conceptually simple data structure

collision detection
    sometimes two unique values will have the same key
    be prepared to handle this situation

* chaining
    - each index constains all values at that index (buckets)
    - the easiest way to resolve collisions but devotes a considerable amount of memory to pointers
* open addressing
    - the hash table is maintained as an array of elements initialized to null
    - on insertion check to see if position is empty; if so, insert it
    - if not insert the item into the next open slot in the array (sequential probing)
    - if the table isn't too full the contiguous runs should be short hence each element should be closet to its intended position
    - searching for an element now requires us to go to the index and check if it's the one we want, if not keep checking the length of the run
    - deletion in open addressing is tricky because we need to rearrange all elements in the run after the deleted element

Can be helpful when looking for duplicates on large files (collision detection), or detecting if a file has changed or not

| Worst-case bounds on hashing are terrible, but a proper hash function can confidently yield good behavior.
| Hashing is a fundamental idea in randomized algorithms yielding linear expected-time algorithms for problems otherwise O(n log n) or O(n^2).


Specialized Data Structures
---------------------------

String Data Structures
    Character strings are usually arrays
    suffix trees/arrays preprocess strings to make pattern matching faster

Geometric Data Structures
    usually a collection of data points and regions (polygons)
    kd-trees organize points and regions by geometric location to support faster search

Graph Data Structures
    typically represented by adjancency matrices or adjancency lists (sometimes objects and pointers)
    graph representation can have a substantial impact on operational time

Set Data Structures
    subsets of items are generally represented using a dictionary to support fast membership queries


Heaps
=====

* supports priority queue operations: insert and extract-min/max
* heaps work by maintaining an order which is weaker than sorted order (more efficient)
  but stronger than random order (min/max element can be identified)
* the power of any hierarchically-structured organization is reflected
  by a tree where each node and edge (x, y) implies that x supervises or dominates y
* the root entry is at the top of the heap
* a heap labeled tree is a binary tree where each node dominates the keys of its children
    - min-heap: the root key is smaller than its children
    - max-heap: the root key is bigger than its children


Operations
----------
* insert
* extract/delete min/max value


Composition
-----------

Heaps are binary trees and can be constructed with pointers OR an array: arrays are generally better for heaps

* in an array the parent is array[floor(n/2)], and its children are array[2*n] and array[2*n + 1]
* the catch with the array is the gain in access efficiency is offset by having all missing nodes still take up space
* lose flexibility: cannot store arbitrary topologies without wasting a lot of space,
  cannot move subtrees around by chaning pointers
* because of this cannot use arrays to represent binary search trees, but it works fine for heaps
* cannot use a heap to search for an element: heaps are NOT binary search trees
    - are only interested in the root: min/max value


Construction
------------

* construct a heap by inserting a new element into the left-most open spot in the array (n + 1) position.
    - ensures a balanced tree
* if the new key is not dominated by its parent then swap the parent and child
    - the relationship with the other child will be preserved because the dominance will be strengthened
* recurse (bubble up) the new key up the tree to its proper position
* each insert takes O(log n), so constructing a heap takes O(n log n) with n insertions


Extact Dominant Element (min/max)
---------------------------------

* extracting the max/min is easy because it's the first element of the array, but leaves a hole
* move the right-most element to replace the root
* rebalance the tree by swapping with the most dominant child and bubbling down or heapify
* bubble down takes O(lg n)


=====
Trees
=====

| Know about trees; basic tree construction, traversal and manipulation algorithms.
| Be familiar with at least one type of balanced binary tree, whether it's a red/black tree, a splay tree or an AVL tree, and know how it's implemented.
| Understand tree traversal
| trees utilize recursion

Pre-Order, In-Order and Post-Order
==================================

depth first search traversal methods

Starting at the root of binary tree the order in which the nodes are visited define these traversal types.

Basically there are 3 main steps. (1) Visting the current node, (2) Traverse the left node and (3) Traverse the right nodes.
From Wikipedia,

To traverse a non-empty binary tree in preorder, perform the following operations recursively at each node, starting with the root node:

#. Visit the root.
#. Traverse the left subtree.
#. Traverse the right subtree.

To traverse a non-empty binary tree in inorder (symmetric), perform the following operations recursively at each node:

#. Traverse the left subtree.
#. Visit the root.
#. Traverse the right subtree.

To traverse a non-empty binary tree in postorder, perform the following operations recursively at each node:

#. Traverse the left subtree.
#. Traverse the right subtree.
#. Visit the root.


Binary Trees
============

* trees where nodes can have at most 2 children
* the number of leaves doubles every time we increase the height by one
* leaves = 2^height: or height = log 2 (n)
* short trees can have many leaves


Binary Search Tree
------------------

* have fast access to two elements: the median elements above and below the node
* built with linked lists with two pointers per node
* for any node x, all nodes in left subtree of x have keys < x, and all nodes in right subtree of x have keys > x
* all nodes have left and right pointer, parent pointer is optional
* depends entirely on the insert order to be balanced

operations

* search: O(h) h = height
* traversal: visit all nodes in tree
* insertion: can only insert in the place after an unsuccessful search of item
* deletion: more complex, need to re-link child-parent nodes across deleted element: if element had two nodes pick the smallest element in the right subtree to replace deleted node
* min/max: left/right most node


red-black trees
splay trees
n-ary trees
trie-trees


=======
Graphs:
=======

| Graphs are one of the unifying themes of Computer Science, and are really important at Google. 
| So many models can be abstracted into a graph: transportation systems, networks, circuits, interactions, relationships etc . . .
| Key to solving problems is to correctly model the data to take advantage of existing algorithms.

::

    G = (V, E): a (G) Graph is set of (V) Vertices together with a set of (E) Edges or vertex pairs.
    'n' number of vertices and 'm' edges


Flavors
=======

* undirected vs directed
    - it's undirected if edge (x, y) also implies (y, x) also exists: otherwise it's directed (can only travel one way along an edge)
    - most graphs are undirected
* weighted vs unweighted
    - A weighted graph assignes either eatch edge or vertex a weight
    - an unwighted graph has no cost distinction between edges and vertices
    - shortest paths can be found with breadth-first search on unweighted graphs, weighted graphs need more sophisticated algorithms
* simple vs non-simple
    - some edge types complicate graph structures
        + self-loop: an edge with one vertex (x, x)
        + multiedge: if edge (x, y) occurs more than once in the graph
    - any graph that avoids self-loop and multiedge are simple, otherwise the graph is non-simple
* sparse vs dense
    - a graph is sparse when only a small fraction of possible vertex pairs actually have edges
    - a graph is dense when a large fraction of possible vertex pairs have edges
    - there is no boundry between the distinctions, but typically a sparse graph has a linear amount of edges
      where a dense graph has a quadratic amount of edges
    - graphs are typically sparse
* cyclic vs acyclic
    - an acyclic graph does not contain any cycles
        + trees are connected, acyclic undirected graphs
    - directed acyclic graphs are call DAGs
        + arrise naturally in scheduling where directed edge (x, y) where activity x must occure before y
        + topological sorting orders the vertices of a DAG
* embeded vs topological
    - embedded graphs have their vertices and edges assigned geometric positions
        + any drawing of a graph is an embedding
    - sometimes graphs are defined by the geometry of its embedding
    - the underlying topology is the complete graph connected each pair of vertices: the weights are typically the distance between two pair of points
* implicit vs explicit
    - some graphs are not explicitly constructed and then traversed, but built as we use them making them implicit
    - can represent states or information about where you are in a search/sort
* labeled vs unlabeled
    - labeled graphs has each vertices assigned a name or identifier
    - unlabled graphs have no such distinctions

| the degree of a vertex is the number of edges adjacent to it: sparce graphs have low degree and dense graphs have high degree
| a graph is connected if there is a path between any two vertices
|     a connected component of an undirected graph is the set of vertices that there is a path between every pair


Friendship Graph
----------------

represents friends connections in a social network

* sparse: I have a small-subset of friends compared to the rest of the world
* undirected: we're both each other's friends
* unweighted: no friendship strength association (0 - enimies, 10 - blood brother)
* simple: I'm not my own friend
* the most popular person has the highest "degree"
* embedded: friends have locations attatched to them
* implicit: I know who my friends are (explicit), but calculations of friends of my friends are deferred.
* unlabeled: my friends have names, but generally that has no effect on analyzing the graph. Typically friends and connections are just points to be processed.


Graph Data Structures
=====================

* the data structure of a graph can have an enormous effect on performance


Adjacency Matrix
----------------

G is represented using an n x n matrix (M) where M[i,j] = 1 if (i, j) is an edge and 0 if it isn't.

* fast answer to "is (i, j) in G?"
* rapid updates for edge insertion and deletion
* uses excessive space for graphs with many vertices and relatively few edges (matrix is mostly empty)


Adjacency Lists
---------------

* adjacency lists are the right data structure for most applications of graphs
* sparse graphs can be best represented using linked lists to store the neighbors adjacent to each vertex (requires pointers)
* harder to verify if edge (i, j) is in G
    - key is to design algorithms that don't need that information

===================================== ======================
Comparison                            Winner
===================================== ======================
faster to test (x, y) is in graph     matrix
faster to find the degree of a vertex lists
less memory on small graphs           lists (m + n) vs (n^2)
less memory on large graphs           matrices
edge insertion or deletion            matrices O(1) vs O(d)
faster to traverse                    lists (m + n) vs (n^2)
better for most problems              lists
===================================== ======================


Traversal
=========

visiting every edge and vertex: traveral is a fundamental graph problem.

* graphs are like mazes: need to know how to get out
* efficiency
    - make sure we don't repeatedly go back to the same place
    - get out as fast as possible
* correctness
    - guarentee that we get out
* the key is to mark each vertex when visited and keep track of the unexplored
    - undiscovered: the initialized vertex
    - discovered: the vertex when it has been found, but have yet to check all incident edges
    - processed: the vertex after we have visited all of its incident edges

#. start with one discovered vertex
#. evaluate each edge leaving from vertex
#. if edge leads to an undiscovered vertex mark it as visited
   and add it to the list of work to do
#. igore edges that go to a discovered or processed vertex
#. consider each undirected edge twice, and directed edges once

| There are two primary ways to traverse a graph: Breadth-First Search and Depth-First Search;
| the difference is in the order in which the vertices are explored. This order depends on
| the container data structure used to store the discovered (not processed) vertices.

Queue (BFS)
    By using FIFO we explore the oldest vertices first, eploration radiates slowly out
    from the starting vertex.

Stack (DFS)
    By using LIFO we explore the vertices along a path quickly wandering away from the
    starting vertex.


Breadth-First Search
--------------------

http://en.wikipedia.org/wiki/Breadth-first_search

| BFS is an uninformed search method that aims to expand and examine all nodes of a
| graph or combination of sequences by systematically searching through every solution.
| In other words, it exhaustively searches the entire graph or sequence without considering the goal until it finds it.
|
| From the standpoint of the algorithm, all child nodes obtained by expanding a node are added to a FIFO
| (i.e., First In, First Out) queue. In typical implementations, nodes that have not yet been examined for
| their neighbors are placed in some container (such as a queue or linked list) called "open" and then once
| examined are placed in the container "closed".


Implementation
^^^^^^^^^^^^^^

* a way to discover every point
* start with the root node
* inspect all neighboring nodes
* for all neighboring nodes in turn inspect their neighboring nodes which are unvisited 
* you process nodes in the order that they are discovered
    * nodes closest to the root node are processed first
    * this property is useful in shortest path problems

#. Enqueue the root node
#. Dequeue a node and examine it
#. If the element sought is found in this node, quit the search and return a result
   (or just process the node depending on what you need to do).
#. Otherwise enqueue any successors (the direct child nodes) that have not yet been discovered.
#. If the queue is empty, every node on the graph has been examined – quit the search and return "not found".
#. If the queue is not empty, repeat from Step 2.

::
    # Graph G and a root v of G

    procedure BFS(G,v):
        create a queue Q
        enqueue v onto Q
        mark v

        while Q is not empty:
            t ← Q.dequeue()

            if t is what we are looking for:
                # process vertex
                return t

            for all edges e in G.incidentEdges(t) do
                # process edge
                o ← G.opposite(t, e)

                if o is not marked:
                    mark o
                    enqueue o onto Q

* use a data structure to maintain our knowledge about each vertex (discovered/processed)
* a vertex is discovered when we visit it the first time
* a vertex is processed when all outgoing edges from it


Path Finding
^^^^^^^^^^^^

BFS is very useful in finding paths

* the vertex that discovered vertex i is the parent[i]
* every vertex is discovered in the traversal, so every vertex except the root has a parent
* vertexes are discovered in order of increasing distance from the root resulting in a shortest path tree
* the shortest path tree is only useful if it was performed with x as the root
* BFS gives the shortest path only if the graph is unweighted


Graph Coloring
^^^^^^^^^^^^^^

Attempts to color each vertex so that no edge links two vertexes of the same color using the least amount of colors

* a bipartite graph can be colored using two colors


Depth-First Search
------------------

http://en.wikipedia.org/wiki/Depth-first_search 

| Depth-first search (DFS) is an algorithm for traversing or searching a tree, tree structure, or graph.
| One starts at the root (selecting some node as the root in the graph case) and explores as far as possible
| along each branch before backtracking.
|
| Formally, DFS is an uninformed search that progresses by expanding the first child node of the search tree
| that appears and thus going deeper and deeper until a goal node is found, or until it hits a node that has no children.
| Then the search backtracks, returning to the most recent node it hasn't finished exploring. In a non-recursive
| implementation, all freshly expanded nodes are added to a stack for exploration.

::

    Input: A graph G and a vertex v of G
    Output: A labeling of the edges in the connected component of v as discovery edges and back edges

    procedure DFS(G,v):
        label v as explored

        for all edges e in G.incidentEdges(v) do
            if edge e is unexplored then
                w ← G.opposite(v,e)

                if vertex w is unexplored then
                    label e as a discovery edge
                    recursively call DFS(G,w)
                else 
                  label e as a back edge

* DFS is conceptually just BFS using a stack insead of a queue, but recursion can eliminate the need for a stack for DFS
* DFS can track the traversal time for each vertex (every time you enter or exit a vertex increase the time counter):
  entry and exit times, which can track interesting properties
    - who is an anccestor? the time interval of y must be properly nested with x
    - how many descendants? the difference between entry and exit times divided by two for vertex v tells how many descendants v has
* DFS builds only two edge types
    - tree edges: discover new vertices
    - back edges: link to an ancestor and point back into the tree


Finding Edges
^^^^^^^^^^^^^

* back edges are the key to finding cycles in an undirected graph
* if there are no back edges then all edges are tree edges and no cycles exist
* any back edge going from x to an ancestor y creates a cycle from y to x


Articulation Vertices
^^^^^^^^^^^^^^^^^^^^^

Also called a cut-node, an Articulation Vertex is an isolated node that connects a connected component.

Any graph that has an articulation vertex is fragile because the loss of one node disconnects the graph.

The connectivity of a graph is the smallest number of vertices whose deletion will dissconnect the graph.
It is one if there is an articulation vertex.

More robust graphs without an articulation vertex are biconnected.

General graphs are more complex than trees. A DFS of a graph partitions the edges into tree edges and back edges.
Think of back edges as security cables linking a vertex back to its ancestors; the back-edge prevents any of the
vertices in between x and y to be articulation vertices.

Finding articulation vertices requires maintaining the extent to which back edges link chunks of the DFS tree back to ancestor nodes.
The relative age/rank of our ancestors can be determined from their entry times.

The key issue is determining how the reachability relation impacts whether vertex v is an articulation vertex. There are three cases:

* root cut nodes: If the root of the DFS tree has two or more children, it must be an articulation vertex.
* bridge cut nodes: If the earliest reachable vertex from v is v (there's no bridge), then deleting the single edge (parent[v], v) disconnects the graph.
  parent[v] is an articulation vertex, and so is v unless it is a leaf
* parent cut nodes: If the earliest reachable vertex from v is the parent of v, then the parent must server v from the tree unless if
  the parent is the root.

A single edge whose deletin disconnects the graph is a bridge; any graph without such an edge is edge-biconnected.

* edge (x, y) is a bridge if 1) it is a tree edge and 2) no back edge connects from y or below to x or above.


DFS on Directed Graphs
^^^^^^^^^^^^^^^^^^^^^^

When traversing undirected graphs every edge is either in the DFS tree or a back edge to an ancestor.

4 Types of edges

* tree edge - links to a child
* forward edge - links to a grandchild
* back edge - links to a grandparent
* cross edge - links to a sibling

::
    int edge_classification(int x, int y) {
        if (parent[y] == x) return (TREE);
        if (discovered[y] && !processed[y]) return (BACK);
        if (processed[y] && (entry_time[y] > entry_time[x])) return (FORWARD);
        if (processed[y] && (entry_time[y] < entry_time[x])) return (CROSS);

        printf('Warning: unclassified edge (%d, %d)\n', x, y);
    }


    DFS-graph(G)
        for each vertex u in V[G] do
            state[u] = 'undiscovered'

            for each vertex u in v[G] do
                if state[u] = 'undiscovered' then
                    initialize new component, if desired
                    DFS(G, u)


Topological Sort
^^^^^^^^^^^^^^^^

| Topological sorting is the most important oporation on directed acyclic graphs (DAGs)
| It orders the vertices on a line such that all directed edges go from left to right.
| DAGs can't contain cycles.
|
| Every DAG has at least one topological sort: it tells us an ordering to process each vertex before its sucessors.
|
| Labeling the vertices in the reverse order (can use stack) that they are marked processed finds a topological sort.


Strongly Connected Components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Strongly connected components are chunks of a graph where directed paths exist between all pairs of vertices within a given chunk.

A directed graph is strongly connected if there is a directed path between any two vertices.

Road networks should be strongly connected.


Weighted Graphs
===============

Graphs that have a weight assigned to an edge need more advanced algorithms.


Minimum Spanning Trees
----------------------

| A spanning tree to graph G = (V, E) is a subset of edges from E forming a tree connecting all vertices of V.
| The minimum spanning tree is whose sum of edge weights is as small as possible.
|
| Any tree is the smallest possible connected graph in terms of edges.
| The minimum spanning tree is the smallest connected graph in terms of edge weight.
|
| A minimum spanning tree minimizes the total length over all possible spanning trees.
| There can be more than one minimum spanning tree in a graph.


Prim's Algorithm
^^^^^^^^^^^^^^^^

Start from one vertex and grow the rest of the tree one edge at a time picking the smallest
available choice until all vertices are included.

It's a primitive GREEDY algorithm that repeatedly selects the smallest weight edge to build a minimum spanning tree.

Pretty slow: O(n^2) unoptimized, or O(m + n lg(n)) optimized

::

    Prim-MST(G)
        select arbitrary vertex s to start the tree from

        while (there are still nontree vertices)
            select the edge of minimum eight between a tree and nontree vertex
            add the selected edge and vertex to the tree


Kruskal's Algorithm
^^^^^^^^^^^^^^^^^^^

Another GREEDY algorithm to build Minimum Spanning Trees that works more efficiently on sparse graphs than Prim's

It doesn't start with a vertex; instead it builds up connected components.

* each vertex starts out as a separate component
* repeatedly consider the smallest remaing edge and test whether the two endpoints lie within a single component
* if the endpoints are in different components insert the edge and merge the components together
* edge weight ties are broken arbitrarily
* since each component is a tree we don't test for cycles

| runs in O(mn) time using a general O(n lg n) sort,
| but can run in O(n lg n) using a union-find that runs in O(lg n)

::

    Kruskal-MST(G)
        put the edges in a priority queue ordered by weight
        count = 0

        while (count < n -1)
            get next edge (v, w)

            if (component(v) != component(w))
                add to Tree
                merge component(v) and component(w)


Union-Find Data Structure
-------------------------

http://en.wikipedia.org/wiki/Disjoint-set_data_structure

| A set partition is a partitioning of the elements into a collection of disjointed subsets.
| Each element is in one subset. Connected components of a graph can be represented as a set partition.

We need these functions:

* Find: Determine which subset a particular element is in. This can be used for determining if two elements are in the same subset.
* Union: Join two subsets into a single subset.
* MakeSet: makes a set containing only a given element

Always attach the smaller tree to the larger


The Shortest Path (TSP)
-----------------------

| A path is a sequence of edges connecting two vertices

The shortest path of an unweighted graph can be found using Breadth First Search

Determining shortest paths on weighted graphs requires more sophisticated algorithms


Dijkstra's Algorithm
^^^^^^^^^^^^^^^^^^^^

Given a starting vertex (s) it finds the shortest path to every other vertex in the graph including the target (t).

Performed in a series of rounds where each round finds a new shortest path to another vertex

Runs in O(n^2)

::

    Dijkstra-TSP(G, s, t)
        known = {s}

        for i = 1 to n, dist[i] = infinity
        for each edge (s, v), dist[v] = w(s, v)
        last = s

        while (last != t)
            select v-next, the unknown vertex minimizing dist[v]

            for each edge (v-next, x), dist[x] = min[dist[x], dist[v-next] + w(v-next, x)]
            last = v-next
            known = known U {v-next}

| The basic idea is similar to Prim's algorithm: for each iteration we add exactly one vertex to the shortest path tree.
| Like Prim's we keep track of the best paths seen for all visible vertices outside the tree and insert them in order of increasing cost.

| The difference between Prim and Dijkstra is how they rate the desirability of each outside vertex.
| Prim only cares about edge weight, Dijkstra cares about the distance of the outside vertex to s.

| Dijkstra only works on positive cost weights.


All Pairs Shortest Path
^^^^^^^^^^^^^^^^^^^^^^^


A* 
^^^^


=====================
Other Data Structures
=====================

| You should study up on as many other data structures and algorithms as possible.
| You should especially know about the most famous classes of NP-complete problems,
| such as traveling salesman and the knapsack problem,
| and be able to recognize them when an interviewer asks you them in disguise.


==========================
Sorting: Know how to sort.
==========================

* sorting is the basic building block that many algorithms are built around
* most algorithms involve sorting
* historically computers spend more cycles sorting than doing anything else
* sorting is the most thoroughly studied problem in computer science
* many problems become easy once the data is sorted
    - searching: binary search reduces search times to O(log n); search preprocessing is arguably the most important application of sorting.
    - closest pair: elements are next to each other
    - uniqueness: special case closest pair
    - frequency distribution: easy to count since identical items are lumped together
    - selection: can get the kth larges item by looking at the kth position
    - convex hulls: What is the polygon of smallest area that contains a given set of points? like a rubber band stretched over the points. Construct by inserting points from left to right.
* O(n^2) will work only to around 1,000 ~ 10,000 data points, beyond that you'll need O(n log n)


Bubble Sort: O(n^2)
===================

| iterate through the entire array swapping the smaller neighbor with the larger
| repeat until no swaps are needed


Selection Sort: O(n^2)
======================

| repeatedly identify the smallest remaining unsorted element and put it at the end of the sorted portion of the array
| easy to program but slow


Insertion Sort: O(n^2)
======================

start with a single element and incrementally insert the remaining elements into a new array that you keep sorted


Sorting by Incremental Insertion
================================

| incremental insertion builds up a complex structure of n items by building n-1 items then inserting the last item
| insertion sort takes O(n^2), but it performs much better if the data is already sorted.
| inserting into a balanced search tree takes O(log n) for a total of O(n log n)
| useful in geometric algorithms


Heap Sort: O(n log n)
=====================

`Heaps`_

| use data structures to drive the logic
| simply an implementation of selection sort using the right data structure (heap / priority queue)
| speeds the operation from O(n^2) to O(n log n)

::

    SelectionSort(A)
        for i = 1 to n do
            sort[i] = find-minimum from A
            delete-minimum from a
        return sort


Merge Sort O(n log n)
=====================

| divide and conquer
| recursive algorithms reduce large problems into smaller ones
| runs great on linked-lists because doesn't rely on random access like heapsort and quicksort

* split the data into two groups
* sort the two groups recursively
* interleave the two sorted lists to order the elements
* disadvantage is it needs an auxilary buffer when sorting arrays

::

    The merge() method merges the two sorted sublists.
    The mergesort() method, which runs recursively,
    divides the unsorted lists into two sublists and sorts each sublist.

    mergesort(A):
        merge(mergesort(a[0, n/2]), mergesort(a[n/2] + 1, n))


Quick Sort 0(n log n) *on average
=================================

sort by randomization

::

    * The performance depends on picking pivots that bisect the array in the middle.
    Worst case of always picking either smallest or largest element gives us selection sort and O(n^2).

    Generally speaking quick sort runs 2-3 times FASTER than merge sort and heap sort primarily because
    the operations on the inner-most loop are simpler. Good thing it lives up to its name!


* select a random pivot item p from n items
* separate the rest of the items into two groups
    - low pile: contains items before p in sorted order
    - high pile: contains items afer p in sorted order
* combined groups = low + equal + hight

How does this work?

#. the pivot element ends up in the correct position in the array
#. after partitioning no elements flop from one site/pile to the other
#. you can sort elements to the right and left of the pivot independently


Randomization is a good tool to improve algorithms with bad worst-case bug good avarage-cost complexity.

random sampling
    can get the median value of n things without looking at them all by picking a random sub-set

randomized hashing
    randomizing the hash function so that data doesn't end up grouped on the same keys

randomized search
    randomizing can be used in search techniques lik simulated annealing


Distribution Sort
=================

distribution sort is a form of bucketing

* read through the list and group items into buckets of known sort order
    - i.e. to sort names into a phone book look at the last name and group by starting letter
    - we now know group O comes before group P etc...
* move through each group further segmenting the list by second letter
* it is a good method when we know there is a relatively even distribution
* downside is performance is terrible on unexpected data sets
* there is no guarenteed worst-case behavior unlike balanced binary trees
    - heuristic data structures provide no promises on unexpected input distributions


======
Search
======

Depth-first Search

Breadth-first Search


============
Mathematics:
============

Some interviewers ask basic discrete math questions. This is more prevalent at Google than at other companies because counting problems, probability problems, and other Discrete Math 101 situations surrounds us. Spend some time before the interview refreshing your memory on (or teaching yourself) the essentials of combinatorics and probability.

You should be familiar with n-choose-k problems and their ilk – the more the better.


==================
Operating Systems:
==================

Know about processes, threads and concurrency issues. Know about locks and mutexes and semaphores and monitors and how they work.

Know about deadlock and livelock and how to avoid them. Know what resources a processes needs, and a thread needs, and how context switching works, and how it's initiated by the operating system and underlying hardware. Know a little about scheduling.

The world is rapidly moving towards multi-core, so know the fundamentals of "modern" concurrency constructs.

For information on System Design:
http://research.google.com/pubs/DistributedSystemsandParallelComputing.html



A few last tips:
•	Talk through your thought process about the questions you are asked. In all of Google's interviews, our engineers are evaluating not only your technical abilities but also how you approach problems and how you try to solve them.
•	Ask clarifying questions if you do not understand the problem or need more information. Many of the questions asked in Google interviews are deliberately underspecified because our engineers are looking to see how you engage the problem. In particular, they are looking to see which areas leap to your mind as the most important piece of the technological puzzle you've been presented.
•	Think about ways to improve the solution you'll present. In many cases, the first answer that springs to mind isn't the most elegant solution and may need some refining. It's definitely worthwhile to talk about your initial thoughts to a question, but jumping immediately into presenting a brute force solution will be received less well than taking time to compose a more efficient solution.























http://steve-yegge.blogspot.com/2008/03/get-that-job-at-google.html
Tech Prep Tips

The best tip is: go get a computer science degree. The more computer science you have, the better. You don't have to have a CS degree, but it helps. It doesn't have to be an advanced degree, but that helps too.

However, you're probably thinking of applying to Google a little sooner than 2 to 8 years from now, so here are some shorter-term tips for you.

Algorithm Complexity: you need to know Big-O. It's a must. If you struggle with basic big-O complexity analysis, then you are almost guaranteed not to get hired. It's, like, one chapter in the beginning of one theory of computation book, so just go read it. You can do it.

Sorting: know how to sort. Don't do bubble-sort. You should know the details of at least one n*log(n) sorting algorithm, preferably two (say, quicksort and merge sort). Merge sort can be highly useful in situations where quicksort is impractical, so take a look at it.

For God's sake, don't try sorting a linked list during the interview.

Hashtables: hashtables are arguably the single most important data structure known to mankind. You absolutely have to know how they work. Again, it's like one chapter in one data structures book, so just go read about them. You should be able to implement one using only arrays in your favorite language, in about the space of one interview.

Trees: you should know about trees. I'm tellin' ya: this is basic stuff, and it's embarrassing to bring it up, but some of you out there don't know basic tree construction, traversal and manipulation algorithms. You should be familiar with binary trees, n-ary trees, and trie-trees at the very very least. Trees are probably the best source of practice problems for your long-term warmup exercises.

You should be familiar with at least one flavor of balanced binary tree, whether it's a red/black tree, a splay tree or an AVL tree. You should actually know how it's implemented.

You should know about tree traversal algorithms: BFS and DFS, and know the difference between inorder, postorder and preorder.

You might not use trees much day-to-day, but if so, it's because you're avoiding tree problems. You won't need to do that anymore once you know how they work. Study up!

Graphs

Graphs are, like, really really important. More than you think. Even if you already think they're important, it's probably more than you think.

There are three basic ways to represent a graph in memory (objects and pointers, matrix, and adjacency list), and you should familiarize yourself with each representation and its pros and cons.

You should know the basic graph traversal algorithms: breadth-first search and depth-first search. You should know their computational complexity, their tradeoffs, and how to implement them in real code.

You should try to study up on fancier algorithms, such as Dijkstra and A*, if you get a chance. They're really great for just about anything, from game programming to distributed computing to you name it. You should know them.

Whenever someone gives you a problem, think graphs. They are the most fundamental and flexible way of representing any kind of a relationship, so it's about a 50-50 shot that any interesting design problem has a graph involved in it. Make absolutely sure you can't think of a way to solve it using graphs before moving on to other solution types. This tip is important!

Other data structures

You should study up on as many other data structures and algorithms as you can fit in that big noggin of yours. You should especially know about the most famous classes of NP-complete problems, such as traveling salesman and the knapsack problem, and be able to recognize them when an interviewer asks you them in disguise.

You should find out what NP-complete means.

Basically, hit that data structures book hard, and try to retain as much of it as you can, and you can't go wrong.

Math

Some interviewers ask basic discrete math questions. This is more prevalent at Google than at other places I've been, and I consider it a Good Thing, even though I'm not particularly good at discrete math. We're surrounded by counting problems, probability problems, and other Discrete Math 101 situations, and those innumerate among us blithely hack around them without knowing what we're doing.

Don't get mad if the interviewer asks math questions. Do your best. Your best will be a heck of a lot better if you spend some time before the interview refreshing your memory on (or teaching yourself) the essentials of combinatorics and probability. You should be familiar with n-choose-k problems and their ilk – the more the better.

I know, I know, you're short on time. But this tip can really help make the difference between a "we're not sure" and a "let's hire her". And it's actually not all that bad – discrete math doesn't use much of the high-school math you studied and forgot. It starts back with elementary-school math and builds up from there, so you can probably pick up what you need for interviews in a couple of days of intense study.

Sadly, I don't have a good recommendation for a Discrete Math book, so if you do, please mention it in the comments. Thanks.

Operating Systems

This is just a plug, from me, for you to know about processes, threads and concurrency issues. A lot of interviewers ask about that stuff, and it's pretty fundamental, so you should know it. Know about locks and mutexes and semaphores and monitors and how they work. Know about deadlock and livelock and how to avoid them. Know what resources a processes needs, and a thread needs, and how context switching works, and how it's initiated by the operating system and underlying hardware. Know a little about scheduling. The world is rapidly moving towards multi-core, and you'll be a dinosaur in a real hurry if you don't understand the fundamentals of "modern" (which is to say, "kinda broken") concurrency constructs.

The best, most practical book I've ever personally read on the subject is Doug Lea'sConcurrent Programming in Java. It got me the most bang per page. There are obviously lots of other books on concurrency. I'd avoid the academic ones and focus on the practical stuff, since it's most likely to get asked in interviews.

Coding

You should know at least one programming language really well, and it shouldpreferably be C++ or Java. C# is OK too, since it's pretty similar to Java. You will be expected to write some code in at least some of your interviews. You will be expected to know a fair amount of detail about your favorite programming language.












1. Make sure you are comfortable with a programming language – either C++ or Java would be good, but I think they don’t mind really if you use some other language. Python, for instance. I read through a C++ book, about a chapter a day, just to refresh concepts, and also got more comfortable with the STL (it had been awhile!).


2. Make sure you can write simple loops and manipulate simple data structures in your sleep, blindfolded with your hands tied behind your back. Just practice a few things like quick sort, merge sort, tree traversal, etc. There’s no way someone is going to ask you to write a merge sort, but it is really good practice. I did a ton of this while reading through a data structures book. 


3. Make sure you know your order notation and which well-known algorithms have which complexity. For sorting algorithms, it’s handy to know which require random access, which can benefit from parallel processing, etc. 


4. Practice writing code on a whiteboard. Take a problem that you don’t know the answer to, and try to solve it on the whiteboard. Work out the algorithm, maybe draw a picture, and then write the code. Don’t do it in an IDE, don’t even do it in an editor. I would even recommend a whiteboard over paper. It’s just different, and you have to practice it to be comfortable with it.


5. Get a list of problems and practice solving them – I found the book “Programming Interviews Exposed – 2nd Edition” to be great. The problems in this book were mostly harder than the ones I got in my interviews. Doing them really got me in the mind-set of solving problems, though, which is essential. Here are some (from the internet – obviously they won’t ask you these, but again, good practice!):

a. http://www.drizzle.com/~jpaint/google.html has this one, which is a good small practice one: Write a function f(a, b) which takes two character string arguments and returns a string containing only the characters found in both strings in the order of a. Write a version which is order N-squared and one which is order N.

b. http://careers.cse.sc.edu/googleinterview has this one (and others): Write some code to find all permutations of the letters in a particular string.

c. People also recommended this site: http://www.topcoder.com/tc?module=Static&d1=tutorials&d2=alg_index (I didn’t use it at all, but I know of others here who did)

http://stevenwoods.blogspot.com/2009_11_29_archive.html#7476959582586330421
6. Get comfortable with big numbers.

a. There is a question here:http://www.drizzle.com/~jpaint/google.html at the bottom of the page. Try to work out what you think is the right answer. You can read what this person wrote, but the point is to just start doing problems with big numbers.

b. I’m sure you can find other problems on the internet if you look around. Google might help you there too!

I also have some non-technical prep advice that might be helpful:

1. Practice talking about yourself, what you've done in your career, what you're good at, why your resume looks the way it does, etc. Even go so far as preparing an answer to the terrifying open-ended “tell me about yourself” interview starter. No one at Google in my interviews asked me anything like that (but I know people who do). It was good confidence-building, and some of the things I practiced saying did come in handy. Make a friend listen to you as if they were an interviewer. When someone else is listening, you become more aware of all the "um's" and other bad habits you may have.

2. Prepare answers to a few standard questions. Again, these didn’t all come up with Google interviews (some did), but I found it good practice talking about myself. 

a. What did you do at your last job?

b. What is one of your strengths/weaknesses? (one place asked me for a second weakness, so I was glad I’d practiced that!)

c. Where do you see yourself in the next 3 to 5 years?

d. Why do you want this job?

e. What has been your biggest success/failure? (this is hard!)

f. Recount a situation where you encountered a conflict with a co-worker or customer.


3. Other interview tips:

a. Don’t over answer, at least at the beginning of the interview – give a brief answer and then ask them if they want you to expand. It’s really annoying as an interviewer, if the interviewee won’t stop talking!

b. Make eye contact when you answer. 

c. With problem-solving questions, keep talking as you try to navigate the problem. Make sure you understand the question and ask clarifying questions to make sure you really do. Ask if you can make assumptions, don’t just make them, etc.

d. Make sure you eat a proper breakfast - no, really, it’s important to have protein for breakfast before interviews – it will keep you going a lot better than just carbs. I actually did have bacon and eggs both mornings of my interviews – haha. Another thought is here

e. Prepare some great questions for them, ask them for business cards, learn their names before you get there – basically be interested in them!

f. Be super enthusiastic and make sure they know you LOVE their company. Also make sure you communicate that you love hard problems :-0!

4. Remember to prepare for systems-style questions as well as programming ones. For instance consider:

a) refreshing your memory on basic design patterns (probably via one of the standard text books)

b) refreshing your memory on basic protocols and communication mechanisms (TCP/IP, UDP, etc.)

c) read a bit about high-level design patterns for networks (e.g., different network structures, handling failures, etc.)

d) read about the architecture of a couple of real high-performance, highly robust systems (e.g., GFS, Sawzall, S3, etc.)
