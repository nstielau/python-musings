#!/usr/bin/env python 

import unittest

def not_tail_permute(input):
    if len(input) == 0 or len(input) == 1:
        return [input]
    permutations = []
    for i in range(len(input)):
        for subperm in permute(input[0:i] + input[i+1:]):
            permutations.append(input[i] + subperm)
    return permutations

def permute(input, prefix='', permuations=[]):
    if len(input) == 0 or len(input) == 1:
        permutations.append(prefix+input)
        return ''       
    for i in range(len(input)):
        permutations.append permute(input[0:i] + input[i+1:], prefix + input[i], permutations):

class TestPermutation(unittest.TestCase):
    def test_one_char_permute(self):
        results = permute('a')
        self.assertEquals(len(results), 1)
        self.assertEquals(results[0], 'a')

    def test_two_char_permute(self):
        results = permute('ab')
        self.assertEquals(len(results), 2)
        self.assertIn('ab', results)
        self.assertIn('ba', results)

    def test_three_char_permute(self):
        results = permute('abc')
        self.assertEquals(len(results), 6)
        self.assertIn('abc', results)
        self.assertIn('acb', results)
        self.assertIn('bac', results)
        self.assertIn('bca', results)
        self.assertIn('cab', results)
        self.assertIn('cba', results)

if __name__ == "__main__":
    unittest.main()
