#!/usr/bin/env python

import unittest

def fizzbuzz(input):
    # input is nil, negative, non-number, float
    if int(input) % 3 == 0 and int(input) % 5 == 0:
        return 'fizzbuzz'
    if int(input) % 3 == 0:
        return 'fizz'
    if int(input) % 5 == 0:
        return 'buzz'
    return None

class GoogleInterviewException(Exception):
    pass

class TestFizzBuzz(unittest.TestCase):
    def test_mod_3(self):
        self.assertEquals(fizzbuzz(3), 'fizz')

    def test_mod_5(self):
        self.assertEquals(fizzbuzz(5), 'buzz')

    def test_mod_3_and_mod_5(self):
        self.assertEquals(fizzbuzz(15), 'fizzbuzz')

    def test_mod_3_and_mod_5(self):
        fizzbuzz(2)

if __name__ == "__main__":
    unittest.main()
