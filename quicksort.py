#!/usr/bin/python

import unittest

# quicksort
# Pick a pivot, return cat(less-than-pivot,pivot,greater-than-pivot)
# Pivot can be first element, but that sucks for sorted lists
# O(nLogn)

def quicksort(to_sort):
    if not type(to_sort) == list:
        raise TypeError
    if len(to_sort) <= 1:
        return to_sort
    pivot = to_sort[0]
    less_than_pivot = []
    greater_than_pivot = []
    for item in to_sort[1:]:
        if item <= pivot:
            less_than_pivot.append(item)
        else:
            greater_than_pivot.append(item)
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

class QuickSortTest(unittest.TestCase):
    def test_should_sort_basic_sort(self):
        self.assertEquals([1,2,3,4,5], quicksort([5,4,1,3,2]))

    def test_should_raise_nonlist_input(self):
        with self.assertRaises(TypeError):
            quicksort('a')
        with self.assertRaises(TypeError):
            quicksort(1)


if __name__ == "__main__":
    unittest.main()
