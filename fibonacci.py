#!/usr/bin/env python

import unittest

def nthFibonacciRecursive(index, previousCount=0):
    if index == 0:
        return 0 + previousCount
    elif index == 1:
        return 1 + previousCount
    else:
        return nthFibonacci(index - 1, nthFibonacci(index - 2, previousCount))

def nthFibonacci(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        prev = 1
        prev_prev = 0
        sum = 0
        for i in range(index-1):
            sum = prev + prev_prev
            prev_prev = prev
            prev = sum
        return sum
            

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
