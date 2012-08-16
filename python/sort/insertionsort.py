#!/usr/bin/env python
def insertion_sort(element):
    """
    O(n^2)

    start with a single element and incrementally insert the remaining elements into an array and sorting the elements sorted in the inserted section
    easy to program but slow
    """
    length = len(element)

    print element

    # loop through each element
    for i in range(length):
        j = i

        while(j>0 and element[j] < element[j-1]):
            # swap
            element[j], element[j-1] = element[j-1], element[j]
            j -= 1

        print element

    return element


if __name__ == '__main__':
    sorts = insertion_sort(list('INSERTIONSORT'))
