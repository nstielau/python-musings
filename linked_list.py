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


root = Node(-1)
for i in range(10):
    a = Node(i)
    root.append(a)

print "Display:"
root.display()
print "Reversed:"
root.display_reverse()
