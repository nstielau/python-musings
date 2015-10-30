import unittest

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def append(self, n):
        end = self
        while end.next:
            end = end.next
        end.next = n
        n.prev = end

    def display(self):
        node = self
        while node:
            print node.value
            node = node.next

    def display_reverse(self):
        node = self
        while node.next:
            node = node.next

        while node:
            print node.value
            node = node.prev

    def to_array(self):
        to_return = []
        node = self
        while node:
            to_return.append(node.value)
            node = node.next
        return to_return

class TestLinkedList(unittest.TestCase):
    """Tests for my linked list"""
    def test_append_should_increase_length(self):
        root = Node(-1)
        new_node = Node(2)
        root.append(new_node)
        self.assertEquals(len(root.to_array()), 2)

    def test_to_array_should_create_array(self):
        root = Node(-1)
        new_node = Node(2)
        root.append(new_node)
        self.assertEquals(root.to_array(), [-1, 2])

if __name__ == "__main__":
    unittest.main()
