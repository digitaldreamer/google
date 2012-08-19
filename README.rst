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


==========================
Sorting: Know how to sort.
==========================

Bubble Sort (BAD): O(n^2)
=========================

| iterate through the entire array swapping the smaller neighbor with the larger
| repeat until no swaps are needed


Selection Sort (BAD): O(n^2)
============================

| repeatedly identify the smallest remaining unsorted element and put it at the end of the sorted portion of the array
| easy to program but slow


Insertion Sort (BAD): O(n^2)
============================

start with a single element and incrementally insert the remaining elements into a new array

You should know the details of at least one n*log(n) sorting algorithm, preferably two (say, quick sort and merge sort). Merge sort can be highly useful in situations where quick sort is impractical, so take a look at it.

Hashtables: Arguably the single most important data structure known to mankind. You absolutely should know how they work. Be able to implement one using only arrays in your favorite language, in about the space of one interview.


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

| can be implamented with either arrays or linked lists,
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


===========
Algorithms:
===========

depth-first search
breadth-first search


=======
Graphs:
=======

Graphs are really important at Google.

There are 3 basic ways to represent a graph in memory (objects and pointers, matrix, and adjacency list); familiarize yourself with each representation and its pros & cons.

You should know the basic graph traversal algorithms: breadth-first search and depth-first search. Know their computational complexity, their tradeoffs, and how to implement them in real code.

If you get a chance, try to study up on fancier algorithms, such as Dijkstra and A*.


======================
Other Data Structures:
======================

You should study up on as many other data structures and algorithms as possible. You should especially know about the most famous classes of NP-complete problems, such as traveling salesman and the knapsack problem, and be able to recognize them when an interviewer asks you them in disguise. Find out what NP-complete means.


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
