import unittest

class TestClass(unittest.TestCase):
    def test_bobo(self):
        self.assertEqual('bobo', "bo" + 'bo')

if __name__ == "__main__":
    unittest.main()
