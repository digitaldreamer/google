#!/usr/bin/env python
def selection_sort(element):
    """
    O(n^2)

    repeatedly identify the smallest remaining unsorted element and put it at the end of the sorted portion of the array
    easy to program but slow
    """
    length = len(element)

    # loop through each element
    for i in range(length):
        placement = i
        min_char = element[i]

        # search for the minimum value
        for j in range(i, length):
            if element[j] < min_char:
                min_char = element[j]
                placement = j

        # swap the pair
        element[i], element[placement] = element[placement], element[i]

    return element


if __name__ == '__main__':
    sorts = selection_sort(list('SELECTIONSORT'))
