#!/usr/bin/env python
from random import randrange

def quicksort(arr):
    """
    implements quick sort on arrays using list comprehension and a randomized pivot

    If the array is guarenteed to be radomized
    it is better to just keep picking the first element in the array

    However this will fail if we run quicksort on an already sorted array,
    in which case we need the rangom pivot.

    You can do the following if the array is guarenteed to be random:
    will not work on already sorted arrays.

    pivot = arr[0]
    lesser = quicksort([x for x in arr[1:] if x <= pivot])
    greater = quicksort([x for x in arr[1:] if x > pivot])

    In production it's recommended to use Python's built-in `sorted` function

    http://en.literateprograms.org/Quicksort_(Python)
    """
    # just return the array if we don't have more than 1 element
    if len(arr) <= 1:
        return arr

    # take out random element
    pivot = arr.pop(randrange(len(arr)))

    # regroup array into lower, higher sets
    lesser = quicksort([x for x in arr if x <= pivot])
    greater = quicksort([x for x in arr if x > pivot])

    # combine and return groups
    return lesser + [pivot] + greater


def quicksort2(arr):
    """
    this implements a more traditional quicksort with the standard partitioning step

    Although this is an intuitively appealing way to perform list partitioning,
    Python's lack of support for recursion elimination causes the recursive implementation
    to suffer from linear stack usage, which is not acceptable for large lists.

    An iterative implementation (i.e. a manual tail call optimization) solves this problem.
    """
    if len(arr) <= 1: 
        return arr
    else:
        pivot = arr[0]
        lesser, equal, greater = _partition(arr[1:], [], [pivot], [])
        return quicksort2(lesser) + equal + quicksort2(greater)

def _partition(arr, lesser, equal, greater):
    if arr == []:
        return (lesser, equal, greater)
    else:
        head = arr[0]

        if head < equal[0]:
            return _partition(arr[1:], lesser + [head], equal, greater)
        elif head > equal[0]:
            return _partition(arr[1:], lesser, equal, greater + [head])
        else:
            return _partition(arr[1:], lesser, equal + [head], greater)


if __name__ == '__main__':
    print quicksort(list('QUICKSORT'))
    print quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3])

    print quicksort2(list('QUICKSORT'))
    print quicksort2([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3])
