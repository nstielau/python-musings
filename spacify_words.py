#!/usr/bin/env python

import unittest

import re

def spacify_words(input, dictionary=None):
    dictionary = dictionary or {
        'hello':'',
        'ash': '',
        'a':'',
        '\d': '',
        'world': '',
        'germ': '',
        'sale': ''
    }
    results = []
    current_word = ''
    for i in range(len(input)):
        current_word += input[i]
        for pattern in dictionary:
            if pattern == current_word or re.match(pattern, current_word):
                results.append(current_word)
                current_word = ''
    return ' '.join(results)


class TestSpacify(unittest.TestCase):
    def test_spacify_words(self):
        self.assertEqual(spacify_words('ash'),'ash')
        self.assertEqual(spacify_words('ashash'),'ash ash')
        self.assertEqual(spacify_words('1123'), '1 1 2 3')
        self.assertEqual(spacify_words(''), '')
        #with self.assert_raises(Exception):
        #    spacify_words(None)
        self.assertEqual(spacify_words('helloworld'), 'hello world')
        self.assertEqual(spacify_words('germsale'), 'germ sale')
        self.assertEqual(spacify_words('ashaash'), 'ash a ash')

if __name__ == "__main__":
    unittest.main()
