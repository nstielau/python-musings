#!/usr/bin/env python 

import unittest

class Heap(object):
    def __init__(self, value, depth=1, side=None):
        self.value = value
        self.left = None
        self.right = None
        self.depth = depth
        self.side = side

    def full(self):
        return self.left and self.right

    def insert(self, newvalue):
        print "Inserting %s at %s" % (newvalue, self.depth) 
        if newvalue > self.value:
            # swap root, and retry
            old_value = self.value
            self.value = newvalue
            self.insert(old_value)
        else:
            # Find the right child
            if self.left == None:
                self.left = Heap(newvalue, self.depth+1, -1)
            elif self.right == None:
                self.right = Heap(newvalue, self.depth+1, 1)
            else:
                if self.left.full() and self.right.full():
                    self.left.insert(newvalue)
                elif self.left.full():
                    self.right.insert(newvalue)
                else:
                    self.left.insert(newvalue)

    def get_sequence(self, values_by_depth=None):
        values_by_depth = values_by_depth or {}
        values_by_depth[self.depth] = values_by_depth.get(self.depth) or []
        values_by_depth[self.depth].append(self.value)
        if self.left:
            self.left.get_sequence(values_by_depth)
        if self.right:
            self.right.get_sequence(values_by_depth)
        return values_by_depth

    def __repr__(self):
        repr = '\n'
        sequence = self.get_sequence()
        max_width = max([len(entries) for entries in sequence.values()])
        print "%s%s"% (" ", sequence)
        for i in range(len(sequence)):            
            try:
                stringified = [str(v) for v in sequence[i+1]]
                repr += "%s\n" % (' '.join(stringified))
            except Exception as e: 
                print 'Error at %s: %s' % (i, e)
        return repr + '\n'

class TestHeap(unittest.TestCase):
    def test_empty_heap(self):
        heap = Heap(None)
        self.assertEqual(heap.value, None)

    def test_single_entry_heap(self):
        heap = Heap(3)
        self.assertEqual(heap.value, 3)

    def test_single_tier_heap(self):
        heap = Heap(2)
        heap.insert(1)
        heap.insert(3)
        print heap
        self.assertEqual(heap.value, 3)

    def test_mutile_tier_heap(self):
        heap = Heap(2)
        heap.insert(1)
        heap.insert(24)
        heap.insert(11)
        heap.insert(8)
        heap.insert(4)
        print heap
        self.assertEqual(heap.value, 24)
         

if __name__ == "__main__":
    unittest.main()
