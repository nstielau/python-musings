#!/usr/bin/env python

import unittest

fibonacci_sequence = [0, 1]

def nthFibonacci(index):
    """Takes a zero-based index and return that element of the fibonacci sequence"""
    # TODO: validate input (negatives, or non-integer)
    # happy case, weve already generated the sequence up to that point
    # we can return it in O(1)
    if len(fibonacci_sequence) > index:
          return fibonacci_sequence[index]

    # Well have to generate the sequence
    current_index = len(fibonacci_sequence) - 1
    for i in range(index - current_index):
        current_value = fibonacci_sequence[current_index + i]
        prev_value = fibonacci_sequence[current_index + i - 1]
        fibonacci_sequence.append(current_value + prev_value)

    return fibonacci_sequence[index]



class TestFibonacci(unittest.TestCase):
    def test_0th(self):
        self.assertEquals(nthFibonacci(0), 0)

    def test_1st(self):
        self.assertEquals(nthFibonacci(1), 1)

    def test_2nd(self):
        self.assertEquals(nthFibonacci(2), 1)

    def test_3rd(self):
        self.assertEquals(nthFibonacci(3), 2)

    def test_4th(self):
        self.assertEquals(nthFibonacci(4), 3)

    def test_5th(self):
        self.assertEquals(nthFibonacci(5), 5)

    def test_5th(self):
        self.assertEquals(nthFibonacci(6), 8)

if __name__ == "__main__":
    unittest.main()
