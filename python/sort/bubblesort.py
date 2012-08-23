#!/usr/bin/env python
def bubble_sort(element):
    """
    O(n^2)

    iterate through the entire array swappping the smaller neighbor with the larger
    repeat until no more swaps are needed
    easy to program but slow
    """
    length = len(element)
    swapped = True

    # loop through each element
    while swapped:
        swapped = False

        for i in range(length-1):
            if element[i] > element[i+1]:
                element[i], element[i+1] = element[i+1], element[i]
                swapped = True

    return element


if __name__ == '__main__':
    sorts = bubble_sort(list('BUBBLESORT'))
