#!/usr/bin/env python
"""
merge sort using arrays

sort by divide and conquere
"""
def mergesort(arr):
    """
    keep splitting the array down to one element
    then merge the arrays
    """
    length = len(arr)

    # return the array if only 1 or 0 elements
    if length < 2:
        return arr
    else:
        middle = length / 2

    left = mergesort(arr[:middle])
    right = mergesort(arr[middle:])

    return _merge(left, right)


def _merge(left, right):
    """
    merge the arrays keeping them sorted
    """
    ret = []
    i, j = 0, 0
    left_length = len(left)
    right_length = len(left)

    # keep plucking the smallest element until the end of an array
    while i < left_length and j < right_length:
        if left[i] <= right[j]:
            ret.append(left[i])
            i += 1
        else:
            ret.append(right[j])
            j += 1

    # we might have ended with elements left in one array, add them
    ret += left[i:]
    ret += right[j:]

    return ret
                

if __name__ == '__main__':
    merge = mergesort(list('MERGESORT'))
    print merge
