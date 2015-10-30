import unittest

class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = {}

    def __repr__(self):
        return "<Node: value={}>".format(self.value)

    def display(self):
        # print self.children
    	for letter, subtree in self.children.iteritems():
                print letter
                subtree.display()

    def words(self):
        words = []
        if len(self.children) == 0:
            return [self.value]
        for child in self.children.values():
            for word in child.words():
                words.append(self.value+word)

        return words

    def add_word(self, word):
        if len(word) > 0:
            if self.children.has_key(word[0]):
                self.children[word[0]].add_word(word[1:])
            else:
                first_letter = Node(word[0])
                first_letter.add_word(word[1:])
                self.children[word[0]] = first_letter

class TestTrie(unittest.TestCase):
    def test_adding_word_should_update_children(self):
        root = Node('')
        root.add_word('party')
        self.assertEquals(root.value, '')
        self.assertEquals(len(root.children), 1)
        self.assertIn('p', root.children.keys())

    def test_add_two_word(self):
        root = Node('')
        root.add_word('party')
        root.add_word('porche')
        pNode = root.children.values()[0]
        self.assertEquals(len(pNode.children), 2)
        self.assertIn('a', pNode.children.keys())
        self.assertIn('o', pNode.children.keys())

    def test_words_with_two_words(self):
        root = Node('')
        root.add_word('party')
        root.add_word('porche')
        self.assertEquals(len(root.words()), 2)

if __name__ == '__main__':
    unittest.main()
