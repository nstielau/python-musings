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

    def add_word(self, word):
        if len(word) > 0:
            if self.children.has_key(word[0]):
                self.children[word[0]].add_word(word[1:])
            else:
                first_letter = Node(word[0])
                first_letter.add_word(word[1:])
                self.children[word[0]] = first_letter



root = Node('')
root.add_word('party')
root.add_word('panache')
root.add_word('porche')
root.display()
