#!/usr/bin/env python
class Heap(object):
    """
    implements a min-heap for integers

    to simplify the index calculations we start at array[1] leaving array[0] = None

    in practice just use heapq
    """
    priority_queue = [None]

    @property
    def number_of_elements(self):
        """
        we need to compensate for having array[0] = None
        """
        return len(self.priority_queue) - 1

    def __init__(self, heap=[]):
        for element in heap:
            self.insert(element)

    def insert(self, element):
        self.priority_queue.append(element)
        self._bubble_up(len(self.priority_queue) - 1)

        return True

    def pop(self):
        if len(self.priority_queue) == 1:
            return None

        dominant = self.priority_queue[1]

        if len(self.priority_queue) == 1:
            return
        elif len(self.priority_queue) == 2:
            self.priority_queue.pop(1)
        else:
            self.priority_queue[1] = self.priority_queue.pop(len(self.priority_queue) - 1)
            self._bubble_down(1)

        return dominant

    def show(self):
        print self.priority_queue[1:]

    def _bubble_up(self, index):
        parent = self._parent(index)

        # we're at the root
        if parent == -1:
            return

        elif self.priority_queue[parent] > self.priority_queue[index]:
            self.priority_queue[parent], self.priority_queue[index] = self.priority_queue[index], self.priority_queue[parent]
            self._bubble_up(parent)

    def _bubble_down(self, index):
        """
        this is also referred to as heapify
        """
        parent = self.priority_queue[index]
        left_child_index = self._left_child_index(index)
        right_child_index = self._right_child_index(index)

        # get children
        try:
            left_child = self.priority_queue[left_child_index]
        except IndexError:
            left_child = None

        try:
            right_child = self.priority_queue[right_child_index]
        except IndexError:
            right_child = None

        # determine dominant child
        if not left_child and not right_child:
            # don't need to do anything when there are no children
            return
        elif left_child and right_child:
            if left_child < right_child:
                dominant_child_index = left_child_index
            else:
                dominant_child_index = right_child_index
        elif left_child and not right_child:
            dominant_child_index = left_child_index
        elif not left_child and right_child:
            dominant_child_index = right_child_index
        else:
            dominant_child_index = None

        # test dominant child and swap
        if dominant_child_index and self.priority_queue[dominant_child_index] < parent:
            self.priority_queue[index], self.priority_queue[dominant_child_index] = self.priority_queue[dominant_child_index], self.priority_queue[index]
            self._bubble_down(dominant_child_index)

    def _parent(self, index):
        return int(index / 2)

    def _left_child_index(self, index):
        return index * 2

    def _right_child_index(self, index):
        return index * 2 + 1


if __name__ == '__main__':
    """
    this main function implements Heap Sort
    """
    # test1 = [1492, 1783, 1776, 1804, 1865, 1945, 1963, 1918, 2001, 1941]
    test2 = [1945, 1963, 1918, 2001, 1941, 1492, 1783, 1776, 1804, 1865]
    heap = Heap(test2)
    heap.show()

    sort = [heap.pop() for index in range(heap.number_of_elements)]

    print sort
