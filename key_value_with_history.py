import time
import unittest

class KeyValueStore(object):

    def __init__(self):
        self.data = {}

    def get(self, key):
        return self.data[key][0][1]

    def set(self, key, value):
        if not self.data.has_key(key):
            self.data[key] = []
        self.data[key].insert(0, [time.time(), value])

    def history(self, key):
        return self.data[key]

class TestKeyValueHistory(unittest.TestCase):
    def test_basic(self):
        kv = KeyValueStore()
        kv.set('a', 123)
        self.assertEqual(kv.get('a'), 123)

    def test_history(self):
        kv = KeyValueStore()
        kv.set('a', 123)
        kv.set('a', 321)
        self.assertEqual(len(kv.history('a')), 2)
        self.assertEqual(kv.history('a')[0][1], 321)
        self.assertEqual(kv.history('a')[1][1], 123)

if __name__ == '__main__':
    unittest.main()